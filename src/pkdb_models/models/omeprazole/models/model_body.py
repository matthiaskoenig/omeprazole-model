"""Whole-body model of omeprazole: distribution, the organs and the dosing.

The substances are S-omeprazole (`some`) and R-omeprazole (`rome`), which are
dosed separately (a racemic dose of omeprazole is half of each), and their
metabolites 5-hydroxyomeprazole (`omeoh`), omeprazole sulfone (`omesul`) and
the other metabolites (`omeoth`: 5-hydroxyomeprazole sulfone,
carboxyomeprazole, 5-O-desmethylomeprazole). The concentrations are the ones
of the plasma; the blood flows carry the blood concentration (blood to plasma
ratio `BP_<sid>`). All substances distribute into the tissues with the same
exchange flow and partition coefficient (`ftissue_ome`, `Kp_ome`).
"""

from typing import NotRequired, TypedDict

import numpy as np
from pkpdsim.templates import terms_of_use
from sbmlutils.factory import (
    PORT_SUFFIX,
    AssignmentRule,
    Compartment,
    ExternalModelDefinition,
    Model,
    Parameter,
    RateRule,
    Reaction,
    ReplacedElement,
    Species,
    Submodel,
    UnitDefinition,
    create_model,
)
from sbmlutils.metadata import BQB, SBO

from pkdb_models.models.omeprazole.models import annotations, templates
from pkdb_models.models.omeprazole.models.fits import FITS


# -----------------------------------------------------------------------------
# Whole Body Metabolism
# -----------------------------------------------------------------------------
class U(templates.U):
    """UnitDefinitions."""

    kg = UnitDefinition("kg")
    ml = UnitDefinition("ml")
    hr = UnitDefinition("hr")
    cm = UnitDefinition("cm")
    per_hr = UnitDefinition("per_hr", "1/hr")
    mg_per_l = UnitDefinition("mg_per_l", "mg/l")
    mg_per_hr = UnitDefinition("mg_per_hr", "mg/hr")
    l_per_hr = UnitDefinition("l_per_hr", "l/hr")
    l_per_kg = UnitDefinition("l_per_kg", "l/kg")
    l_per_ml = UnitDefinition("l_per_ml", "l/ml")
    ml_per_min = UnitDefinition("ml_per_min", "ml/min")
    mg_per_min = UnitDefinition("mg_per_min", "mg/min")
    ml_per_s = UnitDefinition("ml_per_s", "ml/s")
    ml_per_s_kg = UnitDefinition("ml_per_s_kg", "ml/s/kg")
    ml_per_l = UnitDefinition("ml_per_l", "ml/l")
    s_per_min = UnitDefinition("s_per_min", "s/min")


_m = Model(
    "omeprazole_body",
    name="PBPK/PD model of omeprazole",
    notes="""
    # Whole-body model of omeprazole

    PBPK/PD model of omeprazole with its enantiomers S-omeprazole and
    R-omeprazole, their metabolism in the liver by CYP2C19 and CYP3A4, the
    renal and biliary excretion of the metabolites, the absorption of the
    application forms and the inhibition of the gastric proton pumps.
    """
    + terms_of_use,
    creators=templates.creators,
    units=U,
    model_units=templates.model_units,
)


class SubstanceBody(TypedDict):
    """Definition of a substance transported in the whole-body model."""

    name: str
    unit: UnitDefinition
    cinit: float  # initial concentration [mmole/l]
    Mr: float  # molecular weight [g/mole]
    BP: float  # blood to plasma ratio [-]
    IVDOSE: NotRequired[float]  # intravenous dose [mg]
    PODOSE: NotRequired[float]  # oral dose [mg]


SUBSTANCES_BODY: dict[str, SubstanceBody] = {
    "some": {
        "name": "S-omeprazole",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 345.416,
        # blood to plasma ratio 0.6 (Regaardh1990, ref 20)
        "BP": 0.6,
        "IVDOSE": 0,
        "PODOSE": 0,
    },
    "rome": {
        "name": "R-omeprazole",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 345.416,
        "BP": 0.6,
        "IVDOSE": 0,
        "PODOSE": 0,
    },
    "omeoh": {
        "name": "5-hydroxyomeprazole",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 361.415,
        "BP": 1.0,
    },
    "omesul": {
        "name": "omeprazole sulfone",
        "unit": U.mmole,
        "cinit": 0.0,
        "Mr": 361.42,
        "BP": 1.0,
    },
    "omeoth": {
        "name": "other omeprazole metabolites",
        "unit": U.mmole,
        "cinit": 0.0,
        # lumped: 5-hydroxyomeprazole sulfone 377.4, carboxyomeprazole 375.4,
        # 5-O-desmethylomeprazole 331.4 g/mole
        "Mr": 375.4,
        "BP": 1.0,
    },
}

