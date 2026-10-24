[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5555814.svg)](https://doi.org/10.5281/zenodo.5555814)
[![GitHub Action](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/python.yml/badge.svg)](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/python.yml)
[![GitHub Action](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/docker.yml/badge.svg)](https://github.com/matthiaskoenig/omeprazole-model/actions/workflows/docker.yml)

# omeprazole model
This repository provides the omeprazole physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model: the absorption of the application forms of omeprazole (enteric-coated forms, buffered and unprotected solutions), its distribution into the tissues, the hepatic metabolism of S-omeprazole (esomeprazole) and R-omeprazole by CYP2C19 and CYP3A4 to 5-hydroxyomeprazole, omeprazole sulfone and other metabolites with the mechanism-based inactivation of CYP2C19 by omeprazole, the renal and biliary excretion of the metabolites and the inhibition of the gastric proton pumps with the stomach pH. The model describes the effects of the dose, the application form, food, the CYP2C19 genotype, of hepatic and renal impairment and of inhibitors of CYP3A4 (clarithromycin) and CYP2C19 (ethinylestradiol).

The model is distributed in [SBML](http://sbml.org) format available from [`omeprazole_body_flat.xml`](./models/omeprazole_body_flat.xml) with 
corresponding [SBML4humans model report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fomeprazole-model%2Fmain%2Fmodels%2Fomeprazole_body_flat.xml) and [model equations](./models/omeprazole_body_flat.md).

The COMBINE archive is available from [`omeprazole_model.omex`](./omeprazole_model.omex).

### Comp submodels
* **liver** submodel [`omeprazole_liver.xml`](./models/omeprazole_liver.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fomeprazole-model%2Fmain%2Fmodels%2Fomeprazole_liver.xml) and [equations](./models/omeprazole_liver.md).
* **kidney** submodel [`omeprazole_kidney.xml`](./models/omeprazole_kidney.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fomeprazole-model%2Fmain%2Fmodels%2Fomeprazole_kidney.xml) and [equations](./models/omeprazole_kidney.md).
* **intestine** submodel [`omeprazole_intestine.xml`](./models/omeprazole_intestine.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fomeprazole-model%2Fmain%2Fmodels%2Fomeprazole_intestine.xml) and [equations](./models/omeprazole_intestine.md).
* **whole-body** submodel [`omeprazole_body.xml`](./models/omeprazole_body.xml) with [SBML4humans report](https://sbml4humans.de/report?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmatthiaskoenig%2Fomeprazole-model%2Fmain%2Fmodels%2Fomeprazole_body.xml) and [equations](./models/omeprazole_body.md).

## How to cite
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5555814.svg)](https://doi.org/10.5281/zenodo.5555814)

> Leal Pujol, H., Balci, S. & König, M. (2026).
> *Physiologically based pharmacokinetic/pharmacodynamic (PBPK/PD) model of omeprazole.*   
> Zenodo. [https://doi.org/10.5281/zenodo.5555814](https://doi.org/10.5281/zenodo.5555814)

## License

* Source Code: [MIT](https://opensource.org/license/MIT)
* Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
* Models: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

## Run simulations
### python
Clone the repository 
```bash
git clone https://github.com/matthiaskoenig/omeprazole-model.git
cd omeprazole-model
```

#### uv
Setup environment with uv (https://docs.astral.sh/uv/getting-started/installation/)
```bash
uv sync
```
Run the complete analysis:
```bash
uv run run_simulation pkdb_models.models.omeprazole -a all -r results
```

#### pip
If you use pip install the package via
```bash
pip install -e .
```
Run the complete analysis in the environment via:
```bash
run_simulation pkdb_models.models.omeprazole -a all -r results
```

### docker
Simulations can also be run within a docker container:

```bash
docker run -v "${PWD}/results:/results" -it matthiaskoenig/omeprazole:latest /bin/bash
```

Run the complete analysis:
```bash
uv run run_simulation pkdb_models.models.omeprazole -a all -r /results
```
The results are written into the mounted `/results` folder on the host.

In case of permission issues with the mounted folder, adjust ownership and access rights with:
```bash
sudo chown $(id -u):$(id -g) -R "${PWD}/results"
sudo chmod 775 "${PWD}/results"
```

## Funding
Matthias König was supported by the Federal Ministry of Research, Technology and Space (BMFTR, Germany) within ATLAS by grant number 031L0304B and by the German Research Foundation (DFG) within the Research Unit Program FOR 5151 QuaLiPerF (Quantifying Liver Perfusion-Function Relationship in Complex Resection - A Systems Medicine Approach) by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA). This work was supported by the BMBF-funded de.NBI Cloud within the German Network for Bioinformatics Infrastructure (de.NBI) (031A537B, 031A533A, 031A538A, 031A533B, 031A535A, 031A537C, 031A534A, 031A532B).

© 2020-2026 Matthias König, [Systems Medicine of the Liver](https://livermetabolism.com)
