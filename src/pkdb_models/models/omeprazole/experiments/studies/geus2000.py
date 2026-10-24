"""Simulation experiment of the study Geus2000."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
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
from sbmlsim.units import Quantity

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Geus2000(OmeprazoleSimulationExperiment):
    """Simulation experiment of Geus2000.

    16 healthy H. pylori negative subjects (9 F, 7 M; 73 kg) received
    omeprazole 20 mg as a MUPS tablet (enteric-coated micropellets) or
    pantoprazole 40 mg once daily for 6 days immediately before a standard
    breakfast (fed) in a randomised crossover; median plasma omeprazole on
    day 1 and day 6 (Fig4). The 24 hr intragastric pH (Fig1, Fig2, Tab1) is
    not mapped.
    """

    dset_ids: ClassVar[list[str]] = [
        "ome_20_day1",
        "ome_20_day6",
    ]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig4"]:
            df = self.load_dataframe(fig_id)
            # the data before the dose, i.e., before the start of the
            # simulation, is dropped
            df = df[df["time"] >= 0]
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("median", 1 / self.Mr.ome)
                dsets[label] = dset

        return dsets

    def study_changes(self) -> dict[str, Quantity]:
        """Get the changes of the subjects and the application form."""
        return {
            **self.form_changes(ApplicationForm.TABLET),  # MUPS
            **self.fed_changes(Fasting.FED),  # before breakfast
            "BW": Q(73, "kg"),
        }

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}

        # single application
        dose = 20  # [mg] omeprazole
        simulations[f"ome{dose}_single"] = Simulation(
            time_unit="min",
            end=24 * 60,
            preinit_changes={
                **self.default_changes(),
                **self.study_changes(),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
                "PODOSE_some": Q(dose / 2.0, "mg"),
            },
        )
        simulations[f"ome{dose}_multi"] = Simulation(
            time_unit="min",
            end=6 * 24 * 60,  # day 6 measured for 9 hours
            preinit_changes={
                **self.default_changes(),
                **self.study_changes(),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
                "PODOSE_some": Q(dose / 2.0, "mg"),
            },
            changes=[
                self.add_doses(
                    [k * 24 * 60 for k in range(1, 6)],
                    {
                        "PODOSE_rome": Q(dose / 2.0, "mg"),
                        "PODOSE_some": Q(dose / 2.0, "mg"),
                    },
                )
            ],
            time_shift=-5 * 24 * 60,
        )
        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for k, dset_id in enumerate(self.dset_ids):
            suffix = "single" if k == 0 else "multi"

            mappings[f"fm_ome20_{suffix}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dset_id,
                    xid="time",
                    yid="median",
                    yid_sd=None,
                    count="count",
                ),
                observable=FitData(
                    self, task=f"task_ome20_{suffix}", xid="time", yid="[Cve_ome]"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.TABLET,
                    dosing=Dosing.SINGLE if suffix == "single" else Dosing.MULTIPLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FED,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        figures = []
        for dosing in ["single", "multi"]:
            dset_id = "ome_20_day1" if dosing == "single" else "ome_20_day6"
            day = "day 1" if dosing == "single" else "day 6"
            fig = Figure(
                experiment=self, sid=f"Fig4_{dosing}", name=self.__class__.__name__
            )

            plots = fig.create_plots(
                xaxis=Axis(
                    self.label_time,
                    unit=self.unit_time,
                    min=-24 if dosing == "multi" else -0.5,
                    max=12.5,
                ),
                yaxis=Axis(self.label_ome, unit=self.unit_ome),
                legend=True,
            )

            # simulation
            plots[0].add_data(
                task=f"task_ome20_{dosing}",
                xid="time",
                yid="[Cve_ome]",
                label=f"Sim po20 fed {day}",
                color=self.dose_colors[20],
            )

            # dataset
            plots[0].add_data(
                dataset=dset_id,
                xid="time",
                yid="median",
                count="count",
                label=f"po20 fed {day}",
                color=self.dose_colors[20],
            )
            figures.append(fig)

        return self.figures_by_sid(*figures)


if __name__ == "__main__":
    MODEL.run_experiments(Geus2000, output_dir=Geus2000.__name__)
