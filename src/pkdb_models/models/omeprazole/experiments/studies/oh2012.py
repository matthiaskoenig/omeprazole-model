"""Simulation experiment of the study Oh2012."""

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


class Oh2012(OmeprazoleSimulationExperiment):
    """Simulation experiment of Oh2012.

    13 healthy Korean volunteers (CYP2C19 genotype, sex and body weight not
    reported) took one capsule of the Inje cocktail at 09:00: caffeine 10 mg,
    losartan 2 mg, omeprazole 0.2 mg, dextromethorphan 2 mg and midazolam
    0.1 mg (`Coadministration.COCKTAIL`, no interaction expected at these
    doses); fasting not reported. Omeprazole and 5-hydroxyomeprazole in plasma
    (Fig3, mean and SD; the error type is not stated). The omeprazole of the
    capsule is enteric coated: neither analyte is detected before 1.5 h, the
    points from 0 to 1 h are below the LLOQ (0.05 ng/ml) and set to 0.

    The microdose of 0.2 mg is far below the clinical doses: the data validate
    the dose dependency of the model.
    """

    dose: ClassVar[float] = 0.2  # [mg]
    form: ClassVar[ApplicationForm] = ApplicationForm.CAPSULE
    info: ClassVar[dict[str, str]] = {
        "[Cve_ome]": "omeprazole",
        "[Cve_omeoh]": "hydroxyomeprazole",
    }
    sids: ClassVar[dict[str, str]] = {"[Cve_ome]": "ome", "[Cve_omeoh]": "omeoh"}

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig3"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)

                # unit conversion to mole/l
                if label == "omeprazole":
                    dset.unit_conversion("mean", 1 / self.Mr.ome)
                elif label == "hydroxyomeprazole":
                    dset.unit_conversion("mean", 1 / self.Mr.omeoh)

                dsets[self.to_sid(label)] = dset

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}

        # single dose
        tcsims[self.to_sid(f"po_ome{self.dose}")] = Simulation(
            time_unit="min",
            end=15 * 60,  # [min]
            preinit_changes={
                **self.default_changes(),
                **self.form_changes(self.form),
                "PODOSE_some": Q(self.dose / 2, "mg"),
                "PODOSE_rome": Q(self.dose / 2, "mg"),
            },
        )
        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}
        for sid, name in self.info.items():
            mappings[self.to_sid(f"fm_po{self.dose}_{self.sids[sid]}")] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=self.to_sid(name),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=self.to_sid(f"task_po_ome{self.dose}"),
                    xid="time",
                    yid=sid,
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.PLASMA,
                    route=Route.PO,
                    application_form=self.form,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.NR,
                    coadministration=Coadministration.COCKTAIL,
                    data_type=DataType.MEAN,
                ),
            )
        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.fig3(),
        }

    def fig3(self) -> dict[str, Figure]:
        """Figure of omeprazole and hydroxyomeprazole in plasma (Fig3)."""
        fig = Figure(
            experiment=self,
            sid="Fig3",
            num_rows=2,
            name=f"{self.__class__.__name__} (healthy, cocktail)",
        )
        plots = fig.create_plots(
            xaxis=Axis(self.label_time, unit=self.unit_time, max=12), legend=True
        )
        plots[0].set_yaxis(self.label_ome, unit=self.unit_ome)
        plots[1].set_yaxis(self.label_omeoh, unit=self.unit_omeoh)

        for k, sid in enumerate(self.info):
            name = self.info[sid]

            # simulation
            plots[k].add_data(
                task=self.to_sid(f"task_po_ome{self.dose}"),
                xid="time",
                yid=sid,
                label="Sim 0.2 mg",
                color="black",
            )
            # data
            plots[k].add_data(
                dataset=self.to_sid(name),
                xid="time",
                yid="mean",
                yid_sd="mean_sd",
                count="count",
                label="0.2 mg",
                color="black",
            )

        return self.figures_by_sid(fig)


if __name__ == "__main__":
    MODEL.run_experiments(Oh2012, output_dir=Oh2012.__name__)
