"""Simulation experiment of the study Palovaara2003."""

from typing import ClassVar, override

from pkpdsim.metadata import (
    ApplicationForm,
    Coadministration,
    DataType,
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


class Palovaara2003(OmeprazoleSimulationExperiment):
    """Simulation experiment of Palovaara2003.

    10 healthy women (19-26 years, BMI 18-26, body weight not reported,
    non-smokers, no oral contraceptives for at least 2 months), CYP2C19
    7 *1/*1 and 3 *1/*2 (no poor metabolizer), simulated with the mean
    activity of the group. Open three phase crossover with a single oral dose of
    40 mg omeprazole (Losec MUPS, enteric-coated multiple unit tablet) after an
    overnight fast, a standardized lunch at 3 h:

    - `OME40`: omeprazole alone (control),
    - `EE_LNG_OME40`: omeprazole on day 10 of ethinylestradiol 40 µg +
      levonorgestrel 75 µg once daily (Trikvilar), 1 h after the last dose;
      ethinylestradiol inhibits CYP2C19 (`F_CYP2C19_ETHINYLESTRADIOL`, the
      observed omeprazole AUC x1.38),
    - `LNG_OME40`: omeprazole on day 10 of levonorgestrel 60 µg once daily
      (Microluton), no change of the omeprazole kinetics.

    Plasma omeprazole, 5-hydroxyomeprazole and omeprazole sulfone (Fig2, mean
    without error bars, times are the nominal sampling times).
    """

    dose: ClassVar[float] = 40  # [mg]
    form: ClassVar[ApplicationForm] = ApplicationForm.TABLET
    #: activity of CYP2C19 of the group: 7 extensive and 3 intermediate
    #: metabolizers
    f_cyp2c19: ClassVar[float] = (
        7 * OmeprazoleSimulationExperiment.cyp2c19_map["EM"]
        + 3 * OmeprazoleSimulationExperiment.cyp2c19_map["IM"]
    ) / 10
    #: CYP2C19 activity factor of the treatments
    treatments: ClassVar[dict[str, float]] = {
        "OME40": 1.0,
        "EE_LNG_OME40": OmeprazoleSimulationExperiment.F_CYP2C19_ETHINYLESTRADIOL,
        "LNG_OME40": 1.0,
    }
    treatment_labels: ClassVar[dict[str, str]] = {
        "OME40": "control",
        "EE_LNG_OME40": "EE + LNG",
        "LNG_OME40": "LNG",
    }
    colors: ClassVar[dict[str, str]] = {
        "OME40": "black",
        "EE_LNG_OME40": "tab:red",
        "LNG_OME40": "tab:green",
    }
    yids: ClassVar[list[str]] = ["[Cve_ome]", "[Cve_omeoh]", "[Cve_omesul]"]
    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
    ]
    sids: ClassVar[list[str]] = ["ome", "omeoh", "omesul"]

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig2"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                # the concentrations are in nM
                dsets[self.to_sid(label)] = DataSet.from_df(df_label, self.ureg)

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for treatment, f_interaction in self.treatments.items():
            tcsims[self.to_sid(f"po{self.dose}_{treatment}")] = Simulation(
                time_unit="min",
                end=10 * 60,  # measured for 8 hours
                preinit_changes={
                    **self.default_changes(),
                    **self.form_changes(self.form),
                    "LI__f_cyp2c19": Q(self.f_cyp2c19 * f_interaction, "dimensionless"),
                    "PODOSE_rome": Q(self.dose / 2.0, "mg"),
                    "PODOSE_some": Q(self.dose / 2.0, "mg"),
                },
            )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for treatment in self.treatments:
            for ks, substance in enumerate(self.substances):
                mappings[
                    self.to_sid(f"fm_po{self.dose}_{treatment}_{self.sids[ks]}")
                ] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"{treatment}_{substance}"),
                        xid="time",
                        yid="mean",
                        yid_sd=None,
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_po{self.dose}_{treatment}"),
                        xid="time",
                        yid=self.yids[ks],
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO,
                        application_form=self.form,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                        coadministration=Coadministration.NONE
                        if treatment == "OME40"
                        else Coadministration.ORAL_CONTRACEPTIVES,
                        data_type=DataType.MEAN,
                    ),
                )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        fig = Figure(
            experiment=self,
            sid="Fig2",
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

        for treatment in self.treatments:
            label = self.treatment_labels[treatment]
            color = self.colors[treatment]
            for ks, substance in enumerate(self.substances):
                # simulation
                plots[ks].add_data(
                    task=self.to_sid(f"task_po{self.dose}_{treatment}"),
                    xid="time",
                    yid=self.yids[ks],
                    label=f"Sim {label}",
                    color=color,
                    # the simulation of LNG is the control simulation
                    linestyle="--" if treatment == "LNG_OME40" else "-",
                )
                # data
                plots[ks].add_data(
                    dataset=self.to_sid(f"{treatment}_{substance}"),
                    xid="time",
                    yid="mean",
                    yid_sd=None,
                    count="count",
                    label=label,
                    color=color,
                )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Palovaara2003, output_dir=Palovaara2003.__name__)
