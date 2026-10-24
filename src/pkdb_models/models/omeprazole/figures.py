"""Figures of the omeprazole experiments created from their fit mappings."""

import logging

import numpy as np
from sbmlsim.data import Data
from sbmlsim.fit import FitData, FitMapping
from sbmlsim.plot import Figure

from pkdb_models.models.omeprazole.experiments.base_experiment import (
    OmeprazoleSimulationExperiment,
)

logger = logging.getLogger(__name__)


def _selection(data: Data | None) -> str | None:
    """Get the selection of an optional data of a fit."""
    return data.selection if data else None


def _index(data: Data | None) -> str | None:
    """Get the index of an optional data of a fit."""
    return data.index if data else None


def figure_from_mappings(
    fig_id: str,
    experiment: OmeprazoleSimulationExperiment,
    mappings: list[FitMapping],
    colors: list[str] | None = None,
    labels: list[str] | None = None,
    sim_labels: list[str] | None = None,
    nrows: int | None = None,
    ncols: int | None = None,
) -> dict[str, Figure]:
    """Create a figure with a plot of the simulation and the data of every mapping.

    Args:
        fig_id: id of the figure.
        experiment: the experiment of the mappings.
        mappings: the fit mappings, one plot each.
        colors: color of every mapping, black by default.
        labels: label of the data of every mapping, "data" by default.
        sim_labels: label of the simulation of every mapping, "Sim" and the
            task without its prefix "task_" by default.
        nrows: rows of the figure, from the number of mappings by default.
        ncols: columns of the figure, from the number of mappings by default.

    Returns:
        The figure by its id.
    """
    n_mappings = len(mappings)

    if nrows is None or ncols is None:
        if n_mappings <= 3:
            nrows, ncols = n_mappings, 1
        elif n_mappings == 4:
            nrows, ncols = 2, 2
        elif n_mappings <= 6:
            nrows, ncols = 3, 2
        elif n_mappings <= 9:
            nrows, ncols = 3, 3
        else:
            nrows = int(np.ceil(np.sqrt(n_mappings)))
            ncols = nrows

    fig = Figure(
        experiment=experiment,
        sid=fig_id,
        num_rows=nrows,
        num_cols=ncols,
        name=experiment.sid,
    )
    plots = fig.create_plots(legend=True)

    # create axis
    for k, mapping in enumerate(mappings):
        color = colors[k] if colors else "black"
        observable: FitData = mapping.observable
        reference: FitData = mapping.reference
        # the x data of a fit data is optional in sbmlsim 0.9
        if observable.x is None or reference.x is None:
            raise ValueError(f"A mapping without x data: '{mapping}'")
        logger.debug("%s ~ %s", observable.x.index, observable.y.index)
        plots[k].set_xaxis(
            label=experiment.labels.get(observable.x.selection, observable.x.selection),
            unit=experiment.units[observable.x.selection],
        )
        plots[k].set_yaxis(
            label=experiment.labels.get(observable.y.selection, observable.y.selection),
            unit=experiment.units[observable.y.selection],
        )

        # simulation
        task_id = observable.task_id
        if task_id is None:
            raise ValueError(f"The observable of a mapping is not a task: '{mapping}'")
        label = sim_labels[k] if sim_labels else f"Sim {task_id.replace('task_', '')}"
        plots[k].add_data(
            task=task_id,
            xid=observable.x.selection,
            xid_sd=_selection(observable.x_sd),
            xid_se=_selection(observable.x_se),
            yid=observable.y.selection,
            yid_sd=_selection(observable.y_sd),
            yid_se=_selection(observable.y_se),
            label=label,
            color=color,
            linestyle="-",
        )
        # dataset
        label = labels[k] if labels else "data"
        plots[k].add_data(
            dataset=reference.dset_id,
            xid=reference.x.index,
            xid_sd=_index(reference.x_sd),
            xid_se=_index(reference.x_se),
            yid=reference.y.index,
            yid_sd=_index(reference.y_sd),
            yid_se=_index(reference.y_se),
            count=reference.count,
            label=label,
            color=color,
            linestyle="--",
        )

    return {fig_id: fig}
