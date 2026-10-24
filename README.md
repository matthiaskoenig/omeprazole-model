[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5555814.svg)](https://doi.org/10.5281/zenodo.5555814)
[![Release](https://img.shields.io/github/v/release/matthiaskoenig/omeprazole-model)](https://github.com/matthiaskoenig/omeprazole-model/releases)
[![Documentation](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/docs.yml/badge.svg)](https://matthiaskoenig.github.io/omeprazole-model/)
[![CI](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/ci.yml/badge.svg)](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/docker/v/matthiaskoenig/omeprazole?sort=semver&label=docker)](https://hub.docker.com/r/matthiaskoenig/omeprazole)
[![Python](https://img.shields.io/badge/python-3.14-blue)](https://www.python.org)
[![Code license: MIT](https://img.shields.io/badge/code%20license-MIT-blue)](https://opensource.org/license/MIT)
[![Model license: CC BY-SA 4.0](https://img.shields.io/badge/model%20license-CC%20BY--SA%204.0-lightgrey)](https://creativecommons.org/licenses/by-sa/4.0/)

# Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of omeprazole

This repository provides the omeprazole physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption of the application forms of omeprazole, the metabolism of S- and R-omeprazole by CYP2C19 and CYP3A4 in the liver with the mechanism-based inactivation of CYP2C19, the renal and biliary excretion of the metabolites, the inhibition of the gastric proton pumps and the effects of the CYP2C19 genotype, of interacting drugs and of impaired renal and hepatic function.

Documentation: <https://matthiaskoenig.github.io/omeprazole-model/>

## Quick start

```bash
git clone https://github.com/matthiaskoenig/omeprazole-model.git && cd omeprazole-model
uv sync
uv run run_simulation pkdb_models.models.omeprazole --action all -r results
```

## How to cite

> Leal Pujol, H., Balci, S. & König, M. (2026). *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of omeprazole*. Zenodo. https://doi.org/10.5281/zenodo.5555814

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

&copy; 2020-2026 Helen Leal Pujol, Sükrü Balci and Matthias König
