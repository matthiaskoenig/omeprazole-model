"""Oral and intravenous application of omeprazole, single and multiple doses."""

from typing import override

from sbmlsim import Q
from sbmlsim.plot import Axis, Figure
from sbmlsim.simulation import Simulation

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)


class ApplicationExperiment(OmeprazoleSimulationExperiment):
    """Tests oral and intravenous application of omeprazole."""

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        day = 60 * 24  # [min]

        # a day without omeprazole, a dose of 40 mg every day (single: one day,
        # multi: 6 days) and 5 days after the last dose
        for route in ["iv", "po"]:
            doses = {
                f"{route.upper()}DOSE_some": Q(20, "mg"),
                f"{route.upper()}DOSE_rome": Q(20, "mg"),
            }
            for dosing, n_doses in [("single", 1), ("multi", 6)]:
                n_days = 1 + n_doses + 5
                tcsims[f"ome_{route}_{dosing}"] = Simulation(
                    time_unit="min",
                    end=n_days * day,
                    # [2.4 min]
                    preinit_changes={
                        **self.default_changes(),
                    },
                    changes=[
                        self.add_doses([k * day for k in range(1, n_doses + 1)], doses)
                    ],
                    time_shift=120,
                )

        return tcsims

    @override
    def figures(self) -> dict[str, Figure]:
        names = {
            "single": "Oral vs. intravenous omeprazole application",
            "multi": "Single vs. multiple omeprazole application",
        }
        figures = []
        for dosing, name in names.items():
            fig = Figure(
                experiment=self,
                sid=f"Fig_{dosing}",
                num_rows=3,
                num_cols=3,
                name=name,
            )
            plots = fig.create_plots(xaxis=Axis("time", unit="day"), legend=True)
            plots[0].set_yaxis("omeprazole", unit="µM")
            plots[3].set_yaxis("omeprazole metabolites\n", unit="µM")
            plots[6].set_yaxis("omeprazole metabolites\n(urine)", unit="µmole")
            plots[1].set_yaxis("stomach pH", unit="dimensionless")
            plots[4].set_yaxis("rates", unit="µmole/min")
            plots[7].set_yaxis("protons", unit="mM")
            plots[2].set_yaxis("proton pumps", unit="dimensionless")
            plots[5].set_yaxis("proton pump turnover\n", unit="mmole/min")
            plots[8].set_yaxis("fraction absorbed", unit="dimensionless")

            for application in ["iv", "po"]:
                task_id = f"task_ome_{application}_{dosing}"
                linestyle = "-" if application == "iv" else "--"

                # simulation
                plots[0].add_data(
                    task=task_id,
                    xid="time",
                    yid="[Cve_ome]",
                    label=f"omeprazole venous ({application})",
                    color="black",
                    linestyle=linestyle,
                )
                plots[0].add_data(
                    task=task_id,
                    xid="time",
                    yid="[Cve_some]",
                    label=f"S-omeprazole venous ({application})",
                    color="tab:blue",
                    linestyle=linestyle,
                )
                plots[0].add_data(
                    task=task_id,
                    xid="time",
                    yid="[Cve_rome]",
                    label=f"R-omeprazole venous ({application})",
                    color="tab:orange",
                    linestyle=linestyle,
                )

                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid="[Cve_omesul]",
                    label=f"omeprazole-sulfone venous ({application})",
                    color="tab:red",
                    linestyle=linestyle,
                )
                plots[3].add_data(
                    task=task_id,
                    xid="time",
                    yid="[Cve_omeoh]",
                    label=f"OH-omeprazole venous ({application})",
                    color="tab:green",
                    linestyle=linestyle,
                )

                plots[6].add_data(
                    task=task_id,
                    xid="time",
                    yid="Aurine_omeoth",
                    label=f"omeprazole-sulfone urine ({application})",
                    color="tab:red",
                    linestyle=linestyle,
                )
                plots[6].add_data(
                    task=task_id,
                    xid="time",
                    yid="Aurine_omeoh",
                    label=f"OH-omeprazole urine ({application})",
                    color="tab:green",
                    linestyle=linestyle,
                )

                plots[1].add_data(
                    task=task_id,
                    xid="time",
                    yid="pH",
                    label=f"pH ({application})",
                    color="black",
                    linestyle=linestyle,
                )

                plots[4].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_rate",
                    label=f"H+ secretion ({application})",
                    color="black",
                    linestyle=linestyle,
                )
                plots[4].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__gacid_loss",
                    label=f"H+ GA loss ({application})",
                    color="tab:brown",
                    linestyle=linestyle,
                )
                plots[7].add_data(
                    task=task_id,
                    xid="time",
                    yid="[GU__protons_stomach]",
                    label=f"H+ stomach ({application})",
                    color="black",
                    linestyle=linestyle,
                )

                plots[2].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_active",
                    label=f"PP active ({application})",
                    color="black",
                    linestyle=linestyle,
                )
                plots[2].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_inactive",
                    label=f"PP inactive ({application})",
                    color="grey",
                    linestyle=linestyle,
                )
                plots[2].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_total",
                    label=f"PP total ({application})",
                    color="tab:red",
                    linestyle=linestyle,
                )
                plots[5].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_active_degradation",
                    label=f"PP active degradation ({application})",
                    color="black",
                    linestyle=linestyle,
                )
                plots[5].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_inactive_degradation",
                    label=f"PP inactive degradation ({application})",
                    color="grey",
                    linestyle=linestyle,
                )
                plots[5].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__pp_synthesis",
                    label=f"PP synthesis ({application})",
                    color="tab:red",
                    linestyle=linestyle,
                )

                plots[8].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__F_ome_pH2",
                    label=f"F (pH2, {application})",
                    color="tab:blue",
                    linestyle=linestyle,
                )
                plots[8].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__F_ome_pH6",
                    label=f"F (pH6, {application})",
                    color="tab:orange",
                    linestyle=linestyle,
                )
                plots[8].add_data(
                    task=task_id,
                    xid="time",
                    yid="GU__F_ome_pH",
                    label=f"F ({application})",
                    color="black",
                    linestyle=linestyle,
                )

            figures.append(fig)

        return self.figures_by_sid(*figures)


if __name__ == "__main__":
    MODEL.run_experiments(ApplicationExperiment, output_dir="test")
