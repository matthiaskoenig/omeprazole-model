"""Omeprazole: PBPK/PD model of the proton pump inhibitor omeprazole.

The enantiomers S-omeprazole (esomeprazole) and R-omeprazole are metabolized
in the liver by CYP2C19 (R: 5-hydroxyomeprazole, S: 5-O-desmethylomeprazole)
and CYP3A4 (omeprazole sulfone); the activity of CYP2C19 follows the genotype
and is lost by the mechanism-based inactivation by omeprazole. The application
forms (enteric-coated, buffered, unprotected) and the inhibition of the gastric
proton pumps are part of the model.

The paths of the model and its model object `MODEL`, which the commands
`run_simulation`, `run_fit`, `run_report` and `run_identifiability` of pkpdsim
run by its package `pkdb_models.models.omeprazole`.
"""

from pathlib import Path

from pkpdsim.model import FigureSettings, PKPDModel, SimulatorSettings
from pkpdsim.release.settings import Author, ReleaseSettings

from pkdb_models.models.omeprazole.tolerances import ABSOLUTE_TOLERANCE

OMEPRAZOLE_PATH = Path(__file__).parent

MODEL_BASE_PATH = OMEPRAZOLE_PATH / "models" / "output" / "models"
MODEL_PATH = MODEL_BASE_PATH / "omeprazole_body_flat.xml"

DATA_PATH_BASE = OMEPRAZOLE_PATH / "data"
DATA_PATH_OMEPRAZOLE = DATA_PATH_BASE / "omeprazole"
# the cocktail study Oh2012 is curated with the caffeine studies
DATA_PATH_CAFFEINE = DATA_PATH_BASE / "caffeine"
DATA_PATHS = [DATA_PATH_OMEPRAZOLE, DATA_PATH_CAFFEINE]

MODEL = PKPDModel(
    name="omeprazole",
    package=__name__,
    title="Omeprazole PBPK model",
    path=OMEPRAZOLE_PATH,
    model_path=MODEL_PATH,
    data_paths=tuple(DATA_PATHS),
    archive_path=MODEL_BASE_PATH.parent / "omeprazole_model.omex",
    factory=".models.factory:create_omeprazole_models",
    experiments=".simulations:EXPERIMENTS",
    fit_definitions=".fitting.fitting:FIT_DEFINITIONS",
    simulator=SimulatorSettings(
        absolute_tolerance=ABSOLUTE_TOLERANCE, relative_tolerance=1e-10
    ),
    figures=FigureSettings(formats=("svg",), legend_fontsize=10),
    # the adopted fits, the factory reads the fitted values from their records
    fits=("PK_20261020_090631__aa2cf",),
    fit_identifiability=True,
    # the release of the model repository
    release=ReleaseSettings(
        title=(
            "Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model"
            " of omeprazole"
        ),
        repository="matthiaskoenig/omeprazole-model",
        doi="10.5281/zenodo.5555814",
        authors=(
            Author(
                "Leal Pujol, Helen",
                None,
                "Humboldt-University Berlin, Institute for Theoretical Biology, Berlin",
            ),
            Author(
                "Balci, Sükrü",
                "0000-0001-8536-2905",
                "Humboldt-University Berlin, Institute for Theoretical Biology, Berlin",
            ),
            Author(
                "König, Matthias",
                "0000-0003-1725-179X",
                (
                    "Humboldt-Universität zu Berlin, Faculty of Life Sciences,"
                    " Department of Biology, Institute of Theoretical Biology, Systems"
                    " Medicine of the Liver; University of Stuttgart, Institute of"
                    " Structural Mechanics and Dynamics in Aerospace Engineering;"
                    " University of Southern Denmark, Clinical Pharmacology, Pharmacy"
                    " and Environmental Medicine, Department of Public Health;"
                    " University Hospital Schleswig-Holstein, Campus Lübeck, First"
                    " Department of Medicine, Lübeck, Germany"
                ),
            ),
        ),
        keywords=(
            "model",
            "omeprazole",
            "esomeprazole",
            "proton pump inhibitor",
            "CYP2C19",
            "pharmacokinetics",
            "pharmacodynamics",
            "PBPK",
            "physiologically based pharmacokinetic model",
            "SBML",
        ),
        docker_image="matthiaskoenig/omeprazole",
        funding=(
            "Matthias König was supported by the Federal Ministry of Research,"
            " Technology and Space (BMFTR, Germany) within ATLAS by grant number"
            " 031L0304B and by the German Research Foundation (DFG) within the"
            " Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver"
            " Perfusion-Function Relationship in Complex Resection - A Systems"
            " Medicine Approach) by grant number 436883643 and by grant number"
            " 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This"
            " work was supported by the BMBF-funded de.NBI Cloud within the German"
            " Network for Bioinformatics Infrastructure (de.NBI) (031A537B,"
            " 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A,"
            " 031A532B)."
        ),
        description=(
            "This repository provides the omeprazole physiologically based"
            " pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption of"
            " the application forms of omeprazole, the metabolism of S- and"
            " R-omeprazole by CYP2C19 and CYP3A4 in the liver with the"
            " mechanism-based inactivation of CYP2C19, the renal and biliary"
            " excretion of the metabolites, the inhibition of the gastric proton"
            " pumps and the effects of the CYP2C19 genotype, of interacting drugs"
            " and of impaired renal and hepatic function."
        ),
        first_year=2020,
    ),
)
"""The omeprazole model: its commands, see `pkpdsim.model`."""
