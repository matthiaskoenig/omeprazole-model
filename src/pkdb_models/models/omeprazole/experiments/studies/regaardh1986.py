"""Simulation experiment of the study Regaardh1986."""

from typing import ClassVar, NamedTuple, override

import pandas as pd
from pkpdsim.metadata import (
    ApplicationForm,
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


class Arm(NamedTuple):
    """An arm of the study: a dose of a route to a group."""

    route: str
    dose: int
    group: str


class Regaardh1986(OmeprazoleSimulationExperiment):
    """Simulation experiment of Regaardh1986.

    Review of four studies of omeprazole given IV (in PEG 400 and water,
    simulated as a bolus) or orally as a buffered solution:

    - `young`: balance study, 8 young healthy subjects, 10 mg IV and 20 mg
      orally of 14C omeprazole; plasma omeprazole (Fig1, mean and SEM), the
      cumulative radioactivity in urine and feces (omeprazole equivalents)
      after the oral dose (Fig2, mean; the feces are faeces + urine minus urine);
      no unchanged omeprazole in urine and feces.
    - `renal`: 12 patients with impaired renal function (creatinine clearance
      10-64 ml/min, mean 28.8 ml/min, normal liver function), 20 mg IV and
      40 mg orally; plasma omeprazole (Fig5, mean and SEM) and the radioactive
      metabolites in the urine over 24 h after the IV dose of every patient
      against the creatinine clearance (Fig6), simulated with the renal
      function of the group (28.8/101) and of every patient (CLcr/101).
    - `elderly`: 8 healthy non-smokers of 75-80 years, 20 mg IV and 40 mg
      orally; plasma omeprazole (Fig7, mean and SEM). The clearance of the
      elderly (200 ml/min) is a third of the young subjects (530-660 ml/min);
      the model has no effect of age, the elderly are simulated with the
      physiology of the young.

    The dose dependency of 10 young men (Tab2, Fig4) is not simulated.
    Times of Fig5: the curated IV and oral series had swapped time grids,
    the copy has the times of the symbols.
    """

    young_arms: ClassVar[list[Arm]] = [Arm("iv", 10, "young"), Arm("po", 20, "young")]
    renal_arms: ClassVar[list[Arm]] = [Arm("iv", 20, "renal"), Arm("po", 40, "renal")]
    elderly_arms: ClassVar[list[Arm]] = [
        Arm("iv", 20, "elderly"),
        Arm("po", 40, "elderly"),
    ]
    #: figure of the plasma data of a group
    fig_ids: ClassVar[dict[str, str]] = {
        "young": "Fig1",
        "renal": "Fig5",
        "elderly": "Fig7",
    }
    #: mean creatinine clearance of the patients with renal impairment
    #: [ml/min] (Fig6)
    clcr_renal: ClassVar[float] = 28.8
    #: GFR of the model [ml/min]
    gfr_base: ClassVar[float] = 101.0
    excretions: ClassVar[dict[str, str]] = {
        "urine": "Aurine_omemets",
        "feces": "Afeces_omemets",
    }
    colors: ClassVar[dict[str, str]] = {
        "young": "black",
        "renal": "tab:red",
        "elderly": "tab:blue",
    }

    @staticmethod
    def arm_sid(arm: Arm) -> str:
        """Get the key of the simulation and dataset of an arm."""
        return f"{arm.route}{arm.dose}_{arm.group}"

    @property
    def arms(self) -> list[Arm]:
        """Get the arms with plasma data."""
        return [*self.young_arms, *self.renal_arms, *self.elderly_arms]

    def patients(self) -> pd.DataFrame:
        """Get the creatinine clearance and the 24 h urinary metabolites of the patients."""
        df = self.load_dataframe("Fig6")
        df["patient"] = df["individual"].str.split("_").str[0]
        return df

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        # plasma omeprazole
        for fig_id in ["Fig1", "Fig5", "Fig7"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                dsets[str(label)] = DataSet.from_df(df_label, self.ureg)

        # radioactivity in urine and feces in omeprazole equivalents
        df = self.load_dataframe("Fig2")
        df = df[df.measurement_type == "cumulative amount"]
        for label, df_label in df.groupby("label"):
            dset = DataSet.from_df(df_label, self.ureg)
            dset.unit_conversion("mean", 1 / self.Mr.ome)
            dsets[str(label)] = dset

        # radioactive metabolites in urine over 24 h of every patient
        for _, row in self.patients().iterrows():
            df_patient = pd.DataFrame(
                {
                    "time": [float(row["time"])],
                    "time_unit": [row["time_unit"]],
                    "value": [float(row["y_value"])],
                    "unit": [row["y_units"]],
                    "count": [1],
                }
            )
            dset = DataSet.from_df(df_patient, self.ureg)
            dset.unit_conversion("value", 1 / self.Mr.ome)
            dsets[f"{row['patient']}_urine"] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        for arm in self.arms:
            changes = {
                **self.default_changes(),
                f"{arm.route.upper()}DOSE_some": Q(arm.dose / 2.0, "mg"),
                f"{arm.route.upper()}DOSE_rome": Q(arm.dose / 2.0, "mg"),
            }
            if arm.route == "po":
                changes.update(self.form_changes(ApplicationForm.BUFFERED_SOLUTION))
            if arm.group == "renal":
                changes["KI__f_renal_function"] = Q(
                    self.clcr_renal / self.gfr_base, "dimensionless"
                )
            # the balance study ran for 96 h
            hours = 96 if arm == Arm("po", 20, "young") else 12
            tcsims[f"ome_{self.arm_sid(arm)}"] = Simulation(
                time_unit="min",
                end=hours * 60,
                preinit_changes=changes,
            )

        # every patient with renal impairment, 20 mg IV
        for _, row in self.patients().iterrows():
            tcsims[f"ome_iv20_{row['patient']}"] = Simulation(
                time_unit="min",
                end=25 * 60,
                preinit_changes={
                    **self.default_changes(),
                    "IVDOSE_some": Q(10.0, "mg"),
                    "IVDOSE_rome": Q(10.0, "mg"),
                    "KI__f_renal_function": Q(
                        float(row["x_value"]) / self.gfr_base, "dimensionless"
                    ),
                },
            )

        return tcsims

    def metadata(
        self,
        arm: Arm,
        tissue: Tissue = Tissue.PLASMA,
        data_type: DataType = DataType.MEAN,
    ) -> PKPDMappingMetaData:
        """Get the metadata of the mappings of an arm."""
        return PKPDMappingMetaData(
            tissue=tissue,
            route=Route.IV if arm.route == "iv" else Route.PO,
            application_form=ApplicationForm.SOLUTION
            if arm.route == "iv"
            else ApplicationForm.BUFFERED_SOLUTION,
            dosing=Dosing.SINGLE,
            health=Health.RENAL_IMPAIRMENT if arm.group == "renal" else Health.HEALTHY,
            fasting=Fasting.NR,
            data_type=data_type,
        )

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        # plasma omeprazole
        for arm in self.arms:
            sid = self.arm_sid(arm)
            mappings[f"fm_{sid}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=sid,
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self, task=f"task_ome_{sid}", xid="time", yid="[Cve_ome]"
                ),
                metadata=self.metadata(arm),
            )

        # radioactivity in urine and feces after 20 mg orally
        arm = Arm("po", 20, "young")
        for tissue, yid in self.excretions.items():
            mappings[f"fm_{self.arm_sid(arm)}_{tissue}"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"po20_amount_{tissue}",
                    xid="time",
                    yid="mean",
                    count="count",
                ),
                observable=FitData(
                    self, task=f"task_ome_{self.arm_sid(arm)}", xid="time", yid=yid
                ),
                metadata=self.metadata(
                    arm, tissue=Tissue.URINE if tissue == "urine" else Tissue.FECES
                ),
            )

        # radioactive metabolites in urine of every patient, 20 mg IV
        for patient in self.patients()["patient"]:
            mappings[f"fm_iv20_{patient}_urine"] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=f"{patient}_urine",
                    xid="time",
                    yid="value",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=f"task_ome_iv20_{patient}",
                    xid="time",
                    yid="Aurine_omemets",
                ),
                metadata=self.metadata(
                    Arm("iv", 20, "renal"),
                    tissue=Tissue.URINE,
                    data_type=DataType.INDIVIDUAL,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_plasma("young", self.young_arms, scale="linear", hours=2.2),
            **self.figure_plasma("renal", self.renal_arms, scale="log", hours=2.2),
            **self.figure_plasma("elderly", self.elderly_arms, scale="log", hours=4.5),
            **self.figure2(),
            **self.figure6(),
        }

    def figure_plasma(
        self, group: str, arms: list[Arm], scale: str, hours: float
    ) -> dict[str, Figure]:
        """Figure of omeprazole in plasma of a group (Fig1, Fig5, Fig7)."""
        fig = Figure(
            experiment=self,
            sid=self.fig_ids[group],
            num_rows=1,
            num_cols=1,
            name=f"{self.__class__.__name__} ({group})",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=hours),
            legend=True,
        )
        plots[0].set_yaxis(
            self.label_ome,
            unit=self.unit_ome,
            scale=scale,
            min=0.05 if scale == "log" else None,
        )
        for arm in arms:
            sid = self.arm_sid(arm)
            color = self.colors[group] if arm.route == "iv" else "tab:orange"
            label = f"{arm.route.upper()} {arm.dose} mg"
            plots[0].add_data(
                task=f"task_ome_{sid}",
                xid="time",
                yid="[Cve_ome]",
                label=f"Sim {label}",
                color=color,
            )
            plots[0].add_data(
                dataset=sid,
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label=label,
                color=color,
            )

        return self.figures_by_sid(fig)

    def figure2(self) -> dict[str, Figure]:
        """Figure of the radioactivity in urine and feces (Fig2)."""
        fig = Figure(
            experiment=self,
            sid="Fig2",
            num_rows=1,
            num_cols=1,
            name=f"{self.__class__.__name__} (young)",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
        )
        plots[0].set_yaxis(self.label_omemets, unit=self.unit_metabolite_urine)

        arm = Arm("po", 20, "young")
        for tissue, yid in self.excretions.items():
            color = "tab:orange" if tissue == "urine" else "tab:brown"
            plots[0].add_data(
                task=f"task_ome_{self.arm_sid(arm)}",
                xid="time",
                yid=yid,
                label=f"Sim PO 20 mg {tissue}",
                color=color,
            )
            plots[0].add_data(
                dataset=f"po20_amount_{tissue}",
                xid="time",
                yid="mean",
                count="count",
                label=f"PO 20 mg {tissue}",
                color=color,
            )

        return self.figures_by_sid(fig)

    def figure6(self) -> dict[str, Figure]:
        """Figure of the metabolites in urine of every patient (Fig6)."""
        fig = Figure(
            experiment=self,
            sid="Fig6",
            num_rows=1,
            num_cols=1,
            name=f"{self.__class__.__name__} (renal)",
            settings={"legend_position": "outside"},
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=25),
            legend=True,
        )
        plots[0].set_yaxis(self.label_omemets_urine, unit=self.unit_metabolite_urine)

        patients = self.patients().sort_values("x_value")
        cmap = ["#fee5d9", "#fcae91", "#fb6a4a", "#de2d26", "#a50f15"]
        clcrs = patients["x_value"].astype(float)
        for _, row in patients.iterrows():
            clcr = float(row["x_value"])
            k = int((clcr - clcrs.min()) / (clcrs.max() - clcrs.min()) * 4.999)
            color = cmap[::-1][k]
            patient = row["patient"]
            plots[0].add_data(
                task=f"task_ome_iv20_{patient}",
                xid="time",
                yid="Aurine_omemets",
                label=f"Sim CLcr {clcr:.0f} ml/min",
                color=color,
            )
            plots[0].add_data(
                dataset=f"{patient}_urine",
                xid="time",
                yid="value",
                count="count",
                label=None,
                color=color,
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Regaardh1986, output_dir=Regaardh1986.__name__)
