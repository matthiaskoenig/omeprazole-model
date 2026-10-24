"""Simulation experiment of the study HassanAlin2005."""

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


class HassanAlin2005(OmeprazoleSimulationExperiment):
    """Simulation experiment of Hassan-Alin2005.

    Oral S-omeprazole, R-omeprazole and racemic omeprazole once daily for 5
    days in a three way crossover, two dose groups of healthy Caucasian
    CYP2C19 extensive metabolizers: 20 mg (12 subjects, 77 kg, one dropout
    before R-omeprazole) and 40 mg (12 subjects, 69 kg). The doses are
    solutions of the sodium salts with bicarbonate buffer (a buffered
    solution), fasted. Fig1 the first dose (`*_SINGLE`), Fig2 the fifth dose
    (`*_MULTI`).
    """

    dset_ids: ClassVar[list[str]] = [
        "OME20_SINGLE",
        "SOME20_SINGLE",
        "ROME20_SINGLE",
        "OME20_MULTI",
        "SOME20_MULTI",
        "ROME20_MULTI",
        "OME40_SINGLE",
        "SOME40_SINGLE",
        "ROME40_SINGLE",
        "OME40_MULTI",
        "SOME40_MULTI",
        "ROME40_MULTI",
    ]
    doses: ClassVar[list[int]] = [20, 40]
    #: body weight [kg] of the dose groups
    bodyweights: ClassVar[dict[int, float]] = {20: 77.0, 40: 69.0}
    dose_substances: ClassVar[list[str]] = ["OME", "SOME", "ROME"]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        simulations = {}

        # single dose
        for substance in self.dose_substances:
            for dose in self.doses:
                if substance == "OME":
                    changes = {
                        "PODOSE_some": Q(dose / 2, "mg"),
                        "PODOSE_rome": Q(dose / 2, "mg"),
                    }
                elif substance == "SOME":
                    changes = {
                        "PODOSE_some": Q(dose, "mg"),
                    }
                elif substance == "ROME":
                    changes = {
                        "PODOSE_rome": Q(dose, "mg"),
                    }
                changes0 = {
                    **self.default_changes(),
                    "BW": Q(self.bodyweights[dose], "kg"),
                    **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                    **self.fed_changes(Fasting.FASTED),
                    **changes,
                }

                # single application
                simulations[f"ome_{substance}{dose}_SINGLE"] = Simulation(
                    time_unit="min",
                    end=24 * 60,  # measured for 12 hours
                    preinit_changes=changes0,
                )
                # multiple application, a dose every day for 5 days
                simulations[f"ome_{substance}{dose}_MULTI"] = Simulation(
                    time_unit="min",
                    end=5 * 24 * 60,
                    preinit_changes=changes0,
                    changes=[
                        self.add_doses([k * 24 * 60 for k in range(1, 5)], changes)
                    ],
                    time_shift=-4 * 24 * 60,
                )

        return simulations

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for dset_id in self.dset_ids:
            token = dset_id.split("_")[0]
            substance = token[0:-2]

            mappings[f"fm_{dset_id}"] = FitMapping(
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
                    self,
                    task=f"task_ome_{dset_id}",
                    xid="time",
                    yid=f"[Cve_{substance.lower()}]",
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=ApplicationForm.BUFFERED_SOLUTION,
                    dosing=Dosing.SINGLE
                    if dset_id.endswith("_SINGLE")
                    else Dosing.MULTIPLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                    phenotype=Phenotype.CYP2C19_EM,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure1_2(),
        }

    def figure1_2(self) -> dict[str, Figure]:
        """Figure of omeprazole and its enantiomers, single and multiple doses."""
        fig = Figure(
            experiment=self,
            sid="Fig1_2",
            num_rows=3,
            num_cols=2,
            name=self.sid,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[1].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[2].set_yaxis(self.label_some, unit=self.unit_ome)
        plots[3].set_yaxis(self.label_some, unit=self.unit_ome)
        plots[4].set_yaxis(self.label_rome, unit=self.unit_ome)
        plots[5].set_yaxis(self.label_rome, unit=self.unit_ome)
        for k in [1, 3, 5]:
            plots[k].set_xaxis(self.label_time, unit=self.unit_time, min=-24)

        for dset_id in self.dset_ids:
            # parse information
            tokens = dset_id.split("_")
            token = tokens[0]
            dosing = tokens[1]
            dose = int(token[-2:])
            substance = token[0:-2]

            color = self.dose_colors[dose]

            if substance == "OME":
                row = 0
            elif substance == "SOME":
                row = 1
            elif substance == "ROME":
                row = 2

            col = 0 if dosing == "SINGLE" else 1
            kp = 2 * row + col

            # simulation
            plots[kp].add_data(
                task=f"task_ome_{dset_id}",
                xid="time",
                yid=f"[Cve_{substance.lower()}]",
                label=f"Sim po{dose}",
                color=color,
            )

            # datasets
            plots[kp].add_data(
                dataset=dset_id,
                xid="time",
                yid="mean",
                yid_sd=None,
                count="count",
                label=f"po{dose}",
                color=color,
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(HassanAlin2005, output_dir=HassanAlin2005.__name__)
