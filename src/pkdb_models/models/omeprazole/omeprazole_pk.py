"""Pharmacokinetic parameters of the omeprazole scans.

The parameters are the non-compartmental analysis of `pkpdutils`, named like
the variables of its `NCAResult` (e.g. `auc_inf_obs`, `cmax`, `tmax`, `thalf`,
`lambda_z`, `cl_f`, `vz_f`), with the unit of every parameter in
`<name>_unit`, in venous plasma. The analytes are omeprazole (S- and
R-omeprazole) with the dose of both enantiomers, the enantiomers with their own
dose and the metabolites without a dose, i.e., without clearance and volume.
The dose is the oral or the intravenous dose (bolus and infusion) of the
simulation; with an oral dose the route is oral. The concentrations below
`LLOQ_FRACTION` of the maximum are below the limit of quantification, so that
the noise of the integrator is not the terminal phase.

A scan has one dimension, the scanned parameter; a run over the draws of the
fitted parameters (`run_simulation pkdb_models.models.omeprazole --uncertainty`)
adds the dimension of the draws. The parameters are calculated for every point
of every dimension, a row per point with its position along each dimension
(the columns `point` and, with draws, `draw`), see `summarize`.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

import numpy as np
import pandas as pd
from pkpdsim.pk import nca_frame
from pkpdsim.scan import end_values, scan_dimensions, start_values
from pkpdutils import NCAResult, Route, Timecourses, nca
from sbmlsim import Q
from sbmlsim.result import ScanResult

if TYPE_CHECKING:
    from xarray import DataArray

    from pkdb_models.models.omeprazole.experiments.base_experiment import (
        OmeprazoleSimulationExperiment,
    )

#: the analytes -> their concentration and the enantiomers of their dose
ANALYTES: dict[str, tuple[str, tuple[str, ...]]] = {
    "ome": ("[Cve_ome]", ("some", "rome")),
    "some": ("[Cve_some]", ("some",)),
    "rome": ("[Cve_rome]", ("rome",)),
    "omeoh": ("[Cve_omeoh]", ()),
    "omesul": ("[Cve_omesul]", ()),
}
#: the limit of quantification relative to the maximal concentration
LLOQ_FRACTION = 1e-4


def _mass(
    res: ScanResult, sid: str, values: Callable[[ScanResult, str], DataArray]
) -> np.ndarray | float:
    """Get a dose of every simulation of a scan [mg], zero without the dose.

    Args:
        res: result of the scan.
        sid: the dose.
        values: `start_values` or `end_values`, the dose at the start or the
            end of the simulation.
    """
    if sid not in res.units:
        return 0.0
    return Q(values(res, sid).values, res.units[sid]).to("mg").magnitude


def _infusion(res: ScanResult, sid: str) -> tuple[np.ndarray, np.ndarray]:
    """Get the start and the duration of the infusion of every simulation of a scan.

    The infusion starts at the time point before the cumulative dose
    (`cum_dose_<sid>`) rises and ends at the time point after which it is
    complete; a simulation without an infusion has a meaningless window.
    """
    timecourses = res.to_timecourses(sid)
    # the times and the values of a ragged result are padded with `NaN`
    time, cum_dose = timecourses.times, timecourses.values
    last = cum_dose.shape[-1] - 1
    infusing = cum_dose < end_values(res, sid).values[..., None] * (1 - 1e-9)
    # the last time point of the infusion and the first one with a dose
    end = last - np.argmax(infusing[..., ::-1], axis=-1)
    first = np.argmax(cum_dose > 0, axis=-1)
    start = np.take_along_axis(time, np.maximum(first - 1, 0)[..., None], axis=-1)
    stop = np.take_along_axis(time, np.minimum(end + 1, last)[..., None], axis=-1)
    return start[..., 0], (stop - start)[..., 0]


def _dose(
    experiment: OmeprazoleSimulationExperiment,
    res: ScanResult,
    enantiomers: tuple[str, ...],
) -> tuple[dict[str, np.ndarray], np.ndarray]:
    """Get the dose of the enantiomers of every simulation of a scan.

    The oral and the intravenous bolus dose at the start, the infused dose at
    the end (`cum_dose_<sid>`); the route is oral if there is an oral dose, an
    infusion if there is an infused dose (its window from the cumulative
    dose), an intravenous bolus otherwise.

    Returns:
        The doses (`amount` [mmole], `time` and `duration` of an infusion)
        and the routes over the dimensions of the scan, the route `None` for
        a simulation without a dose.
    """
    shape = tuple(res.ds.sizes[dim] for dim in res.dims)
    oral = bolus = infused = np.zeros(shape)
    for e in enantiomers:
        oral = oral + _mass(res, f"PODOSE_{e}", start_values)
        bolus = bolus + _mass(res, f"IVDOSE_{e}", start_values)
        infused = infused + _mass(res, f"cum_dose_{e}", end_values)
    total = oral + bolus + infused
    amount = (Q(total, "mg") / experiment.Mr.ome).to("mmole").magnitude
    routes = np.full(shape, None, dtype=object)
    routes[total > 0] = Route.IV_BOLUS
    routes[(total > 0) & (infused > 0) & (oral <= 0)] = Route.IV_INFUSION
    routes[(total > 0) & (oral > 0)] = Route.ORAL
    dose = {"amount": amount}
    if (routes == Route.IV_INFUSION).any():
        dose["time"], dose["duration"] = _infusion(res, f"cum_dose_{enantiomers[0]}")
    return dose, routes


def _nca(
    res: ScanResult,
    concentration: str,
    substance: str,
    dose: dict[str, np.ndarray | str],
    route: Route | None,
) -> NCAResult:
    """Get the analysis of a concentration in every simulation of a scan.

    The doses of all simulations are given by the one route (`scan_nca`, with
    the window of an infusion), the route `None` analyses without a dose.
    """
    timecourses = (
        res.to_timecourses(concentration, substance=substance)
        if route is None
        else res.to_timecourses(
            concentration, dose=dose, route=route, substance=substance
        )
    )
    values = timecourses.ds["value"]
    cmax = values.max(dim=[d for d in values.dims if d not in res.dims])
    lloq = (LLOQ_FRACTION * cmax).where(cmax > 0)
    return nca(Timecourses(timecourses.ds.assign(lloq=lloq)))


def pk_parameters(
    experiment: OmeprazoleSimulationExperiment,
    res: ScanResult,
    substance: str,
) -> pd.DataFrame:
    """Calculate the pharmacokinetic parameters of an analyte in every simulation of a scan.

    The non-compartmental analysis of all simulations with a dose of one route
    at once, and of all simulations without a dose at once.

    Args:
        experiment: experiment of the scan, for the molecular weight.
        res: result of the scan.
        substance: the analyte, a key of `ANALYTES`.

    Returns:
        One row per simulation of the scan (in the order of the dimensions of
        the scan), with its position along every dimension (a column named
        after the dimension), `substance`, the parameters and their units
        (`<name>_unit`).
    """
    concentration, enantiomers = ANALYTES[substance]
    dose, routes = _dose(experiment, res, enantiomers)
    # an analysis per route (in the order of the first simulation of a route),
    # of which the simulations of the route are taken; the doses of the
    # simulations of the other routes are left out (an infusion needs a window)
    labels = routes.ravel()
    frames = []
    for route in dict.fromkeys(labels):
        given = routes == route
        route_dose: dict[str, np.ndarray | str] = {
            key: np.where(given, value, np.nan) for key, value in dose.items()
        }
        route_dose["unit"] = "mmol"
        df = nca_frame(_nca(res, concentration, substance, route_dose, route))
        frames.append(df.drop(columns="nca_flags")[labels == route])
    df = pd.concat(frames).sort_index()
    df.insert(len(res.dims), "substance", substance)
    return df


def calculate_omeprazole_pk(
    experiment: OmeprazoleSimulationExperiment,
    res: ScanResult,
    across: str | None = None,
) -> pd.DataFrame:
    """Calculate the pharmacokinetic parameters of every simulation of a scan.

    Args:
        experiment: experiment of the scan.
        res: result of the scan.
        across: the dimension of the draws of the fitted parameters, `None`
            for a scan without draws.

    Returns:
        One row per simulation of the scan and analyte, with its position
        (`point`, and `draw` with draws).

    Raises:
        ValueError: if the scan has not one dimension besides the draws.
    """
    dims = scan_dimensions(res, across)
    if len(dims) != 1:
        raise ValueError(
            f"A scan of one dimension is required, not of {dims} (draws: {across})."
        )
    names = {dims[0]: "point", **({across: "draw"} if across is not None else {})}
    return pd.concat(
        [
            pk_parameters(experiment, res, substance).rename(columns=names)
            for substance in ANALYTES
        ],
        ignore_index=True,
    )


def summarize(
    df: pd.DataFrame, key: str, quantiles: tuple[float, float]
) -> pd.DataFrame:
    """Get the median and the quantiles of a parameter over the draws of every point.

    Args:
        df: the parameters with the columns `point` and `draw`.
        key: the parameter.
        quantiles: the lower and the upper quantile.

    Returns:
        One row per point (the index), the columns `lower`, `median`, `upper`.
    """
    low, high = quantiles
    grouped = df.groupby("point")[key]
    return pd.DataFrame(
        {
            "lower": grouped.quantile(low),
            "median": grouped.median(),
            "upper": grouped.quantile(high),
        }
    ).astype(np.float64)