# -----------------------------------------------------------------------------
# Submodels
# -----------------------------------------------------------------------------
COMPARTMENTS_BODY = {
    "gu": "gut",
    "ki": "kidney",
    "li": "liver",
    "lu": "lung",
    "pa": "pancreas",
    "sp": "spleen",
    "re": "rest",
    "ar": "arterial plasma",
    "ve": "venous plasma",
    "po": "portal vein",
    "hv": "hepatic vein",
}

#: the compartments without tissue distribution: the blood vessels and the
#: organs of the submodels
NO_TISSUE: list[str] = ["ve", "ar", "po", "hv", "li", "ki", "gu"]

SUBMODEL_SID_DICT = {  # tissue to submodel mapping
    "li": "LI",  # liver
    "ki": "KI",  # kidney
    "gu": "GU",  # gut/intestine
}

liver_id = "omeprazole_liver"
kidney_id = "omeprazole_kidney"
gut_id = "omeprazole_intestine"

_m.external_model_definitions = [
    ExternalModelDefinition(
        sid="liver", name="liver model", source=f"{liver_id}.xml", modelRef=liver_id
    ),
    ExternalModelDefinition(
        sid="kidney", name="kidney model", source=f"{kidney_id}.xml", modelRef=kidney_id
    ),
    ExternalModelDefinition(
        sid="gut", name="gut model definition", source=f"{gut_id}.xml", modelRef=gut_id
    ),
]

_m.submodels = [
    Submodel(sid=SUBMODEL_SID_DICT["li"], modelRef="liver", name="liver submodel"),
    Submodel(sid=SUBMODEL_SID_DICT["ki"], modelRef="kidney", name="kidney submodel"),
    Submodel(sid=SUBMODEL_SID_DICT["gu"], modelRef="gut", name="gut submodel"),
]

# -------------------------------------------------------------------------------------
# Compartments
# -------------------------------------------------------------------------------------
_m.compartments = [
    Compartment(
        cid,
        metaId=f"meta_{cid}",
        value=1,
        unit=U.liter,
        constant=False,
        name=name,
        sboTerm=SBO.PHYSICAL_COMPARTMENT,
        annotations=annotations.compartments[akey],
    )
    for cid, name, akey in [
        ("Vre", "rest of body", "re"),
        ("Vgu", "gut", "gu"),
        ("Vki", "kidney", "ki"),
        ("Vli", "liver", "li"),
        ("Vlu", "lung", "lu"),
        ("Vsp", "spleen", "sp"),
        ("Vpa", "pancreas", "pa"),
        ("Vve", "venous plasma", "plasma"),
        ("Var", "arterial plasma", "plasma"),
        ("Vpo", "portal plasma", "po"),
        ("Vhv", "hepatic venous plasma", "hv"),
    ]
]
_m.compartments.extend(
    [
        Compartment(
            "Vurine",
            metaId="meta_Vurine",
            value=1,
            unit=U.liter,
            constant=True,
            name="urine",
            sboTerm=SBO.PHYSICAL_COMPARTMENT,
            annotations=annotations.compartments["urine"],
        ),
        Compartment(
            "Vfeces",
            metaId="meta_Vfeces",
            value=1,
            unit=U.liter,
            constant=True,
            name="feces",
            sboTerm=SBO.PHYSICAL_COMPARTMENT,
            annotations=annotations.compartments["feces"],
        ),
    ]
)

# create plasma and tissue compartments (for correct blood volume)
for cid, cname in COMPARTMENTS_BODY.items():
    if cid not in ["ar", "ve", "po", "hv"]:
        _m.compartments.extend(
            [
                Compartment(
                    f"V{cid}_tissue",
                    value=1,
                    unit=U.liter,
                    constant=False,
                    name=f"{cname} tissue",
                    metaId=f"meta_V{cid}_tissue",
                    port=True,
                    sboTerm=SBO.PHYSICAL_COMPARTMENT,
                ),
                Compartment(
                    f"V{cid}_plasma",
                    value=1,
                    unit=U.liter,
                    constant=False,
                    name=f"{cname} plasma",
                    metaId=f"meta_V{cid}_plasma",
                    port=True,
                    sboTerm=SBO.PHYSICAL_COMPARTMENT,
                    annotations=annotations.compartments["plasma"],
                ),
            ]
        )


# replace volumes of submodels
_m.replaced_elements = [
    ReplacedElement(
        sid=sid,
        metaId=sid,
        elementRef=element,
        submodelRef=SUBMODEL_SID_DICT[tkey],
        portRef=f"{port}{PORT_SUFFIX}",
    )
    for sid, element, tkey, port in [
        # liver
        ("Vli_tissue_RE", "Vli_tissue", "li", "Vli"),
        ("Vli_plasma_RE", "Vli_plasma", "li", "Vext"),
        ("Vgu_li_RE", "Vgu", "li", "Vlumen"),
        # kidney
        ("Vki_tissue_RE", "Vki_tissue", "ki", "Vki"),
        ("Vki_plasma_RE", "Vki_plasma", "ki", "Vext"),
        ("Vurine_RE", "Vurine", "ki", "Vurine"),
        # intestine
        ("Vgu_plasma_RE", "Vgu_plasma", "gu", "Vext"),
        ("Vgu_RE", "Vgu", "gu", "Vlumen"),
        ("Vfeces_RE", "Vfeces", "gu", "Vfeces"),
    ]
]


