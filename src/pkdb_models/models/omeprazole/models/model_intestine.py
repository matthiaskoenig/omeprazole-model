"""Intestine model of omeprazole: application forms, absorption and the stomach pH.

Omeprazole is an acid labile benzimidazole: an unprotected solution is degraded
by the gastric acid, depending on the stomach pH (`F_ome_pH`); the clinical
forms protect it, either by a bicarbonate buffer (buffered solution or
suspension, fast absorption, tmax 0.2-0.3 hr [Andersson1990a, Regaardh1990])
or by an enteric coating (capsules with enteric-coated pellets, tablets, MUPS,
granules), which delays the release until the pellets reach the small
intestine (tmax 1.5-2.5 hr, no omeprazole before 0.5-1.5 hr [Oh2012,
Elkoshi2002, Palovaara2003]). Omeprazole is absorbed completely; the
bioavailability below 1 is the hepatic first pass. Food delays the absorption
of the enteric-coated forms and lowers it (high-fat breakfast at steady state:
Cmax x0.34-0.40, AUC x0.62-0.66, tmax +1.5 to +3 hr [VazdaSilva2005]).

The other metabolites (`omeoth`) reach the lumen with the bile and are
excreted in the feces.

The stomach pH is described by the proton pumps of the parietal cells, which
omeprazole inhibits irreversibly.
"""

from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    Parameter,
    RateRule,
    Reaction,
    Species,
    UnitDefinition,
    create_model,
)
from sbmlutils.metadata import BQB, SBO

from pkdb_models.models.omeprazole.models import annotations, templates
from pkdb_models.models.omeprazole.models.fits import FITS


class U(templates.U):
    """UnitDefinitions."""

    per_hr = UnitDefinition("per_hr", "1/hr")
    mg_per_min = UnitDefinition("mg_per_min", "mg/min")
    min_per_hr = UnitDefinition("min_per_hr", "min/hour")
    per_mmole = UnitDefinition("per_mmole", "1/mmole")


_m = Model(
    "omeprazole_intestine",
    name="Model for omeprazole absorption in the intestine",
    # the trailing spaces inside the code spans are part of the SBML notes
    notes="""
    # Model for omeprazole absorption in the intestine and the stomach pH

    ## Application forms
    The oral dose is in the stomach (`PODOSE_<sid>`, mg). The form is set by
    the switches `f_ec` and `f_unprotected`:
    - buffered solution or suspension (`f_ec = 0`, `f_unprotected = 0`): the
      dose enters the intestinal lumen with `Ka_dis_ome`, no degradation.
    - unprotected solution or suspension (`f_ec = 0`, `f_unprotected = 1`):
      the fraction `F_ome_pH` (depending on the stomach pH) enters the lumen,
      the rest is degraded by the gastric acid.
    - enteric-coated form (`f_ec = 1`): the pellets leave the stomach with
      `Ka_ec_ome` (`POEC_<sid>`, mg, pellets in the small intestine) and
      release omeprazole with the same rate into the lumen: a delayed release
      (two steps), no degradation.
    - food (`fed = 1`): the gastric emptying and the dissolution are slower
      by `FED_f_dissolution`, the fraction absorbed is `FED_f_absorption`.

    ## Absorption
    S- and R-omeprazole are absorbed with `OMEABS_k`, completely
    (`F_ome_abs = 1`, no unchanged omeprazole in the feces); the
    bioavailability is the hepatic first pass.

    ## Proton pumps and stomach pH
    The model describes the change in stomach pH depending on omeprazole. A key
    component are the proton pumps in the parietal cells.

    - proton-pumps (PP) in gastric wall (gastric parietal cells, protein amount)
    - PP can be inhibited by omeprazole in the gastric wall; the activation processes
      from omeprazole to the active inhibitor in the gastric wall are not modeled in
      detail, but omeprazole was assumed to directly inhibit the PPs.
    - inhibition of PP converts the active in the inactive form
    - PP have a continuous turnover consisting of PP protein synthesis and PP
      degradation. The newly synthesized PP protein is active. Active and inactive PP
      are degraded identically.
    - pH in the stomach is modeled by calculating the amount of protons in the stomach.
    - PP (active) can secrete protons in the lumen (-> decrease pH)
    - only omeprazole, but not the omeprazole metabolites were assumed to have proton
      pump inhibitor (PPI) activity.

    ```
    PP (active) + OME -> PP-OME (inactive)
    --synthesis--> PP (active)
    PP (active) --degradation-->
    PP-OME (inactive) --degradation-->
    ```

    ## pH calculation
    - pH is calculated as decimal logarithm of reciprocal hydrogen ion activity
      `pH = - log10 ([H+])`. `[H+]` is in [mole/litre] = [mmole/litre] in stomach
      volume.
    - The normal stomach pH values are: pH=1-3

    ## gastric acid secretion
    - A typical adult human stomach will secrete about 1.5 liters of gastric acid daily.
    - Stomach volume is around 100 [ml]
    - PP pump H+ into [gastric acid]; `[gastric acid] --1.5 [l/day]-->
      [stomach (100[ml])] --1.5 [l/day]-->`.
    - `1.5 [l/day] = 1.5 [l/day]/(24*60 [min/day])* 1000 [ml/l] = 1.04 [ml/min]`
    - acid output basal: `4.3 [mmole (H+)/hr] placebo => 4.3 mmole/100 ml
      = 0.043 mmole/ml = 43 mole/litre (in 1 hr)`.
      `Delta pH (1 hr) = - log10(43) = -1.63`
    - stimulated (food stimulated): ~ 8 [mmole (H+)/hr] = 70-80 [mole/litre].
      `Delta pH (1 hr) = - log10(350) = -1.88`
    - stimulated (pentagastrin): 35 [mmole (H+)/hr] = 350 [mole/litre].
      `Delta pH (1 hr) = - log10(350) = -2.54`

    ## pH changes
    Stomach pH should be ~1-3 pH at steady state and go up to ~7 pH at maximum PP
    inhibition at 80-90%.
    """
    + terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
)

