"""Parameter fit problems for omeprazole.

The data of a fit is selected from the fit mappings of the studies in three
steps, see `sbmlsim.fit.helpers`: the filters on the metadata of the mappings
select the training data of the fit and exclude the rest, the outliers are
named once for all mappings and are the training data which is not usable, and
the validation data is the part of the training data a fit is evaluated on but
not fitted to. The metadata of a mapping describes its curve, what a fit does
with the curve is decided here.

The training data is omeprazole alone in healthy subjects (and in patients
with a duodenal ulcer in remission, whose pharmacokinetics is that of healthy
subjects), fasted, after single doses and exactly encoded repeated doses. The
CYP2C19 genotypes are training data: their activities are fixed by the
genotype (`cyp2c19_map`), so the poor metabolizers identify the CYP3A4 route
(including its 5-hydroxyomeprazole), and the repeated doses identify the
mechanism-based inactivation of CYP2C19.

The validation data has five parts, each a different question: the
interactions (`INTERACTION_VALIDATION`, the arms with a coadministered drug
whose interaction the model describes with factors which are not fitted), the
doses (`DOSE_VALIDATION`, doses outside the range of the training), the
populations (`POPULATION_VALIDATION`, the elderly, renal impairment, genotyped
individuals and extreme subjects, which the model describes with its
covariates), food (`FOOD_VALIDATION`, the fed arms, whose effect is fixed) and
the limitations (`LIMITATION_VALIDATION`, data of a population, a formulation
or a process the model does not describe). The summaries of data which is
fitted one by one are excluded (`AGGREGATE_MAPPINGS`).
"""

from pkpdsim.fit import metadata_filter
from pkpdsim.metadata import Coadministration, Fasting, Health
from sbmlsim.console import console
from sbmlsim.experiment import SimulationExperiment
from sbmlsim.fit import FitMapping, FitMappingCollection, MappingKind
from sbmlsim.fit.helpers import FitMappings, MappingFilter

from pkdb_models.models.omeprazole import DATA_PATHS, OMEPRAZOLE_PATH
from pkdb_models.models.omeprazole.experiments.studies import (
    Andersson1990a,
    Andersson1993,
    Andersson2001,
    Cederberg1992,
    Elkoshi2002,
    Faruquee2010,
    Geus2000,
    HassanAlin2000,
    HassanAlin2005,
    Kita2001,
    Kita2002,
    Landahl1992,
    Lind1983,
    Naesdal1986,
    Oh2012,
    Palovaara2003,
    Park2017,
    Prichard1985,
    Qadir2017,
    Regaardh1986,
    Regaardh1990,
    Sohn1992,
    Uno2007,
    VazdaSilva2001,
    VazdaSilva2005,
    Walt1985,
)

#: the keys of fit mappings by study: the keys of the mappings are SIds of their
#: experiment, which two studies can share, so a named mapping is named with
#: its study
type NamedMappings = dict[str, set[str]]

EXPERIMENT_CLASSES: list[type[SimulationExperiment]] = [
    Andersson1990a,
    Andersson1993,
    Andersson2001,
    Cederberg1992,
    Elkoshi2002,
    Faruquee2010,
    Geus2000,
    HassanAlin2000,
    HassanAlin2005,
    Kita2001,
    Kita2002,
    Landahl1992,
    Lind1983,
    Naesdal1986,
    Oh2012,
    Palovaara2003,
    Park2017,
    Prichard1985,
    Qadir2017,
    Regaardh1986,
    Regaardh1990,
    Sohn1992,
    Uno2007,
    VazdaSilva2001,
    VazdaSilva2005,
    Walt1985,
]

#: mappings which are not fitted, the data is not usable
OUTLIER_MAPPINGS: NamedMappings = {
    # the assay is not specific for omeprazole: 41 % of the dose as unchanged
    # omeprazole in urine with a urinary half-life of 21 hr, against no
    # unchanged omeprazole in the urine of every 14C study
    "Faruquee2010": {"fm_ome20_cum_amount", "fm_ome20_ex_rate"},
    # the mean curve contradicts Tab1 of the same subjects: its peak lies above
    # the mean Cmax and its AUC is 2.2 times the reported one
    "Kita2002": {"fm_ome_EM_20_omeprazole"},
}

