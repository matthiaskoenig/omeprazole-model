"""Sensitivity analysis of the omeprazole model.

The outputs are the pharmacokinetic parameters of omeprazole, its enantiomers
and its metabolites after a single oral dose of racemic omeprazole (the
non-compartmental analysis of `pkpdutils`) and the extremes of the
pharmacodynamics: the highest stomach pH and the lowest fraction of active
proton pumps. The dose is 20 mg of an enteric-coated form, fasted, the dose of
most studies. The parameters are the parameters of the model with bounds of
+-15 % around their value. The analyses are run as a script, the local
analysis by default:

    python -m pkdb_models.models.omeprazole.sensitivity.sensitivity_analysis
    python -m pkdb_models.models.omeprazole.sensitivity.sensitivity_analysis local sampling

The analyses run on `pkpdsim.sensitivity.SensitivityRunner`, which writes the
table of the parameters into `results/sensitivity` of the model and the tables
and figures of an analysis into `results/sensitivity/<analysis>`.
An analysis does not vary a parameter which one of its groups sets
(`pkpdsim.sensitivity.free_parameters`): every group sets the enteric-coated
form (`GU__f_ec`), `sampling`, over the groups, leaves out `f_cirrhosis` as
well. The environment variable `PKPDSIM_SENSITIVITY_N` replaces the numbers of
samples of the global analyses for a quick run, see
`pkpdsim.sensitivity.sample_size`.

The model without omeprazole is stationary, so the simulation of a group
starts with the dose. The dose is followed for `END_HR` hours: the half-life of
omeprazole is about 1 hr (3.5 hr in poor metabolizers) and the proton pumps
recover within about 2 days.
"""

from collections.abc import Callable, Mapping

import numpy as np
from pkpdsim.sensitivity import (
    FastAnalysis,
    LocalAnalysis,
    ParameterType,
    SamplingAnalysis,
    SensitivityGroup,
    SensitivityOutput,
    SensitivityParameter,
    SensitivityRunner,
    SobolAnalysis,
    parameters_from_sbml,
    set_bounds,
    set_relative_bounds,
)
from pkpdutils import NCAOptions
from sbmlsim import Q
from sbmlsim.simulation import PK, Custom, Formula, Simulation

from pkdb_models.models.omeprazole import MODEL, MODEL_PATH
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)
from pkdb_models.models.omeprazole.fitting.parameters import (
    parameters_pk as fit_parameters,
)

#: oral dose of racemic omeprazole of the analysis [mg], half S- and half
#: R-omeprazole
DOSE_OME = 20
#: the hours after the dose
END_HR = 48
#: the limit of quantification of the non-compartmental analysis [mM], about
#: 1e-6 of the maximal concentration of omeprazole after 20 mg (5e-4 mM), so
#: that the noise of the integrator is not the terminal phase
LLOQ = 5e-10
#: fraction of the bounds of a parameter relative to its value
BOUNDS_FRACTION = 0.15

#: outputs of the non-compartmental analysis of omeprazole -> unit
PK_OUTPUTS_OME: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "tmax": "min",
    "thalf": "min",
    "vz_f": "l",
    "cl_f": "ml/min",
}
#: outputs of an enantiomer (no clearance or volume) -> unit
PK_OUTPUTS_ENANTIOMER: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "tmax": "min",
    "thalf": "min",
}
#: outputs of a metabolite -> unit; the flat maxima of the metabolites make
#: their tmax jump between the output times for a change of 1 %, it is left out
PK_OUTPUTS_METABOLITE: dict[str, str] = {
    "auc_inf_obs": "mM*min",
    "cmax": "mM",
    "thalf": "min",
}
#: the outputs whose unit has the amount of the dose: the dose is a mass
#: (`PODOSE_some` in mg), so they are divided by the molecular weight (its value
#: at the start, a value per simulation like the parameter of the analysis);
#: the analysis of omeprazole has the dose of S-omeprazole, the racemic dose
#: is that of both enantiomers
PK_PER_DOSE_MASS: frozenset[str] = frozenset({"vz_f", "cl_f"})
#: the racemic dose over the dose of S-omeprazole
RACEMIC = "(at(PODOSE_some, 0) + at(PODOSE_rome, 0)) / at(PODOSE_some, 0)"


def max_after_dose(time: np.ndarray, values: dict[str, np.ndarray]) -> float:
    """Get the maximum of a timecourse after the dose (time 0)."""
    (x,) = values.values()
    return float(np.max(x[time >= 0]))