_m.compartments = [
    Compartment(
        "Vext",
        1.0,
        name="plasma",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["plasma"],
    ),
    Compartment(
        "Vlumen",
        1.2825 * 0.9,
        name="intestinal lumen (inner part of intestine)",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        constant=False,
        port=True,
        annotations=annotations.compartments["gu_lumen"],
    ),
    Compartment(
        "Vfeces",
        metaId="meta_Vfeces",
        value=1,
        unit=U.liter,
        constant=True,
        name="feces",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        port=True,
        annotations=annotations.compartments["feces"],
    ),
    Compartment(
        "Vstomach",
        metaId="meta_Vstomach",
        value=1,
        unit=U.liter,
        constant=True,
        name="stomach",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        port=True,
        annotations=annotations.compartments["stomach"],
    ),
    Compartment(
        "Vpar",
        1.0,
        name="parietal cells",
        unit=U.liter,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments["parietal cell"],
        notes="""The proton pumps are dimensionless amounts, the volume is not used.""",
    ),
]

#: S- and R-omeprazole
ENANTIOMERS: dict[str, str] = {"some": "S-omeprazole", "rome": "R-omeprazole"}

_m.species = []
for sid, sname in ENANTIOMERS.items():
    _m.species.extend(
        [
            Species(
                f"{sid}_stomach",
                metaId=f"meta_{sid}_stomach",
                initialConcentration=0.0,
                compartment="Vstomach",
                substanceUnit=U.mmole,
                name=f"{sname} (stomach)",
                hasOnlySubstanceUnits=True,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                boundaryCondition=True,
                notes="""
                Placeholder of the dose, which is the parameter `PODOSE_<sid>`
                (stomach) and `POEC_<sid>` (enteric-coated pellets in the
                small intestine) in mg.
                """,
            ),
            Species(
                f"{sid}_lumen",
                initialConcentration=0.0,
                name=f"{sname} (intestinal lumen)",
                compartment="Vlumen",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            ),
            Species(
                f"{sid}_ext",
                initialConcentration=0.0,
                name=f"{sname} (plasma)",
                compartment="Vext",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            ),
            Species(
                f"{sid}_feces",
                initialConcentration=0.0,
                name=f"{sname} (feces)",
                compartment="Vfeces",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=True,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            ),
        ]
    )

