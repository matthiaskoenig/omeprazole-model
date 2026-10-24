# Model for omeprazole absorption in the intestine

Model `omeprazole_intestine`, SBML Level 3 Version 2, read from omeprazole\_intestine.xml, written by sbmlode 0.3.0.

Model for omeprazole absorption in the intestine and the stomach pH

Application forms

The oral dose is in the stomach (PODOSE\_&lt;sid&gt;, mg). The form is set by the switches f\_ec and f\_unprotected:

buffered solution or suspension (f\_ec = 0, f\_unprotected = 0): the dose enters the intestinal lumen with Ka\_dis\_ome, no degradation.

unprotected solution or suspension (f\_ec = 0, f\_unprotected = 1): the fraction F\_ome\_pH (depending on the stomach pH) enters the lumen, the rest is degraded by the gastric acid.

enteric-coated form (f\_ec = 1): the pellets leave the stomach with Ka\_ec\_ome (POEC\_&lt;sid&gt;, mg, pellets in the small intestine) and release omeprazole with the same rate into the lumen: a delayed release (two steps), no degradation.

food (fed = 1): the gastric emptying and the dissolution are slower by FED\_f\_dissolution, the fraction absorbed is FED\_f\_absorption.

Absorption

S- and R-omeprazole are absorbed with OMEABS\_k, completely (F\_ome\_abs = 1, no unchanged omeprazole in the feces); the bioavailability is the hepatic first pass.

Proton pumps and stomach pH

The model describes the change in stomach pH depending on omeprazole. A key component are the proton pumps in the parietal cells.

proton-pumps (PP) in gastric wall (gastric parietal cells, protein amount)

PP can be inhibited by omeprazole in the gastric wall; the activation processes from omeprazole to the active inhibitor in the gastric wall are not modeled in detail, but omeprazole was assumed to directly inhibit the PPs.

inhibition of PP converts the active in the inactive form

PP have a continuous turnover consisting of PP protein synthesis and PP degradation. The newly synthesized PP protein is active. Active and inactive PP are degraded identically.

pH in the stomach is modeled by calculating the amount of protons in the stomach.

PP (active) can secrete protons in the lumen (-&gt; decrease pH)

only omeprazole, but not the omeprazole metabolites were assumed to have proton pump inhibitor (PPI) activity.

PP (active) + OME -&gt; PP-OME (inactive) --synthesis--&gt; PP (active) PP (active) --degradation--&gt; PP-OME (inactive) --degradation--&gt;

pH calculation

pH is calculated as decimal logarithm of reciprocal hydrogen ion activity pH = - log10 (\[H+\]). \[H+\] is in \[mole/litre\] = \[mmole/litre\] in stomach volume.

The normal stomach pH values are: pH=1-3

gastric acid secretion

A typical adult human stomach will secrete about 1.5 liters of gastric acid daily.

Stomach volume is around 100 \[ml\]

PP pump H+ into \[gastric acid\]; \[gastric acid\] --1.5 \[l/day\]--&gt; \[stomach (100\[ml\])\] --1.5 \[l/day\]--&gt;.

1\.5 \[l/day\] = 1.5 \[l/day\]/(24\*60 \[min/day\])\* 1000 \[ml/l\] = 1.04 \[ml/min\]

acid output basal: 4.3 \[mmole (H+)/hr\] placebo =&gt; 4.3 mmole/100 ml = 0.043 mmole/ml = 43 mole/litre (in 1 hr). Delta pH (1 hr) = - log10(43) = -1.63

stimulated (food stimulated): \~ 8 \[mmole (H+)/hr\] = 70-80 \[mole/litre\]. Delta pH (1 hr) = - log10(350) = -1.88

stimulated (pentagastrin): 35 \[mmole (H+)/hr\] = 350 \[mole/litre\]. Delta pH (1 hr) = - log10(350) = -2.54

pH changes