# -------------------------------------------------------------------------------------------------
# Species
# -------------------------------------------------------------------------------------------------
_m.species = []
for sid, sdict in SUBSTANCES_BODY.items():
    # plasma species
    for cid, cname in COMPARTMENTS_BODY.items():
        if cid in ["ve", "ar", "po", "hv"]:
            sid_ex = f"C{cid}_{sid}"
            cid_ex = f"V{cid}"
        else:
            # plasma compartment
            sid_ex = f"C{cid}_plasma_{sid}"
            cid_ex = f"V{cid}_plasma"

        _m.species.append(
            Species(
                sid_ex,
                metaId=f"meta_{sid_ex}",
                initialConcentration=sdict["cinit"],
                compartment=cid_ex,
                substanceUnit=sdict["unit"],
                name=f"{sdict['name']} ({cname} plasma)",
                hasOnlySubstanceUnits=False,
                port=True,
                sboTerm=SBO.SIMPLE_CHEMICAL,
                annotations=annotations.species[sid],
            ),
        )
    # tissue species
    for cid, cname in COMPARTMENTS_BODY.items():
        if cid not in NO_TISSUE:
            sid_ex = f"C{cid}_{sid}"
            _m.species.append(
                Species(
                    sid_ex,
                    metaId=f"meta_{sid_ex}",
                    initialConcentration=sdict["cinit"],
                    compartment=f"V{cid}_tissue",
                    substanceUnit=sdict["unit"],
                    name=f"{sdict['name']} ({cname} tissue)",
                    hasOnlySubstanceUnits=False,
                    port=True,
                    sboTerm=SBO.SIMPLE_CHEMICAL,
                    annotations=annotations.species[sid],
                )
            )

#: species of the urine, the feces and the intestinal lumen
URINE_SPECIES: list[str] = ["omeoh", "omeoth"]
FECES_SPECIES: list[str] = ["some", "rome", "omeoth"]
LUMEN_SPECIES: list[str] = ["some", "rome", "omeoth"]

for sid in URINE_SPECIES:
    sdict = SUBSTANCES_BODY[sid]
    _m.species.append(
        Species(
            f"Aurine_{sid}",
            metaId=f"meta_Aurine_{sid}",
            initialConcentration=0,
            compartment="Vurine",
            substanceUnit=sdict["unit"],
            name=f"{sdict['name']} (urine)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[sid],
        )
    )
for sid in FECES_SPECIES:
    sdict = SUBSTANCES_BODY[sid]
    _m.species.append(
        Species(
            f"Afeces_{sid}",
            metaId=f"meta_Afeces_{sid}",
            initialConcentration=0,
            compartment="Vfeces",
            substanceUnit=sdict["unit"],
            name=f"{sdict['name']} (feces)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[sid],
        )
    )
for sid in LUMEN_SPECIES:
    sdict = SUBSTANCES_BODY[sid]
    _m.species.append(
        Species(
            f"Cgu_{sid}",
            metaId=f"meta_Cgu_{sid}",
            initialConcentration=0,
            compartment="Vgu",
            substanceUnit=sdict["unit"],
            name=f"{sdict['name']} (intestinal lumen)",
            hasOnlySubstanceUnits=False,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[sid],
        )
    )

# readouts
_m.species.extend(
    [
        Species(
            sid,
            metaId=f"meta_{sid}",
            initialConcentration=0,
            compartment="Vve",
            substanceUnit=U.mmole,
            name=name,
            hasOnlySubstanceUnits=False,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species[akey],
        )
        for sid, name, akey in [
            ("Cve_ome", "omeprazole (venous plasma)", "ome"),
            ("Cve_omemets", "omeprazole metabolites (venous plasma)", "omemets"),
            (
                "Cve_ometot",
                "omeprazole and its metabolites (venous plasma)",
                "omemets",
            ),
        ]
    ]
)
_m.species.extend(
    [
        Species(
            "Aurine_omemets",
            metaId="meta_Aurine_omemets",
            initialConcentration=0,
            compartment="Vurine",
            substanceUnit=U.mmole,
            name="omeprazole metabolites (urine)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["omemets"],
        ),
        Species(
            "Afeces_omemets",
            metaId="meta_Afeces_omemets",
            initialConcentration=0,
            compartment="Vfeces",
            substanceUnit=U.mmole,
            name="omeprazole metabolites (feces)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["omemets"],
        ),
        Species(
            "Afeces_ome",
            metaId="meta_Afeces_ome",
            initialConcentration=0,
            compartment="Vfeces",
            substanceUnit=U.mmole,
            name="omeprazole (feces)",
            hasOnlySubstanceUnits=True,
            sboTerm=SBO.SIMPLE_CHEMICAL,
            annotations=annotations.species["ome"],
        ),
    ]
)


