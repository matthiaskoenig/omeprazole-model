"""Simulation experiment of the study Cederberg1992."""

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
from sbmlsim.simulation import Change, Simulation
from sbmlsim.units import Quantity

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)
from pkdb_models.models.omeprazole.figures import figure_from_mappings


class Cederberg1992(OmeprazoleSimulationExperiment):
    """Simulation experiment of Cederberg1992.

    Nine fasted patients with a duodenal ulcer in symptomatic remission,
    otherwise healthy (`Health.DUODENAL_ULCER`), received omeprazole once
    daily for 5 days: 20 mg orally (hard gelatine capsule with enteric-coated
    granules, before breakfast), 10 mg and 40 mg IV (injections every 30 s
    over 5 min, simulated as a 5 min infusion); plasma omeprazole on day 1
    and day 5 (Fig4). The 24 hr intragastric pH (Fig1, Fig2, Tab1) is not
    mapped.
    """

    single_interventions: ClassVar[list[str]] = [
        "iv10",
        "iv40",
        "po20",
    ]

    multi_interventions: ClassVar[list[str]] = [
        "iv10_multi",
        "iv40_multi",
        "po20_multi",
    ]

    interventions: ClassVar[list[str]] = [*single_interventions, *multi_interventions]
    colors: ClassVar[dict[str, str]] = {
        "iv10": "black",
        "iv40": "dimgrey",
        "po20": "tab:blue",
        "iv10_multi": "black",
        "iv40_multi": "dimgrey",
        "po20_multi": "tab:blue",
    }
    #: legend names of the interventions
    legends: ClassVar[dict[str, str]] = {
        "iv10": "10 mg iv",
        "iv40": "40 mg iv",
        "po20": "20 mg po",
        "iv10_multi": "10 mg iv, multiple doses",
        "iv40_multi": "40 mg iv, multiple doses",
        "po20_multi": "20 mg po, multiple doses",
    }

    #: duration of the intravenous injections [min]
    injection_duration: ClassVar[float] = 5.0

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig4"]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for substance, df in dframes.items():
                for intervention, df_int in df.groupby("interventions"):
                    # concentrations below the limit of quantification are
                    # digitized as 0 after the peak (IV10): they are dropped
                    tmax = df_int.loc[df_int["mean"].idxmax(), "time"]
                    df_int = df_int[(df_int["mean"] > 0) | (df_int["time"] <= tmax)]
                    dsets[f"{fig_id}_{substance}_{intervention}"] = DataSet.from_df(
                        df_int, self.ureg
                    )

        return dsets

    def _dosing(self, route: str, dose: float) -> dict[str, Quantity]:
        """Get the changes of a dose of racemic omeprazole.

        Args:
            route: "iv" (injection over 5 min) or "po" (capsule).
            dose: the dose [mg].

        Returns:
            The changes of the dose, the start of the infusion for IV.
        """
        if route == "iv":
            rate = dose / 2.0 / self.injection_duration
            return {"Ri_some": Q(rate, "mg/min"), "Ri_rome": Q(rate, "mg/min")}
        return {"PODOSE_some": Q(dose / 2.0, "mg"), "PODOSE_rome": Q(dose / 2.0, "mg")}

    def _simulation(self, route: str, dose: float, days: int) -> Simulation:
        """Get the simulation of once daily doses.

        Args:
            route: "iv" (injection over 5 min) or "po" (capsule).
            dose: the dose [mg].
            days: the number of daily doses, the time of the last dose is 0.

        Returns:
            The simulation.
        """
        day = 24 * 60  # [min]
        changes = []
        if days > 1:
            times = [k * day for k in range(1, days)]
            dosing = self._dosing(route, dose)
            # an oral dose adds to the dose state, an injection sets the rate
            changes.append(
                self.add_doses(times, dosing)
                if route == "po"
                else Change(times, dosing)
            )
        if route == "iv":
            # end of the infusions
            changes.append(
                Change(
                    [k * day + self.injection_duration for k in range(days)],
                    {"Ri_some": Q(0, "mg/min"), "Ri_rome": Q(0, "mg/min")},
                )
            )
        form = self.form_changes(ApplicationForm.CAPSULE) if route == "po" else {}
        end = (days - 1) * day + 8 * 60
        return Simulation(
            time_unit="min",
            end=end,
            # a step of 1 min resolves the 5 min injections
            preinit_changes={
                **self.default_changes(),
                **form,
                **self._dosing(route, dose),
            },
            changes=changes,
            time_shift=-(days - 1) * day,
        )

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}
        for route, dose in [("iv", 10), ("iv", 40), ("po", 20)]:
            simulations[f"{route}{dose}"] = self._simulation(route, dose, days=1)
            simulations[f"{route}{dose}_multi"] = self._simulation(route, dose, days=5)

        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for intervention in self.interventions:
            mappings[f"fm_some_{intervention}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"Fig4_omeprazole_OME_{intervention}",
                    xid="time",
                    yid="mean",
                    count="count",
                ),
                observable=FitData(
                    self, task=f"task_{intervention}", xid="time", yid="[Cve_ome]"
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.IV if intervention.startswith("iv") else Route.PO,
                    application_form=ApplicationForm.SOLUTION
                    if intervention.startswith("iv")
                    else ApplicationForm.CAPSULE,
                    dosing=Dosing.MULTIPLE
                    if intervention.endswith("_multi")
                    else Dosing.SINGLE,
                    health=Health.DUODENAL_ULCER,
                    fasting=Fasting.FASTED,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure1_single(),
            **self.figure1_multi(),
            **self.figures_iv_po(),
        }

    def figures_iv_po(self) -> dict[str, Figure]:
        """Figures of the intravenous and the oral doses, single and multiple."""
        figures = []
        interventions_info = {
            "iv_single": ["iv10", "iv40"],
            "po_single": ["po20"],
            "iv_multi": ["iv10_multi", "iv40_multi"],
            "po_multi": ["po20_multi"],
        }
        for intervention_key, interventions in interventions_info.items():
            dosing = intervention_key.split("_")[1]

            fig = Figure(
                experiment=self,
                sid=f"Fig1_{intervention_key}",
                name=self.__class__.__name__,
            )
            plots = fig.create_plots(
                xaxis=Axis(
                    self.label_time,
                    unit=self.unit_time,
                    min=-24 if dosing == "multi" else None,
                ),
                legend=True,
            )
            plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)

            for intervention in interventions:
                dose = int(intervention.split("_")[0][2:])
                color = self.dose_colors[dose]

                # simulation
                plots[0].add_data(
                    task=f"task_{intervention}",
                    xid="time",
                    yid="[Cve_ome]",
                    label=f"Sim {self.legends[intervention]}",
                    color=color,
                )

                # dataset
                plots[0].add_data(
                    dataset=f"Fig4_omeprazole_OME_{intervention}",
                    xid="time",
                    yid="mean",
                    count="count",
                    label=self.legends[intervention],
                    color=color,
                )

            figures.append(fig)

        return self.figures_by_sid(*figures)

    def _figure_of_mappings(
        self, fig_id: str, interventions: list[str]
    ) -> dict[str, Figure]:
        """Figure of the fit mappings of the interventions."""
        mappings = self.fit_mappings()
        return figure_from_mappings(
            fig_id=fig_id,
            experiment=self,
            mappings=[mappings[f"fm_some_{i}"] for i in interventions],
            colors=[self.colors[i] for i in interventions],
            sim_labels=[f"Sim {self.legends[i]}" for i in interventions],
        )

    def figure1_single(self) -> dict[str, Figure]:
        """Figure of the fit mappings of the single doses."""
        return self._figure_of_mappings("Fig1B_single", self.single_interventions)

    def figure1_multi(self) -> dict[str, Figure]:
        """Figure of the fit mappings of the multiple doses."""
        return self._figure_of_mappings("Fig1B_multi", self.multi_interventions)


if __name__ == "__main__":
    MODEL.run_experiments(Cederberg1992, output_dir=Cederberg1992.__name__)
