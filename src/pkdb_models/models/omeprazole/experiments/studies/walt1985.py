"""Simulation experiment of the study Walt1985."""

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
from sbmlsim.simulation import Change, Simulation

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Walt1985(OmeprazoleSimulationExperiment):
    """Simulation experiment of Walt1985.

    5 men (72 kg, non-smokers) with a duodenal ulcer in symptomatic remission
    (`Health.DUODENAL_ULCER`) received 80 mg omeprazole IV (sodium salt
    reconstituted in PEG, 20 ml) infused at 99.9 ml/h, i.e. over 12 min, after
    an overnight fast; lunch 4 h after the dose. Plasma omeprazole until
    7 h 50 min (Fig5, mean and SEM of the five patients on two occasions; the
    count is the 5 patients). The times are from the start of the infusion.
    """

    bodyweight: ClassVar[float] = 72.0  # [kg]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig5"]:
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

        # single application
        dose = 80  # [mg]
        tcsims["iv80"] = Simulation(
            time_unit="min",
            end=8 * 60,
            preinit_changes={
                **self.default_changes(),
                "BW": Q(self.bodyweight, "kg"),
                # 80mg iv racemic mix 50/50 some rome, infused over 12 min
                "Ri_some": Q((dose / 2) / 12, "mg/min"),
                "Ri_rome": Q((dose / 2) / 12, "mg/min"),
            },
            changes=[
                # end of the infusion
                Change(
                    12,
                    {
                        "Ri_some": Q(0, "mg/min"),
                        "Ri_rome": Q(0, "mg/min"),
                    },
                )
            ],
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        return {
            "fm_ome_iv80": FitMapping(
                self,
                # data
                reference=FitData(
                    self,
                    dataset="Fig5_omeprazole_D_OME_iv_80",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                # simulation
                observable=FitData(self, task="task_iv80", xid="time", yid="[Cve_ome]"),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.IV,
                    application_form=ApplicationForm.SOLUTION,
                    dosing=Dosing.SINGLE,
                    health=Health.DUODENAL_ULCER,
                    fasting=Fasting.FASTED,
                    data_type=DataType.MEAN,
                ),
            ),
        }

    @override
    def figures(self) -> dict[str, Figure]:
        name = "Fig5"

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
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome, scale="log", min=0.01)

        # simulation
        plots[0].add_data(
            task="task_iv80",
            xid="time",
            yid="[Cve_ome]",
            label="Sim 80 mg IV",
            color=self.dose_colors[80],
        )

        # datasets
        plots[0].add_data(
            dataset="Fig5_omeprazole_D_OME_iv_80",
            xid="time",
            yid="mean",
            yid_sd="mean_sd",
            count="count",
            label="80 mg IV",
            color=self.dose_colors[80],
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Walt1985, output_dir=Walt1985.__name__)
