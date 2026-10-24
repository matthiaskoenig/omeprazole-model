"""Simulation experiment of the study Kita2001."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
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


class Kita2001(OmeprazoleSimulationExperiment):
    """Simulation experiment of Kita2001.

    Omeprazole 20 mg enteric-coated tablets twice daily (09:00 and 21:00), 30
    min after breakfast (fed), in 6 healthy Japanese men (54.5 kg) of known
    CYP2C19 genotype: subject 1 *1/*1 (EM), subjects 2 and 3 *1/*2 (IM, the
    paper counts them as extensive metabolizers), subjects 4 and 5 *2/*2,
    subject 6 *3/*3 (PM). Fig1 the individual concentrations in ng/ml from 0
    to 12 hr after the morning dose (the second dose at 12 hr).
    """

    subjects: ClassVar[list[str]] = [
        "S1_EM",
        "S2_IM",
        "S3_IM",
        "S4_PM",
        "S5_PM",
        "S6_PM",
    ]
    #: legend names of the subjects
    legends: ClassVar[dict[str, str]] = {
        "S1_EM": "subject 1 (*1/*1, EM)",
        "S2_IM": "subject 2 (*1/*2, IM)",
        "S3_IM": "subject 3 (*1/*2, IM)",
        "S4_PM": "subject 4 (*2/*2, PM)",
        "S5_PM": "subject 5 (*2/*2, PM)",
        "S6_PM": "subject 6 (*3/*3, PM)",
    }
    variants: ClassVar[list[str]] = ["EM", "IM", "PM"]

    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
    ]
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]
    bodyweight: ClassVar[float] = 54.5  # [kg]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1"]:
            df = self.load_dataframe(fig_id)
            mrs = {
                "omeprazole": self.Mr.ome,
                "5-hydroxyomeprazole": self.Mr.omeoh,
                "omeprazole sulfone": self.Mr.omesul,
            }
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                substance = str(df_label["substance"].iloc[0])
                dset.unit_conversion("value", 1 / mrs[substance])
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        dose = 20
        doses = {
            "PODOSE_rome": Q(dose / 2.0, "mg"),
            "PODOSE_some": Q(dose / 2.0, "mg"),
        }

        for variant in self.variants:
            f_cyp2c19 = self.cyp2c19_map[variant]
            tcsims[self.to_sid(f"ome20_{variant}")] = Simulation(
                time_unit="min",
                end=14 * 60,
                preinit_changes={
                    **self.default_changes(),
                    "BW": Q(self.bodyweight, "kg"),
                    **self.form_changes(ApplicationForm.TABLET),
                    **self.fed_changes(Fasting.FED),
                    **doses,
                    "LI__f_cyp2c19": Q(f_cyp2c19, "dimensionless"),
                },
                # the evening dose, after the last sample
                changes=[self.add_doses(12 * 60, doses)],
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for ks, substance in enumerate(self.substances):
            for subject in self.subjects:
                variant = subject.split("_")[-1]
                dset_id = f"{subject}_{substance}"
                mappings[self.to_sid(f"fm_ome20po_{dset_id}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(dset_id),
                        xid="time",
                        yid="value",
                        yid_sd=None,
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_ome20_{variant}"),
                        xid="time",
                        yid=self.yids[ks],
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=ApplicationForm.TABLET,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FED,
                        phenotype=Phenotype[f"CYP2C19_{variant}"],
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        name = "Fig1"

        fig = Figure(
            experiment=self,
            sid=self.to_sid(name),
            num_rows=3,
            num_cols=1,
            name=self.__class__.__name__,
        )

        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[1].set_yaxis(self.label_omeoh, unit=self.unit_omeoh)
        plots[2].set_yaxis(self.label_omesul, unit=self.unit_omesul)

        # simulation
        for variant in self.variants:
            for k, yid in enumerate(self.yids):
                plots[k].add_data(
                    task=self.to_sid(f"task_ome20_{variant}"),
                    xid="time",
                    yid=yid,
                    label=f"Sim {variant}",
                    color=self.cyp2c19_colors[variant],
                )

        # datasets
        for subject in self.subjects:
            variant = subject.split("_")[-1]
            for ksu, substance in enumerate(self.substances):
                plots[ksu].add_data(
                    dataset=self.to_sid(f"{subject}_{substance}"),
                    xid="time",
                    yid="value",
                    count="count",
                    label=self.legends[subject],
                    color=self.cyp2c19_colors[variant],
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Kita2001, output_dir=Kita2001.__name__)
