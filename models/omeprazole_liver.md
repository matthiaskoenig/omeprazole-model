# Model for omeprazole metabolism in the liver

Model `omeprazole_liver`, SBML Level 3 Version 2, read from omeprazole\_liver.xml, written by sbmlode 0.3.0.

Model for omeprazole metabolism in the liver

S-omeprazole and R-omeprazole exchange fast between the plasma and the liver and are metabolized by CYP2C19 and CYP3A4, which act on the liver concentration (apparent Michaelis constants of the total concentration).

R-omeprazole: CYP2C19 to 5-hydroxyomeprazole, CYP3A4 to omeprazole sulfone.

S-omeprazole: CYP2C19 to 5-O-desmethylomeprazole (other metabolites) and a fraction to 5-hydroxyomeprazole, CYP3A4 to omeprazole sulfone.

5-hydroxyomeprazole is released into the plasma or oxidized in the liver to the other metabolites; omeprazole sulfone exchanges with the plasma and is metabolized by CYP2C19 and a CYP2C19 independent route to the other metabolites; the other metabolites are excreted into the bile.

CYP2C19 activity: genotype and interactions f\_cyp2c19, mechanism-based inactivation by omeprazole cyp2c19\_active; CYP3A4 activity: interactions f\_cyp3a4.

The content of this model has been carefully created in a manual research effort.

Terms of use

Copyright © 2026 Matthias König.

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.

Redistribution and use of any part of this model, with or without modification, are permitted provided that the following conditions are met:

Redistributions of this SBML file must retain the above copyright notice, this list of conditions and the following disclaimer.

Redistributions in a different form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

This model is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Units

| Time | Substance | Extent | Volume | Area | Length |
| --- | --- | --- | --- | --- | --- |
| min | mmol | mmol | l | m<sup>2</sup> | m |

## Compartments