# replace species
replaced_species = {
    "li": ["some", "rome", "omeoh", "omesul", "omeoth"],
    "ki": ["omeoh", "omeoth"],
    "gu": ["some", "rome"],
}
# plasma to external species
for tkey, skey_list in replaced_species.items():
    for skey in skey_list:
        _m.replaced_elements.append(
            ReplacedElement(
                sid=f"C{tkey}_plasma_{skey}_RE",
                metaId=f"C{tkey}_plasma_{skey}_RE",
                elementRef=f"C{tkey}_plasma_{skey}",
                submodelRef=SUBMODEL_SID_DICT[tkey],
                portRef=f"{skey}_ext{PORT_SUFFIX}",
            )
        )

for skey in URINE_SPECIES:
    _m.replaced_elements.append(
        ReplacedElement(
            sid=f"Aurine_{skey}_RE",
            metaId=f"Aurine_{skey}_RE",
            elementRef=f"Aurine_{skey}",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"{skey}_urine{PORT_SUFFIX}",
        )
    )

for skey in FECES_SPECIES:
    _m.replaced_elements.append(
        ReplacedElement(
            sid=f"Afeces_{skey}_RE",
            metaId=f"Afeces_{skey}_RE",
            elementRef=f"Afeces_{skey}",
            submodelRef=SUBMODEL_SID_DICT["gu"],
            portRef=f"{skey}_feces{PORT_SUFFIX}",
        )
    )

# lumen species: the absorption in the gut, the bile of the liver
for skey in LUMEN_SPECIES:
    tkeys = ["gu", "li"] if skey == "omeoth" else ["gu"]
    for tkey in tkeys:
        _m.replaced_elements.append(
            ReplacedElement(
                sid=f"Cgu_{skey}_{tkey}_RE",
                metaId=f"Cgu_{skey}_{tkey}_RE",
                elementRef=f"Cgu_{skey}",
                submodelRef=SUBMODEL_SID_DICT[tkey],
                portRef=f"{skey}_lumen{PORT_SUFFIX}",
            )
        )

