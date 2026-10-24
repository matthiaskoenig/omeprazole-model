"""Simulation experiment of the study Sohn1992."""

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


class Sohn1992(OmeprazoleSimulationExperiment):
    """Simulation experiment of Sohn1992.

    16 healthy Korean men, phenotyped with S-mephenytoin (8 extensive, 60.4 kg,
    and 8 poor metabolizers of CYP2C19, 65.5 kg; not genotyped), took a single
    dose of 20 mg omeprazole as enteric-coated capsule (Losec) after an
    overnight fast, lunch 3 h after the dose. Plasma omeprazole,
    5-hydroxyomeprazole and the sulfone (Fig2, mean and SE; the
    5-hydroxyomeprazole of the poor metabolizers from 7 subjects) and the
    cumulative 5-hydroxyomeprazole in urine (Fig5, percent of the dose, in the
    data mg omeprazole equivalents). The data are the re-digitization of
    pkdb_data (2026-10, log axis, nominal times).
    """

    phenotypes: ClassVar[list[str]] = ["EM", "PM"]
    bodyweights: ClassVar[dict[str, float]] = {"EM": 60.4, "PM": 65.5}  # [kg]
    #: observables of the substances of the data
    substances: ClassVar[dict[str, tuple[str, str]]] = {
        # substance: (sid, observable)
        "omeprazole": ("ome", "[Cve_ome]"),
        "5-hydroxyomeprazole": ("omeoh", "[Cve_omeoh]"),
        "omeprazole sulfone": ("omesul", "[Cve_omesul]"),
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # plasma
        df = self.load_dataframe("Fig2")
        for _, df_label in df.groupby("label"):
            group = df_label.group.iloc[0]
            sid = self.substances[df_label.substance.iloc[0]][0]
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / getattr(self.Mr, sid))
            dsets[f"{group}_{sid}"] = dset

        # urine, 5-hydroxyomeprazole as mg omeprazole equivalents (the recovery
        # in percent of the molar dose times 20 mg)
        df = self.load_dataframe("Fig5")
        for group, df_group in df.groupby("group"):
            dset = DataSet.from_df(df_group, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.ome)
            dsets[f"{group}_omeoh_urine"] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose = 20

        for phenotype in self.phenotypes:
            tcsims[f"ome20_{phenotype}"] = Simulation(
                time_unit="min",
                # until the last data point (24 hr)
                end=25 * 60,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[phenotype], "kg"),
                    **self.form_changes(ApplicationForm.CAPSULE),
                    "LI__f_cyp2c19": Q(self.cyp2c19_map[phenotype], "dimensionless"),
                    "PODOSE_rome": Q(dose / 2.0, "mg"),
                    "PODOSE_some": Q(dose / 2.0, "mg"),
                },
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        observables = dict(self.substances.values())
        observables["omeoh_urine"] = "Aurine_omeoh"
        for phenotype in self.phenotypes:
            for sid, yid in observables.items():
                dset_id = f"{phenotype}_{sid}"
                mappings[f"fm_ome20po_{dset_id}"] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=dset_id,
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self, task=f"task_ome20_{phenotype}", xid="time", yid=yid
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.URINE
                        if sid.endswith("_urine")
                        else Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.CAPSULE,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        phenotype=Phenotype[f"CYP2C19_{phenotype}"],
                        data_type=DataType.MEAN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure2(),
            **self.figure5(),
        }

    def figure2(self) -> dict[str, Figure]:
        """Omeprazole and its metabolites in plasma by CYP2C19 phenotype."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=1,
            num_cols=3,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=25),
            legend=True,
        )
        for k, (sid, yid) in enumerate(self.substances.values()):
            plots[k].set_yaxis(
                self.labels[yid], unit=self.unit_metabolite, scale="log", min=0.003
            )
            for phenotype in self.phenotypes:
                plots[k].add_data(
                    task=f"task_ome20_{phenotype}",
                    xid="time",
                    yid=yid,
                    label=f"Sim {phenotype}",
                    color=self.cyp2c19_colors[phenotype],
                )
                plots[k].add_data(
                    dataset=f"{phenotype}_{sid}",
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=phenotype,
                    color=self.cyp2c19_colors[phenotype],
                )

        return self.figures_by_sid(fig)

    def figure5(self) -> dict[str, Figure]:
        """5-hydroxyomeprazole in urine by CYP2C19 phenotype."""
        fig = Figure(
            experiment=self,
            sid="Fig5",
            num_rows=1,
            num_cols=1,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=25),
            legend=True,
        )
        plots[0].set_yaxis(self.label_omeoh_urine, unit=self.unit_omeoh_urine)
        for phenotype in self.phenotypes:
            plots[0].add_data(
                task=f"task_ome20_{phenotype}",
                xid="time",
                yid="Aurine_omeoh",
                label=f"Sim {phenotype}",
                color=self.cyp2c19_colors[phenotype],
            )
            plots[0].add_data(
                dataset=f"{phenotype}_omeoh_urine",
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=phenotype,
                color=self.cyp2c19_colors[phenotype],
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Sohn1992, output_dir=Sohn1992.__name__)
