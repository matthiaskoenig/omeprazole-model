"""Simulation experiment of the study Andersson1993."""

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

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Andersson1993(OmeprazoleSimulationExperiment):
    """Simulation experiment of Andersson1993.

    Eight fasted patients with liver cirrhosis (Child-Pugh A 3, B 4, C 1;
    median 70 kg) received [14C]omeprazole 20 mg IV (infused over 5 min) and
    40 mg orally as a buffered solution (PEG 400 and sodium bicarbonate) in a
    randomised crossover. Plasma omeprazole, 5-hydroxyomeprazole, the sulphone
    and the total radioactive metabolites for 24 hr (Fig1, Fig2) and the
    cumulative urinary radioactivity for 96 hr (Fig3).

    The data are mapped to the simulation of the group, whose cirrhosis is the
    mean of the Child-Pugh classes of the patients (`f_cirrhosis_group`); the
    figure shows the classes as a scan.
    """

    routes: ClassVar[list[str]] = ["IV", "PO"]
    doses: ClassVar[list[int]] = [20, 40]
    sids: ClassVar[list[str]] = ["ome", "omeoh", "omesul", "omemets", "amount"]
    yids: ClassVar[list[str]] = [
        "[Cve_ome]",
        "[Cve_omeoh]",
        "[Cve_omesul]",
        "[Cve_omemets]",
        "Aurine_omemets",
    ]
    #: Child-Pugh classes of the 8 patients (Tab1): A 3, B 4, C 1
    child_pugh_counts: ClassVar[dict[str, int]] = {
        "Mild cirrhosis": 3,
        "Moderate cirrhosis": 4,
        "Severe cirrhosis": 1,
    }
    #: duration of the intravenous infusion [min]
    infusion_duration: ClassVar[float] = 5.0
    color_group: ClassVar[str] = "tab:red"

    @property
    def f_cirrhosis_group(self) -> float:
        """Get the cirrhosis of the group, the mean of the Child-Pugh classes."""
        n = sum(self.child_pugh_counts.values())
        return (
            sum(self.cirrhosis_map[c] * k for c, k in self.child_pugh_counts.items())
            / n
        )

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig2", "Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dsets[self.to_sid(label)] = dset

                # urinary radioactivity in omeprazole equivalents
                if fig_id == "Fig3" and "_amount" in label:
                    dset.unit_conversion("mean", 1 / self.Mr.ome)

        return dsets

    def _simulation(self, route: str, dose: int, f_cirrhosis: float) -> Simulation:
        """Get the simulation of a dose for a cirrhosis.

        Args:
            route: "IV" (5 min infusion) or "PO" (buffered solution).
            dose: the dose of racemic omeprazole [mg].
            f_cirrhosis: the cirrhosis of the liver.

        Returns:
            The simulation of the dose.
        """
        changes: list[Change] = []
        if route == "IV":
            rate = dose / 2.0 / self.infusion_duration
            dosing = {
                "Ri_some": Q(rate, "mg/min"),
                "Ri_rome": Q(rate, "mg/min"),
            }
            changes = [
                Change(
                    self.infusion_duration,
                    {"Ri_some": Q(0, "mg/min"), "Ri_rome": Q(0, "mg/min")},
                )
            ]
        else:
            dosing = {
                **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                "PODOSE_some": Q(dose / 2.0, "mg"),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
            }
        return Simulation(
            time_unit="min",
            end=97 * 60,
            # a step of 1 min resolves the 5 min infusion
            preinit_changes={
                **self.default_changes(),
                "BW": Q(70, "kg"),  # median
                "f_cirrhosis": Q(f_cirrhosis, "dimensionless"),
                **dosing,
            },
            changes=changes,
        )

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}
        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]
            # the group of patients
            simulations[f"ome_{route}_{dose}"] = self._simulation(
                route, dose, self.f_cirrhosis_group
            )
            # the classes of cirrhosis
            for group, cir in self.cirrhosis_map.items():
                simulations[self.to_sid(f"ome_{route}_{dose}_{group}")] = (
                    self._simulation(route, dose, cir)
                )

        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]

            for k, yid in enumerate(self.yids):
                sid = self.sids[k]
                mappings[self.to_sid(f"fm_ome{route.lower()}{dose}_{sid}")] = (
                    FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=self.to_sid(f"OME{dose}_{route}_{sid}_cirrhosis"),
                            xid="time",
                            yid="mean",
                            yid_sd="mean_sd",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=f"task_ome_{route}_{dose}",
                            xid="time",
                            yid=yid,
                        ),
                        metadata=PKPDMappingMetaData(
                            tissue=Tissue.URINE if sid == "amount" else Tissue.PLASMA,
                            route=Route.IV if route == "IV" else Route.PO,
                            application_form=ApplicationForm.SOLUTION
                            if route == "IV"
                            else ApplicationForm.BUFFERED_SOLUTION,
                            dosing=Dosing.SINGLE,
                            health=Health.CIRRHOSIS,
                            fasting=Fasting.FASTED,
                        ),
                    )
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure1_2_3(),
        }

    def figure1_2_3(self) -> dict[str, Figure]:
        """Figure of omeprazole, its metabolites and the urinary excretion."""
        fig = Figure(
            experiment=self,
            sid="Fig1_2_3",
            num_rows=5,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-0.5, max=24),
            legend=True,
        )
        for k in [0, 1]:
            plots[k].set_yaxis(self.label_ome, unit=self.unit_ome)
        for k in [2, 3]:
            plots[k].set_yaxis(self.label_omeoh, unit=self.unit_omeoh)
        for k in [4, 5]:
            plots[k].set_yaxis(self.label_omesul, unit=self.unit_omesul)
        for k in [6, 7]:
            plots[k].set_yaxis(self.label_omemets, unit=self.unit_omemets)
        for k in [8, 9]:
            plots[k].set_yaxis(self.label_omemets_urine, unit=self.unit_omemets_urine)
            plots[k].set_xaxis(self.label_time, unit=self.unit_time, min=-2, max=98)

        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]

            kc = 0 if route == "PO" else 1

            for group in self.cirrhosis_map:
                # simulation of the classes
                for k, yid in enumerate(self.yids):
                    plots[2 * k + kc].add_data(
                        task=self.to_sid(f"task_ome_{route}_{dose}_{group}"),
                        xid="time",
                        yid=yid,
                        label=f"Sim {route.lower()}{dose} {group}",
                        color=self.cirrhosis_colors[group],
                        linestyle="dashed",
                    )
            # simulation of the group
            for k, yid in enumerate(self.yids):
                plots[2 * k + kc].add_data(
                    task=f"task_ome_{route}_{dose}",
                    xid="time",
                    yid=yid,
                    label=f"Sim {route.lower()}{dose} patients",
                    color=self.color_group,
                )

            # dataset
            for k, sid in enumerate(self.sids):
                dset_id = f"OME{dose}_{route}_{sid}_cirrhosis"
                plots[2 * k + kc].add_data(
                    dataset=self.to_sid(dset_id),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"{route.lower()}{dose} patients",
                    color=self.color_group,
                )

        # healthy volunteers of Andersson1990a and Regaardh1990 (reference, not mapped)
        plots[0].add_data(
            dataset="OME40_PO_ome_healthy",
            xid="time",
            yid="mean",
            count="count",
            label="po40 healthy",
            color=self.cirrhosis_colors["Control"],
        )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Andersson1993, output_dir=Andersson1993.__name__)