| Symbol | Id | Name | Size | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{Vext}$ | `Vext` | plasma | $1.5$ | l | ✓ |
| $\mathrm{Vli}$ | `Vli` | liver | $1.5$ | l | ✓ |
| $\mathrm{Vlumen}$ | `Vlumen` | intestinal lumen (inner part of intestine) | $1$ | l |  |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{some}_{\mathrm{ext}}$ | `some_ext` | S-omeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{some}$ | `some` | S-omeprazole (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{rome}_{\mathrm{ext}}$ | `rome_ext` | R-omeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{rome}$ | `rome` | R-omeprazole (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoh}_{\mathrm{ext}}$ | `omeoh_ext` | 5-hydroxyomeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoh}$ | `omeoh` | 5-hydroxyomeprazole (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{omesul}_{\mathrm{ext}}$ | `omesul_ext` | omeprazole sulfone (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{omesul}$ | `omesul` | omeprazole sulfone (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoth}_{\mathrm{ext}}$ | `omeoth_ext` | other omeprazole metabolites (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoth}$ | `omeoth` | other omeprazole metabolites (liver) | $\mathrm{Vli}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoth}_{\mathrm{lumen}}$ | `omeoth_lumen` | other omeprazole metabolites (intestinal lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $f_{\mathrm{cyp2c19}}$ | `f_cyp2c19` | activity of CYP2C19 (genotype, interactions) | $1$ | \- | ✓ |
| $f_{\mathrm{cyp3a4}}$ | `f_cyp3a4` | activity of CYP3A4 (interactions) | $1$ | \- | ✓ |
| $\mathrm{OMEIM}_{\mathrm{k}}$ | `OMEIM_k` | rate of the omeprazole exchange between plasma and liver | $10$ | 1/min | ✓ |
| $\mathrm{CYP2C19}_{\mathrm{Km}}$ | `CYP2C19_Km` | Km CYP2C19 omeprazole (apparent, total concentration) | $0.1$ | mmol/l | ✓ |
| $\mathrm{CYP3A4}_{\mathrm{Km}}$ | `CYP3A4_Km` | Km CYP3A4 omeprazole (apparent, total concentration) | $0.1$ | mmol/l | ✓ |
| $f_{\mathrm{some\_omeoh}}$ | `f_some_omeoh` | fraction 5-hydroxyomeprazole of the CYP2C19 metabolism of S-omeprazole | $0.1$ | \- | ✓ |
| $f_{\mathrm{rome\_cyp3a4\_omeoh}}$ | `f_rome_cyp3a4_omeoh` | fraction 5-hydroxyomeprazole of the CYP3A4 metabolism of R-omeprazole | $0.464385319357792$ | \- | ✓ |
| $\mathrm{cyp2c19}_{\mathrm{active}}$ | `cyp2c19_active` | fraction of active CYP2C19 | $1$ | \- |  |
| $\mathrm{CYP2C19}_{\mathrm{kdeg}}$ | `CYP2C19_kdeg` | degradation rate of CYP2C19 | $0.000444230769230769$ | 1/min | ✓ |
| $\mathrm{CYP2C19}_{\mathrm{kinact}}$ | `CYP2C19_kinact` | maximal inactivation rate of CYP2C19 by omeprazole | $0.0185056804400849$ | 1/min | ✓ |
| $\mathrm{CYP2C19}_{\mathrm{KI}}$ | `CYP2C19_KI` | concentration of half-maximal inactivation of CYP2C19 | $0.002$ | mmol/l | ✓ |
| $\mathrm{CYP2C19}_{\mathrm{Vmax\_some}}$ | `CYP2C19_Vmax_some` | Vmax CYP2C19 S-omeprazole | $0.0429809444865293$ | mmol/min/l | ✓ |
| $\mathrm{CYP2C19}_{\mathrm{Vmax\_rome}}$ | `CYP2C19_Vmax_rome` | Vmax CYP2C19 R-omeprazole | $0.0879250267535046$ | mmol/min/l | ✓ |
| $\mathrm{CYP3A4}_{\mathrm{Vmax\_some}}$ | `CYP3A4_Vmax_some` | Vmax CYP3A4 S-omeprazole | $0.00347040955371226$ | mmol/min/l | ✓ |
| $\mathrm{CYP3A4}_{\mathrm{Vmax\_rome}}$ | `CYP3A4_Vmax_rome` | Vmax CYP3A4 R-omeprazole | $0.00812409201505695$ | mmol/min/l | ✓ |
| $\mathrm{OMEOHEX}_{\mathrm{k}}$ | `OMEOHEX_k` | rate of the 5-hydroxyomeprazole release from the liver | $0.274485257726021$ | 1/min | ✓ |
| $\mathrm{OMEOHM}_{\mathrm{k}}$ | `OMEOHM_k` | rate of the 5-hydroxyomeprazole oxidation in the liver | $0.6$ | 1/min | ✓ |
| $\mathrm{OMEMEX}_{\mathrm{k}}$ | `OMEMEX_k` | rate of the metabolite exchange between plasma and liver | $10$ | 1/min | ✓ |
| $\mathrm{OMESUL2C19}_{\mathrm{k}}$ | `OMESUL2C19_k` | rate of the CYP2C19 metabolism of omeprazole sulfone | $0.0562470024857024$ | 1/min | ✓ |
| $\mathrm{OMESULM}_{\mathrm{k}}$ | `OMESULM_k` | rate of the CYP2C19 independent metabolism of omeprazole sulfone | $0.0629735593807952$ | 1/min | ✓ |
| $\mathrm{OMEOTHBIL}_{\mathrm{k}}$ | `OMEOTHBIL_k` | rate of the biliary excretion of the other metabolites | $0.00492138159856471$ | 1/min | ✓ |
| $\mathrm{cyp2c19}_{\mathrm{activity}}$ | `cyp2c19_activity` | activity of CYP2C19 |  | \- |  |
| $\mathrm{SOMECYP2C19}_{\mathrm{rate}}$ | `SOMECYP2C19_rate` | rate of the CYP2C19 metabolism of S-omeprazole |  | mmol/min |  |
| $\mathrm{ROMECYP3A4}_{\mathrm{rate}}$ | `ROMECYP3A4_rate` | rate of the CYP3A4 metabolism of R-omeprazole |  | mmol/min |  |

## Initial assignments and assignment rules

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{cyp2c19}_{\mathrm{activity}} &= f_{\mathrm{cyp2c19}} \cdot \mathrm{cyp2c19}_{\mathrm{active}} \\[1ex]
\mathrm{SOMECYP2C19}_{\mathrm{rate}} &= \frac{\mathrm{cyp2c19}_{\mathrm{activity}} \cdot \mathrm{CYP2C19}_{\mathrm{Vmax\_some}} \cdot \mathrm{Vli} \cdot \mathrm{some}}{\mathrm{CYP2C19}_{\mathrm{Km}} + \mathrm{some}} \\[1ex]
\mathrm{ROMECYP3A4}_{\mathrm{rate}} &= \frac{f_{\mathrm{cyp3a4}} \cdot \mathrm{CYP3A4}_{\mathrm{Vmax\_rome}} \cdot \mathrm{Vli} \cdot \mathrm{rome}}{\mathrm{CYP3A4}_{\mathrm{Km}} + \mathrm{rome}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{SOMEIM}}$ | `SOMEIM` | S-omeprazole exchange plasma and liver | $\mathrm{some}_{\mathrm{ext}} \rightleftharpoons \mathrm{some}$ |
| $v_{\mathrm{ROMEIM}}$ | `ROMEIM` | R-omeprazole exchange plasma and liver | $\mathrm{rome}_{\mathrm{ext}} \rightleftharpoons \mathrm{rome}$ |
| $v_{\mathrm{SOMECYP2C19}}$ | `SOMECYP2C19` | S-omeprazole to 5-O-desmethylomeprazole (CYP2C19) | $\mathrm{some} \longrightarrow \mathrm{omeoth}$ |
| $v_{\mathrm{SOMECYP2C19OH}}$ | `SOMECYP2C19OH` | S-omeprazole to 5-hydroxyomeprazole (CYP2C19) | $\mathrm{some} \longrightarrow \mathrm{omeoh}$ |
| $v_{\mathrm{ROMECYP2C19}}$ | `ROMECYP2C19` | R-omeprazole to 5-hydroxyomeprazole (CYP2C19) | $\mathrm{rome} \longrightarrow \mathrm{omeoh}$ |
| $v_{\mathrm{SOMECYP3A4}}$ | `SOMECYP3A4` | S-omeprazole to omeprazole sulfone (CYP3A4) | $\mathrm{some} \longrightarrow \mathrm{omesul}$ |
| $v_{\mathrm{ROMECYP3A4}}$ | `ROMECYP3A4` | R-omeprazole to omeprazole sulfone (CYP3A4) | $\mathrm{rome} \longrightarrow \mathrm{omesul}$ |
| $v_{\mathrm{ROMECYP3A4OH}}$ | `ROMECYP3A4OH` | R-omeprazole to 5-hydroxyomeprazole (CYP3A4) | $\mathrm{rome} \longrightarrow \mathrm{omeoh}$ |
| $v_{\mathrm{OMEOHEX}}$ | `OMEOHEX` | 5-hydroxyomeprazole release | $\mathrm{omeoh} \longrightarrow \mathrm{omeoh}_{\mathrm{ext}}$ |
| $v_{\mathrm{OMEOHM}}$ | `OMEOHM` | 5-hydroxyomeprazole oxidation | $\mathrm{omeoh} \longrightarrow \mathrm{omeoth}$ |
| $v_{\mathrm{OMESULEX}}$ | `OMESULEX` | omeprazole sulfone exchange liver and plasma | $\mathrm{omesul} \rightleftharpoons \mathrm{omesul}_{\mathrm{ext}}$ |
| $v_{\mathrm{OMESULM}}$ | `OMESULM` | omeprazole sulfone metabolism | $\mathrm{omesul} \longrightarrow \mathrm{omeoth}$ |
| $v_{\mathrm{OMEOTHEX}}$ | `OMEOTHEX` | other metabolites exchange liver and plasma | $\mathrm{omeoth} \rightleftharpoons \mathrm{omeoth}_{\mathrm{ext}}$ |
| $v_{\mathrm{OMEOTHBIL}}$ | `OMEOTHBIL` | other metabolites biliary excretion | $\mathrm{omeoth} \longrightarrow \mathrm{omeoth}_{\mathrm{lumen}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{SOMEIM}} &= \mathrm{OMEIM}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{some}_{\mathrm{ext}} - \mathrm{some}\right) \\[1ex]
v_{\mathrm{ROMEIM}} &= \mathrm{OMEIM}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{rome}_{\mathrm{ext}} - \mathrm{rome}\right) \\[1ex]
v_{\mathrm{SOMECYP2C19}} &= \mathopen{}\left(1 - f_{\mathrm{some\_omeoh}}\right) \cdot \mathrm{SOMECYP2C19}_{\mathrm{rate}} \\[1ex]
v_{\mathrm{SOMECYP2C19OH}} &= f_{\mathrm{some\_omeoh}} \cdot \mathrm{SOMECYP2C19}_{\mathrm{rate}} \\[1ex]
v_{\mathrm{ROMECYP2C19}} &= \frac{\mathrm{cyp2c19}_{\mathrm{activity}} \cdot \mathrm{CYP2C19}_{\mathrm{Vmax\_rome}} \cdot \mathrm{Vli} \cdot \mathrm{rome}}{\mathrm{CYP2C19}_{\mathrm{Km}} + \mathrm{rome}} \\[1ex]
v_{\mathrm{SOMECYP3A4}} &= \frac{f_{\mathrm{cyp3a4}} \cdot \mathrm{CYP3A4}_{\mathrm{Vmax\_some}} \cdot \mathrm{Vli} \cdot \mathrm{some}}{\mathrm{CYP3A4}_{\mathrm{Km}} + \mathrm{some}} \\[1ex]
v_{\mathrm{ROMECYP3A4}} &= \mathopen{}\left(1 - f_{\mathrm{rome\_cyp3a4\_omeoh}}\right) \cdot \mathrm{ROMECYP3A4}_{\mathrm{rate}} \\[1ex]
v_{\mathrm{ROMECYP3A4OH}} &= f_{\mathrm{rome\_cyp3a4\_omeoh}} \cdot \mathrm{ROMECYP3A4}_{\mathrm{rate}} \\[1ex]
v_{\mathrm{OMEOHEX}} &= \mathrm{OMEOHEX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathrm{omeoh} \\[1ex]
v_{\mathrm{OMEOHM}} &= \mathrm{OMEOHM}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathrm{omeoh} \\[1ex]
v_{\mathrm{OMESULEX}} &= \mathrm{OMEMEX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{omesul} - \mathrm{omesul}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{OMESULM}} &= \mathopen{}\left(\mathrm{cyp2c19}_{\mathrm{activity}} \cdot \mathrm{OMESUL2C19}_{\mathrm{k}} + \mathrm{OMESULM}_{\mathrm{k}}\right) \cdot \mathrm{Vli} \cdot \mathrm{omesul} \\[1ex]
v_{\mathrm{OMEOTHEX}} &= \mathrm{OMEMEX}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathopen{}\left(\mathrm{omeoth} - \mathrm{omeoth}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{OMEOTHBIL}} &= \mathrm{OMEOTHBIL}_{\mathrm{k}} \cdot \mathrm{Vli} \cdot \mathrm{omeoth}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{some}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{SOMEIM}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{some}}{\mathrm{d} t} &= \frac{v_{\mathrm{SOMEIM}} - v_{\mathrm{SOMECYP2C19}} - v_{\mathrm{SOMECYP2C19OH}} - v_{\mathrm{SOMECYP3A4}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{rome}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{ROMEIM}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{rome}}{\mathrm{d} t} &= \frac{v_{\mathrm{ROMEIM}} - v_{\mathrm{ROMECYP2C19}} - v_{\mathrm{ROMECYP3A4}} - v_{\mathrm{ROMECYP3A4OH}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoh}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{OMEOHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoh}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vli}} \Bigl( v_{\mathrm{SOMECYP2C19OH}} + v_{\mathrm{ROMECYP2C19}} + v_{\mathrm{ROMECYP3A4OH}} - v_{\mathrm{OMEOHEX}} \\
&\quad {} - v_{\mathrm{OMEOHM}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{omesul}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{OMESULEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omesul}}{\mathrm{d} t} &= \frac{v_{\mathrm{SOMECYP3A4}} + v_{\mathrm{ROMECYP3A4}} - v_{\mathrm{OMESULEX}} - v_{\mathrm{OMESULM}}}{\mathrm{Vli}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{OMEOTHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vli}} \Bigl( v_{\mathrm{SOMECYP2C19}} + v_{\mathrm{OMEOHM}} + v_{\mathrm{OMESULM}} - v_{\mathrm{OMEOTHEX}} \\
&\quad {} - v_{\mathrm{OMEOTHBIL}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{v_{\mathrm{OMEOTHBIL}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{cyp2c19}_{\mathrm{active}}}{\mathrm{d} t} &= \mathrm{CYP2C19}_{\mathrm{kdeg}} \cdot \mathopen{}\left(1 - \mathrm{cyp2c19}_{\mathrm{active}}\right) - \frac{\mathrm{CYP2C19}_{\mathrm{kinact}} \cdot \mathrm{cyp2c19}_{\mathrm{active}} \cdot \mathopen{}\left(\mathrm{some} + \mathrm{rome}\right)}{\mathrm{CYP2C19}_{\mathrm{KI}} + \mathrm{some} + \mathrm{rome}} \qquad \text{(rate rule)}
\end{aligned}
$$
