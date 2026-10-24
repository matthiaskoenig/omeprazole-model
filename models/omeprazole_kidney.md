# Model for the renal excretion of the omeprazole metabolites

Model `omeprazole_kidney`, SBML Level 3 Version 2, read from omeprazole\_kidney.xml, written by sbmlode 0.3.0.

Model for the renal excretion of the omeprazole metabolites

no omeprazole and no omeprazole sulfone are excreted in the urine

5-hydroxyomeprazole and the other metabolites are excreted from the plasma into the urine, with clearances relative to the glomerular filtration rate (GFR)

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
| $\mathrm{Vki}$ | `Vki` | kidney | $0.3$ | l | ✓ |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{omeoh}_{\mathrm{ext}}$ | `omeoh_ext` | 5-hydroxyomeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoh}_{\mathrm{urine}}$ | `omeoh_urine` | 5-hydroxyomeprazole (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{omeoth}_{\mathrm{ext}}$ | `omeoth_ext` | other omeprazole metabolites (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoth}_{\mathrm{urine}}$ | `omeoth_urine` | other omeprazole metabolites (urine) | $\mathrm{Vurine}$ |  | mmol | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $f_{\mathrm{renal\_function}}$ | `f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate (healthy) | $101$ | ml/min | ✓ |
| $\mathrm{OMEOHEX}_{\mathrm{f}}$ | `OMEOHEX_f` | renal clearance of 5-hydroxyomeprazole relative to the GFR | $1.83915259344785$ | \- | ✓ |
| $\mathrm{OMEOTHEX}_{\mathrm{f}}$ | `OMEOTHEX_f` | renal clearance of the other metabolites relative to the GFR | $0.256693039466168$ | \- | ✓ |
| $\mathrm{GFR}$ | `GFR` | glomerular filtration rate |  | ml/min |  |
| $\mathrm{OMEMETSEX}$ | `OMEMETSEX` | renal excretion rate of the omeprazole metabolites |  | mmol/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{omeoh}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{omeoth}_{\mathrm{urine}} &= 0 \cdot \mathrm{Vurine}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{GFR} &= f_{\mathrm{renal\_function}} \cdot \mathrm{GFR}_{\mathrm{base}} \\[1ex]
\mathrm{OMEMETSEX} &= v_{\mathrm{OMEOHEX}} + v_{\mathrm{OMEOTHEX}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation |
| --- | --- | --- | --- |
| $v_{\mathrm{OMEOHEX}}$ | `OMEOHEX` | 5-hydroxyomeprazole renal excretion | $\mathrm{omeoh}_{\mathrm{ext}} \longrightarrow \mathrm{omeoh}_{\mathrm{urine}}$ |
| $v_{\mathrm{OMEOTHEX}}$ | `OMEOTHEX` | other omeprazole metabolites renal excretion | $\mathrm{omeoth}_{\mathrm{ext}} \longrightarrow \mathrm{omeoth}_{\mathrm{urine}}$ |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{OMEOHEX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{OMEOHEX}_{\mathrm{f}} \cdot \mathrm{omeoh}_{\mathrm{ext}} \\[1ex]
v_{\mathrm{OMEOTHEX}} &= \mathrm{GFR} \cdot 0.001 \cdot \mathrm{OMEOTHEX}_{\mathrm{f}} \cdot \mathrm{omeoth}_{\mathrm{ext}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{omeoh}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{OMEOHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoh}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{OMEOHEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{OMEOTHEX}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{urine}}}{\mathrm{d} t} &= v_{\mathrm{OMEOTHEX}}
\end{aligned}
$$
