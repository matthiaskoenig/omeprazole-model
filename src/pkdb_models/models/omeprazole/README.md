# Omeprazole

Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of the proton pump inhibitor omeprazole and its enantiomers S-omeprazole (esomeprazole) and R-omeprazole: the absorption of the application forms (enteric-coated forms released with a delay, buffered solutions absorbed fast, unprotected solutions degraded by the gastric acid), the distribution into the tissues, the hepatic metabolism by CYP2C19 (R-omeprazole to 5-hydroxyomeprazole, S-omeprazole mainly to 5-O-desmethylomeprazole) and CYP3A4 (omeprazole sulfone, and 5-hydroxyomeprazole from R-omeprazole, the route of poor metabolizers) with the mechanism-based inactivation of CYP2C19 by omeprazole (the rise of the exposure on repeated doses), the metabolism of the metabolites, the renal excretion of the metabolites relative to the GFR and their biliary excretion into the feces, and the inhibition of the gastric proton pumps with the stomach pH. The model describes the effects of the dose, the application form, food, the CYP2C19 genotype (poor, intermediate, extensive, rapid and ultrarapid metabolizers), of hepatic and renal impairment and of the inhibitors clarithromycin (CYP3A4) and ethinylestradiol (CYP2C19).

The published version of the model is [omeprazole-model](https://github.com/matthiaskoenig/omeprazole-model) ([doi:10.5281/zenodo.5555814](https://doi.org/10.5281/zenodo.5555814)).

## Structure

- `__init__.py`: the paths of the model and its model object `MODEL` with its release metadata and its adopted fits, which the commands below run (pkpdsim).
- `models/`: the tissue models (`model_intestine.py` with the stomach and the proton pumps, `model_liver.py`, `model_kidney.py`) and the whole-body model (`model_body.py`). `models/factory.py` creates the SBML models, the flattened whole-body model which is simulated, the ODEs and the COMBINE archive in `models/output/`; the fitted values come from the adopted fits (`models/fits.py`, `models/output/fits/`).
- `experiments/`: the simulation experiments of the 26 clinical studies (`studies/`), the application forms and the stomach pH after single and repeated doses (`misc/`) and the parameter scans of dose, food, hepatic and renal function and CYP2C19 and CYP3A4 activity (`scans/`). The fit mappings are described with the vocabulary of `pkpdsim.metadata`; the base of the experiments (`base_experiment.py`) holds the application forms, food, the CYP2C19 phenotypes and the literature based factors of the interactions.
- `fitting/`: the fit problem of the pharmacokinetics (`PK`), its parameters and the selection of the training, validation (interactions, doses, populations, food, limitations), outlier and aggregate data.
- `sensitivity/`: the sensitivity analysis of the pharmacokinetics and of the stomach pH.
- `omeprazole_pk.py`: the pharmacokinetic parameters of the scans, the non-compartmental analysis of `pkpdutils`.
- `tolerances.py`: the absolute tolerances of the integrator per state.
- `simulations.py`: the simulation experiments and their groups, `MODEL` runs them.
- `data/`: the data of the studies, a subset of the PK-DB studies (`data/collect_data.py`); copies corrected against the publications where the curation is wrong (see `TODO.md`).
- `TODO.md`: the open issues of the model.

## Commands

```bash
# models, simulations
run_simulation pkdb_models.models.omeprazole --action factory
run_simulation pkdb_models.models.omeprazole --action list_experiments
run_simulation pkdb_models.models.omeprazole --action simulate --experiments all
run_simulation pkdb_models.models.omeprazole --action simulate --experiments all --uncertainty

# fits, adoption of a fit, reports of stored parameters, identifiability
run_fit pkdb_models.models.omeprazole --subset=PK --runs=5 --cores=3 --method=LSQ
run_fit pkdb_models.models.omeprazole --adopt PK_<fit id>
run_report pkdb_models.models.omeprazole --subset=PK results/fit/PK_<fit id>/parameters.json
run_identifiability pkdb_models.models.omeprazole --subset=PK results/fit/PK_<fit id>/parameters.json

# sensitivity analysis (local by default)
python -m pkdb_models.models.omeprazole.sensitivity.sensitivity_analysis
```

The results are written into `results/` of the model.

## Adopted fits and uncertainty

The values of the fitted parameters come from the adopted fits of the model,
not from numbers in the code. `run_fit pkdb_models.models.omeprazole --adopt <fit id>`
copies the record of a finished fit (its parameters, problem, profile
likelihood and Fisher information) into `models/output/fits/<fit id>/`, which is
tracked; the ids of the adopted fits are listed in `fits` of the model object
(`__init__.py`). The factory takes the fitted values and their uncertainty from
the records (`models/fits.py`) and writes the uncertainty into the SBML
(`distrib:uncertainty`). `run_simulation ... --uncertainty` runs the
experiments over draws of these distributions and draws the simulations as the
median with a band of quantiles into `results/simulation_uncertainty`. A refit
is: fit, adopt, replace the id in `fits`, rebuild the model. See the
documentation of the repository on fitting (`docs/fitting.md`).

The adopted fit `PK_20261020_090631__aa2cf` is a least squares fit (5 starts,
all at one optimum): a differential evolution of this problem takes about 9 hr
per run and reached the same cost.