#: the validation of the interactions: the arms with a coadministered drug,
#: simulated with factors of CYP3A4 and CYP2C19 which are not fitted
INTERACTION_VALIDATION: NamedMappings = {
    # clarithromycin, CYP3A4 (`F_CYP3A4_CLARITHROMYCIN`), with amoxicillin
    # which does not interact
    "Andersson2001": {"fm_some40po_SOME_CLA_AMO"},
    # ethinylestradiol, CYP2C19 (`F_CYP2C19_ETHINYLESTRADIOL`), and
    # levonorgestrel alone, the negative control without an interaction
    "Palovaara2003": {
        "fm_po40_EE_LNG_OME40_ome",
        "fm_po40_EE_LNG_OME40_omeoh",
        "fm_po40_EE_LNG_OME40_omesul",
        "fm_po40_LNG_OME40_ome",
        "fm_po40_LNG_OME40_omeoh",
        "fm_po40_LNG_OME40_omesul",
    },
}

#: the validation of the doses: doses outside the range of the training, which
#: the dependence of the first pass and the clearance on the dose predicts
DOSE_VALIDATION: NamedMappings = {
    # 90 mg, the saturation of the first pass outside the clinical range
    "Andersson1990a": {"fm_omepo90_ome"},
    # a 0.2 mg microdose of the Inje cocktail, whose drugs do not interact with
    # omeprazole at these doses
    "Oh2012": {"fm_po0p2_ome", "fm_po0p2_omeoh"},
    # 80 mg intravenously, patients with a duodenal ulcer in remission
    "Walt1985": {"fm_ome_iv80"},
}

#: the validation of the populations: subjects which the model describes with
#: its covariates (renal function, CYP2C19 activity), not with fitted values
POPULATION_VALIDATION: NamedMappings = {
    # individual subjects of known genotype, Japanese, fed
    "Kita2001": {
        f"fm_ome20po_S{subject}_{substance}"
        for subject in ["1_EM", "2_IM", "3_IM", "4_PM", "5_PM", "6_PM"]
        for substance in [
            "omeprazole",
            "5_hydroxyomeprazole",
            "omeprazole_sulfone",
        ]
    },
    # the elderly with the clearance of the young halved: the model has no age
    "Landahl1992": {
        "fm_ome_iv20_omeprazole",
        "fm_ome_po40_omeprazole",
        "fm_ome_iv20_5_hydroxyomeprazole",
        "fm_ome_po40_5_hydroxyomeprazole",
        "fm_ome_iv20_omeprazole_sulfone",
        "fm_ome_po40_omeprazole_sulfone",
        "fm_ome_iv20_omeprazole_metabolites",
        "fm_ome_po40_omeprazole_metabolites",
        "fm_ome_iv20_amount_omeprazole_metabolites",
        "fm_ome_po40_amount_omeprazole_metabolites",
    },
    # renal impairment: omeprazole unchanged, the excretion of the metabolites
    # reduced with the creatinine clearance
    "Naesdal1986": {
        "fm_OME20_IV_omeprazole",
        "fm_OME40_PO_omeprazole",
        "fm_OME20_IV_5_hydroxyomeprazole",
        "fm_OME40_PO_5_hydroxyomeprazole",
        "fm_OME20_IV_omeprazole_sulfone",
        "fm_OME40_PO_omeprazole_sulfone",
        "fm_OME20_IV_MRI_omeprazole_metabolites",
        "fm_OME20_IV_SRI_omeprazole_metabolites",
        "fm_OME40_PO_MRI_omeprazole_metabolites",
        "fm_OME40_PO_SRI_omeprazole_metabolites",
        "fm_OME20_IV_RI_excretion_rate_omemets",
    },
    # renal impairment, the group and the urine of the single patients with
    # their creatinine clearance
    "Regaardh1986": {
        "fm_iv20_renal",
        "fm_po40_renal",
        *{f"fm_iv20_renal{k}_urine" for k in range(1, 13)},
    },
    # the extreme subjects of the study: subject 7 the fastest metabolizer,
    # subject 2 a poor metabolizer by phenotype
    "Regaardh1990": {
        "fm_ome_iv10_adult7",
        "fm_ome_po20_adult7",
        "fm_ome_iv10_adult2",
        "fm_ome_po20_adult2",
        "fm_omesul_po20_adult2",
        "fm_omeoh_po20_adult2",
    },
}