Stomach pH should be \~1-3 pH at steady state and go up to \~7 pH at maximum PP inhibition at 80-90%.

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
| $\mathrm{Vext}$ | `Vext` | plasma | $1$ | l | ✓ |
| $\mathrm{Vlumen}$ | `Vlumen` | intestinal lumen (inner part of intestine) | $1.15425$ | l |  |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vstomach}$ | `Vstomach` | stomach | $1$ | l | ✓ |
| $\mathrm{Vpar}$ | `Vpar` | parietal cells | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{some}_{\mathrm{stomach}}$ | `some_stomach` | S-omeprazole (stomach) | $\mathrm{Vstomach}$ |  | mmol | amount, boundary |
| $\mathrm{some}_{\mathrm{lumen}}$ | `some_lumen` | S-omeprazole (intestinal lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{some}_{\mathrm{ext}}$ | `some_ext` | S-omeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{some}_{\mathrm{feces}}$ | `some_feces` | S-omeprazole (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{rome}_{\mathrm{stomach}}$ | `rome_stomach` | R-omeprazole (stomach) | $\mathrm{Vstomach}$ |  | mmol | amount, boundary |
| $\mathrm{rome}_{\mathrm{lumen}}$ | `rome_lumen` | R-omeprazole (intestinal lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{rome}_{\mathrm{ext}}$ | `rome_ext` | R-omeprazole (plasma) | $\mathrm{Vext}$ | $0$ | mmol/l | concentration |
| $\mathrm{rome}_{\mathrm{feces}}$ | `rome_feces` | R-omeprazole (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{omeoth}_{\mathrm{lumen}}$ | `omeoth_lumen` | other omeprazole metabolites (intestinal lumen) | $\mathrm{Vlumen}$ | $0$ | mmol/l | concentration |
| $\mathrm{omeoth}_{\mathrm{feces}}$ | `omeoth_feces` | other omeprazole metabolites (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{protons}_{\mathrm{stomach}}$ | `protons_stomach` | H+ (stomach gastric fluid) | $\mathrm{Vstomach}$ | $10$ | mmol/l | concentration |
| $\mathrm{pp}_{\mathrm{active}}$ | `pp_active` | proton pump (active) | $\mathrm{Vpar}$ | $1$ | \- | amount |
| $\mathrm{pp}_{\mathrm{inactive}}$ | `pp_inactive` | proton pump (inactive) | $\mathrm{Vpar}$ | $0$ | \- | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{pH}$ | `pH` | pH value stomach |  | \- |  |
| $\mathrm{Qstomach}$ | `Qstomach` | stomach fluid loss | $0.01$ | l/min | ✓ |
| $\mathrm{cf}_{\mathrm{species\_dimensionless}}$ | `cf_species_dimensionless` | dimensionless species conversion | $1$ | 1/mmol | ✓ |
| $f_{\mathrm{ec}}$ | `f_ec` | enteric-coated form (0 solution or suspension, 1 enteric-coated) | $0$ | \- | ✓ |
| $f_{\mathrm{unprotected}}$ | `f_unprotected` | unprotected solution (0 buffered or enteric-coated, 1 unprotected) | $0$ | \- | ✓ |
| $\mathrm{Ka}_{\mathrm{dis\_ome}}$ | `Ka_dis_ome` | rate of the gastric emptying of a solution | $30$ | 1/hr | ✓ |
| $\mathrm{Ka}_{\mathrm{ec\_ome}}$ | `Ka_ec_ome` | rate of the gastric emptying and the release of an enteric-coated form | $1.45474229513195$ | 1/hr | ✓ |
| $\mathrm{fed}$ | `fed` | fed state (0 fasted, 1 fed) | $0$ | \- | ✓ |
| $\mathrm{FED}_{\mathrm{f\_dissolution}}$ | `FED_f_dissolution` | fed effect on the gastric emptying and dissolution | $0.35$ | \- | ✓ |
| $\mathrm{FED}_{\mathrm{f\_absorption}}$ | `FED_f_absorption` | fed effect on the fraction absorbed | $0.65$ | \- | ✓ |
| $F_{\mathrm{ome\_abs}}$ | `F_ome_abs` | fraction absorbed omeprazole | $1$ | \- | ✓ |
| $\mathrm{OMEABS}_{\mathrm{k}}$ | `OMEABS_k` | rate of omeprazole absorption | $0.0909283349017812$ | 1/min | ✓ |
| $\mathrm{OMEOTHEXC}_{\mathrm{k}}$ | `OMEOTHEXC_k` | rate of the fecal excretion of the other metabolites | $0.0007$ | 1/min | ✓ |
| $\mathrm{Mr}_{\mathrm{ome}}$ | `Mr_ome` | Molecular weight omeprazole \[g/mole\] | $345.416$ | g/mol | ✓ |
| $F_{\mathrm{ome\_pH2}}$ | `F_ome_pH2` | fraction not degraded at pH 2 | $0.35$ | \- | ✓ |
| $F_{\mathrm{ome\_pH6}}$ | `F_ome_pH6` | fraction not degraded at pH 6 | $1$ | \- | ✓ |
| $F_{\mathrm{ome\_KpH}}$ | `F_ome_KpH` | midpoint of the pH effect on the degradation | $4$ | \- | ✓ |
| $F_{\mathrm{ome\_n}}$ | `F_ome_n` | Hill coefficient of the pH effect on the degradation | $2$ | \- | ✓ |
| $\mathrm{PODOSE}_{\mathrm{some}}$ | `PODOSE_some` | oral dose S-omeprazole in the stomach \[mg\] | $0$ | mg |  |
| $\mathrm{POEC}_{\mathrm{some}}$ | `POEC_some` | enteric-coated S-omeprazole in the small intestine \[mg\] | $0$ | mg |  |
| $\mathrm{PODOSE}_{\mathrm{rome}}$ | `PODOSE_rome` | oral dose R-omeprazole in the stomach \[mg\] | $0$ | mg |  |
| $\mathrm{POEC}_{\mathrm{rome}}$ | `POEC_rome` | enteric-coated R-omeprazole in the small intestine \[mg\] | $0$ | mg |  |
| $\mathrm{pp}_{\mathrm{rate\_k}}$ | `pp_rate_k` | Rate of proton secretion | $0.1$ | mmol/min | ✓ |
| $\mathrm{ppi}_{\mathrm{k}}$ | `ppi_k` | Inhibition rate PP | $5$ | l/min | ✓ |
| $\mathrm{pp}_{\mathrm{synthesis\_k}}$ | `pp_synthesis_k` | Synthesis rate PP | $0.0004$ | mmol/min | ✓ |
| $\mathrm{pp}_{\mathrm{degradation\_k}}$ | `pp_degradation_k` | Degradation rate PP | $0.0004$ | mmol/min | ✓ |
| $\mathrm{pp}_{\mathrm{total}}$ | `pp_total` | total proton pump |  | \- |  |
| $F_{\mathrm{ome\_pH}}$ | `F_ome_pH` | fraction of an unprotected solution not degraded in the stomach |  | \- |  |
| $F_{\mathrm{ome\_stomach}}$ | `F_ome_stomach` | fraction of a solution not degraded in the stomach |  | \- |  |
| $\mathrm{Ka}_{\mathrm{emptying}}$ | `Ka_emptying` | rate of the gastric emptying of the form |  | 1/hr |  |
| $F_{\mathrm{ome\_abs\_eff}}$ | `F_ome_abs_eff` | fraction absorbed omeprazole (fed state) |  | \- |  |
| $\mathrm{emptying}_{\mathrm{some}}$ | `emptying_some` | gastric emptying S-omeprazole |  | mmol/min |  |
| $\mathrm{absorption}_{\mathrm{some}}$ | `absorption_some` | absorption S-omeprazole |  | mmol/min |  |
| $\mathrm{emptying}_{\mathrm{rome}}$ | `emptying_rome` | gastric emptying R-omeprazole |  | mmol/min |  |
| $\mathrm{absorption}_{\mathrm{rome}}$ | `absorption_rome` | absorption R-omeprazole |  | mmol/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{some}_{\mathrm{stomach}} &= 0 \cdot \mathrm{Vstomach} \\[1ex]
\mathrm{some}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{rome}_{\mathrm{stomach}} &= 0 \cdot \mathrm{Vstomach} \\[1ex]
\mathrm{rome}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{omeoth}_{\mathrm{feces}} &= 0 \cdot \mathrm{Vfeces}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
\mathrm{pp}_{\mathrm{total}} &= \mathrm{pp}_{\mathrm{active}} + \mathrm{pp}_{\mathrm{inactive}} \\[1ex]
\mathrm{pH} &= -\log_{10}\mathopen{}\left(\frac{\mathrm{protons}_{\mathrm{stomach}}}{1000}\right) \\[1ex]
F_{\mathrm{ome\_pH}} &= F_{\mathrm{ome\_pH2}} + \frac{\mathopen{}\left(F_{\mathrm{ome\_pH6}} - F_{\mathrm{ome\_pH2}}\right) \cdot \mathopen{}\left(\max\mathopen{}\left(0, \mathrm{pH} - 2\right)\right)^{F_{\mathrm{ome\_n}}}}{\mathopen{}\left(\max\mathopen{}\left(0, \mathrm{pH} - 2\right)\right)^{F_{\mathrm{ome\_n}}} + F_{\mathrm{ome\_KpH}}^{F_{\mathrm{ome\_n}}}} \\[1ex]
F_{\mathrm{ome\_stomach}} &= 1 - f_{\mathrm{unprotected}} \cdot \mathopen{}\left(1 - F_{\mathrm{ome\_pH}}\right) \\[1ex]
\mathrm{Ka}_{\mathrm{emptying}} &= \mathopen{}\left(1 + \mathrm{fed} \cdot \mathopen{}\left(\mathrm{FED}_{\mathrm{f\_dissolution}} - 1\right)\right) \cdot \mathopen{}\left(\mathopen{}\left(1 - f_{\mathrm{ec}}\right) \cdot \mathrm{Ka}_{\mathrm{dis\_ome}} + f_{\mathrm{ec}} \cdot \mathrm{Ka}_{\mathrm{ec\_ome}}\right) \\[1ex]
F_{\mathrm{ome\_abs\_eff}} &= F_{\mathrm{ome\_abs}} \cdot \mathopen{}\left(1 + \mathrm{fed} \cdot \mathopen{}\left(\mathrm{FED}_{\mathrm{f\_absorption}} - 1\right)\right) \\[1ex]
\mathrm{emptying}_{\mathrm{some}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{emptying}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{some}}}{\mathrm{Mr}_{\mathrm{ome}}} \\[1ex]
\mathrm{absorption}_{\mathrm{some}} &= \mathrm{OMEABS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{some}_{\mathrm{lumen}} \\[1ex]
\mathrm{emptying}_{\mathrm{rome}} &= \frac{\frac{\mathrm{Ka}_{\mathrm{emptying}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{rome}}}{\mathrm{Mr}_{\mathrm{ome}}} \\[1ex]
\mathrm{absorption}_{\mathrm{rome}} &= \mathrm{OMEABS}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{rome}_{\mathrm{lumen}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation | Modifiers |
| --- | --- | --- | --- | --- |
| $v_{\mathrm{pp\_rate}}$ | `pp_rate` | Proton secretion by proton pump | $\varnothing \longrightarrow \mathrm{protons}_{\mathrm{stomach}}$ | $\mathrm{pp}_{\mathrm{active}}$ |
| $v_{\mathrm{gacid\_loss}}$ | `gacid_loss` | Gastric acid loss to intestine | $\mathrm{protons}_{\mathrm{stomach}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{ppi}}$ | `ppi` | PP inhibition | $\mathrm{pp}_{\mathrm{active}} \longrightarrow \mathrm{pp}_{\mathrm{inactive}}$ | $\mathrm{some}_{\mathrm{ext}}, \mathrm{rome}_{\mathrm{ext}}$ |
| $v_{\mathrm{pp\_synthesis}}$ | `pp_synthesis` | PP synthesis | $\varnothing \longrightarrow \mathrm{pp}_{\mathrm{active}}$ |  |
| $v_{\mathrm{pp\_active\_degradation}}$ | `pp_active_degradation` | degradation PP active | $\mathrm{pp}_{\mathrm{active}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{pp\_inactive\_degradation}}$ | `pp_inactive_degradation` | degradation PP inactive | $\mathrm{pp}_{\mathrm{inactive}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{OMEOTHEXC}}$ | `OMEOTHEXC` | excretion other metabolites (feces) | $\mathrm{omeoth}_{\mathrm{lumen}} \longrightarrow \mathrm{omeoth}_{\mathrm{feces}}$ |  |
| $v_{\mathrm{dissolution\_some}}$ | `dissolution_some` | gastric emptying of the solution S-omeprazole | $\mathrm{some}_{\mathrm{stomach}} \longrightarrow \mathrm{some}_{\mathrm{lumen}}$ |  |
| $v_{\mathrm{degradation\_some}}$ | `degradation_some` | acid degradation S-omeprazole | $\mathrm{some}_{\mathrm{stomach}} \longrightarrow \varnothing$ | $\mathrm{protons}_{\mathrm{stomach}}$ |
| $v_{\mathrm{release\_some}}$ | `release_some` | release from the enteric-coated pellets S-omeprazole | $\mathrm{some}_{\mathrm{stomach}} \longrightarrow \mathrm{some}_{\mathrm{lumen}}$ |  |
| $v_{\mathrm{SOMEABS}}$ | `SOMEABS` | absorption S-omeprazole | $\mathrm{some}_{\mathrm{lumen}} \longrightarrow \mathrm{some}_{\mathrm{ext}}$ |  |
| $v_{\mathrm{SOMEEXC}}$ | `SOMEEXC` | excretion S-omeprazole (feces) | $\mathrm{some}_{\mathrm{lumen}} \longrightarrow \mathrm{some}_{\mathrm{feces}}$ |  |
| $v_{\mathrm{dissolution\_rome}}$ | `dissolution_rome` | gastric emptying of the solution R-omeprazole | $\mathrm{rome}_{\mathrm{stomach}} \longrightarrow \mathrm{rome}_{\mathrm{lumen}}$ |  |
| $v_{\mathrm{degradation\_rome}}$ | `degradation_rome` | acid degradation R-omeprazole | $\mathrm{rome}_{\mathrm{stomach}} \longrightarrow \varnothing$ | $\mathrm{protons}_{\mathrm{stomach}}$ |
| $v_{\mathrm{release\_rome}}$ | `release_rome` | release from the enteric-coated pellets R-omeprazole | $\mathrm{rome}_{\mathrm{stomach}} \longrightarrow \mathrm{rome}_{\mathrm{lumen}}$ |  |
| $v_{\mathrm{ROMEABS}}$ | `ROMEABS` | absorption R-omeprazole | $\mathrm{rome}_{\mathrm{lumen}} \longrightarrow \mathrm{rome}_{\mathrm{ext}}$ |  |
| $v_{\mathrm{ROMEEXC}}$ | `ROMEEXC` | excretion R-omeprazole (feces) | $\mathrm{rome}_{\mathrm{lumen}} \longrightarrow \mathrm{rome}_{\mathrm{feces}}$ |  |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{pp\_rate}} &= \mathrm{pp}_{\mathrm{rate\_k}} \cdot 10^{\frac{-1.1}{\mathrm{pp}_{\mathrm{active}} + 0.1} + 1} \\[1ex]
v_{\mathrm{gacid\_loss}} &= \mathrm{Qstomach} \cdot \mathrm{protons}_{\mathrm{stomach}} \\[1ex]
v_{\mathrm{ppi}} &= \mathrm{ppi}_{\mathrm{k}} \cdot \mathrm{pp}_{\mathrm{active}} \cdot \mathopen{}\left(\mathrm{some}_{\mathrm{ext}} + \mathrm{rome}_{\mathrm{ext}}\right) \\[1ex]
v_{\mathrm{pp\_synthesis}} &= \mathrm{pp}_{\mathrm{synthesis\_k}} \\[1ex]
v_{\mathrm{pp\_active\_degradation}} &= \mathrm{pp}_{\mathrm{degradation\_k}} \cdot \mathrm{pp}_{\mathrm{active}} \\[1ex]
v_{\mathrm{pp\_inactive\_degradation}} &= \mathrm{pp}_{\mathrm{degradation\_k}} \cdot \mathrm{pp}_{\mathrm{inactive}} \\[1ex]
v_{\mathrm{OMEOTHEXC}} &= \mathrm{OMEOTHEXC}_{\mathrm{k}} \cdot \mathrm{Vlumen} \cdot \mathrm{omeoth}_{\mathrm{lumen}} \\[1ex]
v_{\mathrm{dissolution\_some}} &= \mathopen{}\left(1 - f_{\mathrm{ec}}\right) \cdot F_{\mathrm{ome\_stomach}} \cdot \mathrm{emptying}_{\mathrm{some}} \\[1ex]
v_{\mathrm{degradation\_some}} &= \mathopen{}\left(1 - f_{\mathrm{ec}}\right) \cdot \mathopen{}\left(1 - F_{\mathrm{ome\_stomach}}\right) \cdot \mathrm{emptying}_{\mathrm{some}} \\[1ex]
v_{\mathrm{release\_some}} &= \frac{\frac{\mathopen{}\left(1 + \mathrm{fed} \cdot \mathopen{}\left(\mathrm{FED}_{\mathrm{f\_dissolution}} - 1\right)\right) \cdot \mathrm{Ka}_{\mathrm{ec\_ome}}}{60} \cdot \mathrm{POEC}_{\mathrm{some}}}{\mathrm{Mr}_{\mathrm{ome}}} \\[1ex]
v_{\mathrm{SOMEABS}} &= F_{\mathrm{ome\_abs\_eff}} \cdot \mathrm{absorption}_{\mathrm{some}} \\[1ex]
v_{\mathrm{SOMEEXC}} &= \mathopen{}\left(1 - F_{\mathrm{ome\_abs\_eff}}\right) \cdot \mathrm{absorption}_{\mathrm{some}} \\[1ex]
v_{\mathrm{dissolution\_rome}} &= \mathopen{}\left(1 - f_{\mathrm{ec}}\right) \cdot F_{\mathrm{ome\_stomach}} \cdot \mathrm{emptying}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{degradation\_rome}} &= \mathopen{}\left(1 - f_{\mathrm{ec}}\right) \cdot \mathopen{}\left(1 - F_{\mathrm{ome\_stomach}}\right) \cdot \mathrm{emptying}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{release\_rome}} &= \frac{\frac{\mathopen{}\left(1 + \mathrm{fed} \cdot \mathopen{}\left(\mathrm{FED}_{\mathrm{f\_dissolution}} - 1\right)\right) \cdot \mathrm{Ka}_{\mathrm{ec\_ome}}}{60} \cdot \mathrm{POEC}_{\mathrm{rome}}}{\mathrm{Mr}_{\mathrm{ome}}} \\[1ex]
v_{\mathrm{ROMEABS}} &= F_{\mathrm{ome\_abs\_eff}} \cdot \mathrm{absorption}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{ROMEEXC}} &= \mathopen{}\left(1 - F_{\mathrm{ome\_abs\_eff}}\right) \cdot \mathrm{absorption}_{\mathrm{rome}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{some}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{v_{\mathrm{dissolution\_some}} + v_{\mathrm{release\_some}} - v_{\mathrm{SOMEABS}} - v_{\mathrm{SOMEEXC}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{some}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{SOMEABS}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{some}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{SOMEEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{rome}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{v_{\mathrm{dissolution\_rome}} + v_{\mathrm{release\_rome}} - v_{\mathrm{ROMEABS}} - v_{\mathrm{ROMEEXC}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{rome}_{\mathrm{ext}}}{\mathrm{d} t} &= \frac{v_{\mathrm{ROMEABS}}}{\mathrm{Vext}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{rome}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{ROMEEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{lumen}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{OMEOTHEXC}}}{\mathrm{Vlumen}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{omeoth}_{\mathrm{feces}}}{\mathrm{d} t} &= v_{\mathrm{OMEOTHEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{protons}_{\mathrm{stomach}}}{\mathrm{d} t} &= \frac{v_{\mathrm{pp\_rate}} - v_{\mathrm{gacid\_loss}}}{\mathrm{Vstomach}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{pp}_{\mathrm{active}}}{\mathrm{d} t} &= -\mathrm{cf}_{\mathrm{species\_dimensionless}} \cdot v_{\mathrm{ppi}} + \mathrm{cf}_{\mathrm{species\_dimensionless}} \cdot v_{\mathrm{pp\_synthesis}} - \mathrm{cf}_{\mathrm{species\_dimensionless}} \cdot v_{\mathrm{pp\_active\_degradation}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{pp}_{\mathrm{inactive}}}{\mathrm{d} t} &= \mathrm{cf}_{\mathrm{species\_dimensionless}} \cdot v_{\mathrm{ppi}} - \mathrm{cf}_{\mathrm{species\_dimensionless}} \cdot v_{\mathrm{pp\_inactive\_degradation}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{some}}}{\mathrm{d} t} &= -\mathrm{emptying}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{POEC}_{\mathrm{some}}}{\mathrm{d} t} &= \mathopen{}\left(f_{\mathrm{ec}} \cdot \mathrm{emptying}_{\mathrm{some}} - v_{\mathrm{release\_some}}\right) \cdot \mathrm{Mr}_{\mathrm{ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{rome}}}{\mathrm{d} t} &= -\mathrm{emptying}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{POEC}_{\mathrm{rome}}}{\mathrm{d} t} &= \mathopen{}\left(f_{\mathrm{ec}} \cdot \mathrm{emptying}_{\mathrm{rome}} - v_{\mathrm{release\_rome}}\right) \cdot \mathrm{Mr}_{\mathrm{ome}} \qquad \text{(rate rule)}
\end{aligned}
$$
