"""Simulation experiment of the study Elkoshi2002."""

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


class Elkoshi2002(OmeprazoleSimulationExperiment):
    """Simulation experiment of Elkoshi2002.

    40 fasted healthy males (not phenotyped for CYP2C19, the arithmetic means
    include poor metabolizers) received omeprazole 20 mg once daily for 5 days
    as Losec (reference, enteric-coated capsules, LOS) or Omepradex (test,
    enteric-coated caplets, OMEX) in a randomised crossover; plasma
    omeprazole on day 1 (Fig1) and day 5 (Fig2). The coating of the caplets
    fails at pH 3-4 in vitro (earlier tmax 1.1-1.25 hr vs 1.8-2.1 hr): the
    model has no partial failure of a coating, the caplets are simulated as
    an enteric-coated tablet.
    """

    single_interventions: ClassVar[list[str]] = [
        "LOS20_SINGLE",
        "OMEX20_SINGLE",
    ]

    multi_interventions: ClassVar[list[str]] = [
        "LOS20_MULTIPLE",
        "OMEX20_MULTIPLE",
    ]

    #: the application form of the products
    forms: ClassVar[dict[str, ApplicationForm]] = {
        "LOS": ApplicationForm.CAPSULE,
        "OMEX": ApplicationForm.TABLET,
    }
    colors: ClassVar[dict[str, str]] = {
        "LOS": "tab:blue",
        "OMEX": "tab:green",
    }
    markers: ClassVar[dict[str, str]] = {
        "LOS20_SINGLE": "s",
        "OMEX20_SINGLE": "o",
        "LOS20_MULTIPLE": "s",
        "OMEX20_MULTIPLE": "o",
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig2"]:
            df = self.load_dataframe(fig_id)
            if fig_id == "Fig1":
                # the data of the single doses before the dose, i.e., before
                # the start of the simulation, is dropped
                df = df[df["time"] >= 0]
            for intervention, df_intervention in df.groupby("intervention"):
                intervention = str(intervention)
                dset = DataSet.from_df(df_intervention, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr.ome)
                dsets[intervention] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}
        dose = {
            "PODOSE_some": Q(20 / 2.0, "mg"),
            "PODOSE_rome": Q(20 / 2.0, "mg"),
        }
        for product, form in self.forms.items():
            # single application
            simulations[f"{product}20_single"] = Simulation(
                time_unit="min",
                end=14 * 60,  # 14 hr, the data cover 12 hr
                preinit_changes={
                    **self.default_changes(),
                    **self.form_changes(form),
                    **dose,
                },
            )
            # once daily for 5 days, the time of the 5th dose is 0
            simulations[f"{product}20_multi"] = Simulation(
                time_unit="min",
                end=4 * 24 * 60 + 14 * 60,
                preinit_changes={
                    **self.default_changes(),
                    **self.form_changes(form),
                    **dose,
                },
                changes=[self.add_doses([k * 24 * 60 for k in range(1, 5)], dose)],
                time_shift=-4 * 24 * 60,  # [min]
            )

        return simulations

    @staticmethod
    def _task(intervention: str) -> str:
        """Get the task of the intervention, e.g. LOS20_SINGLE -> task_LOS20_single."""
        product, dosing = intervention.split("_")
        return f"task_{product}_{'single' if dosing == 'SINGLE' else 'multi'}"

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for intervention in self.single_interventions + self.multi_interventions:
            dosing = "single" if "SINGLE" in intervention else "multi"
            product = intervention.split("20_")[0]

            mappings[f"fm_ome20po_{intervention}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=intervention,
                    xid="time",
                    yid="mean",
                    yid_sd=None,
                    count="count",
                ),
                observable=FitData(
                    self, task=self._task(intervention), xid="time", yid="[Cve_ome]"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=self.forms[product],
                    dosing=Dosing.SINGLE if dosing == "single" else Dosing.MULTIPLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self._figure("Fig1_single", self.single_interventions),
            **self._figure("Fig2_multi", self.multi_interventions),
        }

    def _figure(self, fig_id: str, interventions: list[str]) -> dict[str, Figure]:
        """Figure of the plasma concentration of the products."""
        multi = "MULTIPLE" in interventions[0]
        fig = Figure(
            experiment=self,
            sid=fig_id,
            num_rows=1,
            num_cols=1,
            name=self.sid,
        )
        plots = fig.create_plots(
            xaxis=Axis(
                self.label_time,
                unit=self.unit_time,
                min=-0.5,
                max=12.5,
            ),
            legend=True,
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)

        for intervention in interventions:
            product = intervention.split("20_")[0]
            label = f"po20 {product} ({self.forms[product].name.lower()})"
            color = self.colors[product]
            # simulation
            plots[0].add_data(
                task=self._task(intervention),
                xid="time",
                yid="[Cve_ome]",
                label=f"Sim {label}" + (" day 5" if multi else ""),
                color=color,
                # both products are enteric coated, the simulations are equal
                linestyle="dashed" if product == "OMEX" else "solid",
            )
            # data
            plots[0].add_data(
                dataset=intervention,
                xid="time",
                yid="mean",
                count="count",
                label=label + (" day 5" if multi else ""),
                color=color,
                marker=self.markers[intervention],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Elkoshi2002, output_dir=Elkoshi2002.__name__)