#: the validation of food: the fed arms, simulated with the fixed effects of
#: food on the release and the absorption (`GU__FED_f_*`)
FOOD_VALIDATION: NamedMappings = {
    "VazdaSilva2005": {"fm_ome_po20_multi_Mopral_fed"},
}

#: the validation of the limitations of the model: valid data of a population,
#: a formulation or a process the model does not describe, which would distort
#: the fitted parameters of the processes it does describe
LIMITATION_VALIDATION: NamedMappings = {
    # cirrhosis: the shared cirrhosis model of the group (f_cirrhosis 0.60)
    # does not reach the clearance of 67 ml/min
    "Andersson1993": {
        "fm_omeiv20_ome",
        "fm_omeiv20_omeoh",
        "fm_omeiv20_omesul",
        "fm_omeiv20_omemets",
        "fm_omeiv20_amount",
        "fm_omepo40_ome",
        "fm_omepo40_omeoh",
        "fm_omepo40_omesul",
        "fm_omepo40_omemets",
        "fm_omepo40_amount",
    },
    # caplets whose enteric coating fails at a gastric pH of 3-4
    "Elkoshi2002": {"fm_ome20po_OMEX20_SINGLE", "fm_ome20po_OMEX20_MULTIPLE"},
    # fed MUPS tablets, which are not delayed by the meal as the capsules of
    # the food effect of the model are
    "Geus2000": {"fm_ome20_single", "fm_ome20_multi"},
    # pentagastrin, nasogastric aspiration and the emptying of the stomach at
    # 55-60 min are not simulated
    "Lind1983": {"fm_ome_po40"},
    # the evening dose: the model has no circadian rhythm and no meals
    "Prichard1985": {"fm_po40_single_pm", "fm_po40_multi_pm"},
    # the elderly with a clearance of 200 ml/min: the model has no age
    "Regaardh1986": {"fm_iv20_elderly", "fm_po40_elderly"},
}

#: the summaries of data which the fits use one by one, excluded from every
#: fit: the second, bioequivalent product of the same subjects would count the
#: subjects twice
AGGREGATE_MAPPINGS: NamedMappings = {
    "VazdaSilva2001": {"fm_ome_po20_multi_OMP20"},
    "VazdaSilva2005": {
        "fm_ome_po20_multi_Ompranyt_fasting",
        "fm_ome_po20_multi_Ompranyt_fed",
    },
}

#: the validation data by the question it answers
VALIDATION_QUESTIONS: dict[str, NamedMappings] = {
    "interactions": INTERACTION_VALIDATION,
    "doses": DOSE_VALIDATION,
    "populations": POPULATION_VALIDATION,
    "food": FOOD_VALIDATION,
    "limitations": LIMITATION_VALIDATION,
}


def merge(*named_mappings: NamedMappings) -> NamedMappings:
    """Merge named mappings study by study."""
    merged: NamedMappings = {}
    for mappings in named_mappings:
        for sid, keys in mappings.items():
            merged.setdefault(sid, set()).update(keys)
    return merged


#: the validation data
VALIDATION_MAPPINGS: NamedMappings = merge(*VALIDATION_QUESTIONS.values())


def study(fit_mapping: FitMapping) -> str:
    """Get the study of a fit mapping, the id of its experiment."""
    return fit_mapping.reference.experiment.sid


def named(
    mappings: NamedMappings, fit_mapping_key: str, fit_mapping: FitMapping
) -> bool:
    """Check whether a fit mapping is one of the named mappings of its study."""
    return fit_mapping_key in mappings.get(study(fit_mapping), set())


def check_named(mappings: NamedMappings, fit_mappings: FitMappings) -> None:
    """Check that the named mappings are fit mappings of their studies.

    Raises:
        ValueError: for a study which is no experiment, or a key which is no fit
            mapping of its study.
    """
    for sid, keys in mappings.items():
        experiment = fit_mappings.experiments.get(sid)
        if experiment is None:
            raise ValueError(f"'{sid}' is no experiment of the fits.")
        if unknown := sorted(keys - set(experiment._fit_mappings)):
            raise ValueError(f"'{unknown}' are no fit mappings of '{sid}'.")


