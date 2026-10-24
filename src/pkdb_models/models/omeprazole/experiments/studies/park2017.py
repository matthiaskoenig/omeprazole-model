"""Simulation experiment of the study Park2017."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    DataType,
    Dosing,
    Fasting,
    Health,
    Phenotype,
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


class Park2017(OmeprazoleSimulationExperiment):
    """Simulation experiment of Park2017.

    24 healthy Korean volunteers (27.2 years, 68.6 kg, 1.74 m), 8 per CYP2C19
    phenotype: extensive (*1/*1, `EM`), intermediate (*1/*2 or *1/*3, `IM`)
    and poor metabolizers (*2/*2, *2/*3 or *3/*3, `PM`), carriers of *17
    excluded. 20 mg omeprazole as enteric-coated granules (Losec) once daily on
    an empty stomach for 8 days; plasma omeprazole, 5-hydroxyomeprazole and
    omeprazole sulfone after the first (single) and the last dose of day 8
    (multi, time 0 is the last dose, the point at 0 the trough 24 h after the
    dose of day 7) (Fig3, mean and SD).

    The data are read from the vector graphics of Fig3: the means exactly, the
    SD from the caps of the bars, which are assigned to the symbols in the order
    of their height where the bars of a time point overlap.
    """

    dose: ClassVar[float] = 20  # [mg]
    form: ClassVar[ApplicationForm] = ApplicationForm.GRANULES
    bodyweight: ClassVar[float] = 68.6  # [kg]
    days: ClassVar[int] = 8
    variants: ClassVar[list[str]] = ["EM", "IM", "PM"]
    dosings: ClassVar[list[str]] = ["single", "multi"]
    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
    ]
    sids: ClassVar[list[str]] = ["ome", "omeoh", "omesul"]
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        mrs = dict(zip(self.substances, self.sids, strict=True))
        for fig_id in ["Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                substance = str(df_label["substance"].iloc[0])
                dset = DataSet.from_df(df_label, self.ureg)
                dset.unit_conversion("mean", 1 / getattr(self.Mr, mrs[substance]))
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose_changes = {
            "PODOSE_rome": Q(self.dose / 2.0, "mg"),
            "PODOSE_some": Q(self.dose / 2.0, "mg"),
        }
        for variant in self.variants:
            changes = {
                **self.default_changes(),
                **self.form_changes(self.form),
                "BW": Q(self.bodyweight, "kg"),
                "LI__f_cyp2c19": Q(self.cyp2c19_map[variant], "dimensionless"),
                **dose_changes,
            }

            # single dose
            tcsims[self.to_sid(f"po{self.dose}_{variant}_single")] = Simulation(
                time_unit="min",
                end=13 * 60,
                preinit_changes=changes,
            )

            # once daily for 8 days, time 0 is the dose of day 8
            tcsims[self.to_sid(f"po{self.dose}_{variant}_multi")] = Simulation(
                time_unit="min",
                end=(self.days - 1) * 24 * 60 + 13 * 60,
                preinit_changes=changes,
                changes=[
                    self.add_doses(
                        [k * 24 * 60 for k in range(1, self.days)],
                        dose_changes,
                    ),
                ],
                time_shift=-(self.days - 1) * 24 * 60,  # [min]
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for variant in self.variants:
            for k, yid in enumerate(self.yids):
                for dosing in self.dosings:
                    mappings[
                        self.to_sid(
                            f"fm_po{self.dose}_{dosing}_{variant}_{self.sids[k]}"
                        )
                    ] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(
                                f"{variant}_OME20_{dosing.upper()}_{self.substances[k]}"
                            ),
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=self.to_sid(f"task_po{self.dose}_{variant}_{dosing}"),
                            xid="time",
                            yid=yid,
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
                            phenotype=Phenotype[f"CYP2C19_{variant}"],
                            data_type=DataType.MEAN,
                        ),
                    )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig3",
            num_rows=3,
            num_cols=2,
            name=self.__class__.__name__,
        )

        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        for k, yid in enumerate(self.yids):
            for kd, dosing in enumerate(self.dosings):
                plots[2 * k + kd].set_yaxis(self.labels[yid], unit=self.unit_metabolite)
                if k == 0:
                    plots[kd].set_title(
                        f"{dosing} dose" if dosing == "single" else "day 8"
                    )
        for k in [1, 3, 5]:
            plots[k].set_xaxis(self.label_time, unit=self.unit_time, min=-12, max=13)

        for kd, dosing in enumerate(self.dosings):
            for variant in self.variants:
                color = self.cyp2c19_colors[variant]
                for k, yid in enumerate(self.yids):
                    # simulation
                    plots[2 * k + kd].add_data(
                        task=self.to_sid(f"task_po{self.dose}_{variant}_{dosing}"),
                        xid="time",
                        yid=yid,
                        label=f"Sim {variant}",
                        color=color,
                    )
                    # data
                    plots[2 * k + kd].add_data(
                        dataset=self.to_sid(
                            f"{variant}_OME20_{dosing.upper()}_{self.substances[k]}"
                        ),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=variant,
                        color=color,
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Park2017, output_dir=Park2017.__name__)
