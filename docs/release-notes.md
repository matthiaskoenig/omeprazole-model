# Release notes

## Release notes for omeprazole-model 0.9.0

Made from pkdb_models 3a0b49144b with pkpdsim 0.11.0.

The changes since 0.8.0.

### Core libraries

The versions of the core libraries cannot be compared, there is no lock file in the previous release. The release uses:

- pkpdsim 0.11.0
- sbmlsim 0.13.0
- sbmlutils 0.17.0

### Libraries

The versions cannot be compared, there is no lock file in the previous release.

### Data

- Added: `caffeine/Oh2012`, `omeprazole/Andersson1990`, `omeprazole/Andersson1990a`, `omeprazole/Andersson1993`, `omeprazole/Andersson2001`, `omeprazole/Cederberg1992`, `omeprazole/Elkoshi2002`, `omeprazole/Faruquee2010`, `omeprazole/Geus2000`, `omeprazole/HassanAlin2000`, `omeprazole/HassanAlin2005`, `omeprazole/Howden1984`, `omeprazole/Howden1984a`, `omeprazole/Iftikhar2024`, `omeprazole/Kita2001`, `omeprazole/Kita2002`, `omeprazole/Landahl1992`, `omeprazole/Lind1983`, `omeprazole/Naesdal1986`, `omeprazole/Palovaara2003`, `omeprazole/Park2017`, `omeprazole/Pounder1986`, `omeprazole/Prichard1985`, `omeprazole/Qadir2017`, `omeprazole/Regaardh1986`, `omeprazole/Regaardh1990`, `omeprazole/Sohn1992`, `omeprazole/Uno2007`, `omeprazole/VazdaSilva2001`, `omeprazole/VazdaSilva2005`, `omeprazole/Walt1983`, `omeprazole/Walt1985`

### Analysis

#### Models

- `omeprazole_body.xml`: added 86 species, 112 reactions, 194 parameters; removed 30 species, 45 reactions, 117 parameters; changed values `ftissue_ome` 0.449478 → 100
- `omeprazole_body_flat.xml`: added 96 species, 145 reactions, 255 parameters; removed 36 species, 55 reactions, 131 parameters; changed values `ftissue_ome` 0.449478 → 100
- `omeprazole_intestine.xml`: new, 13 species, 17 reactions, 35 parameters
- `omeprazole_kidney.xml`: added 4 species, 2 reactions, 6 parameters; removed 2 species, 1 reaction, 1 parameter
- `omeprazole_liver.xml`: added 11 species, 14 reactions, 24 parameters; removed 4 species, 3 reactions, 6 parameters
- `omeprazole_stomach.xml`: removed

#### Experiments

- Added: `Andersson1990a`, `Andersson1993`, `Andersson2001`, `ApplicationExperiment`, `Cederberg1992`, `Elkoshi2002`, `Faruquee2010`, `Geus2000`, `HassanAlin2000`, `HassanAlin2005`, `Kita2001`, `Kita2002`, `Landahl1992`, `Lind1983`, `Naesdal1986`, `Oh2012`, `OmeprazoleParameterScan`, `PHChangeExperiment`, `Palovaara2003`, `Park2017`, `Prichard1985`, `Qadir2017`, `Regaardh1986`, `Regaardh1990`, `Sohn1992`, `Uno2007`, `VazdaSilva2001`, `VazdaSilva2005`, `Walt1985`

#### Fits

- `PK`: `PK_20261020_090631__aa2cf`, no fit record in the previous release

## Release notes for omeprazole-model 0.8.0

We are pleased to release a new version of the omeprazole-model including the 
following changes:

### Features
- parameter fitting finished
- improved stomach pH modeling

Your omeprazole-model team

## Release notes for omeprazole-model 0.7.0

We are pleased to release a new version of the omeprazole-model including the 
following changes:

### Features
- sbml4humans report
- model annotations
- zenodo integration

Your omeprazole-model team

