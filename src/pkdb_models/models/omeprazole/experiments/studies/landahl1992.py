"""Simulation experiment of the study Landahl1992."""

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


class Landahl1992(OmeprazoleSimulationExperiment):
    """Simulation experiment of Landahl1992.

    14 healthy elderly subjects (75 to 79 years, 71 kg), 8 of them with
    [14C]omeprazole: an intravenous infusion of 20 mg over 5 min and an oral
    dose of 40 mg as a buffered solution (sodium bicarbonate before and after
    the dose), fasted, at least one week apart. Fig1 omeprazole (14
    subjects), Fig4 5-hydroxyomeprazole, the sulfone and the radioactive
    metabolites in plasma (8 subjects), Fig5 the cumulative urinary
    radioactivity (metabolites, 8 subjects). The clearance of the elderly is
    half the clearance of young subjects (0.25 vs 0.59 l/min).
    """

    applications: ClassVar[list[str]] = ["OME20_IV", "OME40_PO"]
    routes: ClassVar[list[str]] = ["iv", "po"]
    doses: ClassVar[list[int]] = [20, 40]
    bodyweight: ClassVar[float] = 71.0  # [kg]
    infusion: ClassVar[float] = 5.0  # [min]
    colors: ClassVar[list[str]] = ["tab:blue", "tab:orange"]
    substances: ClassVar[list[str]] = [
        "omeprazole",
        "5-hydroxyomeprazole",
        "omeprazole sulfone",
        "omeprazole metabolites",
    ]
    yids: ClassVar[list[str]] = [
        "[Cve_ome]",
        "[Cve_omeoh]",
        "[Cve_omesul]",
        "[Cve_omemets]",
    ]

    fig_subsets: ClassVar[dict[str, list[str]]] = {
        "all": ["iv20", "po40"],
        "po": ["po40"],
        "iv": ["iv20"],
    }

    @override
    def datasets(self) -> dict[str, DataSet]:
        dsets = {}
        for fig_id in ["Fig1", "Fig4", "Fig5"]:
            df = self.load_dataframe(fig_id)
            for label, df_label in df.groupby("label"):
                label = str(label)
                dset = DataSet.from_df(df_label, self.ureg)
                dsets[self.to_sid(label)] = dset

                if fig_id == "Fig5":
                    dset.unit_conversion("mean", 1 / self.Mr.ome)

        return dsets

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        changes = {
            **self.default_changes(),
            "BW": Q(self.bodyweight, "kg"),
            **self.fed_changes(Fasting.FASTED),
        }

        # intravenous infusion over 5 min
        dose = self.doses[0]
        ri = Q(dose / 2.0, "mg") / Q(self.infusion, "min")
        tcsims[self.to_sid(f"ome_iv{dose}")] = Simulation(
            time_unit="min",
            end=100 * 60,
            preinit_changes={**changes, "Ri_rome": ri, "Ri_some": ri},
            changes=[
                Change(
                    self.infusion,
                    {"Ri_rome": Q(0, "mg/min"), "Ri_some": Q(0, "mg/min")},
                )
            ],
        )
        # oral buffered solution
        dose = self.doses[1]
        tcsims[self.to_sid(f"ome_po{dose}")] = Simulation(
            time_unit="min",
            end=100 * 60,
            preinit_changes={
                **changes,
                **self.form_changes(ApplicationForm.BUFFERED_SOLUTION),
                "PODOSE_rome": Q(dose / 2.0, "mg"),
                "PODOSE_some": Q(dose / 2.0, "mg"),
            },
        )

        return tcsims

    @override
    def fit_mappings(self) -> dict[str, FitMapping]:
        mappings = {}

        # figure 1 and 4
        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]
            for ks, substance in enumerate(self.substances):
                mappings[self.to_sid(f"fm_ome_{route}{dose}_{substance}")] = FitMapping(
                    self,
                    reference=FitData(
                        self,
                        dataset=self.to_sid(f"OME{dose}_{route.upper()}_{substance}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                    ),
                    observable=FitData(
                        self,
                        task=self.to_sid(f"task_ome_{route}{dose}"),
                        xid="time",
                        yid=self.yids[ks],
                    ),
                    metadata=PKPDMappingMetaData(
                        tissue=Tissue.PLASMA,
                        route=Route.PO if route == "po" else Route.IV,
                        application_form=ApplicationForm.BUFFERED_SOLUTION
                        if route == "po"
                        else ApplicationForm.SOLUTION,
                        dosing=Dosing.SINGLE,
                        health=Health.HEALTHY,
                        fasting=Fasting.FASTED,
                    ),
                )
        # figure 5
        for kr, route in enumerate(self.routes):
            dose = self.doses[kr]

            mappings[
                self.to_sid(f"fm_ome_{route}{dose}_amount_omeprazole metabolites")
            ] = FitMapping(
                self,
                reference=FitData(
                    self,
                    dataset=self.to_sid(
                        f"OME{dose}_{route.upper()}_amount_omeprazole metabolites"
                    ),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                ),
                observable=FitData(
                    self,
                    task=self.to_sid(f"task_ome_{route}{dose}"),
                    xid="time",
                    yid="Aurine_omemets",
                ),
                metadata=PKPDMappingMetaData(
                    tissue=Tissue.URINE,
                    route=Route.PO if route == "po" else Route.IV,
                    application_form=ApplicationForm.BUFFERED_SOLUTION
                    if route == "po"
                    else ApplicationForm.SOLUTION,
                    dosing=Dosing.SINGLE,
                    health=Health.HEALTHY,
                    fasting=Fasting.FASTED,
                ),
            )

        return mappings

    @override
    def figures(self) -> dict[str, Figure]:
        return {
            **self.figure_1_4(),
            **self.figure_5(),
        }

    def figure_1_4(self) -> dict[str, Figure]:
        """Figures of the plasma concentrations (Fig1 and Fig4) per subset."""
        figures = []
        for subset, applications in self.fig_subsets.items():
            fig = Figure(
                experiment=self,
                sid=self.to_sid(f"Fig1_4_{subset}"),
                num_rows=4,
                num_cols=1,
                name=self.__class__.__name__,
            )
            plots = fig.create_plots(
                xaxis=Axis(self.label_time, unit=self.unit_time, min=-0.1, max=10),
                legend=True,
            )
            plots[3].set_xaxis(self.label_time, unit=self.unit_time, min=-0.1, max=25)
            plots[0].set_yaxis(self.label_ome, self.unit_ome)
            plots[1].set_yaxis(self.label_omeoh, self.unit_omeoh)
            plots[2].set_yaxis(self.label_omesul, self.unit_omesul)
            plots[3].set_yaxis(self.label_omemets, self.unit_omemets)

            for application in applications:
                route, dose = application[0:2], int(application[2:])
                for ks, substance in enumerate(self.substances):
                    # simulation
                    plots[ks].add_data(
                        task=self.to_sid(f"task_ome_{route}{dose}"),
                        xid="time",
                        yid=self.yids[ks],
                        label=f"Sim {route}{dose}",
                        color=self.dose_colors[dose],
                    )
                    # data
                    plots[ks].add_data(
                        dataset=self.to_sid(f"OME{dose}_{route.upper()}_{substance}"),
                        xid="time",
                        yid="mean",
                        yid_sd="mean_sd",
                        count="count",
                        label=f"{route}{dose}",
                        color=self.dose_colors[dose],
                    )

            figures.append(fig)

        return self.figures_by_sid(*figures)

    def figure_5(self) -> dict[str, Figure]:
        """Figures of the omeprazole metabolites in urine (Fig5) per subset."""
        figures = []
        for subset, applications in self.fig_subsets.items():
            fig = Figure(
                experiment=self,
                sid=self.to_sid(f"Fig5_{subset}"),
                num_rows=1,
                num_cols=1,
                name=self.__class__.__name__,
            )

            plots = fig.create_plots(
                xaxis=Axis(self.label_time, unit=self.unit_time), legend=True
            )
            plots[0].set_yaxis(self.label_omemets_urine, unit=self.unit_omemets_urine)

            for application in applications:
                route, dose = application[0:2], int(application[2:])
                # simulation
                plots[0].add_data(
                    task=self.to_sid(f"task_ome_{route}{dose}"),
                    xid="time",
                    yid="Aurine_omemets",
                    label=f"Sim {route}{dose}",
                    color=self.dose_colors[dose],
                )
                # data
                plots[0].add_data(
                    dataset=self.to_sid(
                        f"OME{dose}_{route.upper()}_amount_omeprazole metabolites"
                    ),
                    xid="time",
                    yid="mean",
                    yid_sd="mean_sd",
                    count="count",
                    label=f"{route}{dose}",
                    color=self.dose_colors[dose],
                )

            figures.append(fig)

        return self.figures_by_sid(*figures)


if __name__ == "__main__":
    MODEL.run_experiments(Landahl1992, output_dir=Landahl1992.__name__)
