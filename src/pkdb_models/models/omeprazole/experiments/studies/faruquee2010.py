"""Simulation experiment of the study Faruquee2010."""

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

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Faruquee2010(OmeprazoleSimulationExperiment):
    """Simulation experiment of Faruquee2010.

    Six fasted healthy adults (4 M, 2 F, 69.8 kg) received omeprazole
    magnesium 20 mg (capsule), levofloxacin 500 mg or both as single doses in
    a randomised crossover; "omeprazole" in the urine for 48 hr by HPLC-UV
    (cumulative excretion Fig3, rate Fig4).

    The assay is not specific for omeprazole: 41 % of the dose as unchanged
    omeprazole with a urinary half-life of 21 hr is incompatible with a drug
    which is completely metabolized (plasma half-life about 1 hr). The data
    are compared with the urinary metabolites of the model and are outliers.
    """

    # the arm with levofloxacin (OME_LEVO) is not used: levofloxacin does not
    # interact with omeprazole (Tab2) and the data are outliers
    prefixes: ClassVar[list[str]] = [
        "OME",
    ]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3", "Fig4"]:
            df = self.load_dataframe(fig_id)

            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                if fig_id == "Fig4":
                    dset.unit_conversion("mean", 1 / self.Mr.ome)
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}

        # single application
        dose = 20  # [mg] omeprazole
        simulations[f"ome{dose}"] = Simulation(
            time_unit="min",
            end=49 * 60,  # urine for 48 hr
            preinit_changes={
                **self.default_changes(),
                **self.form_changes(ApplicationForm.CAPSULE),
                "BW": Q(69.8, "kg"),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
                "PODOSE_some": Q(dose / 2.0, "mg"),
            },
        )
        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for prefix in self.prefixes:
            # figure 3
            mappings["fm_ome20_cum_amount"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"{prefix}_cum_amount",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self, task="task_ome20", xid="time", yid="Aurine_omemets"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.URINE,
                    route=Route.PO,
                    application_form=ApplicationForm.CAPSULE,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
            )
            # figure 4
            mappings["fm_ome20_ex_rate"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"{prefix}_ex_rate",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self, task="task_ome20", xid="time", yid="KI__OMEMETSEX"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.URINE,
                    route=Route.PO,
                    application_form=ApplicationForm.CAPSULE,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure3(),
            **self.figure4(),
        }

    def figure3(self) -> dict[str, Figure]:
        """Figure of the cumulative urinary excretion of the metabolites."""
        name = "Fig3"

        fig3 = Figure(
            experiment=self,
            sid=name,
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )

        plots = fig3.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            yaxis=Axis("Omeprazole metabolites\nurine", unit="µmole"),
            legend=True,
        )
        # simulation
        plots[0].add_data(
            task="task_ome20",
            xid="time",
            yid="Aurine_omemets",
            label="Sim po20",
            color=self.dose_colors[20],
        )
        # data
        for prefix in self.prefixes:
            plots[0].add_data(
                dataset=f"{prefix}_cum_amount",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"po20 {prefix} (assay)",
                color=self.dose_colors[20],
            )

        return self.figures_by_sid(fig3)

    def figure4(self) -> dict[str, Figure]:
        """Figure of the urinary excretion rate of the metabolites."""
        name = "Fig4"

        fig4 = Figure(
            experiment=self,
            sid=name,
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )
        plots = fig4.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time),
            yaxis=Axis(
                "Urinary omeprazole\nmetabolite excretion rate", unit="µmole/hr"
            ),
            legend=True,
        )

        # simulation
        plots[0].add_data(
            task="task_ome20",
            xid="time",
            yid="KI__OMEMETSEX",
            label="Sim po20",
            color=self.dose_colors[20],
        )

        # data
        for prefix in self.prefixes:
            plots[0].add_data(
                dataset=f"{prefix}_ex_rate",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=f"po20 {prefix} (assay)",
                color=self.dose_colors[20],
            )

        return self.figures_by_sid(fig4)


if __name__ == "__main__":
    MODEL.run_experiments(Faruquee2010, output_dir=Faruquee2010.__name__)
