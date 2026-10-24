"""Simulation experiment of the study Prichard1985."""

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


class Prichard1985(OmeprazoleSimulationExperiment):
    """Simulation experiment of Prichard1985.

    8 healthy men (22 years, 74 kg) took 40 mg omeprazole (two capsules of
    20 mg enteric-coated granulate) once daily for 5 days, at 9 AM (`am`) or at
    9 PM (`pm`) in a randomized crossover; food was withheld from 1 h before to
    2 h after the dose. Plasma omeprazole after the dose of day 1 (`single`)
    and of day 5 (`multi`) (Fig2, mean and SEM, n = 8).

    The model has no circadian rhythm and no meals: the morning and the evening
    doses map to the same simulation. The evening dose is absorbed later and
    less on day 1 (tmax 4.8 h, AUC 842 vs 1187 ng*h/ml).

    Fig2 has a log axis (1 to 1000 ng/ml); the curated values were a linear
    reading of it, the data copy is the back transform 1000^((v - 1)/999),
    with which the AUC of the curves agree with Tab2 within 4 %.
    """

    dose: ClassVar[float] = 40  # [mg]
    form: ClassVar[ApplicationForm] = ApplicationForm.CAPSULE
    bodyweight: ClassVar[float] = 74  # [kg]
    days: ClassVar[int] = 5
    dosings: ClassVar[list[str]] = ["single", "multi"]
    day_times: ClassVar[list[str]] = ["am", "pm"]
    colors: ClassVar[dict[str, str]] = {"am": "tab:blue", "pm": "tab:orange"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr.ome)
                dsets[self.to_sid(str(label))] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose_changes = {
            "PODOSE_some": Q(self.dose / 2.0, "mg"),
            "PODOSE_rome": Q(self.dose / 2.0, "mg"),
        }
        changes = {
            **self.default_changes(),
            **self.form_changes(self.form),
            "BW": Q(self.bodyweight, "kg"),
            **dose_changes,
        }

        # first dose
        tcsims[self.to_sid(f"po{self.dose}_single")] = Simulation(
            time_unit="min",
            end=24 * 60,
            preinit_changes=changes,
        )
        # once daily for 5 days, time 0 is the dose of day 5
        tcsims[self.to_sid(f"po{self.dose}_multi")] = Simulation(
            time_unit="min",
            end=self.days * 24 * 60,
            preinit_changes=changes,
            changes=[
                self.add_doses([k * 24 * 60 for k in range(1, self.days)], dose_changes)
            ],
            time_shift=-(self.days - 1) * 24 * 60,  # [min]
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for dosing in self.dosings:
            for day_time in self.day_times:
                mappings[self.to_sid(f"fm_po{self.dose}_{dosing}_{day_time}")] = (
                    FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(f"po{self.dose}_{dosing}_{day_time}"),
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=self.to_sid(f"task_po{self.dose}_{dosing}"),
                            xid="time",
                            yid="[Cve_ome]",
                        ),
                        metadata=PKPDMappingMetaData(
                            tissue=Tissue.PLASMA,
                            route=Route.PO,
                            application_form=self.form,
                            dosing=Dosing.SINGLE
                            if dosing == "single"
                            else Dosing.MULTIPLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                            data_type=DataType.MEAN,
                        ),
                    )
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
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=13),
            legend=True,
        )
        for kp, dosing in enumerate(self.dosings):
            plots[kp].set_yaxis(
                self.label_ome, unit=self.unit_ome, scale="log", min=1e-3, max=5
            )
            plots[kp].set_title("day 1" if dosing == "single" else "day 5")

            # simulation
            plots[kp].add_data(
                task=self.to_sid(f"task_po{self.dose}_{dosing}"),
                xid="time",
                yid="[Cve_ome]",
                label=f"Sim {self.dose} mg",
                color="black",
            )

            # data
            for day_time in self.day_times:
                plots[kp].add_data(
                    dataset=self.to_sid(f"po{self.dose}_{dosing}_{day_time}"),
                    xid="time",
                    yid="mean",
                    # SEM as in the publication
                    yid_se="mean_se",
                    count="count",
                    label=f"{self.dose} mg {day_time.upper()}",
                    color=self.colors[day_time],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Prichard1985, output_dir=Prichard1985.__name__)
