"""Annotations of the omeprazole models: the species and the shared compartments."""

from pkpdsim.annotations import compartments
from sbmlutils.metadata import BQB

__all__ = ["compartments", "species"]

species = {
    "proton": [
        # Proton
        (BQB.IS, "ncit/C17024"),  # Proton
        (BQB.IS, "chebi/CHEBI:24636"),  # proton
    ],
    "ome": [
        # omeprazole
        (BQB.IS, "pubchem.compound/4594"),
        (BQB.IS, "chebi/CHEBI:7772"),
        (BQB.IS, "ncit/C716"),
        (BQB.IS, "inchikey/SUBDBMMJDZJVOS-UHFFFAOYSA-N"),
        (BQB.IS_VERSION_OF, "ncit/C29723"),  # Proton Pump Inhibitor
        (BQB.IS_VERSION_OF, "chebi/CHEBI:49200"),  # proton pump inhibitor
    ],
    "some": [
        # s-omeprazole
        (BQB.IS, "pubchem.compound/9568614"),
        (BQB.IS, "chebi/CHEBI:50275"),
        (BQB.IS, "inchikey/SUBDBMMJDZJVOS-DEOSSOPVSA-N"),
        (BQB.IS_VERSION_OF, "ncit/C29723"),  # Proton Pump Inhibitor
        (BQB.IS_VERSION_OF, "chebi/CHEBI:49200"),  # proton pump inhibitor
    ],
    "rome": [
        # r-omeprazole
        (BQB.IS, "pubchem.compound/9579578"),
        (BQB.IS, "chebi/CHEBI:77262"),
        (BQB.IS, "inchikey/SUBDBMMJDZJVOS-XMMPIXPASA-N"),
        (BQB.IS_VERSION_OF, "ncit/C29723"),  # Proton Pump Inhibitor
        (BQB.IS_VERSION_OF, "chebi/CHEBI:49200"),  # proton pump inhibitor
    ],
    "omeoh": [
        # 5-hydroxyomeprazole
        (BQB.IS, "pubchem.compound/119560"),
        (BQB.IS, "inchikey/CMZHQFXXAAIBKE-UHFFFAOYSA-N"),
        (BQB.IS, "chebi/CHEBI:63840"),
    ],
    "omesul": [
        # omeprazole-sulfone
        (BQB.IS, "pubchem.compound/145900"),
        (BQB.IS, "inchikey/IXEQEYRTSRFZEO-UHFFFAOYSA-N"),
        (BQB.IS, "chebi/CHEBI:166518"),
    ],
    "omeoth": [
        # other omeprazole metabolites: 5-hydroxyomeprazole sulfone,
        # carboxyomeprazole, 5-O-desmethylomeprazole (lumped)
    ],
    "omemets": [
        # omeprazole metabolites
    ],
}
