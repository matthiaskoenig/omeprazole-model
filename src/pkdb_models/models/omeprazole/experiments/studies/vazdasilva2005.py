"""Simulation experiment of the study VazdaSilva2005."""

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


class VazdaSilva2005(OmeprazoleSimulationExperiment):
    """Simulation experiment of VazdaSilva2005.

    23 healthy subjects (66.1 kg; 7 of the 11 women on oral contraceptives)
    took 20 mg omeprazole once daily as Mopral (reference, = Losec) or
    Ompranyt (test), hard capsules with enteric-coated pellets, in four
    consecutive periods of 7 days without washout: fasting (part 1) and with a
    high-fat breakfast (750 kcal) immediately before every dose (part 2).
    Plasma omeprazole over 12 h after the 7th dose of every period (Fig2, mean
    and SEM): circles fasting, triangles fed, filled Mopral, open Ompranyt.
    The 7 doses of a period are simulated, the last one at time 0; food is the
    switch `GU__fed` for every dose of the fed periods.
    """

    #: the products: Mopral (reference) and Ompranyt (test)
    products: ClassVar[list[str]] = ["Mopral", "Ompranyt"]
    foods: ClassVar[dict[str, Fasting]] = {
        "fasting": Fasting.FASTED,
        "fed": Fasting.FED,
    }
    colors: ClassVar[dict[str, str]] = {"fasting": "black", "fed": "tab:orange"}
    markers: ClassVar[dict[str, str]] = {"Mopral": "o", "Ompranyt": "^"}
    bodyweight: ClassVar[float] = 66.1  # [kg]
    n_doses: ClassVar[int] = 7

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        df = self.load_dataframe("Fig2")
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.ome)
            dsets[str(label)] = dset
        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose = 20  # [mg]
        po_dose = {
            "PODOSE_some": Q(dose / 2.0, "mg"),
            "PODOSE_rome": Q(dose / 2.0, "mg"),
        }
        for food, fasting in self.foods.items():
            tcsims[f"po20_multi_{food}"] = Simulation(
                time_unit="min",
                end=self.n_doses * 24 * 60,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    **self.form_changes(ApplicationForm.CAPSULE),
                    **self.fed_changes(fasting),
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

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for product in self.products:
            for food, fasting in self.foods.items():
                mappings[f"fm_ome_po20_multi_{product}_{food}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"{product}_{food}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=f"task_po20_multi_{food}",
                        xid="time",
                        yid="[Cve_ome]",
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.CAPSULE,
                        dosing=Dosing.MULTIPLE,
                        health=Health.HEALTHY,
                        fasting=fasting,
                        data_type=DataType.MEAN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=12),
            legend=True,
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome, min=0)
        plots[1].set_yaxis(self.label_ome, unit=self.unit_ome, scale="log", min=0.005)

        for plot in plots:
            for food in self.foods:
                plot.add_data(
                    task=f"task_po20_multi_{food}",
                    xid="time",
                    yid="[Cve_ome]",
                    label=f"Sim {food}",
                    color=self.colors[food],
                )
                for product in self.products:
                    plot.add_data(
                        dataset=f"{product}_{food}",
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"{product} {food}",
                        color=self.colors[food],
                        marker=self.markers[product],
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(VazdaSilva2005, output_dir=VazdaSilva2005.__name__)
