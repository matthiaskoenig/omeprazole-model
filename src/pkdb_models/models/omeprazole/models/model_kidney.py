"""Kidney model of omeprazole: the renal excretion of the metabolites.

Omeprazole is not excreted in the urine (< 0.1 % of the dose), neither is
omeprazole sulfone (< 1.5 %) [Regaardh1986, Regaardh1990, Landahl1992,
Naesdal1986, Sohn1992]. The urine contains 75-78 % of the radioactivity of a
dose: 5-hydroxyomeprazole (13.5 % in extensive, 5.6 % in poor metabolizers
over 24 hr [Sohn1992]) and the secondary metabolites (5-hydroxyomeprazole
sulfone, carboxyomeprazole, pool `omeoth`). The renal clearances are given
relative to the glomerular filtration rate and scale with the renal function.
"""

from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    AssignmentRule,
    Compartment,
    Model,
    Parameter,
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

    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    l_per_ml = UnitDefinition("l_per_ml", "l/ml")


_m = Model(
    sid="omeprazole_kidney",
    name="Model for the renal excretion of the omeprazole metabolites",
    notes="""
    # Model for the renal excretion of the omeprazole metabolites

    - no omeprazole and no omeprazole sulfone are excreted in the urine
    - 5-hydroxyomeprazole and the other metabolites are excreted from the
      plasma into the urine, with clearances relative to the glomerular
      filtration rate (GFR)
    """
    + terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
    annotations=[
        (BQB.OCCURS_IN, "fma/FMA:7203"),  # kidney
        (BQB.OCCURS_IN, "bto/BTO:0000671"),
        (BQB.OCCURS_IN, "ncit/C12415"),
        (BQB.HAS_PROPERTY, "ncit/C79372"),  # Pharmacokinetics: Excretion
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
        "Vki",
        0.3,
        name="kidney",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["ki"],
    ),
    Compartment(
        "Vurine",
        1.0,
        name="urine",
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        unit=U.liter,
        port=True,
        annotations=annotations.compartments["urine"],
    ),
]

#: the metabolites which are excreted in the urine
SUBSTANCES_KIDNEY: dict[str, str] = {
    "omeoh": "5-hydroxyomeprazole",
    "omeoth": "other omeprazole metabolites",
}

_m.species = []
for sid, name in SUBSTANCES_KIDNEY.items():
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
                f"{sid}_urine",
                initialConcentration=0.0,
                name=f"{name} (urine)",
                compartment="Vurine",
                substanceUnit=U.mmole,
                hasOnlySubstanceUnits=True,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
                port=True,
                notes="Urinary species are amounts.",
            ),
        ]
    )

_m.parameters = [
    Parameter(
        "f_renal_function",
        1.0,
        unit=U.dimensionless,
        name="renal function",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        >1.0: increased kidney function
        1.0: normal kidney function (healthy control)
        <1.0: decreased kidney function

        Renal function relative to the healthy glomerular filtration rate
        GFR_base, which is 101 ml/min at 75 kg; a measured creatinine
        clearance of X ml/min is the renal function X/101.
        """,
    ),
    Parameter(
        "GFR_base",
        101,
        U.ml_per_min,
        name="glomerular filtration rate (healthy)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        port=True,
    ),
    Parameter(
        "OMEOHEX_f",
        **FITS.parameter("KI__OMEOHEX_f", unit=U.dimensionless),
        name="renal clearance of 5-hydroxyomeprazole relative to the GFR",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        The renal clearance of 5-hydroxyomeprazole is OMEOHEX_f times the GFR:
        above 1 a net secretion. The 5-hydroxyomeprazole of the plasma is
        excreted in the urine (13.5 % of the dose in extensive metabolizers
        [Sohn1992]), half-life about 1 hr [Andersson1990a].
        """,
    ),
    Parameter(
        "OMEOTHEX_f",
        **FITS.parameter("KI__OMEOTHEX_f", unit=U.dimensionless),
        name="renal clearance of the other metabolites relative to the GFR",
        sboTerm=SBO.KINETIC_CONSTANT,
        notes="""
        The renal clearance of the secondary metabolites
        (5-hydroxyomeprazole sulfone, carboxyomeprazole) is OMEOTHEX_f times the
        GFR; with the biliary excretion it gives 75-78 % of the dose in the
        urine and 17-19 % in the feces [Regaardh1986, Regaardh1990].
        """,
    ),
]

_m.rules = [
    AssignmentRule(
        "GFR",
        "f_renal_function * GFR_base",
        unit=U.ml_per_min,
        name="glomerular filtration rate",
    ),
]

_m.reactions = [
    Reaction(
        f"{sid.upper()}EX",
        name=f"{name} renal excretion",
        equation=f"{sid}_ext -> {sid}_urine",
        sboTerm=SBO.TRANSPORT_REACTION,
        compartment="Vki",
        # [ml/min] * [l/ml] * [-] * [mmole/l]
        formula=(
            f"GFR * 0.001 l_per_ml * {sid.upper()}EX_f * {sid}_ext",
            U.mmole_per_min,
        ),
        annotations=[(BQB.IS, "ncit/C75913")],  # renal clearance
    )
    for sid, name in SUBSTANCES_KIDNEY.items()
]

_m.rules.append(
    AssignmentRule(
        "OMEMETSEX",
        "OMEOHEX + OMEOTHEX",
        unit=U.mmole_per_min,
        name="renal excretion rate of the omeprazole metabolites",
    ),
)

model_kidney = _m


if __name__ == "__main__":
    from pkdb_models.models.omeprazole import MODEL_BASE_PATH

    result = create_model(
        filepath=MODEL_BASE_PATH / f"{model_kidney.sid}.xml",
        model=model_kidney,
        sbml_level=3,
        sbml_version=2,
    )
