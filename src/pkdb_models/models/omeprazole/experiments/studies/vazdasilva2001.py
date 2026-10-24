"""Simulation experiment of the study VazdaSilva2001."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    DataType,
    Dosing,
    Fasting,
    Health,
    PKPDMappingMetaData,
    Route,
    Tissue,
)
from sbmlsim import Q
from sbmlsim.data import DataSet
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class VazdaSilva2001(OmeprazoleSimulationExperiment):
    """Simulation experiment of VazdaSilva2001.

    Bioequivalence study: 24 healthy Caucasians (67.2 kg) took 20 mg
    omeprazole once daily in the morning, fasted, for 5 days as Mopral
    (reference, = Losec) and for 5 days as Ompranyt (test), both hard capsules
    with enteric-coated pellets, in a crossover without washout. Plasma
    omeprazole over 10 h after the last dose of each period (Fig1, mean and
    SEM): filled circles Mopral, open circles Ompranyt. The 5 doses are
    simulated, the last one at time 0.
    """

    #: the products: Mopral (reference) and Ompranyt (test)
    products: ClassVar[dict[str, str]] = {"MOP20": "Mopral", "OMP20": "Ompranyt"}
    colors: ClassVar[dict[str, str]] = {"MOP20": "black", "OMP20": "tab:blue"}
    bodyweight: ClassVar[float] = 67.2  # [kg]
    n_doses: ClassVar[int] = 5

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig1")
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.ome)
            dsets[str(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        dose = 20  # [mg]
        po_dose = {
            "PODOSE_some": Q(dose / 2.0, "mg"),
            "PODOSE_rome": Q(dose / 2.0, "mg"),
        }
        return {
            "po20_multi": Simulation(
                time_unit="min",
                end=self.n_doses * 24 * 60,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    **self.form_changes(ApplicationForm.CAPSULE),
                    **po_dose,
                },
                changes=[
                    self.add_doses(
                        [k * 24 * 60 for k in range(1, self.n_doses)], po_dose
                    )
                ],
                # the last dose at time 0
                time_shift=-(self.n_doses - 1) * 24 * 60,
            )
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for dset_id in self.products:
            mappings[f"fm_ome_po20_multi_{dset_id}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dset_id,
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self, task="task_po20_multi", xid="time", yid="[Cve_ome]"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.CAPSULE,
                    dosing=Dosing.MULTIPLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                    data_type=DataType.MEAN,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig1",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=12),
            legend=True,
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome, min=0)
        plots[1].set_yaxis(self.label_ome, unit=self.unit_ome, scale="log", min=0.01)

        for plot in plots:
            plot.add_data(
                task="task_po20_multi",
                xid="time",
                yid="[Cve_ome]",
                label="Sim 20 mg, dose 5",
                color="tab:red",
            )
            for dset_id, product in self.products.items():
                plot.add_data(
                    dataset=dset_id,
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=product,
                    color=self.colors[dset_id],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(VazdaSilva2001, output_dir=VazdaSilva2001.__name__)