def min_after_dose(time: np.ndarray, values: dict[str, np.ndarray]) -> float:
    """Get the minimum of a timecourse after the dose (time 0)."""
    (x,) = values.values()
    return float(np.min(x[time >= 0]))


#: the extremes of the pharmacodynamics after the dose: id -> function,
#: selection, unit
EXTREMES: dict[
    str, tuple[Callable[[np.ndarray, dict[str, np.ndarray]], float], str, str]
] = {
    "max_pH": (max_after_dose, "pH", "dimensionless"),
    "min_pp_active": (min_after_dose, "GU__pp_active", "dimensionless"),
}

#: the analytes: id -> concentration, name, outputs
ANALYTES: dict[str, tuple[str, str, dict[str, str]]] = {
    "ome": ("[Cve_ome]", "omeprazole", PK_OUTPUTS_OME),
    "some": ("[Cve_some]", "S-omeprazole", PK_OUTPUTS_ENANTIOMER),
    "rome": ("[Cve_rome]", "R-omeprazole", PK_OUTPUTS_ENANTIOMER),
    "omeoh": ("[Cve_omeoh]", "5-hydroxyomeprazole", PK_OUTPUTS_METABOLITE),
    "omesul": ("[Cve_omesul]", "omeprazole sulfone", PK_OUTPUTS_METABOLITE),
}
#: the names of the outputs of the analysis
PK_NAMES: dict[str, str] = {
    "auc_inf_obs": "AUC∞",
    "cmax": "Cmax",
    "tmax": "tmax",
    "thalf": "Half-life",
    "vz_f": "Vz/F",
    "cl_f": "CL/F",
}

#: the outputs with their ids and names
OUTPUTS: list[SensitivityOutput] = [
    *(
        SensitivityOutput(f"{sid}_{key}", f"{name} {PK_NAMES[key]}")
        for sid, (_, name, outputs) in ANALYTES.items()
        for key in outputs
    ),
    SensitivityOutput("max_pH", "max stomach pH"),
    SensitivityOutput("min_pp_active", "min active proton pumps"),
]


def _pk_observables(sid: str) -> list:
    """Get the non-compartmental analysis of an analyte and its outputs.

    The analysis of omeprazole has the dose of S-omeprazole (`PODOSE_some`),
    its clearance and volume are scaled to the racemic dose (`RACEMIC`); the
    enantiomers have their own dose, the metabolites none.
    """
    concentration, _, outputs = ANALYTES[sid]
    pk_id = f"pk_{sid}"
    dose = {"ome": "PODOSE_some", "some": "PODOSE_some", "rome": "PODOSE_rome"}
    return [
        PK(
            pk_id,
            concentration,
            dose=dose.get(sid),
            route="oral" if sid in dose else None,
            options=NCAOptions(lloq=LLOQ),
            parameters=list(outputs),
        ),
        *(
            Formula(
                f"{sid}_{key}",
                f"{pk_id}.{key} * {RACEMIC} / at(Mr_some, 0)"
                if key in PK_PER_DOSE_MASS
                else f"{pk_id}.{key}",
                unit=unit,
            )
            for key, unit in outputs.items()
        ),
    ]


#: the observables of a simulation, the outputs with their units; the ids of
#: the analyses (`pk_ome`, ...) are no species of the model
OBSERVABLES = [
    *(observable for sid in ANALYTES for observable in _pk_observables(sid)),
    *(
        Custom(key, function, unit, symbols=[selection])
        for key, (function, selection, unit) in EXTREMES.items()
    ),
]

#: the output times [hr]: every 0.02 hr in the first day after the dose
#: (release of the enteric-coated form, absorption and maximum), every 0.5 hr
#: after it
TIMES_HR: tuple[float, ...] = tuple(
    np.unique(
        np.concatenate(
            [
                np.linspace(0, 24, 1201),
                np.linspace(24, END_HR, 2 * (END_HR - 24) + 1),
            ]
        )
    ).tolist()
)


def sensitivity_simulation(changes: Mapping[str, float]) -> Simulation:
    """Get the simulation of a group: a single oral dose of omeprazole at time 0.

    The racemic dose of an enteric-coated form (`GU__f_ec`), fasted.
    """
    return Simulation(
        start=0,
        end=END_HR,
        times=TIMES_HR,
        time_unit="hr",
        preinit_changes={
            **changes,
            "GU__f_ec": Q(1.0, "dimensionless"),
            "PODOSE_some": Q(DOSE_OME / 2, "mg"),
            "PODOSE_rome": Q(DOSE_OME / 2, "mg"),
        },
    )


