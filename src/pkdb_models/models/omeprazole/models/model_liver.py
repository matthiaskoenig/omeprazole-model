"""Liver model of omeprazole: the metabolism of S- and R-omeprazole.

The enantiomers S-omeprazole (esomeprazole, `some`) and R-omeprazole (`rome`)
are cleared by the hepatic cytochromes CYP2C19 and CYP3A4 [Abelo2000,
Andersson2001]:

- R-omeprazole: CYP2C19 to 5-hydroxyomeprazole (`omeoh`), CYP3A4 to
  omeprazole sulfone (`omesul`) and a fraction `f_rome_cyp3a4_omeoh` to
  5-hydroxyomeprazole (the 5-hydroxyomeprazole of poor metabolizers).
- S-omeprazole: CYP2C19 mainly to 5-O-desmethylomeprazole (in the pool of the
  other metabolites `omeoth`), a fraction `f_some_omeoh` to
  5-hydroxyomeprazole, CYP3A4 to omeprazole sulfone. The 5-hydroxyomeprazole
  comes from R-omeprazole, the sulfone from S-omeprazole (HassanAlin2005 Tab4:
  5-OH AUC 1.59 from R, 0.11 from S; sulfone AUC 1.53 from S, 0.11 from R).

The 5-hydroxyomeprazole and the sulfone are metabolized further to the
secondary metabolites (5-hydroxyomeprazole sulfone, the carboxylic acid; pool
`omeoth`): the 5-hydroxyomeprazole formed in the liver is partly released into
the plasma (`OMEOHEX`) and partly oxidized before it leaves the liver
(`OMEOHM`); the sulfone is cleared by CYP2C19 and a CYP2C19 independent route
(half-life 2-2.6 hr in extensive, 7.5-11 hr in poor metabolizers
[Regaardh1990, HassanAlin2000]). The other metabolites are excreted into the
bile (feces 17-19 % of the dose [Regaardh1986, Regaardh1990]) and the urine.

Omeprazole inactivates CYP2C19 (mechanism-based inhibition [Ogilvie2011]):
the fraction of active CYP2C19 (`cyp2c19_active`) is lost with the
omeprazole concentration in the liver and resynthesized with the turnover of
the enzyme, which increases the exposure on repeated doses (Cederberg1992:
clearance of 40 mg IV 446 to 237 ml/min after 5 days).
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
    create_model,
)
from sbmlutils.metadata import BQB, SBO

from pkdb_models.models.omeprazole.models import annotations, templates
from pkdb_models.models.omeprazole.models.fits import FITS


class U(templates.U):
    """UnitDefinitions."""


_m = Model(
    "omeprazole_liver",
    name="Model for omeprazole metabolism in the liver",
    notes="""
    # Model for omeprazole metabolism in the liver

    S-omeprazole and R-omeprazole exchange fast between the plasma and the
    liver and are metabolized by CYP2C19 and CYP3A4, which act on the liver
    concentration (apparent Michaelis constants of the total concentration).

    - R-omeprazole: CYP2C19 to 5-hydroxyomeprazole, CYP3A4 to omeprazole sulfone.
    - S-omeprazole: CYP2C19 to 5-O-desmethylomeprazole (other metabolites) and
      a fraction to 5-hydroxyomeprazole, CYP3A4 to omeprazole sulfone.
    - 5-hydroxyomeprazole is released into the plasma or oxidized in the liver
      to the other metabolites; omeprazole sulfone exchanges with the plasma and
      is metabolized by CYP2C19 and a CYP2C19 independent route to the other
      metabolites; the other metabolites are excreted into the bile.
    - CYP2C19 activity: genotype and interactions `f_cyp2c19`,
      mechanism-based inactivation by omeprazole `cyp2c19_active`; CYP3A4
      activity: interactions `f_cyp3a4`.
    """
    + terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        (BQB.OCCURS_IN, "fma/FMA:7197"),
        (BQB.OCCURS_IN, "bto/BTO:0000759"),
        (BQB.OCCURS_IN, "ncit/C12392"),
        (BQB.HAS_PROPERTY, "ncit/C79371"),  # Pharmacokinetics: Metabolism
    ],
)

_m.compartments = [
    Compartment(
        "Vext",
        1.5,
        name="plasma",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["plasma"],
    ),
    Compartment(
        "Vli",
        1.5,
        name="liver",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["li"],
    ),
    Compartment(
        "Vlumen",
        1.0,
        name="intestinal lumen (inner part of intestine)",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        constant=False,
        port=True,
        annotations=annotations.compartments["gu_lumen"],
    ),
]

#: the substances of the liver by their id
SUBSTANCES_LIVER: dict[str, str] = {
    "some": "S-omeprazole",
    "rome": "R-omeprazole",
    "omeoh": "5-hydroxyomeprazole",
    "omesul": "omeprazole sulfone",
    "omeoth": "other omeprazole metabolites",
}

_m.species = []
for sid, name in SUBSTANCES_LIVER.items():
    _m.species.extend(
        [
            Species(
                f"{sid}_ext",
                initialConcentration=0.0,
                name=f"{name} (plasma)",
                compartment="Vext",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            ),
            Species(
                sid,
                initialConcentration=0.0,
                name=f"{name} (liver)",
                compartment="Vli",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=False,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
            ),
        ]
    )
_m.species.append(
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
    )
)

_m.parameters = [
    Parameter(
        "f_cyp2c19",
        1.0,
        unit=U.dimensionless,
        name="activity of CYP2C19 (genotype, interactions)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Activity of CYP2C19 relative to the extensive metabolizer (*1/*1):
        the mean activity of the two alleles of the genotype (*1 1.0, *2 and
        *3 0 (no function), *17 1.5 (increased function)), i.e. extensive
        metabolizers 1.0, intermediate metabolizers 0.5 and poor metabolizers
        0; multiplied by the factors of inhibiting drugs. Set by the
        experiments, never fitted.
        """,
    ),
    Parameter(
        "f_cyp3a4",
        1.0,
        unit=U.dimensionless,
        name="activity of CYP3A4 (interactions)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Activity of CYP3A4 relative to the reference; inhibitors < 1, inducers
        > 1. Set by the experiments, never fitted.
        """,
    ),
    Parameter(
        "OMEIM_k",
        10.0,
        unit=U.per_min,
        name="rate of the omeprazole exchange between plasma and liver",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Fast exchange (not fitted): the liver is in equilibrium with its plasma,
        the uptake does not limit the metabolism.
        """,
    ),
    Parameter(
        "CYP2C19_Km",
        0.1,
        unit=U.mM,
        name="Km CYP2C19 omeprazole (apparent, total concentration)",
        sboTerm=SBO.MICHAELIS_CONSTANT_FOR_SUBSTRATE,
        notes="""
        Apparent Michaelis constant of CYP2C19 for S- and R-omeprazole of the
        total concentration in the liver: the Km of the high affinity
        5-hydroxylation of liver microsomes (2.5-6 µM unbound, Andersson et
        al. 1993, Br J Clin Pharmacol 36:521) over the unbound fraction of
        omeprazole (0.05, 95 % bound), about 100 µM. Not fitted: the fits ran
        the Km to the upper bound of 50 µM with a lower cost (265 vs 270), it
        is not identifiable above it. The dose dependence of the
        bioavailability (Andersson1990a: 0.40 at 10 mg, 0.58 at 40 mg) comes
        from the mechanism-based inactivation of CYP2C19 during the first pass
        and the saturation of CYP2C19 at the portal concentrations of the
        larger doses.
        """,
    ),
    Parameter(
        "CYP3A4_Km",
        0.1,
        unit=U.mM,
        name="Km CYP3A4 omeprazole (apparent, total concentration)",
        sboTerm=SBO.MICHAELIS_CONSTANT_FOR_SUBSTRATE,
        notes="""
        Michaelis constant of the CYP3A4 sulfoxidation, high (about 100 µM in
        vitro): linear at clinical doses. Not fitted.
        """,
    ),
    Parameter(
        "f_some_omeoh",
        0.1,
        unit=U.dimensionless,
        name="fraction 5-hydroxyomeprazole of the CYP2C19 metabolism of S-omeprazole",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        CYP2C19 converts S-omeprazole mainly to 5-O-desmethylomeprazole; the
        5-hydroxyomeprazole from S-omeprazole is 7 % of the one from
        R-omeprazole (HassanAlin2005 Tab4: AUC 0.11 vs 1.59 µmol*h/l). Not
        fitted.
        """,
    ),
    Parameter(
        "f_rome_cyp3a4_omeoh",
        **FITS.parameter("LI__f_rome_cyp3a4_omeoh", unit=U.dimensionless),
        name="fraction 5-hydroxyomeprazole of the CYP3A4 metabolism of R-omeprazole",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        CYP3A4 forms 5-hydroxyomeprazole besides the sulfone (the low
        affinity 5-hydroxylation of liver microsomes, Andersson et al. 1993,
        Br J Clin Pharmacol 36:521), the route
        of 5-hydroxyomeprazole in CYP2C19 poor metabolizers: their plasma and
        urine contain 5-hydroxyomeprazole (Sohn1992: Cmax 46 ng/ml, urine 5.6 %
        of the dose against 13.5 % of extensive metabolizers; Uno2007: PO AUC
        364 vs 656 ng*h/ml). The 5-hydroxyomeprazole comes from R-omeprazole
        (HassanAlin2005 Tab4), the fraction is fitted.
        """,
    ),
    # mechanism-based inactivation of CYP2C19
    Parameter(
        "cyp2c19_active",
        1.0,
        unit=U.dimensionless,
        constant=False,
        name="fraction of active CYP2C19",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Fraction of CYP2C19 which is not inactivated by omeprazole, 1 without
        omeprazole.
        """,
    ),
    Parameter(
        "CYP2C19_kdeg",
        0.693 / (26 * 60),
        unit=U.per_min,
        name="degradation rate of CYP2C19",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Turnover of hepatic CYP2C19, half-life 26 hr (the turnover of the
        hepatic CYPs in the models of mechanism-based inhibition [Ohno2007]);
        the active enzyme is resynthesized with this rate. Not fitted.
        """,
    ),
    Parameter(
        "CYP2C19_kinact",
        **FITS.parameter("LI__CYP2C19_kinact", unit=U.per_min),
        name="maximal inactivation rate of CYP2C19 by omeprazole",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Maximal rate of the mechanism-based inactivation of CYP2C19 by S- and
        R-omeprazole (in vitro kinact of the order of 0.01-0.05 1/min
        [Ogilvie2011, Boulenc2012]); fitted on the repeated doses.
        """,
    ),
    Parameter(
        "CYP2C19_KI",
        0.002,
        unit=U.mM,
        name="concentration of half-maximal inactivation of CYP2C19",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        Apparent inactivation constant of the total liver concentration (in
        vitro KI of a few µM [Ogilvie2011, Boulenc2012]): the inactivation is
        saturated at the liver concentrations of a dose. Not fitted: not
        identifiable together with the inactivation rate; a KI of 0.1 mM (the
        in vitro KI over the unbound fraction) gave a higher cost (279.6 vs
        265-270).
        """,
    ),
    Parameter(
        "CYP2C19_Vmax_some",
        **FITS.parameter("LI__CYP2C19_Vmax_some", unit=U.mmole_per_min_l),
        name="Vmax CYP2C19 S-omeprazole",
        sboTerm=SBO.MAXIMAL_VELOCITY,
        notes="""
        The intrinsic clearance of S-omeprazole is about a third of the one of
        R-omeprazole [Abelo2000]: S AUC 2.5 fold R after a single oral dose
        (HassanAlin2005).
        """,
    ),
    Parameter(
        "CYP2C19_Vmax_rome",
        **FITS.parameter("LI__CYP2C19_Vmax_rome", unit=U.mmole_per_min_l),
        name="Vmax CYP2C19 R-omeprazole",
        sboTerm=SBO.MAXIMAL_VELOCITY,
    ),
    Parameter(
        "CYP3A4_Vmax_some",
        **FITS.parameter("LI__CYP3A4_Vmax_some", unit=U.mmole_per_min_l),
        name="Vmax CYP3A4 S-omeprazole",
        sboTerm=SBO.MAXIMAL_VELOCITY,
        notes="""
        The clearance of poor metabolizers of CYP2C19 (IV 50-150 ml/min
        [Regaardh1990, Uno2007]) is the one of CYP3A4; the sulfone comes from
        S-omeprazole.
        """,
    ),
    Parameter(
        "CYP3A4_Vmax_rome",
        **FITS.parameter("LI__CYP3A4_Vmax_rome", unit=U.mmole_per_min_l),
        name="Vmax CYP3A4 R-omeprazole",
        sboTerm=SBO.MAXIMAL_VELOCITY,
    ),
    # metabolites
    Parameter(
        "OMEOHEX_k",
        **FITS.parameter("LI__OMEOHEX_k", unit=U.per_min),
        name="rate of the 5-hydroxyomeprazole release from the liver",
        sboTerm=SBO.KINETIC_CONSTANT,
    ),
    Parameter(
        "OMEOHM_k",
        0.6,
        unit=U.per_min,
        name="rate of the 5-hydroxyomeprazole oxidation in the liver",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        The 5-hydroxyomeprazole of the liver is released into the plasma
        (`OMEOHEX_k`) or oxidized to the secondary metabolites
        (5-hydroxyomeprazole sulfone, carboxyomeprazole); the fraction released
        is OMEOHEX_k/(OMEOHEX_k + OMEOHM_k). In the plasma 5-hydroxyomeprazole
        is excreted by the kidneys.
        """,
    ),
    Parameter(
        "OMEMEX_k",
        10.0,
        unit=U.per_min,
        name="rate of the metabolite exchange between plasma and liver",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Fast exchange of omeprazole sulfone and the other metabolites between
        the liver and its plasma (not fitted).
        """,
    ),
    Parameter(
        "OMESUL2C19_k",
        **FITS.parameter("LI__OMESUL2C19_k", unit=U.per_min),
        name="rate of the CYP2C19 metabolism of omeprazole sulfone",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Omeprazole sulfone is hydroxylated by CYP2C19 to 5-hydroxyomeprazole
        sulfone: half-life 2-2.6 hr in extensive metabolizers
        [Andersson1990a, HassanAlin2000, Palovaara2003].
        """,
    ),
    Parameter(
        "OMESULM_k",
        **FITS.parameter("LI__OMESULM_k", unit=U.per_min),
        name="rate of the CYP2C19 independent metabolism of omeprazole sulfone",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        The sulfone of poor metabolizers has a half-life of 7.5-11 hr
        (Regaardh1990 Tab3): a slow CYP2C19 independent clearance.
        """,
    ),
    Parameter(
        "OMEOTHBIL_k",
        **FITS.parameter("LI__OMEOTHBIL_k", unit=U.per_min),
        name="rate of the biliary excretion of the other metabolites",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        Feces 17-19 % of the radioactivity of an IV or oral dose
        [Regaardh1986, Regaardh1990], no unchanged omeprazole.
        """,
    ),
]

_m.rules = [
    AssignmentRule(
        "cyp2c19_activity",
        "f_cyp2c19 * cyp2c19_active",
        unit=U.dimensionless,
        name="activity of CYP2C19",
        notes="""Genotype and interactions times the fraction not inactivated.""",
    ),
    AssignmentRule(
        "SOMECYP2C19_rate",
        "cyp2c19_activity * CYP2C19_Vmax_some * Vli * some/(CYP2C19_Km + some)",
        unit=U.mmole_per_min,
        name="rate of the CYP2C19 metabolism of S-omeprazole",
    ),
    AssignmentRule(
        "ROMECYP3A4_rate",
        "f_cyp3a4 * CYP3A4_Vmax_rome * Vli * rome/(CYP3A4_Km + rome)",
        unit=U.mmole_per_min,
        name="rate of the CYP3A4 metabolism of R-omeprazole",
    ),
]

_m.rate_rules = [
    RateRule(
        "cyp2c19_active",
        "CYP2C19_kdeg * (1 dimensionless - cyp2c19_active) - "
        "CYP2C19_kinact * cyp2c19_active * (some + rome)/(CYP2C19_KI + some + rome)",
        unit=U.per_min,
    ),
]

_m.reactions = [
    Reaction(
        f"{sid.upper()}IM",
        name=f"{SUBSTANCES_LIVER[sid]} exchange plasma and liver",
        equation=f"{sid}_ext <-> {sid}",
        compartment="Vli",
        sboTerm=SBO.TRANSPORT_REACTION,
        formula=(f"OMEIM_k * Vli * ({sid}_ext - {sid})", U.mmole_per_min),
    )
    for sid in ["some", "rome"]
]

_m.reactions.extend(
    [
        Reaction(
            "SOMECYP2C19",
            name="S-omeprazole to 5-O-desmethylomeprazole (CYP2C19)",
            equation="some -> omeoth",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=(
                "(1 dimensionless - f_some_omeoh) * SOMECYP2C19_rate",
                U.mmole_per_min,
            ),
            annotations=[(BQB.IS, "uniprot/P33261")],
        ),
        Reaction(
            "SOMECYP2C19OH",
            name="S-omeprazole to 5-hydroxyomeprazole (CYP2C19)",
            equation="some -> omeoh",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=("f_some_omeoh * SOMECYP2C19_rate", U.mmole_per_min),
            annotations=[(BQB.IS, "uniprot/P33261")],
        ),
        Reaction(
            "ROMECYP2C19",
            name="R-omeprazole to 5-hydroxyomeprazole (CYP2C19)",
            equation="rome -> omeoh",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=(
                "cyp2c19_activity * CYP2C19_Vmax_rome * Vli * rome/(CYP2C19_Km + rome)",
                U.mmole_per_min,
            ),
            annotations=[(BQB.IS, "uniprot/P33261")],
        ),
        Reaction(
            "SOMECYP3A4",
            name="S-omeprazole to omeprazole sulfone (CYP3A4)",
            equation="some -> omesul",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=(
                "f_cyp3a4 * CYP3A4_Vmax_some * Vli * some/(CYP3A4_Km + some)",
                U.mmole_per_min,
            ),
            annotations=[(BQB.IS, "uniprot/P08684")],
        ),
        Reaction(
            "ROMECYP3A4",
            name="R-omeprazole to omeprazole sulfone (CYP3A4)",
            equation="rome -> omesul",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=(
                "(1 dimensionless - f_rome_cyp3a4_omeoh) * ROMECYP3A4_rate",
                U.mmole_per_min,
            ),
            annotations=[(BQB.IS, "uniprot/P08684")],
        ),
        Reaction(
            "ROMECYP3A4OH",
            name="R-omeprazole to 5-hydroxyomeprazole (CYP3A4)",
            equation="rome -> omeoh",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=("f_rome_cyp3a4_omeoh * ROMECYP3A4_rate", U.mmole_per_min),
            annotations=[(BQB.IS, "uniprot/P08684")],
        ),
        Reaction(
            "OMEOHEX",
            name="5-hydroxyomeprazole release",
            equation="omeoh -> omeoh_ext",
            compartment="Vli",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=("OMEOHEX_k * Vli * omeoh", U.mmole_per_min),
        ),
        Reaction(
            "OMEOHM",
            name="5-hydroxyomeprazole oxidation",
            equation="omeoh -> omeoth",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=("OMEOHM_k * Vli * omeoh", U.mmole_per_min),
        ),
        Reaction(
            "OMESULEX",
            name="omeprazole sulfone exchange liver and plasma",
            equation="omesul <-> omesul_ext",
            compartment="Vli",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=("OMEMEX_k * Vli * (omesul - omesul_ext)", U.mmole_per_min),
        ),
        Reaction(
            "OMESULM",
            name="omeprazole sulfone metabolism",
            equation="omesul -> omeoth",
            compartment="Vli",
            sboTerm=SBO.BIOCHEMICAL_REACTION,
            formula=(
                "(cyp2c19_activity * OMESUL2C19_k + OMESULM_k) * Vli * omesul",
                U.mmole_per_min,
            ),
            annotations=[(BQB.IS, "uniprot/P33261")],
        ),
        Reaction(
            "OMEOTHEX",
            name="other metabolites exchange liver and plasma",
            equation="omeoth <-> omeoth_ext",
            compartment="Vli",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=("OMEMEX_k * Vli * (omeoth - omeoth_ext)", U.mmole_per_min),
        ),
        Reaction(
            "OMEOTHBIL",
            name="other metabolites biliary excretion",
            equation="omeoth -> omeoth_lumen",
            compartment="Vli",
            sboTerm=SBO.TRANSPORT_REACTION,
            formula=("OMEOTHBIL_k * Vli * omeoth", U.mmole_per_min),
        ),
    ]
)

model_liver = _m


if __name__ == "__main__":
    from pkdb_models.models.omeprazole import MODEL_BASE_PATH

    result = create_model(
        filepath=MODEL_BASE_PATH / f"{model_liver.sid}.xml",
        model=model_liver,
        sbml_level=3,
        sbml_version=2,
    )
