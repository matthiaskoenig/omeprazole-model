"""Simulation experiment of the study Uno2007."""

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


class Uno2007(OmeprazoleSimulationExperiment):
    """Simulation experiment of Uno2007.

    20 healthy Japanese, genotyped for CYP2C19: 6 homozygous extensive
    metabolizers (*1/*1, 58 kg, `EM`), 8 heterozygous extensive metabolizers
    (*1/*2 or *1/*3, 63 kg, `IM`) and 6 poor metabolizers (*2/*2 or *2/*3,
    67 kg, `PM`), received 40 mg omeprazole orally (two enteric-coated
    tablets) and 20 mg IV (bolus over 60 s) in a crossover after an overnight
    fast. Plasma omeprazole, 5-hydroxyomeprazole and the sulfone (Fig1, mean).

    The error bars of the digitized Fig1 are not usable (most of the bar ends
    lie below their mean), the data are the means without SD. Fig1 draws the
    IV samples on the oral grid (0.5, 1, 1.5 h); the data use the IV times of
    the Methods (0.08, 0.5, 1 h), with which the AUC of the IV means agrees
    with Table 1.
    """

    variants: ClassVar[list[str]] = ["EM", "IM", "PM"]
    routes: ClassVar[list[str]] = ["PO", "IV"]
    doses: ClassVar[list[int]] = [40, 20]
    bodyweights: ClassVar[dict[str, float]] = {"EM": 58, "IM": 63, "PM": 67}  # [kg]
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
                # the label ends with the substance: ome, omeoh or omesul
                sid = label.split("_")[-1]
                dset.unit_conversion("mean", 1 / getattr(self.Mr, sid))
                dsets[label] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        for k, route in enumerate(self.routes):
            dose = self.doses[k]
            form_changes = (
                self.form_changes(ApplicationForm.DELAYED_RELEASE_TABLET)
                if route == "PO"
                else {}
            )
            for variant in self.variants:
                f_cyp2c19 = self.cyp2c19_map[variant]
                tcsims[f"ome{dose}{route}_{variant}"] = Simulation(
                    time_unit="min",
                    end=12 * 60,
                    preinit_changes={
                        **self.default_changes(),
                        "BW": Q(self.bodyweights[variant], "kg"),
                        **form_changes,
                        f"{route.upper()}DOSE_rome": Q(dose / 2.0, "mg"),
                        f"{route.upper()}DOSE_some": Q(dose / 2.0, "mg"),
                        "LI__f_cyp2c19": Q(f_cyp2c19, "dimensionless"),
                    },
                )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        for variant in self.variants:
            for k, yid in enumerate(self.yids):
                sid = self.sids[k]

                for kr, route in enumerate(self.routes):
                    dose = self.doses[kr]
                    mappings[f"fm_ome{dose}{route}_{variant}_{sid}"] = FitMapping(
                        self,
                        reference=FitData(
                            self,
                            dataset=f"OME{dose}{route.upper()}_{variant}_{sid}",
                            xid="time",
                            yid="mean",
                            count="count",
                        ),
                        observable=FitData(
                            self,
                            task=f"task_ome{dose}{route}_{variant}",
                            xid="time",
                            yid=yid,
                        ),
                        metadata=PKPDMappingMetaData(
                            tissue=Tissue.PLASMA,
                            route=Route.PO if route == "PO" else Route.IV,
                            application_form=ApplicationForm.DELAYED_RELEASE_TABLET
                            if route == "PO"
                            else ApplicationForm.SOLUTION,
                            dosing=Dosing.SINGLE,
                            health=Health.HEALTHY,
                            fasting=Fasting.FASTED,
                            phenotype=Phenotype[f"CYP2C19_{variant}"],
                            data_type=DataType.MEAN,
                        ),
                    )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        name = "Fig1"
        fig = Figure(
            experiment=self,
            sid=name,
            num_rows=3,
            num_cols=2,
            name=self.__class__.__name__,
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, min=0, max=9),
            legend=True,
        )
        for k, yid in enumerate(self.yids):
            for kr, route in enumerate(self.routes):
                plots[2 * k + kr].set_yaxis(
                    self.labels[yid], unit=self.unit_metabolite, scale="log", min=1e-3
                )
                if k == 0:
                    plots[kr].set_title(f"{route} {self.doses[kr]} mg")

        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]

            # simulation
            for variant in self.variants:
                for k, yid in enumerate(self.yids):
                    plots[2 * k + kr].add_data(
                        task=f"task_ome{dose}{route}_{variant}",
                        xid="time",
                        yid=yid,
                        label=f"Sim {variant} {route}{dose}",
                        color=self.cyp2c19_colors[variant],
                    )

            # datasets
            for variant in self.variants:
                for k, sid in enumerate(self.sids):
                    dset_id = f"OME{dose}{route.upper()}_{variant}_{sid}"
                    plots[2 * k + kr].add_data(
                        dataset=dset_id,
                        xid="time",
                        yid="mean",
                        count="count",
                        label=f"{variant} {route}{dose}",
                        color=self.cyp2c19_colors[variant],
                    )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Uno2007, output_dir=Uno2007.__name__)