#: the control data: omeprazole alone in healthy subjects or patients with a
#: duodenal ulcer in remission, fasted or without information on food
filter_control = metadata_filter(
    health={Health.HEALTHY, Health.DUODENAL_ULCER},
    coadministration={Coadministration.NONE},
    excluded={"fasting": {Fasting.FED}},
)


def filter_training(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """The control data, besides the named outliers and validation data."""
    if named(VALIDATION_MAPPINGS, fit_mapping_key, fit_mapping) or named(
        OUTLIER_MAPPINGS, fit_mapping_key, fit_mapping
    ):
        return True
    return filter_control(fit_mapping_key, fit_mapping)


def filter_aggregates(fit_mapping_key: str, fit_mapping: FitMapping) -> bool:
    """No summaries of data which is fitted one by one, see `AGGREGATE_MAPPINGS`."""
    return not named(AGGREGATE_MAPPINGS, fit_mapping_key, fit_mapping)


def pairs(mappings: NamedMappings) -> set[tuple[str, str]]:
    """Get the named mappings as pairs of study and key."""
    return {(sid, key) for sid, keys in mappings.items() for key in keys}


def mapping_collections(
    filters: MappingFilter | list[MappingFilter],
    validation: NamedMappings = VALIDATION_MAPPINGS,
) -> dict[str, list[FitMappingCollection]]:
    """Select the data of a fit from the fit mappings of the studies.

    The filters select the training data, the mappings which fail them are
    excluded, and so are the summaries of data which is fitted one by one
    (`AGGREGATE_MAPPINGS`) and every mapping which is neither control data
    nor named (`filter_training`). The outliers are `OUTLIER_MAPPINGS`, the
    validation data is `VALIDATION_MAPPINGS`. Neither kind enters the cost;
    both are simulated and evaluated with the training data, so a report says
    how the fitted parameters describe data they were not fitted on.

    Args:
        filters: filters of the training data.
        validation: the keys of the validation data by study.

    Returns:
        The fit mapping collections of all kinds by experiment id.

    Raises:
        ValueError: if a mapping is named twice, or an outlier is a mapping of
            no study or of several.
    """
    fit_mappings = FitMappings(
        experiment_classes=EXPERIMENT_CLASSES,
        base_path=OMEPRAZOLE_PATH,
        data_path=DATA_PATHS,
    )
    for mappings in [OUTLIER_MAPPINGS, AGGREGATE_MAPPINGS, validation]:
        check_named(mappings, fit_mappings)
    # a mapping has one role
    roles = [OUTLIER_MAPPINGS, AGGREGATE_MAPPINGS, *VALIDATION_QUESTIONS.values()]
    for i, first in enumerate(roles):
        for second in roles[i + 1 :]:
            if twice := sorted(pairs(first) & pairs(second)):
                raise ValueError(f"The mappings {twice} are named twice.")
    # sbmlsim selects the outliers by their keys alone, which must name one
    # mapping of all studies
    outliers = {key for keys in OUTLIER_MAPPINGS.values() for key in keys}
    for key in outliers:
        studies = [
            sid
            for sid, experiment in fit_mappings.experiments.items()
            if key in experiment._fit_mappings
        ]
        if len(studies) != 1:
            raise ValueError(f"The outlier '{key}' is a mapping of {studies}.")
    selection = fit_mappings.select(
        filters=[
            *(filters if isinstance(filters, list) else [filters]),
            filter_aggregates,
            filter_training,
        ],
        outliers=outliers,
        validation=lambda key, fit_mapping: named(validation, key, fit_mapping),
        print_info=False,
    )
    # the counts per experiment and kind, not the single mappings
    selection.print(detail=False)
    # the validation mappings by the question they answer
    selected = {
        (sid, key)
        for sid, kinds in selection.kinds.items()
        for key, kind in kinds.items()
        if kind is MappingKind.VALIDATION
    }
    console.print(
        "validation: "
        + ", ".join(
            f"{len(selected & pairs(mappings))} {question}"
            for question, mappings in VALIDATION_QUESTIONS.items()
        )
    )
    return selection.collections


def f_collections_pk() -> dict[str, list[FitMappingCollection]]:
    """Pharmacokinetic data."""
    return mapping_collections([])


if __name__ == "__main__":
    console.rule(title=f_collections_pk.__name__, align="left", style="white")
    f_collections_pk()
