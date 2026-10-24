"""Simulation experiment of the study Naesdal1986."""

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


class Naesdal1986(OmeprazoleSimulationExperiment):
    """Simulation experiment of Naesdal1986.

    [14C]omeprazole in 12 patients with chronic renal insufficiency (73.7 kg,
    creatinine clearance 10 to 62 ml/min/1.73 m2): an intravenous infusion of
    20 mg over 5 min (10 ml at 2 ml/min) and an oral dose of 40 mg as a
    buffered solution, fasted, 9 days apart. Fig2 omeprazole and Fig4
    5-hydroxyomeprazole and the sulfone (all patients), Fig3 the radioactive
    metabolites in plasma of the patients with a creatinine clearance above
    (MRI, 6) and below (SRI, 6) 25 ml/min, Fig6 the urinary excretion rate of
    the radioactivity (metabolites, all patients) at the midpoints of the
    collection intervals. The intravenous curves of Fig2 and Fig4 are plotted
    from the end of the infusion; the data are shifted by 5 min to the start
    of the infusion.
    """

    doses: ClassVar[list[int]] = [20, 40]  # mg
    routes: ClassVar[list[str]] = ["IV", "PO"]
    colors: ClassVar[list[str]] = ["tab:blue", "tab:green"]

    groups: ClassVar[list[str]] = ["RI", "MRI", "SRI"]
    #: renal function of the groups, the mean creatinine clearance (Table I)
    #: relative to the GFR of the model (101 ml/min): all patients 28.1, the
    #: patients above 25 ml/min (MRI) 40.7, below 25 ml/min (SRI) 15.5 ml/min
    f_renal_functions: ClassVar[list[float]] = [
        28.1 / 101,
        40.7 / 101,
        15.5 / 101,
    ]
    bodyweight: ClassVar[float] = 73.7  # [kg]
    infusion: ClassVar[float] = 5.0  # [min]

    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
    ]
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2", "Fig3", "Fig4", "Fig6"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        # simulation time courses
        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]
            if route == "IV":
                # infusion over 5 min
                ri = Q(dose / 2.0, "mg") / Q(self.infusion, "min")
                dosing = {"Ri_rome": ri, "Ri_some": ri}
                changes = [
                    Change(
                        self.infusion,
                        {"Ri_rome": Q(0, "mg/min"), "Ri_some": Q(0, "mg/min")},
                    )
                ]
            else:
                dosing = {
                    **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                    "PODOSE_rome": Q(dose / 2.0, "mg"),
                    "PODOSE_some": Q(dose / 2.0, "mg"),
                }
                changes = []

            # single application
            for kg, group in enumerate(self.groups):
                tcsims[self.to_sid(f"OME{dose}_{route}_{group}")] = Simulation(
                    time_unit="min",
                    # until the last data point (84.0 hr)
                    end=85 * 60,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweight, "kg"),
                        **self.fed_changes(Fasting.FASTED),
                        "KI__f_renal_function": Q(
                            self.f_renal_functions[kg], "dimensionless"
                        ),
                        **dosing,
                    },
                    changes=changes,
                )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        # Figure 2 & 4
        for kd, dose in enumerate(self.doses):
            route = self.routes[kd]
            for kp, substance in enumerate(self.substances):
                yid = self.yids[kp]

                mappings[self.to_sid(f"fm_OME{dose}_{route}_{substance}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"OME{dose}_{route}_{substance}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_OME{dose}_{route}_RI"),
                        xid="time",
                        yid=yid,
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.IV if route == "IV" else Route.PO,
                        application_form=ApplicationForm.SOLUTION
                        if route == "IV"
                        else ApplicationForm.BUFFERED_SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.FASTED,
                    ),
                )

        # Figure 3
        for kd, dose in enumerate(self.doses):
            route = self.routes[kd]
            for group in ["SRI", "MRI"]:
                mappings[
                    self.to_sid(f"fm_OME{dose}_{route}_{group}_omeprazole metabolites")
                ] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(
                            f"OME{dose}_{route}_{group}_omeprazole metabolites"
                        ),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_OME{dose}_{route}_{group}"),
                        xid="time",
                        yid="[Cve_omemets]",
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.IV if route == "IV" else Route.PO,
                        application_form=ApplicationForm.SOLUTION
                        if route == "IV"
                        else ApplicationForm.BUFFERED_SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.RENAL_IMPAIRMENT,
                        fasting=Fasting.FASTED,
                    ),
                )
        # Figure 6
        mappings["fm_OME20_IV_RI_excretion_rate_omemets"] = FitMapping(
            self,
            reference=FitData(
                self,
                dataset="OME20_IV_excretion_rate_omemets",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
            ),
            observable=FitData(
                self, task="task_OME20_IV_RI", xid="time", yid="KI__OMEMETSEX"
            ),
            metadata=PKPDMappingMetaData(
                tissue=Tissue.URINE,
                route=Route.IV,
                application_form=ApplicationForm.SOLUTION,
                dosing=Dosing.SINGLE,
                health=Health.RENAL_IMPAIRMENT,
                fasting=Fasting.FASTED,
            ),
        )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_2_4(),
            **self.figure_3(),
            **self.figure_6(),
        }

    def figure_2_4(self) -> dict[str, Figure]:
        """Figure of the plasma concentrations (Fig2 and Fig4)."""
        fig = Figure(
            experiment=self,
            sid="Fig2_4",
            num_rows=3,
            num_cols=1,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-0.1, max=5),
            legend=True,
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[1].set_yaxis(self.label_omeoh, unit=self.unit_omeoh)
        plots[2].set_yaxis(self.label_omesul, unit=self.unit_omesul)

        for kd, dose in enumerate(self.doses):
            route = self.routes[kd]

            for kp, substance in enumerate(self.substances):
                yid = self.yids[kp]

                # simulation
                plots[kp].add_data(
                    task=self.to_sid(f"task_OME{dose}_{route}_RI"),
                    xid="time",
                    yid=yid,
                    label=f"Sim {route}{dose}",
                    color=self.colors[kd],
                )

                # datasets
                plots[kp].add_data(
                    dataset=self.to_sid(f"OME{dose}_{route}_{substance}"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"Naesdal1986 {route}{dose}",
                    color=self.colors[kd],
                )

        return self.figures_by_sid(fig)

    def figure_3(self) -> dict[str, Figure]:
        """Figure of the plasma concentrations of the metabolites (Fig3)."""
        fig = Figure(
            experiment=self,
            sid="Fig3",
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )

        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-0.1, max=25),
            legend=True,
        )
        plots[0].set_yaxis(self.label_omemets, unit=self.unit_omemets)

        for kd, dose in enumerate(self.doses):
            route = self.routes[kd]
            for group in ["SRI", "MRI"]:
                # simulation
                plots[0].add_data(
                    task=self.to_sid(f"task_OME{dose}_{route}_{group}"),
                    xid="time",
                    yid="[Cve_omemets]",
                    label=f"Sim {route}{dose} {group}",
                    color=self.colors[kd],
                    linestyle="-" if group == "SRI" else ":",
                )

                # datasets
                plots[0].add_data(
                    dataset=self.to_sid(
                        f"OME{dose}_{route}_{group}_omeprazole metabolites"
                    ),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"Naesdal1986 {route}{dose} {group}",
                    color=self.colors[kd],
                    linestyle="-" if group == "SRI" else ":",
                )

        return self.figures_by_sid(fig)

    def figure_6(self) -> dict[str, Figure]:
        """Figure of the urinary excretion rate of the metabolites (Fig6)."""
        fig = Figure(
            experiment=self,
            sid="Fig6",
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )

        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=-0.1, max=90),
            legend=True,
        )
        plots[0].set_yaxis("urinary excretion\nomeprazole metabolites", unit="µmol/hr")

        for kd, dose in enumerate(self.doses):
            route = self.routes[kd]
            # simulation
            plots[0].add_data(
                task=self.to_sid(f"task_OME{dose}_{route}_RI"),
                xid="time",
                yid="KI__OMEMETSEX",
                label=f"Sim {route}{dose}",
                color=self.colors[kd],
            )
            if route == "IV":
                # datasets
                plots[0].add_data(
                    dataset=self.to_sid(f"OME{dose}_{route}_excretion_rate_omemets"),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"Naesdal1986 {route}{dose}",
                    color=self.colors[kd],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Naesdal1986, output_dir=Naesdal1986.__name__)
