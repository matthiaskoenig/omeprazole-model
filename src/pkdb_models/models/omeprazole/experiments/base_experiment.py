"""Base class of the omeprazole simulation experiments."""

from collections.abc import Mapping
from types import MappingProxyType
from typing import ClassVar, NamedTuple

import pandas as pd
from pkpdsim.experiment import PKPDSimulationExperiment
from pkpdsim.impairment import RENAL_COLORS_END_STAGE, RENAL_FUNCTION_GFR
from pkpdsim.metadata import ApplicationForm, Fasting
from sbmlsim import Q
from sbmlsim.units import Quantity

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.omeprazole_pk import calculate_omeprazole_pk


class MolecularWeights(NamedTuple):
    """Molecular weights of omeprazole, its enantiomers and its metabolites."""

    ome: Quantity
    some: Quantity
    rome: Quantity
    omeoh: Quantity
    omesul: Quantity
    omeoth: Quantity


#: the switches of the intestine model for an application form: enteric-coated
#: forms (`GU__f_ec`), buffered solutions and suspensions (no switch) and
#: unprotected solutions and suspensions, which the gastric acid degrades
#: (`GU__f_unprotected`)
_EC: Mapping[str, float] = MappingProxyType({"GU__f_ec": 1.0, "GU__f_unprotected": 0.0})
_BUFFERED: Mapping[str, float] = MappingProxyType(
    {"GU__f_ec": 0.0, "GU__f_unprotected": 0.0}
)
_UNPROTECTED: Mapping[str, float] = MappingProxyType(
    {"GU__f_ec": 0.0, "GU__f_unprotected": 1.0}
)
FORM_CHANGES: Mapping[ApplicationForm, Mapping[str, float]] = MappingProxyType(
    {
        ApplicationForm.CAPSULE: _EC,
        ApplicationForm.TABLET: _EC,
        ApplicationForm.DELAYED_RELEASE_TABLET: _EC,
        ApplicationForm.GRANULES: _EC,
        ApplicationForm.BUFFERED_SOLUTION: _BUFFERED,
        ApplicationForm.SOLUTION: _UNPROTECTED,
        ApplicationForm.SUSPENSION: _UNPROTECTED,
    }
)


