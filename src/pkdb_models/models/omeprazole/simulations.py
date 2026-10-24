"""The simulation experiments of the omeprazole model and their groups.

They are the registry of `MODEL`, the experiments its commands simulate.
"""

from sbmlsim.experiment import SimulationExperiment

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.misc import (
    ApplicationExperiment,
    PHChangeExperiment,
)
from pkdb_models.models.omeprazole.experiments.scans import OmeprazoleParameterScan
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

EXPERIMENTS: dict[str, list[type[SimulationExperiment]]] = {
    "studies": [
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
    ],
    "hepatic_impairment": [
        Andersson1993,
    ],
    "renal_impairment": [
        Naesdal1986,
    ],
    "cyp2c19": [
        Kita2001,
        Kita2002,
        Park2017,
        Sohn1992,
        Uno2007,
    ],
    "misc": [
        ApplicationExperiment,
        PHChangeExperiment,
    ],
    "scans": [
        OmeprazoleParameterScan,
    ],
}
EXPERIMENTS["all"] = EXPERIMENTS["studies"] + EXPERIMENTS["misc"] + EXPERIMENTS["scans"]


if __name__ == "__main__":
    MODEL.run_simulation_experiments(EXPERIMENTS["all"], MODEL.simulation_dir / "all")
