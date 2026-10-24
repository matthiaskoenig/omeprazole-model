"""Simulation experiment of the study Lind1983."""

from typing import override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
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


class Lind1983(OmeprazoleSimulationExperiment):
    """Simulation experiment of Lind1983.

    11 healthy men (74 kg), Fig3 the plasma omeprazole after 40 mg (6
    subjects). Omeprazole suspended in 50 ml water-methocel with 8 mmol sodium
    bicarbonate and 8 mmol sodium bicarbonate at 0, 10, 20 and 30 min (a
    buffered suspension, simulated as a buffered solution), fasted.
    Intravenous pentagastrin (30 µg/hr from 1 hr before the dose to the end)
    stimulates the gastric acid secretion (`Coadministration.PENTAGASTRIN`),
    the gastric juice is aspirated by a nasogastric tube and the stomach is
    emptied 55 to 60 min after the dose. The emptying is not simulated: the
    buffered solution has left the stomach of the model by then (gastric
    emptying `GU__Ka_dis_ome` 6/hr, 0.4 % of the dose left at 55 min). The
    acid output (Fig2) is not mapped: the model has no stimulation of the
    acid secretion by pentagastrin.
    """

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for substance, df in dframes.items():
                dset = DataSet.from_df(df, self.ureg)
                for intervention in df.interventions.unique():
                    dsets[f"{fig_id}_{substance}_{intervention}"] = dset[
                        dset.interventions == intervention
                    ]

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose = 40

        # single application
        tcsims["ome40"] = Simulation(
            time_unit="min",
            end=4 * 60,
            preinit_changes={
                **self.default_changes(),
                "BW": Q(74.0, "kg"),
                **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                **self.fed_changes(Fasting.FASTED),
                "PODOSE_some": Q(dose / 2.0, "mg"),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
            },
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        mappings["fm_ome_po40"] = FitMapping(
            self,
            # data
            reference=FitData(
                self,
                dataset="Fig3_omeprazole_D_OME_po_40",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
            ),
            # simulation
            observable=FitData(self, task="task_ome40", xid="time", yid="[Cve_ome]"),
            metadata=PKPDMappingMetaData(
                tissue=Tissue.PLASMA,
                route=Route.PO,
                application_form=ApplicationForm.BUFFERED_SOLUTION,
                dosing=Dosing.SINGLE,
                health=Health.HEALTHY,
                fasting=Fasting.FASTED,
                coadministration=Coadministration.PENTAGASTRIN,
            ),
        )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        name = "Fig3"
        fig = Figure(
            experiment=self,
            sid=name,
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )

        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0), legend=True
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)

        # simulation
        plots[0].add_data(
            task="task_ome40",
            xid="time",
            yid="[Cve_ome]",
            label="Sim po40",
            color=self.dose_colors[40],
        )
        # datasets
        plots[0].add_data(
            dataset="Fig3_omeprazole_D_OME_po_40",
            xid="time",
            yid="mean",
            yid_sd="mean_sd",
            count="count",
            label="po40",
            color=self.dose_colors[40],
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Lind1983, output_dir=Lind1983.__name__)
