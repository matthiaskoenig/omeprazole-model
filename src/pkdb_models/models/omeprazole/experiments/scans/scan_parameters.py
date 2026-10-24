"""Parameter scans of the omeprazole model."""

from collections.abc import Mapping
from typing import ClassVar, NamedTuple, NotRequired, TypedDict, override

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.cm import ScalarMappable
from matplotlib.colors import (
    Colormap,
    LinearSegmentedColormap,
    LogNorm,
    Normalize,
    to_hex,
)
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
from matplotlib.typing import ColorType
from pkpdsim.metadata import ApplicationForm, Fasting
from pkpdsim.scan import point_band, point_timecourse, scan_dimensions
from sbmlsim import Q
from sbmlsim.plot.serialization_matplotlib import FigureMPL
from sbmlsim.result import ScanResult
from sbmlsim.simulation import Dimension, Scan, Simulation
from sbmlsim.units import Quantity

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)
from pkdb_models.models.omeprazole.omeprazole_pk import summarize


class ScanSpec(TypedDict):
    """Definition of a single parameter scan.

    The scanned value is set to the parameters times their factor (the
    racemic dose is half S- and half R-omeprazole); the x axis of the figures
    is the scanned value.
    """

    #: the parameters -> the factor of the scanned value
    parameters: dict[str, float]
    default: float
    range: np.ndarray
    scale: str
    units: str
    label: str
    #: the colormap, a matplotlib colormap or the colors at positions from 0
    #: to 1 along the range
    colormap: str | list[tuple[float, str]]
    #: the labels of the ticks of the colorbar, the minimum, the default and
    #: the maximum of the range without
    ticks: NotRequired[dict[float, str]]
    #: only the metabolites depend on the parameter
    metabolites_only: NotRequired[bool]


class Panel(NamedTuple):
    """A panel of the timecourses of a scan."""

    sid: str
    #: the end of the time axis [hr]
    tend: float
    #: the distance of the ticks of the time axis [hr]
    tick: float
    #: a logarithmic axis
    log: bool


def _position(value: float, vmin: float, vmax: float) -> float:
    """Get the position of a value on a logarithmic axis from vmin to vmax."""
    return float((np.log10(value) - np.log10(vmin)) / (np.log10(vmax) - np.log10(vmin)))


def _with(values: np.ndarray, *extra: float) -> np.ndarray:
    """Get the sorted values of a scan with the values `extra` added."""
    return np.unique(np.concatenate([values, np.asarray(extra, dtype=float)]))


_CIRRHOSIS = OmeprazoleSimulationExperiment.cirrhosis_map
_CIRRHOSIS_COLORS = OmeprazoleSimulationExperiment.cirrhosis_colors
_RENAL = OmeprazoleSimulationExperiment.renal_map
_RENAL_COLORS = OmeprazoleSimulationExperiment.renal_colors
_CYP2C19 = OmeprazoleSimulationExperiment.cyp2c19_map
#: the diverging colormaps, whose light center is left out
_DIVERGING = {"RdBu", "PuOr"}


