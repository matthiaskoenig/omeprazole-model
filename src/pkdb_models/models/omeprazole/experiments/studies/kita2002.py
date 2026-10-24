"""Simulation experiment of the study Kita2002."""

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


class Kita2002(OmeprazoleSimulationExperiment):
    """Simulation experiment of Kita2002.

    Single oral doses of 20, 40 and 80 mg omeprazole (enteric-coated tablets,
    more than 3 hr after breakfast, lunch 3 hr after the dose: fasted) in 7
    healthy Japanese men of known CYP2C19 genotype: 4 extensive metabolizers
    (*1/*1, 69.8 kg) and 3 poor metabolizers (*2/*2, *2/*3, 56.7 kg). Fig2 the
    mean concentrations in ng/ml at the nominal times 0, 1, 2, 3, 4, 6, 12 hr.
    """

    doses: ClassVar[list[int]] = [20, 40, 80]  # mg
    linestyles: ClassVar[dict[int, str]] = {20: ":", 40: "--", 80: "-"}
    variants: ClassVar[list[str]] = [
        "EM",
        "PM",
    ]

    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
    ]
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]
    #: body weight [kg] of the genotype groups
    bodyweights: ClassVar[dict[str, float]] = {"EM": 69.8, "PM": 56.7}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2"]:
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
                dset.unit_conversion("mean", 1 / mrs[substance])
                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        for variant in self.variants:
            for dose in self.doses:
                tcsims[self.to_sid(f"ome_{variant}_{dose}")] = Simulation(
                    time_unit="min",
                    end=14 * 60,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweights[variant], "kg"),
                        **self.form_changes(ApplicationForm.TABLET),
                        **self.fed_changes(Fasting.FASTED),
                        "PODOSE_rome": Q(dose / 2.0, "mg"),
                        "PODOSE_some": Q(dose / 2.0, "mg"),
                        "LI__f_cyp2c19": Q(self.cyp2c19_map[variant], "dimensionless"),
                    },
                )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for variant in self.variants:
            for dose in self.doses:
                for k, yid in enumerate(self.yids):
                    substance = self.substances[k]

                    mappings[self.to_sid(f"fm_ome_{variant}_{dose}_{substance}")] = (
                        FitMapping(
                            self,
                            reference=FitData(
                                self,
                                dataset=self.to_sid(f"{variant}_OME{dose}_{substance}"),
                                xid="time",
                                yid="mean",
                                yid_sd="mean_sd",
                                count="count",
                            ),
                            observable=FitData(
                                self,
                                task=self.to_sid(f"task_ome_{variant}_{dose}"),
                                xid="time",
                                yid=yid,
                            ),
                            metadata=PKPDMappingMetaData(
                                tissue=Tissue.PLASMA,
                                route=Route.PO,
                                application_form=ApplicationForm.TABLET,
                                dosing=Dosing.SINGLE,
                                health=Health.HEALTHY,
                                fasting=Fasting.FASTED,
                                phenotype=Phenotype[f"CYP2C19_{variant}"],
                            ),
                        )
                    )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        name = "Fig2"
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
        # one legend right of the first plot, the plots share their curves
        fig.settings = {**fig.settings, "legend_position": "outside"}
        for plot in plots[1:]:
            plot.legend = False

        # simulation
        for variant in self.variants:
            for dose in self.doses:
                linestyle = self.linestyles[dose]
                for k, yid in enumerate(self.yids):
                    plots[k].add_data(
                        task=self.to_sid(f"task_ome_{variant}_{dose}"),
                        xid="time",
                        yid=yid,
                        label=f"Sim {variant} {dose} mg",
                        color=self.cyp2c19_colors[variant],
                        linestyle=linestyle,
                    )

                    # datasets
                    plots[k].add_data(
                        dataset=self.to_sid(
                            f"{variant}_OME{dose}_{self.substances[k]}"
                        ),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"{variant} {dose} mg",
                        color=self.cyp2c19_colors[variant],
                        linestyle=linestyle,
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Kita2002, output_dir=Kita2002.__name__)
