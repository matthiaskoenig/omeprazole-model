"""Simulation experiment of the study Andersson1990a."""

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


class Andersson1990a(OmeprazoleSimulationExperiment):
    """Simulation experiment of Andersson1990a.

    Ten healthy fasted males (70-86 kg) received omeprazole 10 and 40 mg IV
    (duration of the injection not reported, simulated as bolus) and 10, 40
    and 90 mg orally as a solution in PEG 400 diluted with NaHCO3, with 48 mmol
    sodium bicarbonate before, with and after the dose (buffered solution),
    in a randomised five-way crossover. Plasma omeprazole (n=10), omeprazole
    sulphone (n=10; 40 mg IV, 10, 40 and 90 mg PO) and 5-hydroxyomeprazole
    (n=5; 40 mg IV, 40 and 90 mg PO) for 8 hr.

    Fig1 has a logarithmic concentration axis: the copy of the data is the
    re-calibrated reading (the curation read it linearly), which reproduces
    the AUC of Tab1 and Tab2.
    """

    routes: ClassVar[list[str]] = ["IV", "IV", "PO", "PO", "PO"]
    doses: ClassVar[list[int]] = [10, 40, 10, 40, 90]

    sids: ClassVar[list[str]] = ["ome", "omeoh", "omesul"]
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}

        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]
            # single application, the oral dose a buffered solution
            form_changes = (
                self.form_changes(ApplicationForm.BUFFERED_SOLUTION)
                if route == "PO"
                else {}
            )
            simulations[f"ome_{route}_{dose}"] = Simulation(
                time_unit="min",
                end=8 * 60,
                preinit_changes={
                    **self.default_changes(),
                    **form_changes,
                    f"{route.upper()}DOSE_rome": Q(dose / 2.0, "mg"),
                    f"{route.upper()}DOSE_some": Q(dose / 2.0, "mg"),
                },
            )

        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]

            for k, yid in enumerate(self.yids):
                sid = self.sids[k]

                if sid == "omesul" and dose == 10 and route == "IV":
                    continue
                if sid == "omeoh" and dose == 10:
                    continue

                mappings[f"fm_ome{route.lower()}{dose}_{sid}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=f"OME_{route}_{dose}_{sid}",
                        xid="time",
                        yid="mean",
                        yid_sd=None,
                        count="count",
                    ),
                    observable=FitData(
                        self, task=f"task_ome_{route}_{dose}", xid="time", yid=yid
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.IV if route == "IV" else Route.PO,
                        application_form=ApplicationForm.SOLUTION
                        if route == "IV"
                        else ApplicationForm.BUFFERED_SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        figures = []
        for subset in ["IV", "PO"]:
            fig = Figure(
                experiment=self,
                sid=f"Fig1_{subset.lower()}",
                num_rows=3,
                num_cols=1,
                name=self.__class__.__name__,
            )
            plots = fig.create_plots(
                xaxis=Axis(self.label_time, unit=self.unit_time, max=6), legend=True
            )
            # logarithmic axes as in the publication
            plots[0].set_yaxis(
                self.label_ome, unit=self.unit_ome, scale="log", min=0.03
            )
            plots[1].set_yaxis(
                self.label_omeoh, unit=self.unit_omeoh, scale="log", min=0.03
            )
            plots[2].set_yaxis(
                self.label_omesul, unit=self.unit_omesul, scale="log", min=0.03
            )

            for kr, route in enumerate(self.routes):
                if route != subset:
                    continue

                dose = self.doses[kr]
                color = self.dose_colors[dose]

                # simulation
                for k, yid in enumerate(self.yids):
                    plots[k].add_data(
                        task=f"task_ome_{route}_{dose}",
                        xid="time",
                        yid=yid,
                        label=f"Sim {route.lower()}{dose}",
                        color=color,
                    )

                # dataset
                for k, sid in enumerate(self.sids):
                    if sid == "omesul" and dose == 10 and route == "IV":
                        continue
                    if sid == "omeoh" and dose == 10:
                        continue
                    plots[k].add_data(
                        dataset=f"OME_{route}_{dose}_{sid}",
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"{route.lower()}{dose}",
                        color=color,
                    )

            figures.append(fig)

        return self.figures_by_sid(*figures)


if __name__ == "__main__":
    MODEL.run_experiments(Andersson1990a, output_dir=Andersson1990a.__name__)