# -------------------------------------------------------------------------------------
# Parameters
# -------------------------------------------------------------------------------------
_m.parameters = [
    # whole body data
    Parameter("BW", 75, U.kg, constant=True, name="body weight [kg]"),
    Parameter(
        "BW_ref",
        75,
        U.kg,
        constant=True,
        name="reference body weight [kg]",
        notes=(
            "Body weight at which the exchange flow of the tissue "
            "distribution (`ftissue_ome`) is given; it scales with the "
            "body weight as the volumes, the blood flows and the renal "
            "clearance do."
        ),
    ),
    Parameter("HEIGHT", 170, U.cm, constant=True, name="height [cm]"),
    Parameter("BSA", 0, U.m2, constant=False, name="body surface area [m^2]"),
    Parameter(
        "COBW",
        1.548,
        U.ml_per_s_kg,
        constant=True,
        name="cardiac output per bodyweight [ml/s/kg]",
    ),
    Parameter("CO", 108.33, U.ml_per_s, constant=False, name="cardiac output [ml/s]"),
    Parameter(
        "QC",
        108.33 / 1000 * 60,
        U.l_per_min,
        constant=False,
        name="cardiac output [L/min]",
    ),
    Parameter(
        "pH",
        value=2.0,
        unit=U.dimensionless,
        name="pH value stomach",
        constant=False,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # fractional tissue volumes
    Parameter(
        "Fblood",
        0.02,
        U.dimensionless,
        constant=False,
        name="blood fraction of organ volume",
    ),
    Parameter(
        "HCT",
        0.51,
        U.dimensionless,
        constant=True,
        metaId="meta_HCT",
        name="hematocrit",
    ),
    # fractional tissue volumes
    Parameter(
        "FVgu", 0.0171, U.l_per_kg, constant=True, name="gut fractional tissue volume"
    ),
    Parameter(
        "FVki",
        0.0044,
        U.l_per_kg,
        constant=True,
        name="kidney fractional tissue volume",
    ),
    Parameter(
        "FVli", 0.0210, U.l_per_kg, constant=True, name="liver fractional tissue volume"
    ),
    Parameter(
        "FVlu", 0.0076, U.l_per_kg, constant=True, name="lung fractional tissue volume"
    ),
    Parameter(
        "FVsp",
        0.0026,
        U.l_per_kg,
        constant=True,
        name="spleen fractional tissue volume",
    ),
    Parameter(
        "FVpa",
        0.01,
        U.l_per_kg,
        constant=True,
        name="pancreas fractional tissue volume",
    ),
    Parameter(
        "FVre",
        0,
        U.l_per_kg,
        constant=False,
        name="rest of body fractional tissue volume",
    ),  # calculated based on other tissues
    Parameter(
        "FVve",
        0.0514,
        U.l_per_kg,
        constant=True,
        name="venous fractional tissue volume",
    ),
    Parameter(
        "FVar",
        0.0257,
        U.l_per_kg,
        constant=True,
        name="arterial fractional tissue volume",
    ),
    Parameter(
        "FVpo", 0.001, U.l_per_kg, constant=True, name="portal fractional tissue volume"
    ),
    Parameter(
        "FVhv",
        0.001,
        U.l_per_kg,
        constant=True,
        name="hepatic venous fractional tissue volume",
    ),
    # fractional tissue blood flows
    Parameter(
        "FQgu",
        0.146,
        U.dimensionless,
        constant=True,
        name="gut fractional tissue blood flow",
    ),
    Parameter(
        "FQki",
        0.190,
        U.dimensionless,
        constant=True,
        name="kidney fractional tissue blood flow",
    ),
    Parameter(
        "FQh",
        0.215,
        U.dimensionless,
        constant=True,
        name="hepatic (venous side) fractional tissue blood flow",
    ),
    Parameter(
        "FQlu",
        1,
        U.dimensionless,
        constant=True,
        name="lung fractional tissue blood flow",
    ),
    Parameter(
        "FQsp",
        0.017,
        U.dimensionless,
        constant=True,
        name="spleen fractional tissue blood flow",
    ),
    Parameter(
        "FQpa",
        0.017,
        U.dimensionless,
        constant=True,
        name="pancreas fractional tissue blood flow",
    ),
    Parameter(
        "FQre",
        0,
        U.dimensionless,
        constant=False,
        name="rest of body fractional tissue blood flow",
    ),  # calculated based on other tissues
    Parameter(
        "f_cirrhosis",
        0,
        U.dimensionless,
        constant=True,
        name="severity of cirrhosis [0, 0.95]",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        annotations=[
            (BQB.IS, "ncit/C2951"),  # Cirrhosis
            (BQB.IS, "efo/0001422"),  # cirrhosis of liver
        ],
    ),
    Parameter(
        "f_shunts",
        0,
        U.dimensionless,
        constant=False,
        name="fraction of portal venous blood shunted by the liver",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        annotations=[
            (BQB.IS, "hp/HP:0002629"),  # Gastrointestinal arteriovenous malformation
        ],
    ),
    Parameter(
        "f_tissue_loss",
        0,
        U.dimensionless,
        constant=False,
        name="fraction of lost parenchymal liver volume",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
    ),
    # renal function
    Parameter(
        "f_GFR_Qki",
        101 / 1.32354,
        U.ml_per_l,
        constant=True,
        name="relationship GFR and Qki",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        GFR per renal blood flow (76.3 ml/l). Calibrated so that the healthy
        GFR is 101 ml/min at the renal blood flow of 1.32354 l/min of 75 kg,
        the normal GFR of the classes of renal impairment
        (`pkpdsim.impairment`).
        """,
    ),
    Parameter(
        "GFR_base",
        np.nan,
        U.ml_per_min,
        constant=False,
        name="glomerular filtration rate (healthy)",
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        notes="""
        The GFR of healthy kidneys, which scales with the renal blood flow and
        so with the body weight; the GFR is `KI__f_renal_function` times this
        rate.
        """,
    ),
    # tissue distribution
    Parameter(
        "ftissue_ome",
        100.0,
        U.l_per_min,
        constant=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name="tissue distribution omeprazole",
        notes="""
        Exchange flow between the plasma and the tissues at the reference body
        weight `BW_ref`, the same for the enantiomers and the metabolites (not
        identifiable separately). Fast, not fitted: the IV curves show no
        distribution phase and every fit ran to the upper bound (50 and 200
        l/min); the partition `Kp_ome` gives the volume.
        """,
    ),
    Parameter(
        "Kp_ome",
        **FITS.parameter("Kp_ome", unit=U.dimensionless),
        constant=True,
        sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
        name="tissue/plasma partition coefficient omeprazole",
        notes="""
        Vss 0.17-0.30 l/kg (Regaardh1990), 0.14-0.37 l/kg (Andersson1990a,
        Regaardh1986); omeprazole is 95 % bound to plasma proteins.
        """,
    ),
]

_m.replaced_elements.extend(
    [
        ReplacedElement(
            sid="GFR_base_ki_RE",
            metaId="GFR_base_ki_RE",
            elementRef="GFR_base",
            submodelRef=SUBMODEL_SID_DICT["ki"],
            portRef=f"GFR_base{PORT_SUFFIX}",
        ),
        ReplacedElement(
            sid="pH_RE",
            metaId="pH_RE",
            elementRef="pH",
            submodelRef=SUBMODEL_SID_DICT["gu"],
            portRef=f"pH{PORT_SUFFIX}",
        ),
    ]
)

# species specific parameters
for sid, sdict in SUBSTANCES_BODY.items():
    _m.parameters.extend(
        [
            Parameter(
                f"Mr_{sid}",
                sdict["Mr"],
                U.g_per_mole,
                constant=True,
                name=f"Molecular weight {sid} [g/mole]",
                sboTerm=SBO.MOLECULAR_MASS,
            ),
            Parameter(
                f"BP_{sid}",
                sdict["BP"],
                U.dimensionless,
                constant=True,
                name=f"blood to plasma ratio {sid}",
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                notes="""
                The blood flows carry the blood concentration, the plasma
                concentration times this ratio. Omeprazole 0.6 (Regaardh1990,
                ref 20); the metabolites 1 (unknown).
                """,
            ),
        ]
    )

    if "IVDOSE" in sdict:
        _m.parameters.extend(
            [
                Parameter(
                    f"IVDOSE_{sid}",
                    sdict["IVDOSE"],
                    U.mg,
                    constant=False,
                    sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                    name=f"IV bolus dose {sid} [mg]",
                ),
                Parameter(
                    f"ti_{sid}",
                    10,
                    U.second,
                    constant=True,
                    name=f"injection time {sid} [s]",
                ),
                Parameter(
                    f"Ki_{sid}",
                    0.02,
                    U.per_min,
                    constant=False,
                    name=f"Ki [1/min] injection {sid}",
                ),
                Parameter(
                    f"Ri_{sid}",
                    0,
                    U.mg_per_min,
                    constant=True,
                    name=f"Ri [mg/min] rate of infusion {sid}",
                ),
                Parameter(
                    f"cum_dose_{sid}",
                    0,
                    U.mg,
                    constant=False,
                    name=f"Cumulative dose due to infusion {sid}",
                ),
            ]
        )

    if "PODOSE" in sdict:
        _m.parameters.append(
            Parameter(
                f"PODOSE_{sid}",
                sdict["PODOSE"],
                U.mg,
                constant=False,
                sboTerm=SBO.QUANTITATIVE_SYSTEMS_DESCRIPTION_PARAMETER,
                name=f"oral dose {sid} [mg]",
            )
        )
        _m.replaced_elements.append(
            ReplacedElement(
                sid=f"PODOSE_{sid}_RE",
                metaId=f"PODOSE_{sid}_RE",
                elementRef=f"PODOSE_{sid}",
                submodelRef=SUBMODEL_SID_DICT["gu"],
                portRef=f"PODOSE_{sid}{PORT_SUFFIX}",
            )
        )

# -------------------------------------------------------------------------------------------------
# AssignmentRules
# -------------------------------------------------------------------------------------------------
_m.rules = [
    AssignmentRule("f_shunts", "f_cirrhosis", unit=U.dimensionless),
    AssignmentRule("f_tissue_loss", "f_cirrhosis", unit=U.dimensionless),
    # readouts
    AssignmentRule(
        "Cve_ome",
        "Cve_some + Cve_rome",
        unit=U.mM,
        name="omeprazole: S-omeprazole and R-omeprazole",
    ),
    AssignmentRule(
        "Cve_omemets",
        "Cve_omeoh + Cve_omesul + Cve_omeoth",
        unit=U.mM,
        name="omeprazole metabolites",
        notes="""All metabolites, without omeprazole.""",
    ),
    AssignmentRule(
        "Cve_ometot",
        "Cve_ome + Cve_omemets",
        unit=U.mM,
        name="omeprazole and its metabolites",
        notes="""The total radioactivity of a 14C-omeprazole dose.""",
    ),
    AssignmentRule(
        "Aurine_omemets",
        "Aurine_omeoh + Aurine_omeoth",
        unit=U.mmole,
        name="omeprazole metabolites (urine)",
        notes="""The radioactivity of the urine, no omeprazole is excreted.""",
    ),
    AssignmentRule(
        "Afeces_omemets",
        "Afeces_omeoth",
        unit=U.mmole,
        name="omeprazole metabolites (feces)",
    ),
    AssignmentRule(
        "Afeces_ome",
        "Afeces_some + Afeces_rome",
        unit=U.mmole,
        name="omeprazole (feces)",
    ),
    # Rest body volume
    AssignmentRule(
        "FVre",
        "1.0 l_per_kg - (FVgu + FVki + FVli + FVlu + FVsp + FVpa + FVve + FVar)",
        U.l_per_kg,
    ),
    # Rest body perfusion
    AssignmentRule("FQre", "1.0 dimensionless - (FQki + FQh)", U.dimensionless),
    # Body surface area (Haycock1978)
    AssignmentRule(
        "BSA", "0.024265 m2 * power(BW/1 kg, 0.5378) * power(HEIGHT/1 cm, 0.3964)", U.m2
    ),
    # cardiac output (depending on bodyweight)
    AssignmentRule("CO", "BW*COBW", U.ml_per_s),
    AssignmentRule("QC", "CO/1000 ml_per_l * 60 s_per_min", U.l_per_min),
    # volumes
    AssignmentRule("Vgu", "BW*FVgu", U.liter),
    AssignmentRule("Vki", "BW*FVki", U.liter),
    AssignmentRule("Vli", "BW*FVli", U.liter),
    AssignmentRule("Vlu", "BW*FVlu", U.liter),
    AssignmentRule("Vsp", "BW*FVsp", U.liter),
    AssignmentRule("Vpa", "BW*FVpa", U.liter),
    AssignmentRule("Vre", "BW*FVre", U.liter),
    # venous and arterial plasma volume (corrected for tissue blood volumes)
    *[
        AssignmentRule(
            f"V{cid}",
            f"(1 dimensionless - HCT) * (BW*FV{cid} - FV{cid}/(FVar+FVve+FVpo+FVhv) * BW * "
            "Fblood * (1 l_per_kg - (FVar+FVve+FVpo+FVhv)))",
            U.liter,
        )
        for cid in ["ve", "ar", "po", "hv"]
    ],
    # blood flows
    AssignmentRule("Qgu", "QC*FQgu", U.l_per_min, name="gut blood flow"),
    AssignmentRule("Qki", "QC*FQki", U.l_per_min, name="kidney blood flow"),
    AssignmentRule(
        "Qh", "QC*FQh", U.l_per_min, name="hepatic (venous side) blood flow"
    ),
    AssignmentRule(
        "Qha", "Qh - Qgu - Qsp - Qpa", U.l_per_min, name="hepatic artery blood flow"
    ),
    AssignmentRule("Qlu", "QC*FQlu", U.l_per_min, name="lung blood flow"),
    AssignmentRule("Qsp", "QC*FQsp", U.l_per_min, name="spleen blood flow"),
    AssignmentRule("Qpa", "QC*FQpa", U.l_per_min, name="pancreas blood flow"),
    AssignmentRule("Qre", "QC*FQre", U.l_per_min, name="rest of body blood flow"),
    AssignmentRule("Qpo", "Qsp + Qpa + Qgu", U.l_per_min, name="portal blood flow"),
    # glomerular filtration rate of healthy kidneys
    AssignmentRule(
        "GFR_base",
        "f_GFR_Qki * Qki",
        U.ml_per_min,
        name="glomerular filtration rate (healthy)",
    ),
]

# Volumes for explicit tissue models
for cid, cname in COMPARTMENTS_BODY.items():
    if cid in ["ve", "ar", "po", "hv"]:
        continue
    _m.rules.append(
        AssignmentRule(
            f"V{cid}_plasma",
            f"V{cid} * Fblood * (1 dimensionless - HCT)",
            unit=U.liter,
            name=f"plasma volume of {cname}",
        ),
    )
    # Cirrhosis: loss of the parenchymal liver volume
    tissue_loss = " * (1 dimensionless - f_tissue_loss)" if cid == "li" else ""
    _m.rules.append(
        AssignmentRule(
            f"V{cid}_tissue",
            f"V{cid}{tissue_loss} * (1 dimensionless - Fblood)",
            unit=U.liter,
            name=f"tissue volume of {cname}",
        ),
    )


for sid, sdict in SUBSTANCES_BODY.items():
    sname = sdict["name"]

    # injection
    if "IVDOSE" in sdict:
        _m.rules.append(
            AssignmentRule(
                f"Ki_{sid}",
                f"0.693 dimensionless/ti_{sid} * 60 s_per_min",
                U.per_min,
                name="injection rate IV",
                notes="""
                log(2) ~ 0.693 used for conversion of half-life injection time to
                injection rate.
                """,
            ),
        )

    # amounts and mass concentrations of the plasma
    for cid, cname in COMPARTMENTS_BODY.items():
        if cid in ["ve", "ar", "po", "hv"]:
            csid = f"C{cid}_{sid}"
            vid = f"V{cid}"
            key = f"{cid}_{sid}"
        else:
            csid = f"C{cid}_plasma_{sid}"
            vid = f"V{cid}_plasma"
            key = f"{cid}_plasma_{sid}"
        _m.rules.extend(
            [
                AssignmentRule(
                    f"A{key}",
                    f"{csid}*{vid}",
                    U.mmole,
                    name=f"{sname} amount ({cname} plasma)",
                ),
                AssignmentRule(
                    f"X{key}",
                    f"A{key}*Mr_{sid}",
                    U.mg,
                    name=f"{sname} mass ({cname} plasma)",
                ),
                AssignmentRule(
                    f"M{key}",
                    f"{csid}*Mr_{sid}",
                    U.mg_per_l,
                    name=f"{sname} mass concentration ({cname} plasma)",
                ),
            ]
        )

# --------------------------------------------------------------------------------------------------
# Reactions
# --------------------------------------------------------------------------------------------------
_m.reactions = []

for sid, sdict in SUBSTANCES_BODY.items():
    sname = sdict["name"]

    # tissue distribution
    for cid in COMPARTMENTS_BODY:
        if cid not in NO_TISSUE:
            _m.reactions.append(
                Reaction(
                    sid=f"transport_{cid}_{sid}",
                    name=f"transport {sname}",
                    formula=(
                        f"ftissue_ome * BW/BW_ref * (C{cid}_plasma_{sid}*Kp_ome - C{cid}_{sid})",
                        U.mmole_per_min,
                    ),
                    equation=f"C{cid}_plasma_{sid} <-> C{cid}_{sid}",
                    compartment=f"V{cid}_tissue",
                    sboTerm=SBO.TRANSPORT_REACTION,
                ),
            )

    if "IVDOSE" in sdict:
        _m.reactions.append(
            Reaction(
                sid=f"iv_{sid}",
                name=f"iv {sname}",
                formula=(f"Ki_{sid}*IVDOSE_{sid}/Mr_{sid}", U.mmole_per_min),
                equation=f"-> Cve_{sid}",
                sboTerm=SBO.TRANSPORT_REACTION,
                annotations=[(BQB.IS, "ncit/C38276")],
                compartment="Vve",
            ),
        )

    # blood flows: the flows carry the blood concentration BP * C (plasma)
    flows: list[tuple[str, str, str, str]] = [
        # (reaction id, flow, source species, target species)
        (f"Flow_ve_lu_{sid}", "Qlu", f"Cve_{sid}", f"Clu_plasma_{sid}"),
        (f"Flow_lu_ar_{sid}", "Qlu", f"Clu_plasma_{sid}", f"Car_{sid}"),
    ]
    for cid in ["ki", "re"]:
        flows.extend(
            [
                (
                    f"Flow_ar_{cid}_{sid}",
                    f"Q{cid}",
                    f"Car_{sid}",
                    f"C{cid}_plasma_{sid}",
                ),
                (
                    f"Flow_{cid}_ve_{sid}",
                    f"Q{cid}",
                    f"C{cid}_plasma_{sid}",
                    f"Cve_{sid}",
                ),
            ]
        )
    for cid in ["gu", "sp", "pa"]:
        flows.extend(
            [
                (
                    f"Flow_ar_{cid}_{sid}",
                    f"Q{cid}",
                    f"Car_{sid}",
                    f"C{cid}_plasma_{sid}",
                ),
                (
                    f"Flow_{cid}_po_{sid}",
                    f"Q{cid}",
                    f"C{cid}_plasma_{sid}",
                    f"Cpo_{sid}",
                ),
            ]
        )
    flows.extend(
        [
            # arterial inflow of the liver and the arterial shunts
            (
                f"Flow_arli_li_{sid}",
                "(1 dimensionless - f_shunts)*Qha",
                f"Car_{sid}",
                f"Cli_plasma_{sid}",
            ),
            (f"Flow_arli_hv_{sid}", "f_shunts*Qha", f"Car_{sid}", f"Chv_{sid}"),
            # portal inflow of the liver and the portal shunts
            (
                f"Flow_po_li_{sid}",
                "(1 dimensionless - f_shunts)*Qpo",
                f"Cpo_{sid}",
                f"Cli_plasma_{sid}",
            ),
            (f"Flow_po_hv_{sid}", "f_shunts*Qpo", f"Cpo_{sid}", f"Chv_{sid}"),
            (
                f"Flow_li_hv_{sid}",
                "(1 dimensionless - f_shunts)*(Qpo+Qha)",
                f"Cli_plasma_{sid}",
                f"Chv_{sid}",
            ),
            (f"Flow_hv_ve_{sid}", "Qh", f"Chv_{sid}", f"Cve_{sid}"),
        ]
    )
    for rid, flow, source, target in flows:
        _m.reactions.append(
            Reaction(
                sid=rid,
                name=f"blood flow {sname}",
                formula=(f"{flow} * BP_{sid} * {source}", U.mmole_per_min),
                equation=f"{source} -> {target}",
                sboTerm=SBO.TRANSPORT_REACTION,
            )
        )

# -------------------------------------------------------------------------------------
# RateRules
# -------------------------------------------------------------------------------------
_m.rate_rules = []
for sid, sdict in SUBSTANCES_BODY.items():
    if "IVDOSE" in sdict:
        _m.rate_rules.extend(
            [
                # injection of dose
                RateRule(
                    f"IVDOSE_{sid}", f"-iv_{sid}*Mr_{sid} + Ri_{sid}", U.mg_per_min
                ),
                # cumulative infusion dose
                RateRule(f"cum_dose_{sid}", f"Ri_{sid}", U.mg_per_min),
            ]
        )


model_body = _m

if __name__ == "__main__":
    from pkdb_models.models.omeprazole import MODEL_BASE_PATH

    result = create_model(
        filepath=MODEL_BASE_PATH / f"{model_body.sid}.xml",
        model=model_body,
        sbml_level=3,
        sbml_version=2,
    )
