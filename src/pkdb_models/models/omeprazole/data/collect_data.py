"""Collect the data of the omeprazole studies from the PK-DB study folders.

The studies are copied from a `pkdb_data` checkout (`PKDB_DATA`, else
`../pkdb_data`, see `pkpdsim.data.studies_dir`) into the data folder of the
model, see `pkpdsim.data.collect_tsv_files`.
Besides the omeprazole studies, the cocktail study Oh2012 of the caffeine
studies has an omeprazole group.
"""

from pathlib import Path

from pkpdsim.data import collect_tsv_files
from pkpdsim.data import studies_dir as pkdb_studies_dir

from pkdb_models.models.omeprazole import DATA_PATH_CAFFEINE, DATA_PATH_OMEPRAZOLE

#: the studies of other substances which the omeprazole experiments use
CAFFEINE_STUDIES = {"Oh2012"}


def collect_data(studies_dir: Path | None = None) -> None:
    """Copy the data of the omeprazole studies into the data folder of the model.

    Args:
        studies_dir: the `studies` folder of pkdb_data, by default the one of
            the checkout `pkpdsim.data.studies_dir` finds.
    """
    if studies_dir is None:
        studies_dir = pkdb_studies_dir()
    collect_tsv_files(
        source_dir=studies_dir / "omeprazole", target_dir=DATA_PATH_OMEPRAZOLE
    )
    collect_tsv_files(
        source_dir=studies_dir / "caffeine",
        target_dir=DATA_PATH_CAFFEINE,
        filter_study=lambda study: study in CAFFEINE_STUDIES,
    )


if __name__ == "__main__":
    collect_data()
