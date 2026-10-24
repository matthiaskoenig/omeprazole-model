"""Simulation experiment of the study Andersson2001."""

from typing import ClassVar, override

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


class Andersson2001(OmeprazoleSimulationExperiment):
    """Simulation experiment of Andersson2001.

    Review of the interactions of esomeprazole; Fig9 is study [14]: 18 healthy
    men and women received esomeprazole 40 mg once daily for 7 days alone or
    with amoxicillin 1 g and clarithromycin 500 mg twice daily (randomised
    crossover); the profile of day 7. The formulation is not reported:
    esomeprazole is an enteric-coated form (no drug before 0.5 hr, tmax 2 hr),
    simulated as an enteric-coated capsule. Fasting is not reported.

    Clarithromycin inhibits CYP3A4 (`F_CYP3A4_CLARITHROMYCIN`, literature
    based, not fitted), amoxicillin has no effect on the CYP enzymes; the
    observed AUC ratio is 1.70 (13.3 vs 22.7 µmol*h/l).
    """

    #: the arms: esomeprazole alone and with clarithromycin and amoxicillin
    dset_ids: ClassVar[list[str]] = ["SOME", "SOME_CLA_AMO"]
    arm_tasks: ClassVar[dict[str, str]] = {
        "SOME": "task_some40",
        "SOME_CLA_AMO": "task_some40_cla",
    }
    colors: ClassVar[dict[str, str]] = {
        "SOME": "tab:orange",
        "SOME_CLA_AMO": "tab:red",
    }
    labels_arm: ClassVar[dict[str, str]] = {
        "SOME": "po40",
        "SOME_CLA_AMO": "po40 + clarithromycin + amoxicillin",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig9"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dsets[label] = DataSet.from_df(df_label, self.ureg)

        return dsets

    def _simulation(self, f_cyp3a4: float) -> Simulation:
        """Get the simulation of 7 daily doses of 40 mg esomeprazole.

        Args:
            f_cyp3a4: the hepatic activity of CYP3A4.

        Returns:
            The simulation, the time of the 7th dose is 0.
        """
        dose = {"PODOSE_some": Q(40, "mg")}  # 40 mg S-omeprazole
        return Simulation(
            time_unit="min",
            end=7 * 24 * 60,
            preinit_changes={
                **self.default_changes(),
                **self.form_changes(ApplicationForm.CAPSULE),
                "LI__f_cyp3a4": Q(f_cyp3a4, "dimensionless"),
                **dose,
            },
            changes=[self.add_doses([k * 24 * 60 for k in range(1, 7)], dose)],
            time_shift=-(6 * 24) * 60,  # [min]
        )

    @override
    def simulations(self) -> dict[str, Simulation]:
        return {
            "some40": self._simulation(f_cyp3a4=1.0),
            "some40_cla": self._simulation(f_cyp3a4=self.F_CYP3A4_CLARITHROMYCIN),
        }

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for dset_id in self.dset_ids:
            mappings[f"fm_some40po_{dset_id}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=dset_id,
                    xid="time",
                    yid="mean",
                    yid_sd=None,
                    count="count",
                ),
                observable=FitData(
                    self, task=self.arm_tasks[dset_id], xid="time", yid="[Cve_some]"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.NR,
                    dosing=Dosing.MULTIPLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.NR,
                    coadministration=Coadministration.CLARITHROMYCIN
                    if dset_id == "SOME_CLA_AMO"
                    else Coadministration.NONE,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig9",
            name=self.__class__.__name__,
            num_rows=1,
            num_cols=2,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_xaxis(self.label_time, unit=self.unit_time, min=-0.5, max=12.5)
        plots[1].set_xaxis(self.label_time, unit=self.unit_time, min=-24, max=12.5)
        for plot in plots:
            plot.set_yaxis(self.label_some, unit=self.unit_some)

        for dset_id in self.dset_ids:
            for plot in plots:
                # simulation
                plot.add_data(
                    task=self.arm_tasks[dset_id],
                    xid="time",
                    yid="[Cve_some]",
                    label=f"Sim {self.labels_arm[dset_id]}",
                    color=self.colors[dset_id],
                )
                # data
                plot.add_data(
                    dataset=dset_id,
                    xid="time",
                    yid="mean",
                    count="count",
                    label=self.labels_arm[dset_id],
                    color=self.colors[dset_id],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Andersson2001, output_dir=Andersson2001.__name__)
