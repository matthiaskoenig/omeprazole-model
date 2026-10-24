"""Changes of the stomach pH by omeprazole, single and multiple doses."""

from typing import ClassVar, override

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure as FigureMPL
from pkpdsim.scan import point_band, point_timecourse
from sbmlsim import Q
from sbmlsim.simulation import Simulation

from pkdb_models.models.omeprazole import MODEL
from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)

#: the simulations of the groups of the pH data of Cederberg1992 (Fig2)
CEDERBERG1992_GROUPS: dict[str, str] = {
    "_pre": "ome_control",
    "iv_10_day_1": "ome_iv10_single",
    "iv_10_day_5": "ome_iv10_multi",
    "iv_40_day_1": "ome_iv40_single",
    "iv_40_day_5": "ome_iv40_multi",
    "po_20_day_1": "ome_po20_single",
    "po_20_day_5": "ome_po20_multi",
}


class PHChangeExperiment(OmeprazoleSimulationExperiment):
    """Tests oral and intravenous application of omeprazole in single and multiple dose.

    Plots the resulting changes in pH value. In a run over the draws of the
    fitted parameters (`run_simulation pkdb_models.models.omeprazole
    --uncertainty`) the timecourses are the median of the draws with the band
    of their quantiles, the distributions of the pH those of the median.
    """

    #: the opacity of the bands of the draws of the fitted parameters
    band_alpha = 0.15

    doses: ClassVar[list[int]] = [10, 20, 40]
    info: ClassVar[dict[str, dict[str, str]]] = {
        "ome_iv10_single": {"color": "#fcae91", "linestyle": "-"},
        "ome_iv10_multi": {"color": "#fcae91", "linestyle": "--"},
        "ome_iv20_single": {"color": "#fb6a4a", "linestyle": "-"},
        "ome_iv20_multi": {"color": "#fb6a4a", "linestyle": "--"},
        "ome_iv40_single": {"color": "#cb181d", "linestyle": "-"},
        "ome_iv40_multi": {"color": "#cb181d", "linestyle": "--"},
        "ome_po10_single": {"color": "#6baed6", "linestyle": "-"},
        "ome_po10_multi": {"color": "#6baed6", "linestyle": "--"},
        "ome_po20_single": {"color": "#3182bd", "linestyle": "-"},
        "ome_po20_multi": {"color": "#3182bd", "linestyle": "--"},
        "ome_po40_single": {"color": "#08519c", "linestyle": "-"},
        "ome_po40_multi": {"color": "#08519c", "linestyle": "--"},
        "ome_control": {"color": "black", "linestyle": "-"},
    }

    @override
    def simulations(self) -> dict[str, Simulation]:
        tcsims = {}
        day = 60 * 24  # [min]

        tcsims["ome_control"] = Simulation(
            time_unit="min",
            end=day,
            preinit_changes={
                **self.default_changes(),
            },
        )

        # the day of the last dose is returned: a day without omeprazole and,
        # for the multiple doses, 4 days of doses before it
        times = np.linspace(0, day, num=3001).tolist()  # [min]
        for dose in self.doses:
            for dosing, n_doses in [("single", 1), ("multi", 5)]:
                for route in ["iv", "po"]:
                    doses = {
                        f"{route.upper()}DOSE_some": Q(dose / 2, "mg"),
                        f"{route.upper()}DOSE_rome": Q(dose / 2, "mg"),
                    }
                    tcsims[f"ome_{route}{dose}_{dosing}"] = Simulation(
                        time_unit="min",
                        start=-n_doses * day,
                        end=day,
                        times=times,
                        preinit_changes={
                            **self.default_changes(),
                        },
                        changes=[
                            self.add_doses([-k * day for k in range(n_doses)], doses)
                        ],
                    )

        return tcsims

    @override
    def figures_mpl(self) -> dict[str, FigureMPL]:
        fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(
            nrows=3, ncols=2, figsize=(16, 24)
        )
        fig.subplots_adjust(wspace=0.3, hspace=0.3)

        # time, pH, F_ome_pH
        ax1.set_title("Stomach pH")
        ax1.set_ylabel("Stomach pH [-]")
        ax1.set_xlabel("time [hr]")
        ax2.set_title("Fraction absorbed")
        ax2.set_ylabel("Fraction absorbed [-]")
        ax2.set_xlabel("time [hr]")

        ax3.set_title("pH distribution single application")
        ax3.set_ylabel("Density [-]")
        ax3.set_xlabel("Stomach pH [-]")
        ax4.set_title("pH distribution multi application")
        ax4.set_ylabel("Density [-]")
        ax4.set_xlabel("Stomach pH [-]")
        ax5.set_title("Cumulative pH frequency")
        ax5.set_ylabel("Cumulative frequency of\nintragastric pH-values [%]")
        ax5.set_xlabel("Stomach pH [-]")
        ax6.set_title("Data cumulative pH frequency")
        ax6.set_ylabel("Cumulative frequency of\nintragastric pH-values [%]")
        ax6.set_xlabel("Stomach pH [-]")

        axes_titlesize = 20
        axes_titleweight = "bold"
        axes_labelsize = 18
        axes_labelweight = "bold"
        xtick_labelsize = 15
        ytick_labelsize = 15

        fig.suptitle(
            "Omeprazole changes in stomach pH",
            fontsize=self.pkpd_model.figures.fig_titlesize,
            fontweight=self.pkpd_model.figures.fig_titleweight,
        )

        for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
            ax.title.set_fontsize(axes_titlesize)
            ax.title.set_fontweight(axes_titleweight)
            ax.xaxis.label.set_fontsize(axes_labelsize)
            ax.xaxis.label.set_fontweight(axes_labelweight)
            ax.yaxis.label.set_fontsize(axes_labelsize)
            ax.yaxis.label.set_fontweight(axes_labelweight)
            ax.tick_params(axis="x", labelsize=xtick_labelsize)
            ax.tick_params(axis="y", labelsize=ytick_labelsize)

        # plot simulations
        for sim_key, style in self.info.items():
            res = self.results[f"task_{sim_key}"]
            # the timecourses with the state after a dose at its time, as
            # sbmlsim 0.8.5 gave them; the median of the draws with their band
            run = self.uncertainty
            if run is None:
                time, ph = point_timecourse(res, "pH")
                _, f_ph = point_timecourse(res, "GU__F_ome_pH")
            else:
                time, ph_low, ph, ph_high = point_band(
                    res, "pH", across=run.id, quantiles=run.quantiles
                )
                _, f_low, f_ph, f_high = point_band(
                    res, "GU__F_ome_pH", across=run.id, quantiles=run.quantiles
                )
                for ax, low, high in ((ax1, ph_low, ph_high), (ax2, f_low, f_high)):
                    ax.fill_between(
                        time / 60,
                        low,
                        high,
                        color=style["color"],
                        alpha=self.band_alpha,
                        linewidth=0,
                    )

            bins = np.linspace(0, 7, num=50)

            ph_cfreq = np.zeros_like(bins)
            for k, ph_bin in enumerate(bins):
                # get count of all values above ph_bin
                ph_cfreq[k] = np.sum(ph > ph_bin) / len(ph) * 100

            # histogram
            if sim_key.endswith("single"):
                axes = (ax3,)
            elif sim_key.endswith("multi"):
                axes = (ax4,)
            else:  # control
                axes = (ax3, ax4)
            for ax in axes:
                ax.hist(
                    ph,
                    density=True,
                    bins=bins,
                    color=style["color"],
                    alpha=0.7,
                    label=sim_key,
                    histtype="bar",
                )

            ax1.plot(
                time / 60,
                ph,
                marker="",
                label=sim_key,
                color=style["color"],
                linestyle=style["linestyle"],
            )
            ax2.plot(
                time / 60,
                f_ph,
                marker="",
                label=sim_key,
                color=style["color"],
                linestyle=style["linestyle"],
            )
            ax5.plot(
                bins,
                ph_cfreq,
                marker="",
                label=sim_key,
                color=style["color"],
                linestyle=style["linestyle"],
            )

        # plot data
        df = self.load_dataframe("Fig2", study="Cederberg1992")
        for group, df_group in df.groupby("y_label"):
            sim_key = next(
                key
                for suffix, key in CEDERBERG1992_GROUPS.items()
                if str(group).endswith(suffix)
            )
            ax6.plot(
                df_group["x_value"],
                df_group["y_value"],
                marker="o",
                label=sim_key,
                color=self.info[sim_key]["color"],
                linestyle=self.info[sim_key]["linestyle"],
            )
        # the cumulative frequencies of the pH above 1 to 7
        ph_levels = list(range(1, 8))
        ph_labels = [f">{level}" for level in ph_levels]
        ax5.set_xlim(1, 7)
        ax5.set_xticks(ph_levels, ph_labels)
        ax6.set_xticks(ph_levels, ph_labels)

        for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
            ax.legend()

        return {
            "fig_ph": fig,
        }


if __name__ == "__main__":
    MODEL.run_experiments(PHChangeExperiment, output_dir="test")