_m.species.extend(
    [
        Species(
            "omeoth_lumen",
            initialConcentration=0.0,
            name="other omeprazole metabolites (intestinal lumen)",
            compartment="Vlumen",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=False,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["omeoth"],
            port=True,
        ),
        Species(
            "omeoth_feces",
            initialConcentration=0.0,
            name="other omeprazole metabolites (feces)",
            compartment="Vfeces",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["omeoth"],
            port=True,
        ),
        # pH regulation stomach
        Species(
            "protons_stomach",
            initialConcentration=10.0,
            name="H+ (stomach gastric fluid)",
            compartment="Vstomach",
            substanceUnit=U.mmole,
            hasOnlySubstanceUnits=False,
            port=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["proton"],
            # the trailing space of the code block is part of the SBML notes
            notes="""
            Typical stomach pH of: `pH = 1-3; pH=2.0`
            Calculation of proton concentration as:
            ```
            pH = -log10(H+) => H+ = 10^-pH = 10^-2 = 0.01 [mole/litre] = 10 [mmole/l]
               = 10 [mM]
            ```
            """,
        ),
        Species(
            "pp_active",
            initialAmount=1.0,
            name="proton pump (active)",
            compartment="Vpar",
            substanceUnit=U.dimensionless,
            constant=False,
            hasOnlySubstanceUnits=True,
            conversionFactor="cf_species_dimensionless",
            sboTerm=SBO.MACROMOLECULE,
            annotations=[
                (BQB.IS_VERSION_OF, "omit/0017846"),  # Proton Pumps
            ],
        ),
        Species(
            "pp_inactive",
            initialAmount=0.0,
            name="proton pump (inactive)",
            compartment="Vpar",
            substanceUnit=U.dimensionless,
            constant=False,
            hasOnlySubstanceUnits=True,
            conversionFactor="cf_species_dimensionless",
            sboTerm=SBO.MACROMOLECULE,
            annotations=[
                (BQB.IS_VERSION_OF, "omit/0017846"),  # Proton Pumps
            ],
        ),
    ]
)