#: the groups the analyses are run for: the control and the stages of
#: cirrhosis of the simulation experiments
SENSITIVITY_GROUPS: list[SensitivityGroup] = [
    SensitivityGroup("control", "Control", sensitivity_simulation({}), "dimgrey"),
    *(
        SensitivityGroup(
            uid,
            name,
            sensitivity_simulation(
                {"f_cirrhosis": OmeprazoleSimulationExperiment.cirrhosis_map[name]}
            ),
            OmeprazoleSimulationExperiment.cirrhosis_colors[name],
        )
        for uid, name in [
            ("mildCirrhosis", "Mild cirrhosis"),
            ("moderateCirrhosis", "Moderate cirrhosis"),
            ("severeCirrhosis", "Severe cirrhosis"),
        ]
    ),
]


def sensitivity_parameters() -> list[SensitivityParameter]:
    """Get the parameters of the analyses with their bounds and references."""
    parameters = parameters_from_sbml(
        MODEL_PATH,
        exclude_ids={
            # molecular weights
            "Mr_some",
            "Mr_rome",
            "Mr_omeoh",
            "Mr_omesul",
            "Mr_omeoth",
            "GU__Mr_ome",
            # conversion factors
            "GU__cf_species_dimensionless",
            # reference values
            "BW_ref",
            # unchangeable values
            "FQlu",
            "FVhv",
            "FVpo",
            # dosing parameters
            "PODOSE_some",
            "PODOSE_rome",
            "IVDOSE_some",
            "IVDOSE_rome",
            "ti_some",
            "ti_rome",
            # the switches of the application form and of food
            "GU__f_ec",
            "GU__f_unprotected",
            "GU__fed",
        },
        exclude_na=True,
        exclude_zero=True,
    )

    # the fitted parameters, their bounds are set relative to the value below
    set_bounds(
        parameters,
        [(fp.pid, np.nan, np.nan, ParameterType.FIT) for fp in fit_parameters],
    )
    # the scaling factors of the organ functions and of the enzymes
    set_bounds(
        parameters,
        [
            (uid, 1 - BOUNDS_FRACTION, 1 + BOUNDS_FRACTION, ParameterType.SCALING)
            for uid in ["KI__f_renal_function", "LI__f_cyp2c19", "LI__f_cyp3a4"]
        ],
    )
    # the absorption is complete (no unchanged omeprazole in the feces), a
    # fraction above 1 has no meaning
    set_bounds(
        parameters,
        [("GU__F_ome_abs", 1 - BOUNDS_FRACTION, 1.0, ParameterType.DATA)],
    )

    # the references of the values from the literature
    references = {
        "BW": r"\cite{Ogden2004, Jones2013, Thompson2009, Brown1997}",
        "FQgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FQh": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FQki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVar": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVgu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVki": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVli": r"\cite{Jones2013, Wynne1989, Thompson2009, Brown1997}",
        "FVlu": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "FVve": r"\cite{Jones2013, Thompson2009, Brown1997}",
        "COBW": r"\cite{Cattermole2017, Patel2021, Collis2001}",
        "KI__f_renal_function": r"\cite{Stevens2024}",
    }
    by_uid = {p.uid: p for p in parameters}
    for uid, reference in references.items():
        p = by_uid[uid]
        p.reference = reference
        if p.type == ParameterType.NA:
            p.type = ParameterType.DATA

    # every parameter without bounds varies around its value
    set_relative_bounds(parameters, BOUNDS_FRACTION)
    return parameters


#: the analyses of the script, with their groups and numbers of samples
SENSITIVITY = SensitivityRunner(
    model=MODEL,
    parameters=sensitivity_parameters,
    outputs=OUTPUTS,
    observables=OBSERVABLES,
    analyses={
        "local": LocalAnalysis(groups=SENSITIVITY_GROUPS[:1], delta=0.01),
        "sampling": SamplingAnalysis(groups=SENSITIVITY_GROUPS, n=1000),
        "fast": FastAnalysis(groups=SENSITIVITY_GROUPS[:1], n=1000),
        "sobol": SobolAnalysis(groups=SENSITIVITY_GROUPS[:1], n=4096),
    },
    default=("local",),
)


if __name__ == "__main__":
    SENSITIVITY.main()
