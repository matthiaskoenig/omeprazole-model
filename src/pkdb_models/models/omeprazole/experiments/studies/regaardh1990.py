"""Simulation experiment of the study Regaardh1990."""

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
from sbmlsim.simulation import Change, Simulation
from sbmlsim.units import Quantity

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class Regaardh1990(OmeprazoleSimulationExperiment):
    """Simulation experiment of Regaardh1990.

    Eight healthy men (74.1 kg) received 10 mg [14C]omeprazole IV, infused at
    2 mg/min over 5 min, and 20 mg orally as a buffered solution (NaHCO3), in a
    crossover after an overnight fast. The figures plot the times from the
    start of the infusion (the samples 0, 3, 6, 10 ... min after its end are
    drawn at 5, 8, 11, 15 ... min), so the infusion is simulated from 0 to
    5 min; the oral samples are drawn at the same times after the dose.

    Fig2 shows the median and the subjects with the lowest (subject 7, CL
    828 ml/min) and the highest AUC (subject 2, CL 59 ml/min) of omeprazole.
    Subject 2 has very low concentrations of 5-hydroxyomeprazole and high ones
    of the sulfone (Fig3, Fig4): a CYP2C19 poor metabolizer by phenotype (not
    genotyped), simulated with the activity of a poor metabolizer. Subject 1
    (CL 149 ml/min, Fig4) is not mapped, its phenotype is unclear. Fig6 is the
    radioactivity in urine (all metabolites, 78 % of the IV dose) and feces
    (19 %) as mg omeprazole equivalents.
    """

    applications: ClassVar[list[str]] = ["iv", "po"]
    doses: ClassVar[dict[str, int]] = {"iv": 10, "po": 20}  # [mg]
    #: duration of the simulations [hr]: the plasma data (2 h), the urine and
    #: feces (96 h) and the poor metabolizer (Fig4, 24 h)
    durations: ClassVar[dict[str, float]] = {"": 3, "_long": 100, "_PM": 25}
    bodyweight: ClassVar[float] = 74.1  # [kg]
    infusion_duration: ClassVar[float] = 5.0  # [min]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # omeprazole, median and individuals
        for fig_id in ["Fig2", "Fig2B"]:
            dframes = self.load_dataframes_by_substance(fig_id)
            for df in dframes.values():
                dset = DataSet.from_df(df, self.ureg)
                for label in df.label.unique():
                    dsets[f"{label}"] = dset[dset.label == label]

        # metabolites after the oral dose: median (Fig3B), individuals (Fig3)
        # and 24 h of omeprazole and the sulfone of subjects 1 and 2 (Fig4)
        for fig_id in ["Fig3B", "Fig3", "Fig4"]:
            df = self.load_dataframe(fig_id)
            if "count" not in df.columns:
                # the curves of single subjects
                df["count"] = 1
            for label, df_label in df.groupby("label"):
                dsets[str(label)] = DataSet.from_df(df_label, self.ureg)

        # Fig6 cumulative amounts of the radioactivity (mg omeprazole equivalents)
        df = self.load_dataframe("Fig6")
        for application in self.applications:
            intervention = f"OME_{application}{self.doses[application]}"
            for tissue in ["urine", "feces"]:
                df_tissue = df[
                    (df.tissue == tissue)
                    & (df.measurement_type == "cumulative amount")
                    & (df.interventions == intervention)
                ].copy()
                dset = DataSet.from_df(df_tissue, self.ureg)
                dset.unit_conversion("mean", 1 / self.Mr.ome)
                dsets[f"Fig6_amount_{tissue}_{application}"] = dset

        return dsets

    def dosing(self, application: str) -> tuple[dict[str, Quantity], list[Change]]:
        """Get the changes of the dose of an application.

        Args:
            application: `iv` (infusion over 5 min) or `po` (buffered solution).

        Returns:
            The changes at the start and the changes during the simulation.
        """
        dose = self.doses[application]
        if application == "iv":
            rate = Q(dose / 2.0 / self.infusion_duration, "mg/min")
            return (
                {"Ri_some": rate, "Ri_rome": rate},
                [
                    Change(
                        self.infusion_duration,
                        {"Ri_some": Q(0, "mg/min"), "Ri_rome": Q(0, "mg/min")},
                    )
                ],
            )
        return (
            {
                **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                "PODOSE_some": Q(dose / 2.0, "mg"),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
            },
            [],
        )

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for application in self.applications:
            dose = self.doses[application]
            changes_start, changes = self.dosing(application)
            for duration_label, duration_hr in self.durations.items():
                phenotype = "PM" if duration_label == "_PM" else "EM"
                tcsims[f"{application}{dose}{duration_label}"] = Simulation(
                    time_unit="min",
                    end=duration_hr * 60,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweight, "kg"),
                        "LI__f_cyp2c19": Q(
                            self.cyp2c19_map[phenotype], "dimensionless"
                        ),
                        **changes_start,
                    },
                    changes=changes,
                )

        return tcsims

    @staticmethod
    def metadata(
        application: str,
        tissue: Tissue = Tissue.PLASMA,
        data_type: DataType = DataType.MEDIAN,
        phenotype: Phenotype = Phenotype.NR,
    ) -> PKPDMappingMetaData:
        """Get the metadata of a mapping of an application."""
        return PKPDMappingMetaData(
            tissue=tissue,
            route=Route.PO if application == "po" else Route.IV,
            application_form=ApplicationForm.BUFFERED_SOLUTION
            if application == "po"
            else ApplicationForm.SOLUTION,
            dosing=Dosing.SINGLE,
            health=Health.HEALTHY,
            fasting=Fasting.FASTED,
            phenotype=phenotype,
            data_type=data_type,
        )

    def mapping(
        self,
        dataset: str,
        task: str,
        yid: str,
        metadata: PKPDMappingMetaData,
        y_column: str,
    ) -> FitMapping:
        """Get the mapping of a dataset on an observable of a task.

        Args:
            dataset: the key of the dataset.
            task: the key of the task.
            yid: the observable.
            metadata: the metadata of the mapping.
            y_column: `mean` (with SD), `median` or `value` (an individual).

        Returns:
            The fit mapping.
        """
        return FitMapping(
            self,
            reference=FitData(
                self,
                dataset=dataset,
                xid="time",
                yid=y_column,
                yid_sd="mean_sd" if y_column == "mean" else None,
                count="count",
            ),
            observable=FitData(self, task=task, xid="time", yid=yid),
            metadata=metadata,
        )

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for application in self.applications:
            app = f"{application}{self.doses[application]}"

            # median of the 8 subjects
            mappings[f"fm_ome_{app}"] = self.mapping(
                dataset=f"Fig2_{application}",
                task=f"task_{app}",
                yid="[Cve_ome]",
                metadata=self.metadata(application),
                y_column="median",
            )
            # subject 7, the lowest AUC of the 8 subjects (the fastest
            # metabolizer, CL 828 ml/min): an extreme of the population
            mappings[f"fm_ome_{app}_adult7"] = self.mapping(
                dataset=f"Fig2_{application}_adult7",
                task=f"task_{app}",
                yid="[Cve_ome]",
                metadata=self.metadata(application, data_type=DataType.INDIVIDUAL),
                y_column="value",
            )

            # radioactivity in urine and feces: all metabolites
            for tissue, yid in [
                ("urine", "Aurine_omemets"),
                ("feces", "Afeces_omemets"),
            ]:
                mappings[f"fm_omemets_{tissue}_{app}"] = self.mapping(
                    dataset=f"Fig6_amount_{tissue}_{application}",
                    task=f"task_{app}_long",
                    yid=yid,
                    metadata=self.metadata(
                        application,
                        tissue=Tissue.URINE if tissue == "urine" else Tissue.FECES,
                        data_type=DataType.MEAN,
                    ),
                    y_column="mean",
                )

        # metabolites after the oral dose, median
        for sid, label, yid in [
            ("omesul", "Fig3_omesul_po_20", "[Cve_omesul]"),
            ("omeoh", "Fig3_5home_po_20", "[Cve_omeoh]"),
        ]:
            mappings[f"fm_{sid}_po20"] = self.mapping(
                dataset=label,
                task="task_po20",
                yid=yid,
                metadata=self.metadata("po"),
                y_column="median",
            )

        # subject 2, a CYP2C19 poor metabolizer by phenotype: omeprazole after
        # the IV dose (Fig2), omeprazole and the sulfone over 24 h (Fig4, the
        # same curve as the oral one of Fig2) and 5-hydroxyomeprazole (Fig3)
        for key, dataset, task, yid in [
            ("fm_ome_iv10_adult2", "Fig2_iv_adult2", "task_iv10_PM", "[Cve_ome]"),
            ("fm_ome_po20_adult2", "Fig4_ome_po_20_sub_2", "task_po20_PM", "[Cve_ome]"),
            (
                "fm_omesul_po20_adult2",
                "Fig4_omesul_po_20_sub_2",
                "task_po20_PM",
                "[Cve_omesul]",
            ),
            (
                "fm_omeoh_po20_adult2",
                "Fig3_5home_po_20_sub_2",
                "task_po20_PM",
                "[Cve_omeoh]",
            ),
        ]:
            mappings[key] = self.mapping(
                dataset=dataset,
                task=task,
                yid=yid,
                metadata=self.metadata(
                    "iv" if "_iv" in key else "po",
                    data_type=DataType.INDIVIDUAL,
                    phenotype=Phenotype.CYP2C19_PM,
                ),
                y_column="value",
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure2(),
            **self.figure3(),
            **self.figure4(),
            **self.figure6(),
        }

    def figure2(self) -> dict[str, Figure]:
        """Omeprazole after the IV and the oral dose (Fig2)."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit="min", min=0, max=125), legend=True
        )
        for k, application in enumerate(self.applications):
            dose = self.doses[application]
            app = f"{application}{dose}"
            plots[k].set_title(f"{dose} mg {application.upper()}")
            plots[k].set_yaxis(
                self.label_ome, unit=self.unit_ome, scale="log", min=0.01, max=10
            )
            for task, label, color in [
                (f"task_{app}", "Sim", "black"),
                (f"task_{app}_PM", "Sim PM", "tab:red"),
            ]:
                plots[k].add_data(
                    task=task, xid="time", yid="[Cve_ome]", label=label, color=color
                )
            plots[k].add_data(
                dataset=f"Fig2_{application}",
                xid="time",
                yid="median",
                count="count",
                label="median",
                color="black",
            )
            for subject, color in [("adult7", "tab:blue"), ("adult2", "tab:red")]:
                plots[k].add_data(
                    dataset=f"Fig2_{application}_{subject}",
                    xid="time",
                    yid="value",
                    label=f"subject {subject[-1]}",
                    color=color,
                )

        return self.figures_by_sid(fig)

    def figure3(self) -> dict[str, Figure]:
        """Sulfone and 5-hydroxyomeprazole after the oral dose (Fig3)."""
        fig = Figure(
            experiment=self,
            sid="Fig3",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit="min", min=0, max=125), legend=True
        )
        # the lowest sulfone (subject 8) and the highest 5-hydroxyomeprazole
        # (subject 5) of the 8 subjects, not mapped
        panels = [
            ("[Cve_omesul]", self.label_omesul, "omesul", "8"),
            ("[Cve_omeoh]", self.label_omeoh, "5home", "5"),
        ]
        for k, (yid, label, sid, subject) in enumerate(panels):
            plots[k].set_yaxis(label, unit=self.unit_metabolite)
            for task, sim_label, color in [
                ("task_po20", "Sim", "black"),
                ("task_po20_PM", "Sim PM", "tab:red"),
            ]:
                plots[k].add_data(
                    task=task, xid="time", yid=yid, label=sim_label, color=color
                )
            plots[k].add_data(
                dataset=f"Fig3_{sid}_po_20",
                xid="time",
                yid="median",
                count="count",
                label="median",
                color="black",
            )
            for sub, color in [(subject, "tab:blue"), ("2", "tab:red")]:
                plots[k].add_data(
                    dataset=f"Fig3_{sid}_po_20_sub_{sub}",
                    xid="time",
                    yid="value",
                    label=f"subject {sub}",
                    color=color,
                )

        return self.figures_by_sid(fig)

    def figure4(self) -> dict[str, Figure]:
        """Omeprazole and the sulfone of subjects 1 and 2 over 24 h (Fig4)."""
        fig = Figure(
            experiment=self,
            sid="Fig4",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=25),
            legend=True,
        )
        for k, subject in enumerate(["1", "2"]):
            plots[k].set_title(f"subject {subject}")
            plots[k].set_yaxis(
                "concentration", unit=self.unit_ome, scale="log", min=0.01, max=10
            )
            for sid, yid, color in [
                ("ome", "[Cve_ome]", "black"),
                ("omesul", "[Cve_omesul]", "tab:orange"),
            ]:
                for task, sim_label, linestyle in [
                    ("task_po20_long", "EM", "--"),
                    ("task_po20_PM", "PM", "-"),
                ]:
                    plots[k].add_data(
                        task=task,
                        xid="time",
                        yid=yid,
                        label=f"Sim {sim_label} {self.labels[yid]}",
                        color=color,
                        linestyle=linestyle,
                    )
                plots[k].add_data(
                    dataset=f"Fig4_{sid}_po_20_sub_{subject}",
                    xid="time",
                    yid="value",
                    label=self.labels[yid],
                    color=color,
                )

        return self.figures_by_sid(fig)

    def figure6(self) -> dict[str, Figure]:
        """Radioactivity in urine and feces (Fig6)."""
        fig = Figure(
            experiment=self,
            sid="Fig6",
            num_rows=1,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=100),
            legend=True,
        )
        plots[0].set_yaxis(self.label_omemets_urine, unit=self.unit_omemets_urine)
        plots[1].set_yaxis(self.label_omemets_feces, unit=self.unit_omemets_feces)
        for application, color in [("iv", "black"), ("po", "tab:blue")]:
            dose = self.doses[application]
            for k, (tissue, yid) in enumerate(
                [("urine", "Aurine_omemets"), ("feces", "Afeces_omemets")]
            ):
                plots[k].add_data(
                    task=f"task_{application}{dose}_long",
                    xid="time",
                    yid=yid,
                    label=f"Sim {dose} mg {application.upper()}",
                    color=color,
                )
                plots[k].add_data(
                    dataset=f"Fig6_amount_{tissue}_{application}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"{dose} mg {application.upper()}",
                    color=color,
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Regaardh1990, output_dir=Regaardh1990.__name__)
