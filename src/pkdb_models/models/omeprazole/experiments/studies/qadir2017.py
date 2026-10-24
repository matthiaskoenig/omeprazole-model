"""Simulation experiment of the study Qadir2017."""

from typing import ClassVar, override

from pkpdsim.metadata import ApplicationForm
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Qadir2017(OmeprazoleSimulationExperiment):
    """Simulation experiment of Qadir2017.

    8 healthy Pakistani women (24-28 years, 53-64 kg) took a single capsule of
    20 mg enteric-coated omeprazole after an overnight fast. Cumulative
    unchanged omeprazole in urine (Fig5, mean and SE; HPLC-UV), 6.7 % of the
    dose in 8 h.

    The measurement is implausible: every 14C and HPLC study finds no unchanged
    omeprazole in urine (Regaardh1986, Prichard1985), the method has no
    specificity data for the acid labile drug and its metabolites. The model
    has no renal excretion of omeprazole; the data are shown, not mapped.
    """

    dose: ClassVar[int] = 20  # [mg]
    form: ClassVar[ApplicationForm] = ApplicationForm.CAPSULE
    bodyweight: ClassVar[float] = 58.5  # [kg] the middle of 53-64 kg

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig5"]:
            df = self.load_dataframe(fig_id)
            # the amount of unchanged omeprazole, calculated from the recovery
            df = df[df["label"] == "ome_cum_amount"]
            dsets["ome_cum_amount"] = DataSet.from_df(df, self.ureg)

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        tcsims[self.to_sid(f"po{self.dose}")] = Simulation(
            time_unit="min",
            end=10 * 60,  # measured for 8 hours
            preinit_changes={
                **self.default_changes(),
                **self.form_changes(self.form),
                "BW": Q(self.bodyweight, "kg"),
                "PODOSE_rome": Q(self.dose / 2.0, "mg"),
                "PODOSE_some": Q(self.dose / 2.0, "mg"),
            },
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        # unchanged omeprazole in urine has no observable in the model
        return {}

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig5",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[1].set_yaxis(f"{self.label_ome}\nurine", unit=self.unit_metabolite_urine)

        # simulation
        plots[0].add_data(
            task=self.to_sid(f"task_po{self.dose}"),
            xid="time",
            yid="[Cve_ome]",
            label=f"Sim {self.dose} mg",
            color=self.dose_colors[self.dose],
        )
        # data, no simulation: the model has no renal excretion of omeprazole
        plots[1].add_data(
            dataset="ome_cum_amount",
            xid="time",
            yid="mean",
            yid_se="mean_se",
            count="count",
            label=f"{self.dose} mg",
            color=self.dose_colors[self.dose],
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Qadir2017, output_dir=Qadir2017.__name__)