class OmeprazoleSimulationExperiment(PKPDSimulationExperiment):
    """Base class of the omeprazole simulation experiments.

    A racemic dose of omeprazole is half S-omeprazole and half R-omeprazole
    (`PODOSE_some`, `PODOSE_rome`, `IVDOSE_*`, infusions `Ri_*`); esomeprazole
    is S-omeprazole. The application form is set with `form_changes` (enteric
    coated, buffered or unprotected solution), food with `fed_changes`. The
    CYP2C19 genotype is the activity `LI__f_cyp2c19` (`cyp2c19_map`), the
    interactions are the activity factors of `LI__f_cyp2c19` and
    `LI__f_cyp3a4` (`F_CYP2C19_*`, `F_CYP3A4_*`, literature based, never
    fitted), the renal function `KI__f_renal_function` (a measured creatinine
    clearance of X ml/min is X/101, `renal_map`), cirrhosis `f_cirrhosis`.
    """

    pkpd_model = MODEL
    selections = (
        "time",
        # dosing
        "IVDOSE_some",
        "IVDOSE_rome",
        "cum_dose_some",
        "cum_dose_rome",
        "PODOSE_some",
        "PODOSE_rome",
        "GU__POEC_some",
        "GU__POEC_rome",
        # venous plasma
        "[Cve_ome]",
        "[Cve_some]",
        "[Cve_rome]",
        "[Cve_omeoh]",
        "[Cve_omesul]",
        "[Cve_omeoth]",
        "[Cve_omemets]",
        "[Cve_ometot]",
        # liver
        "[LI__some]",
        "[LI__rome]",
        "LI__cyp2c19_active",
        "LI__cyp2c19_activity",
        # urine
        "Aurine_omeoh",
        "Aurine_omeoth",
        "Aurine_omemets",
        "KI__OMEMETSEX",
        # feces
        "Afeces_some",
        "Afeces_rome",
        "Afeces_ome",
        "Afeces_omeoth",
        "Afeces_omemets",
        # pharmacodynamics
        "pH",
        "GU__pp_rate",
        "GU__gacid_loss",
        "[GU__protons_stomach]",
        # proton pumps
        "GU__pp_active",
        "GU__pp_inactive",
        "GU__pp_total",
        "GU__pp_synthesis",
        "GU__pp_active_degradation",
        "GU__pp_inactive_degradation",
        # degradation of an unprotected solution (pH dependent)
        "GU__F_ome_pH",
        "GU__F_ome_pH2",
        "GU__F_ome_pH6",
        "GU__F_ome_stomach",
        # cases
        "KI__f_renal_function",
        "KI__GFR",
        "LI__f_cyp2c19",
        "LI__f_cyp3a4",
        "f_cirrhosis",
        "GU__f_ec",
        "GU__f_unprotected",
        "GU__fed",
    )

    font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 22}
    scan_font: ClassVar[dict[str, str | int]] = {"weight": "bold", "size": 15}
    tick_font_size = 15
    suptitle_font_size = 40

    # labels
    label_time = "time"
    label_ome = "omeprazole"
    label_some = "S-omeprazole"
    label_rome = "R-omeprazole"
    label_omeoh = "5-hydroxyomeprazole"
    label_omesul = "omeprazole sulfone"
    label_omeoth = "other metabolites"
    label_omemets = "omeprazole metabolites"
    label_ometot = "omeprazole and metabolites"
    label_omeoh_urine = label_omeoh + "\nurine"
    label_omeoth_urine = label_omeoth + "\nurine"
    label_omemets_urine = label_omemets + "\nurine"
    label_some_feces = label_some + "\nfeces"
    label_rome_feces = label_rome + "\nfeces"
    label_ome_feces = label_ome + "\nfeces"
    label_omemets_feces = label_omemets + "\nfeces"

    labels: ClassVar[Mapping[str, str]] = {
        "time": label_time,
        "[Cve_ome]": label_ome,
        "[Cve_some]": label_some,
        "[Cve_rome]": label_rome,
        "[Cve_omeoh]": label_omeoh,
        "[Cve_omesul]": label_omesul,
        "[Cve_omeoth]": label_omeoth,
        "[Cve_omemets]": label_omemets,
        "[Cve_ometot]": label_ometot,
        # urine
        "Aurine_omeoh": label_omeoh_urine,
        "Aurine_omeoth": label_omeoth_urine,
        "Aurine_omemets": label_omemets_urine,
        "KI__OMEMETSEX": "metabolite excretion rate",
        # feces
        "Afeces_some": label_some_feces,
        "Afeces_rome": label_rome_feces,
        "Afeces_ome": label_ome_feces,
        "Afeces_omeoth": label_omemets_feces,
        "Afeces_omemets": label_omemets_feces,
        # liver
        "LI__cyp2c19_active": "active CYP2C19",
        "LI__cyp2c19_activity": "CYP2C19 activity",
        # pharmacodynamics
        "pH": "stomach pH",
        "GU__pp_active": "active proton pumps",
        "KI__GFR": "GFR",
    }

    unit_time = "hr"
    unit_metabolite = "µM"
    unit_metabolite_urine = "µmole"
    unit_metabolite_feces = "µmole"
    unit_ome = unit_metabolite
    unit_some = unit_metabolite
    unit_rome = unit_metabolite
    unit_omeoh = unit_metabolite
    unit_omesul = unit_metabolite
    unit_omeoth = unit_metabolite
    unit_omemets = unit_metabolite
    unit_ometot = unit_metabolite
    unit_omeoh_urine = unit_metabolite_urine
    unit_omemets_urine = unit_metabolite_urine
    unit_omemets_feces = unit_metabolite_feces

    units: ClassVar[Mapping[str, str]] = {
        "time": unit_time,
        "[Cve_ome]": unit_ome,
        "[Cve_some]": unit_some,
        "[Cve_rome]": unit_rome,
        "[Cve_omeoh]": unit_omeoh,
        "[Cve_omesul]": unit_omesul,
        "[Cve_omeoth]": unit_omeoth,
        "[Cve_omemets]": unit_omemets,
        "[Cve_ometot]": unit_ometot,
        # urine
        "Aurine_omeoh": unit_metabolite_urine,
        "Aurine_omeoth": unit_metabolite_urine,
        "Aurine_omemets": unit_omemets_urine,
        "KI__OMEMETSEX": "µmole/min",
        # feces
        "Afeces_some": unit_metabolite_feces,
        "Afeces_rome": unit_metabolite_feces,
        "Afeces_ome": unit_metabolite_feces,
        "Afeces_omeoth": unit_metabolite_feces,
        "Afeces_omemets": unit_omemets_feces,
        # liver
        "LI__cyp2c19_active": "dimensionless",
        "LI__cyp2c19_activity": "dimensionless",
        # pharmacodynamics
        "pH": "dimensionless",
        "GU__pp_active": "dimensionless",
        "KI__GFR": "ml/min",
    }

    # ----------- Renal map --------------
    # the renal function of the classes of renal impairment relative to the
    # GFR of 101 ml/min of the model (`KI__GFR_base`); a measured creatinine
    # clearance of X ml/min is the renal function X/101
    renal_map = RENAL_FUNCTION_GFR
    renal_colors = RENAL_COLORS_END_STAGE

    # ----------- CYP2C19 genotype --------------
    #: activity of the CYP2C19 alleles relative to *1 (CPIC/PharmGKB allele
    #: functions: *2, *3 no function, *17 increased function)
    cyp2c19_allele_activity: ClassVar[Mapping[str, float]] = MappingProxyType(
        {
            "*1": 1.0,
            "*2": 0.0,
            "*3": 0.0,
            "*17": 1.5,
        }
    )
    #: activity of CYP2C19 (`LI__f_cyp2c19`) of the phenotypes, the mean
    #: activity of the two alleles: extensive metabolizers *1/*1, intermediate
    #: metabolizers *1/*2 or *1/*3, poor metabolizers *2/*2, *2/*3, *3/*3,
    #: rapid metabolizers *1/*17, ultrarapid metabolizers *17/*17
    cyp2c19_map: ClassVar[Mapping[str, float]] = MappingProxyType(
        {
            "extensive": 1.0,
            "EM": 1.0,
            "intermediate": 0.5,
            "IM": 0.5,
            "poor": 0.0,
            "PM": 0.0,
            "rapid": 1.25,
            "RM": 1.25,
            "ultrarapid": 1.5,
            "UM": 1.5,
        }
    )
    cyp2c19_colors: ClassVar[Mapping[str, str]] = MappingProxyType(
        {
            "extensive": "tab:blue",
            "EM": "tab:blue",
            "intermediate": "tab:orange",
            "IM": "tab:orange",
            "poor": "tab:red",
            "PM": "tab:red",
            "rapid": "tab:green",
            "RM": "tab:green",
            "ultrarapid": "tab:purple",
            "UM": "tab:purple",
        }
    )

    # ----------- Interactions --------------
    #: hepatic CYP3A4 activity with clarithromycin 500 mg bid, a strong
    #: mechanism-based inhibitor of CYP3A4: the clearance of IV midazolam is
    #: 64 % lower after 7 days of clarithromycin 500 mg bid (Gorski1998), a
    #: residual hepatic activity of 0.36. Observed for esomeprazole 40 mg qd:
    #: AUC 13.3 -> 22.7 µmol*h/l (x1.7) at day 7 (Andersson2001 Fig9)
    F_CYP3A4_CLARITHROMYCIN: ClassVar[float] = 0.36
    #: CYP2C19 activity with a combined oral contraceptive (ethinylestradiol
    #: 40 µg + levonorgestrel 75 µg), ethinylestradiol is a mechanism-based
    #: inhibitor of CYP2C19: omeprazole AUC x1.38 and AUC ratio
    #: omeprazole/5-hydroxyomeprazole x1.48 (Palovaara2003); with a fraction
    #: of 0.8 of CYP2C19 in the clearance 1 - 1/1.38 = 0.8 * (1 - f), f = 0.67;
    #: levonorgestrel alone has no effect
    F_CYP2C19_ETHINYLESTRADIOL: ClassVar[float] = 0.67

    dose_colors: ClassVar[Mapping[int, str]] = MappingProxyType(
        {
            10: "black",
            20: "tab:blue",
            40: "tab:orange",
            80: "tab:purple",
            90: "tab:red",
        }
    )

    Mr: ClassVar[MolecularWeights] = MolecularWeights(
        ome=Q(345.416, "g/mole"),
        some=Q(345.416, "g/mole"),
        rome=Q(345.416, "g/mole"),
        omeoh=Q(361.415, "g/mole"),
        omesul=Q(361.42, "g/mole"),
        omeoth=Q(375.4, "g/mole"),
    )

    @staticmethod
    def form_changes(form: ApplicationForm) -> dict[str, Quantity]:
        """Get the changes of the intestine model for an oral application form.

        Enteric-coated forms (capsule, tablet, delayed release tablet,
        granules) release omeprazole with a delay; buffered solutions are
        absorbed fast; unprotected solutions and suspensions are degraded by
        the gastric acid.

        Args:
            form: the application form of the study.

        Returns:
            The changes of `GU__f_ec` and `GU__f_unprotected`.

        Raises:
            ValueError: if the form is not an oral form of omeprazole.
        """
        if form not in FORM_CHANGES:
            raise ValueError(f"No oral form of omeprazole: {form}")
        return {k: Q(v, "dimensionless") for k, v in FORM_CHANGES[form].items()}

    @staticmethod
    def fed_changes(fasting: Fasting) -> dict[str, Quantity]:
        """Get the changes of the intestine model for the fasting state.

        Args:
            fasting: the fasting state of the study; not reported is fasted.

        Returns:
            The change of `GU__fed`.
        """
        return {"GU__fed": Q(1.0 if fasting == Fasting.FED else 0.0, "dimensionless")}

    def calculate_omeprazole_pk(
        self, scans: list[str] | None = None
    ) -> dict[str, pd.DataFrame]:
        """Calculate the pharmacokinetic parameters of the simulations.

        Args:
            scans: keys of the simulations (scans), by default all simulations.

        Returns:
            The parameters by key of the simulation, one row per simulation of a
            scan and analyte, see `omeprazole_pk.calculate_omeprazole_pk`.
        """
        keys = scans if scans else list(self._simulations)
        across = None if self.uncertainty is None else self.uncertainty.id
        return {
            key: calculate_omeprazole_pk(
                experiment=self, res=self.results[f"task_{key}"], across=across
            )
            for key in keys
        }