_m.parameters = [
    Parameter(
        "pH",
        value=2.0,
        unit=U.dimensionless,
        name="pH value stomach",
        constant=False,
        port=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "Qstomach",
        0.01,
        unit=U.l_per_min,
        name="stomach fluid loss",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        loss of stomach fluid to intestine
        """,
    ),
    Parameter(
        sid="cf_species_dimensionless",
        value=1.0,
        unit=U.per_mmole,
        name="dimensionless species conversion",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # application forms
    Parameter(
        "f_ec",
        0,
        U.dimensionless,
        name="enteric-coated form (0 solution or suspension, 1 enteric-coated)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        1: capsule with enteric-coated pellets, enteric-coated tablet, MUPS
        tablet, enteric-coated granules; 0: solution or suspension. Set by the
        experiments from the application form.
        """,
    ),
    Parameter(
        "f_unprotected",
        0,
        U.dimensionless,
        name="unprotected solution (0 buffered or enteric-coated, 1 unprotected)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        1: a solution or suspension without bicarbonate buffer, which the
        gastric acid degrades (`F_ome_pH`); 0: buffered solution or suspension
        and the enteric-coated forms. Set by the experiments.
        """,
    ),
    Parameter(
        "Ka_dis_ome",
        30.0,
        U.per_hr,
        name="rate of the gastric emptying of a solution",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Gastric emptying of a buffered solution: tmax 0.2-0.3 hr
        [Andersson1990a, Andersson1993, Naesdal1986, Regaardh1990]. Fast,
        not fitted: the absorption `OMEABS_k` limits the uptake, the fits
        spread the rate over 9-60 /hr at the same cost.
        """,
    ),
    Parameter(
        "Ka_ec_ome",
        **FITS.parameter("GU__Ka_ec_ome", unit=U.per_hr),
        name="rate of the gastric emptying and the release of an enteric-coated form",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The enteric-coated pellets leave the stomach and dissolve in the small
        intestine, both with this rate (a delayed release): tmax 1.5-2.5 hr
        [Elkoshi2002, Palovaara2003, Uno2007].
        """,
    ),
    Parameter(
        "fed",
        0,
        U.dimensionless,
        name="fed state (0 fasted, 1 fed)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "FED_f_dissolution",
        0.35,
        U.dimensionless,
        name="fed effect on the gastric emptying and dissolution",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        A meal slows the gastric emptying of the enteric-coated pellets: tmax
        +1.5 to +3 hr, Cmax x0.34-0.40 (VazdaSilva2005, high-fat breakfast).
        Not fitted (one study).
        """,
    ),
    Parameter(
        "FED_f_absorption",
        0.65,
        U.dimensionless,
        name="fed effect on the fraction absorbed",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        A meal lowers the exposure: AUC x0.62-0.66 at steady state
        (VazdaSilva2005, high-fat breakfast). Not fitted (one study).
        """,
    ),
    Parameter(
        "F_ome_abs",
        1.0,
        U.dimensionless,
        name="fraction absorbed omeprazole",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Omeprazole is absorbed completely: the urinary recovery of the
        radioactivity is the same after IV and oral doses, no unchanged
        omeprazole in the feces [Regaardh1986, Andersson1993]. Not fitted.
        """,
    ),
    Parameter(
        "OMEABS_k",
        **FITS.parameter("GU__OMEABS_k", unit=U.per_min),
        name="rate of omeprazole absorption",
        sboTerm=SBO.KINETIC_CONSTANT,
    ),
    Parameter(
        "OMEOTHEXC_k",
        0.0007,
        U.per_min,
        name="rate of the fecal excretion of the other metabolites",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Transit of the metabolites of the bile from the intestinal lumen into
        the feces, half-life about 16 hr. Not fitted.
        """,
    ),
    Parameter(
        "Mr_ome",
        345.416,
        U.g_per_mole,
        name="Molecular weight omeprazole [g/mole]",
        sboTerm=SBO.MOLECULAR_MASS,
    ),
    # acid degradation of an unprotected solution
    Parameter(
        "F_ome_pH2",
        0.35,
        U.dimensionless,
        name="fraction not degraded at pH 2",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "F_ome_pH6",
        1.0,
        U.dimensionless,
        name="fraction not degraded at pH 6",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "F_ome_KpH",
        4,
        U.dimensionless,
        name="midpoint of the pH effect on the degradation",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    Parameter(
        "F_ome_n",
        2,
        U.dimensionless,
        name="Hill coefficient of the pH effect on the degradation",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
]

_m.rules = [
    AssignmentRule(
        "pp_total",
        "pp_active + pp_inactive",
        unit=U.dimensionless,
        name="total proton pump",
        sboTerm=SBO.MASS_CONSERVATION_LAW,
    ),
    AssignmentRule(
        "pH",
        "-log10(protons_stomach/1000 mM)",
        metaId="_meta_pH_rule",
        unit=U.dimensionless,
        name="pH",
        sboTerm=SBO.CONVENIENCE_FUNCTION,
        annotations=[
            (BQB.IS, "ncit/C45997"),  # pH
        ],
        notes="""
        pH calculation with conversion of stomach proton concentration:
        `[mmole/l] -> [mole/l]`
        """,
    ),
    AssignmentRule(
        "F_ome_pH",
        "F_ome_pH2 + (F_ome_pH6 - F_ome_pH2) * "
        "power(max(0 dimensionless, pH - 2 dimensionless), F_ome_n)/"
        "(power(max(0 dimensionless, pH - 2 dimensionless), F_ome_n) + power(F_ome_KpH, F_ome_n))",
        unit=U.dimensionless,
        name="fraction of an unprotected solution not degraded in the stomach",
        notes="""
        Sigmoidal interpolation between F_ome_pH2 and F_ome_pH6: omeprazole is
        unstable at a low pH. Only for unprotected solutions (`f_unprotected`).
        """,
    ),
    AssignmentRule(
        "F_ome_stomach",
        "1 dimensionless - f_unprotected * (1 dimensionless - F_ome_pH)",
        unit=U.dimensionless,
        name="fraction of a solution not degraded in the stomach",
    ),
    AssignmentRule(
        "Ka_emptying",
        "(1 dimensionless + fed * (FED_f_dissolution - 1 dimensionless)) * "
        "((1 dimensionless - f_ec) * Ka_dis_ome + f_ec * Ka_ec_ome)",
        unit=U.per_hr,
        name="rate of the gastric emptying of the form",
    ),
    AssignmentRule(
        "F_ome_abs_eff",
        "F_ome_abs * (1 dimensionless + fed * (FED_f_absorption - 1 dimensionless))",
        unit=U.dimensionless,
        name="fraction absorbed omeprazole (fed state)",
    ),
]

_m.reactions = [
    # ---------------
    # protons and pH
    # ---------------
    Reaction(
        sid="pp_rate",
        name="Proton secretion by proton pump",
        pars=[
            Parameter(
                "pp_rate_k",
                1e-1,
                U.mmole_per_min,
                name="Rate of proton secretion",
                sboTerm=SBO.FORWARD_RATE_CONSTANT,
            ),
        ],
        formula=(
            "pp_rate_k*power(10 dimensionless, (-1.1 dimensionless/(pp_active + 0.1 dimensionless) + 1 dimensionless))",
            U.mmole_per_min,
        ),
        equation="-> protons_stomach [pp_active]",
        sboTerm=SBO.IRREVERSIBLE_PROCESS,
    ),
    Reaction(
        sid="gacid_loss",
        name="Gastric acid loss to intestine",
        formula=("Qstomach * protons_stomach", U.mmole_per_min),
        equation="protons_stomach -> ",
        sboTerm=SBO.IRREVERSIBLE_PROCESS,
    ),
    # ---------------
    # proton pumps
    # ---------------
    Reaction(
        sid="ppi",
        name="PP inhibition",
        pars=[
            Parameter(
                "ppi_k",
                5.0,
                U.l_per_min,
                name="Inhibition rate PP",
                sboTerm=SBO.FORWARD_RATE_CONSTANT,
            ),
        ],
        formula=("ppi_k * pp_active * (some_ext + rome_ext)", U.mmole_per_min),
        equation="pp_active -> pp_inactive [some_ext, rome_ext]",
        sboTerm=SBO.INHIBITION,
    ),
    Reaction(
        sid="pp_synthesis",
        name="PP synthesis",
        pars=[
            Parameter(
                "pp_synthesis_k",
                4e-4,
                U.mmole_per_min,
                name="Synthesis rate PP",
                sboTerm=SBO.FORWARD_RATE_CONSTANT,
            ),
        ],
        formula=("pp_synthesis_k", U.mmole_per_min),
        equation="-> pp_active",
        sboTerm=SBO.IRREVERSIBLE_PROCESS,
        notes="""
        **steady state**
        ```
        pp_synthesis = pp_active_degradation (with pp_active = 1 [dimensionless])
        pp_synthesis_k = pp_degradation_k * pp_active
        pp_active = pp_synthesis_k/pp_degradation_k
        ```
        """,
    ),
    Reaction(
        sid="pp_active_degradation",
        name="degradation PP active",
        pars=[
            Parameter(
                "pp_degradation_k",
                4e-4,
                U.mmole_per_min,
                name="Degradation rate PP",
                sboTerm=SBO.FORWARD_RATE_CONSTANT,
            ),
        ],
        formula=("pp_degradation_k * pp_active", U.mmole_per_min),
        equation="pp_active -> ",
        sboTerm=SBO.IRREVERSIBLE_PROCESS,
    ),
    Reaction(
        sid="pp_inactive_degradation",
        name="degradation PP inactive",
        formula=("pp_degradation_k * pp_inactive", U.mmole_per_min),
        equation="pp_inactive -> ",
        sboTerm=SBO.IRREVERSIBLE_PROCESS,
        notes="""
        Identical kinetics to degradation of active PP.
        """,
    ),
    # ---------------
    # metabolites of the bile
    # ---------------
    Reaction(
        sid="OMEOTHEXC",
        name="excretion other metabolites (feces)",
        compartment="Vlumen",
        equation="omeoth_lumen -> omeoth_feces",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=("OMEOTHEXC_k * Vlumen * omeoth_lumen", U.mmole_per_min),
    ),
]

_m.rate_rules = []

for sid, sname in ENANTIOMERS.items():
    _m.parameters.extend(
        [
            Parameter(
                f"PODOSE_{sid}",
                0,
                U.mg,
                constant=False,
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                name=f"oral dose {sname} in the stomach [mg]",
                port=True,
            ),
            Parameter(
                f"POEC_{sid}",
                0,
                U.mg,
                constant=False,
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                name=f"enteric-coated {sname} in the small intestine [mg]",
            ),
        ]
    )
    _m.rules.extend(
        [
            AssignmentRule(
                f"emptying_{sid}",
                f"Ka_emptying/60 min_per_hr * PODOSE_{sid}/Mr_ome",
                unit=U.mmole_per_min,
                name=f"gastric emptying {sname}",
            ),
            AssignmentRule(
                f"absorption_{sid}",
                f"OMEABS_k * Vlumen * {sid}_lumen",
                unit=U.mmole_per_min,
                name=f"absorption {sname}",
            ),
        ]
    )
    _m.reactions.extend(
        [
            Reaction(
                sid=f"dissolution_{sid}",
                name=f"gastric emptying of the solution {sname}",
                formula=(
                    f"(1 dimensionless - f_ec) * F_ome_stomach * emptying_{sid}",
                    U.mmole_per_min,
                ),
                equation=f"{sid}_stomach -> {sid}_lumen",
                compartment="Vlumen",
                sboTerm=SBO.TRANSPORT_REACTION,
            ),
            Reaction(
                sid=f"degradation_{sid}",
                name=f"acid degradation {sname}",
                formula=(
                    f"(1 dimensionless - f_ec) * (1 dimensionless - F_ome_stomach) * emptying_{sid}",
                    U.mmole_per_min,
                ),
                equation=f"{sid}_stomach -> [protons_stomach]",
                compartment="Vlumen",
                sboTerm=SBO.BIOCHEMICAL_REACTION,
            ),
            Reaction(
                sid=f"release_{sid}",
                name=f"release from the enteric-coated pellets {sname}",
                formula=(
                    f"(1 dimensionless + fed * (FED_f_dissolution - 1 dimensionless)) * "
                    f"Ka_ec_ome/60 min_per_hr * POEC_{sid}/Mr_ome",
                    U.mmole_per_min,
                ),
                equation=f"{sid}_stomach -> {sid}_lumen",
                compartment="Vlumen",
                sboTerm=SBO.TRANSPORT_REACTION,
            ),
            Reaction(
                f"{sid.upper()}ABS",
                name=f"absorption {sname}",
                equation=f"{sid}_lumen -> {sid}_ext",
                sboTerm=SBO.TRANSPORT_REACTION,
                compartment="Vlumen",
                formula=(f"F_ome_abs_eff * absorption_{sid}", U.mmole_per_min),
            ),
            Reaction(
                f"{sid.upper()}EXC",
                name=f"excretion {sname} (feces)",
                compartment="Vlumen",
                equation=f"{sid}_lumen -> {sid}_feces",
                sboTerm=SBO.TRANSPORT_REACTION,
                formula=(
                    f"(1 dimensionless - F_ome_abs_eff) * absorption_{sid}",
                    U.mmole_per_min,
                ),
            ),
        ]
    )
    _m.rate_rules.extend(
        [
            RateRule(
                f"PODOSE_{sid}",
                f"-emptying_{sid} * Mr_ome",
                U.mg_per_min,
                name=f"gastric emptying {sname}",
            ),
            RateRule(
                f"POEC_{sid}",
                f"(f_ec * emptying_{sid} - release_{sid}) * Mr_ome",
                U.mg_per_min,
                name=f"enteric-coated pellets {sname}",
            ),
        ]
    )

model_intestine = _m


if __name__ == "__main__":
    from pkdb_models.models.omeprazole import MODEL_BASE_PATH

    result = create_model(
        filepath=MODEL_BASE_PATH / f"{model_intestine.sid}.xml",
        model=model_intestine,
        sbml_level=3,
        sbml_version=2,
    )