class OmeprazoleParameterScan(OmeprazoleSimulationExperiment):
    """Scan the effect of parameters on the pharmacokinetics of an oral dose.

    A single oral dose of 20 mg racemic omeprazole as an enteric-coated
    capsule, fasted, simulated for 48 hr: the half-life of omeprazole is
    about 1 hr, 3.5 hr in poor metabolizers and longer in severe cirrhosis;
    the proton pumps recover within about 2 days. The figures show the first
    12 hr and the 48 hr after the dose of omeprazole and its metabolites in
    plasma (5-hydroxyomeprazole, omeprazole sulfone), their excretion, the
    stomach pH and the active proton pumps, and the pharmacokinetic
    parameters of the non-compartmental analysis (`omeprazole_pk`) of
    omeprazole and of the metabolites over the scanned parameter.

    In a run over the draws of the fitted parameters (`run_simulation
    pkdb_models.models.omeprazole --uncertainty`) every point of a scan is
    simulated for every draw; the figures draw the median of the draws with
    the band of their quantiles.
    """

    #: the pharmacokinetic parameters by scan key, see `figures_mpl`
    pk_dfs: dict[str, pd.DataFrame]

    #: the end of the simulations [hr]
    tend = 48
    #: the output times [hr]: every 0.02 hr in the first 12 hr (release of
    #: the enteric-coated form, absorption and maximum), every 0.1 hr after it
    times: ClassVar[tuple[float, ...]] = tuple(
        np.unique(
            np.concatenate([np.linspace(0, 12, 601), np.linspace(12, tend, 361)])
        ).tolist()
    )
    #: the end of the timecourses of the first hours and of the whole
    #: simulation [hr]
    tend_day = 12
    tend_plot = 48
    #: the decades of the logarithmic axes of the concentrations
    log_decades = 4
    #: the racemic oral dose of the scans [mg]
    dose_ome = 20
    #: the opacity of the bands of the draws of the fitted parameters
    band_alpha = 0.15
    #: the share of the AUC which is extrapolated above which the analysis of
    #: a point is marked
    auc_extrap_warning = 0.2

    #: the variables of the figures and of the pharmacokinetic parameters
    selections = (
        "time",
        "PODOSE_some",
        "PODOSE_rome",
        "[Cve_ome]",
        "[Cve_some]",
        "[Cve_rome]",
        "[Cve_omeoh]",
        "[Cve_omesul]",
        "[Cve_omeoth]",
        "Aurine_omeoh",
        "Aurine_omeoth",
        "Afeces_omemets",
        "pH",
        "GU__pp_active",
        "f_cirrhosis",
        "KI__f_renal_function",
        "GU__fed",
        "LI__f_cyp2c19",
        "LI__f_cyp3a4",
    )
    #: the concentrations of the timecourses, omeprazole first
    concentrations: ClassVar[tuple[str, ...]] = (
        "[Cve_ome]",
        "[Cve_omeoh]",
        "[Cve_omesul]",
    )
    #: the excreted amounts of the timecourses
    amounts: ClassVar[tuple[str, ...]] = (
        "Aurine_omeoh",
        "Aurine_omeoth",
        "Afeces_omemets",
    )
    #: the pharmacodynamics of the timecourses
    pharmacodynamics: ClassVar[tuple[str, ...]] = ("pH", "GU__pp_active")
    #: the variables of a parameter which only the metabolites depend on
    metabolite_concentrations: ClassVar[tuple[str, ...]] = (
        "[Cve_omeoh]",
        "[Cve_omeoth]",
    )
    metabolite_amounts: ClassVar[tuple[str, ...]] = ("Aurine_omeoh", "Aurine_omeoth")

    #: the pharmacokinetic parameters of the analytes of `omeprazole_pk`
    pk_parameters: ClassVar[dict[str, tuple[str, ...]]] = {
        "ome": ("auc_inf_obs", "cmax", "tmax", "thalf", "cl_f", "vz_f"),
        "omeoh": ("auc_inf_obs", "cmax", "tmax", "thalf"),
        "omesul": ("auc_inf_obs", "cmax", "tmax", "thalf"),
    }
    pk_names: ClassVar[dict[str, str]] = {
        "ome": "omeprazole",
        "omeoh": "5-hydroxyomeprazole",
        "omesul": "omeprazole sulfone",
    }
    pk_labels: ClassVar[Mapping[str, str]] = {
        "auc_inf_obs": "AUC",
        "cmax": "Cmax",
        "tmax": "Tmax",
        "thalf": "Half-life",
        "cl_f": "CL/F",
        "vz_f": "Vz/F",
    }
    pk_units: ClassVar[Mapping[str, str]] = {
        "auc_inf_obs": "µmole/l*hr",
        "cmax": "µmole/l",
        "tmax": "hr",
        "thalf": "hr",
        "cl_f": "l/hr",
        "vz_f": "l",
    }

    num_points = 10
    scan_map: ClassVar[dict[str, ScanSpec]] = {
        "dose_scan": {
            # the racemic dose, half S- and half R-omeprazole
            "parameters": {"PODOSE_some": 0.5, "PODOSE_rome": 0.5},
            "default": dose_ome,
            # the doses of the studies
            "range": np.array([10, 20, 30, 40, 60, 80, 90]),
            "scale": "linear",
            "units": "mg",
            "label": "omeprazole dose [mg]",
            "colormap": "Purples",
        },
        "food_scan": {
            "parameters": {"GU__fed": 1.0},
            "default": 0.0,
            # fasted (0) to a meal (1)
            "range": np.linspace(0, 1, num=11),
            "scale": "linear",
            "units": "dimensionless",
            "label": "fed state [-]",
            "colormap": "YlOrBr",
            "ticks": {0.0: "0\nfasted", 0.5: "0.5", 1.0: "1\nfed"},
        },
        "hepatic_scan": {
            "parameters": {"f_cirrhosis": 1.0},
            "default": 0.0,
            # with the degrees of the Child-Pugh classes
            "range": _with(
                np.array([0, 0.1, 0.2, 0.3, 0.5, 0.6, 0.9]), *_CIRRHOSIS.values()
            ),
            "scale": "linear",
            "units": "dimensionless",
            "label": "cirrhosis degree [-]",
            # the colors of the classes at their degrees (of 0 to 0.9)
            "colormap": [
                (0.0, "#d0e1f2"),
                *(
                    (_CIRRHOSIS[key] / 0.9, _CIRRHOSIS_COLORS[key])
                    for key in (
                        "Mild cirrhosis",
                        "Moderate cirrhosis",
                        "Severe cirrhosis",
                    )
                ),
                (1.0, "#023858"),
            ],
            "ticks": {
                0.0: "0",
                _CIRRHOSIS["Mild cirrhosis"]: "CPT A",
                _CIRRHOSIS["Moderate cirrhosis"]: "CPT B",
                _CIRRHOSIS["Severe cirrhosis"]: "CPT C",
            },
        },
        "renal_scan": {
            "parameters": {"KI__f_renal_function": 1.0},
            "default": 1.0,
            # 0.1 to 2, with the limits of the classes of the GFR
            "range": _with(
                np.array([0.1, 0.14, 0.27, 0.7, 1.4, 2.0]),
                *(v for k, v in _RENAL.items() if k != "End stage renal disease"),
            ),
            "scale": "log",
            "units": "dimensionless",
            "label": "renal function [-]",
            # the colors of the classes at their renal function (of 0.1 to 2),
            # light greens for a normal and an increased renal function
            "colormap": [
                (0.0, _RENAL_COLORS["End stage renal disease"]),
                *(
                    (_position(_RENAL[key], 0.1, 2), _RENAL_COLORS[key])
                    for key in (
                        "Severe renal impairment",
                        "Moderate renal impairment",
                        "Mild renal impairment",
                    )
                ),
                (_position(1.0, 0.1, 2), "#a1d99b"),
                (1.0, "#d9f0d3"),
            ],
            "ticks": {0.1: "0.1", 1.0: "1", 2.0: "2"},
            # omeprazole is not excreted by the kidneys, its metabolites are
            "metabolites_only": True,
        },
        "cyp2c19_scan": {
            "parameters": {"LI__f_cyp2c19": 1.0},
            "default": 1.0,
            # poor (0) to ultrarapid metabolizers (1.5), with the phenotypes
            "range": _with(np.linspace(0, 1.5, num=13), *set(_CYP2C19.values())),
            "scale": "linear",
            "units": "dimensionless",
            "label": "CYP2C19 activity [-]",
            "colormap": "RdBu",
            "ticks": {
                _CYP2C19["PM"]: "0\nPM",
                _CYP2C19["IM"]: "0.5\nIM",
                _CYP2C19["EM"]: "1\nEM",
                _CYP2C19["UM"]: "1.5\nUM",
            },
        },
        "cyp3a4_scan": {
            "parameters": {"LI__f_cyp3a4": 1.0},
            "default": 1.0,
            # inhibition (< 1) and induction (> 1)
            "range": _with(np.logspace(-1, 1, num=num_points), 1.0),
            "scale": "log",
            "units": "dimensionless",
            "label": "CYP3A4 activity [-]",
            "colormap": "RdBu",
            "ticks": {0.1: "0.1\ninhibition", 1.0: "1", 10.0: "10\ninduction"},
        },
    }

    @override
    def simulations(self) -> dict[str, Scan]:
        scans = {}
        for scan_key, scan_data in self.scan_map.items():
            # the simulation does not set what the dimension scans (the dose
            # of the dose scan), the dimension would replace it
            preinit_changes = {
                **self.default_changes(),
                **self.form_changes(ApplicationForm.CAPSULE),
                **self.fed_changes(Fasting.FASTED),
                "PODOSE_some": Q(self.dose_ome / 2, "mg"),
                "PODOSE_rome": Q(self.dose_ome / 2, "mg"),
            }
            for parameter in scan_data["parameters"]:
                preinit_changes.pop(parameter, None)
            scans[f"scan_po_{scan_key}"] = Scan(
                simulation=Simulation(
                    time_unit="hr",
                    end=self.tend,
                    times=self.times,
                    preinit_changes=preinit_changes,
                ),
                dimensions=[
                    Dimension(
                        "dim_scan",
                        values={
                            parameter: Q(
                                factor * scan_data["range"], scan_data["units"]
                            )
                            for parameter, factor in scan_data["parameters"].items()
                        },
                    ),
                ],
            )

        return scans

    def _across(self) -> str | None:
        """Get the dimension of the draws of the fitted parameters, `None` without."""
        return None if self.uncertainty is None else self.uncertainty.id

    def _colormap(self, scan: ScanSpec) -> tuple[Colormap, Normalize]:
        """Get the colormap of a scan and the normalization of its values.

        The scans of the cirrhosis and of the renal function have the colors
        of the classes of the impairments (`pkpdsim.impairment`) at the values
        of the classes. The colormaps of matplotlib leave out their lightest
        colors, so that every curve is visible on white: the start of a
        sequential colormap, the center of a diverging one.
        """
        rmin, rmax = float(scan["range"][0]), float(scan["range"][-1])
        colormap = scan["colormap"]
        if isinstance(colormap, str):
            base = matplotlib.colormaps[colormap]
            positions = (
                np.concatenate([np.linspace(0, 0.4, 128), np.linspace(0.6, 1, 128)])
                if colormap in _DIVERGING
                else np.linspace(0.3, 1.0, 256)
            )
            cmap: Colormap = LinearSegmentedColormap.from_list(
                f"{colormap}_visible", [base(v) for v in positions]
            )
        else:
            cmap = LinearSegmentedColormap.from_list("impairment", colormap)
        if scan["scale"] == "linear":
            return cmap, Normalize(vmin=rmin, vmax=rmax, clip=False)
        return cmap, LogNorm(vmin=rmin, vmax=rmax, clip=False)

    def _timecourse(
        self,
        ax: Axes,
        res: ScanResult,
        panel: Panel,
        point: dict[str, int],
        color: ColorType,
    ) -> tuple[np.ndarray, np.ndarray, float, float]:
        """Draw the timecourse of a point of a scan with the band of its draws.

        Returns:
            The time and the values (the median of the draws in a run over
            them) until the end of the panel, and the lowest value at the end
            of the panel and the highest value, of the band in a run over the
            draws.
        """
        sid = panel.sid
        run = self.uncertainty
        if run is None:
            time, values = point_timecourse(res, sid, **point)
            lower = upper = values
        else:
            time, lower, values, upper = point_band(
                res, sid, across=run.id, quantiles=run.quantiles, **point
            )
        t = Q(time, res.units["time"]).to(self.units["time"]).magnitude
        shown = t <= panel.tend

        def convert(v: np.ndarray) -> np.ndarray:
            """Get the values until the end of the panel in the unit of the figure."""
            return Q(v[shown], res.units[sid]).to(self.units[sid]).magnitude

        c, c_lower, c_upper = convert(values), convert(lower), convert(upper)
        if run is not None:
            ax.fill_between(
                t[shown],
                c_lower,
                c_upper,
                color=color,
                alpha=self.band_alpha,
                linewidth=0,
            )
        ax.plot(t[shown], c, color=color, linewidth=2.0)
        return t[shown], c, float(c_lower[-1]), float(np.max(c_upper))

    def _panels(self, scan: ScanSpec) -> tuple[list[Panel | None], int]:
        """Get the panels of the timecourses of a scan and the number of columns.

        A row of the concentrations in the first hours (linear), a row of
        them over the whole simulation (logarithmic), a row of the excreted
        amounts and a row of the pharmacodynamics; for a parameter which only
        the metabolites depend on, their concentrations and amounts. An empty
        place of a row is `None`.
        """
        if scan.get("metabolites_only", False):
            concentrations = list(self.metabolite_concentrations)
            rows = [
                [Panel(sid, self.tend_day, 2, log=False) for sid in concentrations],
                [Panel(sid, self.tend_plot, 8, log=True) for sid in concentrations],
                [
                    Panel(sid, self.tend_plot, 8, log=False)
                    for sid in self.metabolite_amounts
                ],
            ]
        else:
            concentrations = list(self.concentrations)
            rows = [
                [Panel(sid, self.tend_day, 2, log=False) for sid in concentrations],
                [Panel(sid, self.tend_plot, 8, log=True) for sid in concentrations],
                [Panel(sid, self.tend_plot, 8, log=False) for sid in self.amounts],
                [
                    Panel(sid, self.tend_plot, 8, log=False)
                    for sid in self.pharmacodynamics
                ],
            ]
        ncols = max(len(row) for row in rows)
        panels: list[Panel | None] = []
        for row in rows:
            panels.extend([*row, *([None] * (ncols - len(row)))])
        return panels, ncols

    @override
    def figures_mpl(self) -> dict[str, FigureMPL]:
        """Matplotlib figures."""
        # the pharmacokinetic parameters, per draw in a run over the draws
        self.pk_dfs = self.calculate_omeprazole_pk()

        return {
            **self._figures_mpl_timecourses(),
            **self._figures_mpl_pharmacokinetics(),
        }

    def _colorbar(self, f: FigureMPL, axes: np.ndarray, scan: ScanSpec) -> None:
        """Draw the colorbar of a scan above its panels, the default in black."""
        cmap, norm = self._colormap(scan)
        cbar = f.colorbar(
            ScalarMappable(norm=norm, cmap=cmap),
            ax=axes.ravel().tolist(),
            location="top",
            shrink=0.4,
            aspect=30,
        )
        # the gradient as vector cells: matplotlib rasterizes it into an
        # embedded image, which some SVG viewers do not show; the edges of
        # the cells in their color close the seams between them
        if cbar.solids is not None:
            cbar.solids.set_rasterized(False)
            cbar.solids.set_edgecolor("face")
        rmin, rmax = float(scan["range"][0]), float(scan["range"][-1])
        ticks = scan.get(
            "ticks",
            {value: f"{value:g}" for value in sorted({rmin, rmax, scan["default"]})},
        )
        cbar.ax.minorticks_off()
        cbar.set_ticks(list(ticks), labels=list(ticks.values()))
        cbar.ax.tick_params(labelsize=self.tick_font_size)
        cbar.ax.axvline(x=scan["default"], color="black", linewidth=4)
        cbar.set_label(scan["label"], size=self.tick_font_size + 3, weight="bold")

    def _figures_mpl_timecourses(self) -> dict[str, FigureMPL]:
        """Timecourses of the variables for the values of every scan.

        The default of the scanned parameter is black and drawn on top; the
        axes include the bands of the draws.
        """
        figures = {}
        for scan_key, scan_data in self.scan_map.items():
            panels, ncols = self._panels(scan_data)
            nrows = len(panels) // ncols
            cmap, norm = self._colormap(scan_data)

            f, axes = plt.subplots(
                nrows=nrows,
                ncols=ncols,
                figsize=(6 * ncols, 5 * nrows + 1),
                dpi=150,
                layout="constrained",
                squeeze=False,
            )
            res = self.results[f"task_scan_po_{scan_key}"]
            (scandim,) = scan_dimensions(res, self._across())
            par_vec = scan_data["range"]

            for ax, panel in zip(axes.flatten(), panels, strict=True):
                if panel is None:
                    ax.set_visible(False)
                    continue
                bottom, top = np.inf, 0.0
                default: tuple[np.ndarray, np.ndarray] | None = None
                for k_par, par in enumerate(par_vec):
                    is_default = bool(np.isclose(scan_data["default"], par))
                    color = "black" if is_default else cmap(norm(par))
                    t, c, end, cmax = self._timecourse(
                        ax, res, panel, {scandim: k_par}, color
                    )
                    top = max(top, cmax)
                    if end > 0:
                        bottom = min(bottom, end)
                    if is_default:
                        default = (t, c)

                # the default on top
                if default is not None:
                    ax.plot(*default, color="black", linewidth=2.0)

                ax.set_xlim(0, panel.tend)
                ax.set_xticks(np.arange(0, panel.tend + 1, panel.tick))
                if panel.log and np.isfinite(bottom):
                    # from the lowest value at the end to the highest value,
                    # at most `log_decades` below it
                    ax.set_yscale("log")
                    ax.set_ylim(
                        max(0.5 * bottom, 10.0 ** (-self.log_decades) * top),
                        2.0 * top,
                    )
                else:
                    ax.set_ylim(0, 1.05 * top if top > 0 else 1.0)
                ax.set_xlabel(
                    f"{self.label_time} [{self.units['time']}]", fontdict=self.font
                )
                unit = self.units[panel.sid]
                ax.set_ylabel(
                    f"{self.labels[panel.sid]} "
                    f"[{'-' if unit == 'dimensionless' else unit}]",
                    fontdict=self.font,
                )
                ax.tick_params(axis="both", labelsize=self.tick_font_size)

            self._colorbar(f, axes, scan_data)
            figures[f"timecourse__{scan_key}"] = f

        return figures

    def _summary(
        self, df: pd.DataFrame, key: str, unit: str, target: str
    ) -> tuple[Quantity, Quantity, Quantity]:
        """Get a parameter at the points of a scan, the median and the band of the draws.

        Returns:
            The values (the median of the draws in a run over them), and the
            lower and the upper quantile, the values without draws.
        """
        run = self.uncertainty
        if run is None:
            values = Q(df[key].to_numpy(dtype=float), unit).to(target)
            return values, values, values
        summary = summarize(df, key, run.quantiles)
        median, lower, upper = (
            Q(summary[column].to_numpy(), unit).to(target)
            for column in ["median", "lower", "upper"]
        )
        return median, lower, upper

    def _figures_mpl_pharmacokinetics(self) -> dict[str, FigureMPL]:
        """Pharmacokinetic parameters over the scanned parameter.

        A row per analyte, omeprazole and its metabolites 5-hydroxyomeprazole
        and omeprazole sulfone. A point whose AUC is extrapolated by more than
        `auc_extrap_warning` (in a run over the draws in any draw) is a
        diamond.
        """
        figures = {}
        ncols = max(len(keys) for keys in self.pk_parameters.values())
        for scan_key, scan_data in self.scan_map.items():
            substances = (
                ["omeoh"]
                if scan_data.get("metabolites_only", False)
                else ["ome", "omeoh", "omesul"]
            )
            cmap, norm = self._colormap(scan_data)
            f, axes = plt.subplots(
                nrows=len(substances),
                ncols=ncols,
                figsize=(5 * ncols, 5 * len(substances)),
                dpi=150,
                layout="constrained",
                squeeze=False,
            )
            sim_key = f"scan_po_{scan_key}"
            df_all = self.pk_dfs[sim_key]
            x = scan_data["range"]

            for krow, substance in enumerate(substances):
                df = df_all[df_all.substance == substance]
                warning = (
                    (df["auc_extrap_fraction"] > self.auc_extrap_warning)
                    .groupby(df["point"])
                    .any()
                    .to_numpy()
                )
                keys = self.pk_parameters[substance]
                for k, ax in enumerate(axes[krow]):
                    if k >= len(keys):
                        ax.set_visible(False)
                        continue
                    pk_key = keys[k]
                    y, y_lower, y_upper = self._summary(
                        df,
                        pk_key,
                        df[f"{pk_key}_unit"].iloc[0],
                        self.pk_units[pk_key],
                    )
                    ax.axvline(
                        x=scan_data["default"], color="grey", linestyle="--", zorder=1
                    )
                    if self.uncertainty is not None:
                        ax.fill_between(
                            x,
                            y_lower.magnitude,
                            y_upper.magnitude,
                            color="black",
                            alpha=self.band_alpha,
                            linewidth=0,
                        )
                    ax.plot(x, y.magnitude, color="black", linewidth=2.0, zorder=2)
                    # the default black, as in the timecourses
                    colors = np.array(
                        [
                            "black"
                            if np.isclose(v, scan_data["default"])
                            else to_hex(cmap(norm(v)))
                            for v in x
                        ]
                    )
                    for marker, points in (("o", ~warning), ("D", warning)):
                        ax.scatter(
                            x[points],
                            y.magnitude[points],
                            s=80,
                            marker=marker,
                            c=colors[points],
                            edgecolors="black",
                            linewidths=1.5,
                            zorder=3,
                        )
                    ax.set_xscale(scan_data["scale"])
                    if scan_data["scale"] == "log":
                        # 0.1, 1 and 10 instead of the powers of ten
                        ax.xaxis.set_major_formatter(
                            FuncFormatter(lambda value, _: f"{value:g}")
                        )
                    ax.set_ylim(0, 1.1 * float(np.nanmax(y_upper.magnitude)))
                    ax.set_xlabel(scan_data["label"], fontdict=self.scan_font)
                    ax.set_ylabel(
                        f"{self.pk_labels[pk_key]} [{self.pk_units[pk_key]}]",
                        fontdict=self.scan_font,
                    )
                    ax.set_title(self.pk_names[substance], fontdict=self.scan_font)
                    ax.tick_params(axis="both", labelsize=self.tick_font_size)
                    if k == 0 and warning.any():
                        ax.legend(
                            handles=[
                                Line2D(
                                    [0],
                                    [0],
                                    marker="D",
                                    linestyle="",
                                    markerfacecolor="white",
                                    markeredgecolor="black",
                                    markeredgewidth=1.5,
                                    markersize=9,
                                    label=(
                                        "AUC extrapolated > "
                                        f"{100 * self.auc_extrap_warning:g} %"
                                    ),
                                )
                            ],
                            loc="best",
                            fontsize=self.tick_font_size - 3,
                        )

            figures[f"pk_{scan_key}"] = f

        return figures


if __name__ == "__main__":
    MODEL.run_experiments(
        OmeprazoleParameterScan, output_dir=OmeprazoleParameterScan.__name__
    )
