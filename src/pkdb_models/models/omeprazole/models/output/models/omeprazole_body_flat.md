# PBPK/PD model of omeprazole

Model `omeprazole_body`, SBML Level 3 Version 2, read from omeprazole\_body\_flat.xml, written by sbmlode 0.3.0.

Whole-body model of omeprazole

PBPK/PD model of omeprazole with its enantiomers S-omeprazole and R-omeprazole, their metabolism in the liver by CYP2C19 and CYP3A4, the renal and biliary excretion of the metabolites, the absorption of the application forms and the inhibition of the gastric proton pumps.

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
| $\mathrm{Vre}$ | `Vre` | rest of body |  | l |  |
| $\mathrm{Vgu}$ | `Vgu` | gut |  | l |  |
| $\mathrm{Vki}$ | `Vki` | kidney |  | l |  |
| $\mathrm{Vli}$ | `Vli` | liver |  | l |  |
| $\mathrm{Vlu}$ | `Vlu` | lung |  | l |  |
| $\mathrm{Vsp}$ | `Vsp` | spleen |  | l |  |
| $\mathrm{Vpa}$ | `Vpa` | pancreas |  | l |  |
| $\mathrm{Vve}$ | `Vve` | venous plasma |  | l |  |
| $\mathrm{Var}$ | `Var` | arterial plasma |  | l |  |
| $\mathrm{Vpo}$ | `Vpo` | portal plasma |  | l |  |
| $\mathrm{Vhv}$ | `Vhv` | hepatic venous plasma |  | l |  |
| $\mathrm{Vurine}$ | `Vurine` | urine | $1$ | l | ✓ |
| $\mathrm{Vfeces}$ | `Vfeces` | feces | $1$ | l | ✓ |
| $\mathrm{Vgu}_{\mathrm{tissue}}$ | `Vgu_tissue` | gut tissue |  | l |  |
| $\mathrm{Vgu}_{\mathrm{plasma}}$ | `Vgu_plasma` | gut plasma |  | l |  |
| $\mathrm{Vki}_{\mathrm{tissue}}$ | `Vki_tissue` | kidney tissue |  | l |  |
| $\mathrm{Vki}_{\mathrm{plasma}}$ | `Vki_plasma` | kidney plasma |  | l |  |
| $\mathrm{Vli}_{\mathrm{tissue}}$ | `Vli_tissue` | liver tissue |  | l |  |
| $\mathrm{Vli}_{\mathrm{plasma}}$ | `Vli_plasma` | liver plasma |  | l |  |
| $\mathrm{Vlu}_{\mathrm{tissue}}$ | `Vlu_tissue` | lung tissue |  | l |  |
| $\mathrm{Vlu}_{\mathrm{plasma}}$ | `Vlu_plasma` | lung plasma |  | l |  |
| $\mathrm{Vpa}_{\mathrm{tissue}}$ | `Vpa_tissue` | pancreas tissue |  | l |  |
| $\mathrm{Vpa}_{\mathrm{plasma}}$ | `Vpa_plasma` | pancreas plasma |  | l |  |
| $\mathrm{Vsp}_{\mathrm{tissue}}$ | `Vsp_tissue` | spleen tissue |  | l |  |
| $\mathrm{Vsp}_{\mathrm{plasma}}$ | `Vsp_plasma` | spleen plasma |  | l |  |
| $\mathrm{Vre}_{\mathrm{tissue}}$ | `Vre_tissue` | rest tissue |  | l |  |
| $\mathrm{Vre}_{\mathrm{plasma}}$ | `Vre_plasma` | rest plasma |  | l |  |
| $\mathrm{GU}_{\mathrm{\_Vstomach}}$ | `GU__Vstomach` | stomach | $1$ | l | ✓ |
| $\mathrm{GU}_{\mathrm{\_Vpar}}$ | `GU__Vpar` | parietal cells | $1$ | l | ✓ |

## Species

| Symbol | Id | Name | Compartment | Value | Unit | Properties |
| --- | --- | --- | --- | --- | --- | --- |
| $\mathrm{Cgu}_{\mathrm{plasma\_some}}$ | `Cgu_plasma_some` | S-omeprazole (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{plasma\_some}}$ | `Cki_plasma_some` | S-omeprazole (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_some}}$ | `Cli_plasma_some` | S-omeprazole (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_some}}$ | `Clu_plasma_some` | S-omeprazole (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{plasma\_some}}$ | `Cpa_plasma_some` | S-omeprazole (pancreas plasma) | $\mathrm{Vpa}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{plasma\_some}}$ | `Csp_plasma_some` | S-omeprazole (spleen plasma) | $\mathrm{Vsp}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_some}}$ | `Cre_plasma_some` | S-omeprazole (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{some}}$ | `Car_some` | S-omeprazole (arterial plasma plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{some}}$ | `Cve_some` | S-omeprazole (venous plasma plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{some}}$ | `Cpo_some` | S-omeprazole (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{some}}$ | `Chv_some` | S-omeprazole (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{some}}$ | `Clu_some` | S-omeprazole (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{some}}$ | `Cpa_some` | S-omeprazole (pancreas tissue) | $\mathrm{Vpa}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{some}}$ | `Csp_some` | S-omeprazole (spleen tissue) | $\mathrm{Vsp}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{some}}$ | `Cre_some` | S-omeprazole (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_rome}}$ | `Cgu_plasma_rome` | R-omeprazole (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{plasma\_rome}}$ | `Cki_plasma_rome` | R-omeprazole (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_rome}}$ | `Cli_plasma_rome` | R-omeprazole (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_rome}}$ | `Clu_plasma_rome` | R-omeprazole (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{plasma\_rome}}$ | `Cpa_plasma_rome` | R-omeprazole (pancreas plasma) | $\mathrm{Vpa}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{plasma\_rome}}$ | `Csp_plasma_rome` | R-omeprazole (spleen plasma) | $\mathrm{Vsp}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_rome}}$ | `Cre_plasma_rome` | R-omeprazole (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{rome}}$ | `Car_rome` | R-omeprazole (arterial plasma plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{rome}}$ | `Cve_rome` | R-omeprazole (venous plasma plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{rome}}$ | `Cpo_rome` | R-omeprazole (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{rome}}$ | `Chv_rome` | R-omeprazole (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{rome}}$ | `Clu_rome` | R-omeprazole (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{rome}}$ | `Cpa_rome` | R-omeprazole (pancreas tissue) | $\mathrm{Vpa}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{rome}}$ | `Csp_rome` | R-omeprazole (spleen tissue) | $\mathrm{Vsp}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{rome}}$ | `Cre_rome` | R-omeprazole (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_omeoh}}$ | `Cgu_plasma_omeoh` | 5-hydroxyomeprazole (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{plasma\_omeoh}}$ | `Cki_plasma_omeoh` | 5-hydroxyomeprazole (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_omeoh}}$ | `Cli_plasma_omeoh` | 5-hydroxyomeprazole (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_omeoh}}$ | `Clu_plasma_omeoh` | 5-hydroxyomeprazole (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{plasma\_omeoh}}$ | `Cpa_plasma_omeoh` | 5-hydroxyomeprazole (pancreas plasma) | $\mathrm{Vpa}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{plasma\_omeoh}}$ | `Csp_plasma_omeoh` | 5-hydroxyomeprazole (spleen plasma) | $\mathrm{Vsp}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_omeoh}}$ | `Cre_plasma_omeoh` | 5-hydroxyomeprazole (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{omeoh}}$ | `Car_omeoh` | 5-hydroxyomeprazole (arterial plasma plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{omeoh}}$ | `Cve_omeoh` | 5-hydroxyomeprazole (venous plasma plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{omeoh}}$ | `Cpo_omeoh` | 5-hydroxyomeprazole (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{omeoh}}$ | `Chv_omeoh` | 5-hydroxyomeprazole (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{omeoh}}$ | `Clu_omeoh` | 5-hydroxyomeprazole (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{omeoh}}$ | `Cpa_omeoh` | 5-hydroxyomeprazole (pancreas tissue) | $\mathrm{Vpa}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{omeoh}}$ | `Csp_omeoh` | 5-hydroxyomeprazole (spleen tissue) | $\mathrm{Vsp}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{omeoh}}$ | `Cre_omeoh` | 5-hydroxyomeprazole (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_omesul}}$ | `Cgu_plasma_omesul` | omeprazole sulfone (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{plasma\_omesul}}$ | `Cki_plasma_omesul` | omeprazole sulfone (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_omesul}}$ | `Cli_plasma_omesul` | omeprazole sulfone (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_omesul}}$ | `Clu_plasma_omesul` | omeprazole sulfone (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{plasma\_omesul}}$ | `Cpa_plasma_omesul` | omeprazole sulfone (pancreas plasma) | $\mathrm{Vpa}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{plasma\_omesul}}$ | `Csp_plasma_omesul` | omeprazole sulfone (spleen plasma) | $\mathrm{Vsp}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_omesul}}$ | `Cre_plasma_omesul` | omeprazole sulfone (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{omesul}}$ | `Car_omesul` | omeprazole sulfone (arterial plasma plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{omesul}}$ | `Cve_omesul` | omeprazole sulfone (venous plasma plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{omesul}}$ | `Cpo_omesul` | omeprazole sulfone (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{omesul}}$ | `Chv_omesul` | omeprazole sulfone (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{omesul}}$ | `Clu_omesul` | omeprazole sulfone (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{omesul}}$ | `Cpa_omesul` | omeprazole sulfone (pancreas tissue) | $\mathrm{Vpa}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{omesul}}$ | `Csp_omesul` | omeprazole sulfone (spleen tissue) | $\mathrm{Vsp}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{omesul}}$ | `Cre_omesul` | omeprazole sulfone (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{plasma\_omeoth}}$ | `Cgu_plasma_omeoth` | other omeprazole metabolites (gut plasma) | $\mathrm{Vgu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cki}_{\mathrm{plasma\_omeoth}}$ | `Cki_plasma_omeoth` | other omeprazole metabolites (kidney plasma) | $\mathrm{Vki}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cli}_{\mathrm{plasma\_omeoth}}$ | `Cli_plasma_omeoth` | other omeprazole metabolites (liver plasma) | $\mathrm{Vli}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{plasma\_omeoth}}$ | `Clu_plasma_omeoth` | other omeprazole metabolites (lung plasma) | $\mathrm{Vlu}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{plasma\_omeoth}}$ | `Cpa_plasma_omeoth` | other omeprazole metabolites (pancreas plasma) | $\mathrm{Vpa}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{plasma\_omeoth}}$ | `Csp_plasma_omeoth` | other omeprazole metabolites (spleen plasma) | $\mathrm{Vsp}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{plasma\_omeoth}}$ | `Cre_plasma_omeoth` | other omeprazole metabolites (rest plasma) | $\mathrm{Vre}_{\mathrm{plasma}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Car}_{\mathrm{omeoth}}$ | `Car_omeoth` | other omeprazole metabolites (arterial plasma plasma) | $\mathrm{Var}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{omeoth}}$ | `Cve_omeoth` | other omeprazole metabolites (venous plasma plasma) | $\mathrm{Vve}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpo}_{\mathrm{omeoth}}$ | `Cpo_omeoth` | other omeprazole metabolites (portal vein plasma) | $\mathrm{Vpo}$ | $0$ | mmol/l | concentration |
| $\mathrm{Chv}_{\mathrm{omeoth}}$ | `Chv_omeoth` | other omeprazole metabolites (hepatic vein plasma) | $\mathrm{Vhv}$ | $0$ | mmol/l | concentration |
| $\mathrm{Clu}_{\mathrm{omeoth}}$ | `Clu_omeoth` | other omeprazole metabolites (lung tissue) | $\mathrm{Vlu}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cpa}_{\mathrm{omeoth}}$ | `Cpa_omeoth` | other omeprazole metabolites (pancreas tissue) | $\mathrm{Vpa}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Csp}_{\mathrm{omeoth}}$ | `Csp_omeoth` | other omeprazole metabolites (spleen tissue) | $\mathrm{Vsp}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cre}_{\mathrm{omeoth}}$ | `Cre_omeoth` | other omeprazole metabolites (rest tissue) | $\mathrm{Vre}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{omeoh}}$ | `Aurine_omeoh` | 5-hydroxyomeprazole (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Aurine}_{\mathrm{omeoth}}$ | `Aurine_omeoth` | other omeprazole metabolites (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{some}}$ | `Afeces_some` | S-omeprazole (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{rome}}$ | `Afeces_rome` | R-omeprazole (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{omeoth}}$ | `Afeces_omeoth` | other omeprazole metabolites (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Cgu}_{\mathrm{some}}$ | `Cgu_some` | S-omeprazole (intestinal lumen) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{rome}}$ | `Cgu_rome` | R-omeprazole (intestinal lumen) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cgu}_{\mathrm{omeoth}}$ | `Cgu_omeoth` | other omeprazole metabolites (intestinal lumen) | $\mathrm{Vgu}$ | $0$ | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{ome}}$ | `Cve_ome` | omeprazole (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{omemets}}$ | `Cve_omemets` | omeprazole metabolites (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{Cve}_{\mathrm{ometot}}$ | `Cve_ometot` | omeprazole and its metabolites (venous plasma) | $\mathrm{Vve}$ |  | mmol/l | concentration |
| $\mathrm{Aurine}_{\mathrm{omemets}}$ | `Aurine_omemets` | omeprazole metabolites (urine) | $\mathrm{Vurine}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{omemets}}$ | `Afeces_omemets` | omeprazole metabolites (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{Afeces}_{\mathrm{ome}}$ | `Afeces_ome` | omeprazole (feces) | $\mathrm{Vfeces}$ |  | mmol | amount |
| $\mathrm{LI}_{\mathrm{\_some}}$ | `LI__some` | S-omeprazole (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_rome}}$ | `LI__rome` | R-omeprazole (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_omeoh}}$ | `LI__omeoh` | 5-hydroxyomeprazole (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_omesul}}$ | `LI__omesul` | omeprazole sulfone (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{LI}_{\mathrm{\_omeoth}}$ | `LI__omeoth` | other omeprazole metabolites (liver) | $\mathrm{Vli}_{\mathrm{tissue}}$ | $0$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_some\_stomach}}$ | `GU__some_stomach` | S-omeprazole (stomach) | $\mathrm{GU}_{\mathrm{\_Vstomach}}$ |  | mmol | amount, boundary |
| $\mathrm{GU}_{\mathrm{\_rome\_stomach}}$ | `GU__rome_stomach` | R-omeprazole (stomach) | $\mathrm{GU}_{\mathrm{\_Vstomach}}$ |  | mmol | amount, boundary |
| $\mathrm{GU}_{\mathrm{\_protons\_stomach}}$ | `GU__protons_stomach` | H+ (stomach gastric fluid) | $\mathrm{GU}_{\mathrm{\_Vstomach}}$ | $10$ | mmol/l | concentration |
| $\mathrm{GU}_{\mathrm{\_pp\_active}}$ | `GU__pp_active` | proton pump (active) | $\mathrm{GU}_{\mathrm{\_Vpar}}$ | $1$ | \- | amount |
| $\mathrm{GU}_{\mathrm{\_pp\_inactive}}$ | `GU__pp_inactive` | proton pump (inactive) | $\mathrm{GU}_{\mathrm{\_Vpar}}$ | $0$ | \- | amount |

## Parameters

| Symbol | Id | Name | Value | Unit | Constant |
| --- | --- | --- | --- | --- | :---: |
| $\mathrm{BW}$ | `BW` | body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{BW}_{\mathrm{ref}}$ | `BW_ref` | reference body weight \[kg\] | $75$ | kg | ✓ |
| $\mathrm{HEIGHT}$ | `HEIGHT` | height \[cm\] | $170$ | cm | ✓ |
| $\mathrm{BSA}$ | `BSA` | body surface area \[m^2\] |  | m<sup>2</sup> |  |
| $\mathrm{COBW}$ | `COBW` | cardiac output per bodyweight \[ml/s/kg\] | $1.548$ | ml/s/kg | ✓ |
| $\mathrm{CO}$ | `CO` | cardiac output \[ml/s\] |  | ml/s |  |
| $\mathrm{QC}$ | `QC` | cardiac output \[L/min\] |  | l/min |  |
| $\mathrm{pH}$ | `pH` | pH value stomach |  | \- |  |
| $\mathrm{Fblood}$ | `Fblood` | blood fraction of organ volume | $0.02$ | \- |  |
| $\mathrm{HCT}$ | `HCT` | hematocrit | $0.51$ | \- | ✓ |
| $\mathrm{FVgu}$ | `FVgu` | gut fractional tissue volume | $0.0171$ | l/kg | ✓ |
| $\mathrm{FVki}$ | `FVki` | kidney fractional tissue volume | $0.0044$ | l/kg | ✓ |
| $\mathrm{FVli}$ | `FVli` | liver fractional tissue volume | $0.021$ | l/kg | ✓ |
| $\mathrm{FVlu}$ | `FVlu` | lung fractional tissue volume | $0.0076$ | l/kg | ✓ |
| $\mathrm{FVsp}$ | `FVsp` | spleen fractional tissue volume | $0.0026$ | l/kg | ✓ |
| $\mathrm{FVpa}$ | `FVpa` | pancreas fractional tissue volume | $0.01$ | l/kg | ✓ |
| $\mathrm{FVre}$ | `FVre` | rest of body fractional tissue volume |  | l/kg |  |
| $\mathrm{FVve}$ | `FVve` | venous fractional tissue volume | $0.0514$ | l/kg | ✓ |
| $\mathrm{FVar}$ | `FVar` | arterial fractional tissue volume | $0.0257$ | l/kg | ✓ |
| $\mathrm{FVpo}$ | `FVpo` | portal fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FVhv}$ | `FVhv` | hepatic venous fractional tissue volume | $0.001$ | l/kg | ✓ |
| $\mathrm{FQgu}$ | `FQgu` | gut fractional tissue blood flow | $0.146$ | \- | ✓ |
| $\mathrm{FQki}$ | `FQki` | kidney fractional tissue blood flow | $0.19$ | \- | ✓ |
| $\mathrm{FQh}$ | `FQh` | hepatic (venous side) fractional tissue blood flow | $0.215$ | \- | ✓ |
| $\mathrm{FQlu}$ | `FQlu` | lung fractional tissue blood flow | $1$ | \- | ✓ |
| $\mathrm{FQsp}$ | `FQsp` | spleen fractional tissue blood flow | $0.017$ | \- | ✓ |
| $\mathrm{FQpa}$ | `FQpa` | pancreas fractional tissue blood flow | $0.017$ | \- | ✓ |
| $\mathrm{FQre}$ | `FQre` | rest of body fractional tissue blood flow |  | \- |  |
| $f_{\mathrm{cirrhosis}}$ | `f_cirrhosis` | severity of cirrhosis \[0, 0.95\] | $0$ | \- | ✓ |
| $f_{\mathrm{shunts}}$ | `f_shunts` | fraction of portal venous blood shunted by the liver |  | \- |  |
| $f_{\mathrm{tissue\_loss}}$ | `f_tissue_loss` | fraction of lost parenchymal liver volume |  | \- |  |
| $f_{\mathrm{GFR\_Qki}}$ | `f_GFR_Qki` | relationship GFR and Qki | $76.3105006271061$ | ml/l | ✓ |
| $\mathrm{GFR}_{\mathrm{base}}$ | `GFR_base` | glomerular filtration rate (healthy) |  | ml/min |  |
| $\mathrm{ftissue}_{\mathrm{ome}}$ | `ftissue_ome` | tissue distribution omeprazole | $100$ | l/min | ✓ |
| $\mathrm{Kp}_{\mathrm{ome}}$ | `Kp_ome` | tissue/plasma partition coefficient omeprazole | $0.166018345241319$ | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{some}}$ | `Mr_some` | Molecular weight some \[g/mole\] | $345.416$ | g/mol | ✓ |
| $\mathrm{BP}_{\mathrm{some}}$ | `BP_some` | blood to plasma ratio some | $0.6$ | \- | ✓ |
| $\mathrm{IVDOSE}_{\mathrm{some}}$ | `IVDOSE_some` | IV bolus dose some \[mg\] | $0$ | mg |  |
| $\mathrm{ti}_{\mathrm{some}}$ | `ti_some` | injection time some \[s\] | $10$ | s | ✓ |
| $\mathrm{Ki}_{\mathrm{some}}$ | `Ki_some` | Ki \[1/min\] injection some |  | 1/min |  |
| $\mathrm{Ri}_{\mathrm{some}}$ | `Ri_some` | Ri \[mg/min\] rate of infusion some | $0$ | mg/min | ✓ |
| $\mathrm{cum}_{\mathrm{dose\_some}}$ | `cum_dose_some` | Cumulative dose due to infusion some | $0$ | mg |  |
| $\mathrm{PODOSE}_{\mathrm{some}}$ | `PODOSE_some` | oral dose some \[mg\] | $0$ | mg |  |
| $\mathrm{Mr}_{\mathrm{rome}}$ | `Mr_rome` | Molecular weight rome \[g/mole\] | $345.416$ | g/mol | ✓ |
| $\mathrm{BP}_{\mathrm{rome}}$ | `BP_rome` | blood to plasma ratio rome | $0.6$ | \- | ✓ |
| $\mathrm{IVDOSE}_{\mathrm{rome}}$ | `IVDOSE_rome` | IV bolus dose rome \[mg\] | $0$ | mg |  |
| $\mathrm{ti}_{\mathrm{rome}}$ | `ti_rome` | injection time rome \[s\] | $10$ | s | ✓ |
| $\mathrm{Ki}_{\mathrm{rome}}$ | `Ki_rome` | Ki \[1/min\] injection rome |  | 1/min |  |
| $\mathrm{Ri}_{\mathrm{rome}}$ | `Ri_rome` | Ri \[mg/min\] rate of infusion rome | $0$ | mg/min | ✓ |
| $\mathrm{cum}_{\mathrm{dose\_rome}}$ | `cum_dose_rome` | Cumulative dose due to infusion rome | $0$ | mg |  |
| $\mathrm{PODOSE}_{\mathrm{rome}}$ | `PODOSE_rome` | oral dose rome \[mg\] | $0$ | mg |  |
| $\mathrm{Mr}_{\mathrm{omeoh}}$ | `Mr_omeoh` | Molecular weight omeoh \[g/mole\] | $361.415$ | g/mol | ✓ |
| $\mathrm{BP}_{\mathrm{omeoh}}$ | `BP_omeoh` | blood to plasma ratio omeoh | $1$ | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{omesul}}$ | `Mr_omesul` | Molecular weight omesul \[g/mole\] | $361.42$ | g/mol | ✓ |
| $\mathrm{BP}_{\mathrm{omesul}}$ | `BP_omesul` | blood to plasma ratio omesul | $1$ | \- | ✓ |
| $\mathrm{Mr}_{\mathrm{omeoth}}$ | `Mr_omeoth` | Molecular weight omeoth \[g/mole\] | $375.4$ | g/mol | ✓ |
| $\mathrm{BP}_{\mathrm{omeoth}}$ | `BP_omeoth` | blood to plasma ratio omeoth | $1$ | \- | ✓ |
| $\mathrm{Qgu}$ | `Qgu` | gut blood flow |  | l/min |  |
| $\mathrm{Qki}$ | `Qki` | kidney blood flow |  | l/min |  |
| $\mathrm{Qh}$ | `Qh` | hepatic (venous side) blood flow |  | l/min |  |
| $\mathrm{Qha}$ | `Qha` | hepatic artery blood flow |  | l/min |  |
| $\mathrm{Qlu}$ | `Qlu` | lung blood flow |  | l/min |  |
| $\mathrm{Qsp}$ | `Qsp` | spleen blood flow |  | l/min |  |
| $\mathrm{Qpa}$ | `Qpa` | pancreas blood flow |  | l/min |  |
| $\mathrm{Qre}$ | `Qre` | rest of body blood flow |  | l/min |  |
| $\mathrm{Qpo}$ | `Qpo` | portal blood flow |  | l/min |  |
| $\mathrm{Agu}_{\mathrm{plasma\_some}}$ | `Agu_plasma_some` | S-omeprazole amount (gut plasma) |  | mmol |  |
| $\mathrm{Xgu}_{\mathrm{plasma\_some}}$ | `Xgu_plasma_some` | S-omeprazole mass (gut plasma) |  | mg |  |
| $\mathrm{Mgu}_{\mathrm{plasma\_some}}$ | `Mgu_plasma_some` | S-omeprazole mass concentration (gut plasma) |  | mg/l |  |
| $\mathrm{Aki}_{\mathrm{plasma\_some}}$ | `Aki_plasma_some` | S-omeprazole amount (kidney plasma) |  | mmol |  |
| $\mathrm{Xki}_{\mathrm{plasma\_some}}$ | `Xki_plasma_some` | S-omeprazole mass (kidney plasma) |  | mg |  |
| $\mathrm{Mki}_{\mathrm{plasma\_some}}$ | `Mki_plasma_some` | S-omeprazole mass concentration (kidney plasma) |  | mg/l |  |
| $\mathrm{Ali}_{\mathrm{plasma\_some}}$ | `Ali_plasma_some` | S-omeprazole amount (liver plasma) |  | mmol |  |
| $\mathrm{Xli}_{\mathrm{plasma\_some}}$ | `Xli_plasma_some` | S-omeprazole mass (liver plasma) |  | mg |  |
| $\mathrm{Mli}_{\mathrm{plasma\_some}}$ | `Mli_plasma_some` | S-omeprazole mass concentration (liver plasma) |  | mg/l |  |
| $\mathrm{Alu}_{\mathrm{plasma\_some}}$ | `Alu_plasma_some` | S-omeprazole amount (lung plasma) |  | mmol |  |
| $\mathrm{Xlu}_{\mathrm{plasma\_some}}$ | `Xlu_plasma_some` | S-omeprazole mass (lung plasma) |  | mg |  |
| $\mathrm{Mlu}_{\mathrm{plasma\_some}}$ | `Mlu_plasma_some` | S-omeprazole mass concentration (lung plasma) |  | mg/l |  |
| $\mathrm{Apa}_{\mathrm{plasma\_some}}$ | `Apa_plasma_some` | S-omeprazole amount (pancreas plasma) |  | mmol |  |
| $\mathrm{Xpa}_{\mathrm{plasma\_some}}$ | `Xpa_plasma_some` | S-omeprazole mass (pancreas plasma) |  | mg |  |
| $\mathrm{Mpa}_{\mathrm{plasma\_some}}$ | `Mpa_plasma_some` | S-omeprazole mass concentration (pancreas plasma) |  | mg/l |  |
| $\mathrm{Asp}_{\mathrm{plasma\_some}}$ | `Asp_plasma_some` | S-omeprazole amount (spleen plasma) |  | mmol |  |
| $\mathrm{Xsp}_{\mathrm{plasma\_some}}$ | `Xsp_plasma_some` | S-omeprazole mass (spleen plasma) |  | mg |  |
| $\mathrm{Msp}_{\mathrm{plasma\_some}}$ | `Msp_plasma_some` | S-omeprazole mass concentration (spleen plasma) |  | mg/l |  |
| $\mathrm{Are}_{\mathrm{plasma\_some}}$ | `Are_plasma_some` | S-omeprazole amount (rest plasma) |  | mmol |  |
| $\mathrm{Xre}_{\mathrm{plasma\_some}}$ | `Xre_plasma_some` | S-omeprazole mass (rest plasma) |  | mg |  |
| $\mathrm{Mre}_{\mathrm{plasma\_some}}$ | `Mre_plasma_some` | S-omeprazole mass concentration (rest plasma) |  | mg/l |  |
| $\mathrm{Aar}_{\mathrm{some}}$ | `Aar_some` | S-omeprazole amount (arterial plasma plasma) |  | mmol |  |
| $\mathrm{Xar}_{\mathrm{some}}$ | `Xar_some` | S-omeprazole mass (arterial plasma plasma) |  | mg |  |
| $\mathrm{Mar}_{\mathrm{some}}$ | `Mar_some` | S-omeprazole mass concentration (arterial plasma plasma) |  | mg/l |  |
| $\mathrm{Ave}_{\mathrm{some}}$ | `Ave_some` | S-omeprazole amount (venous plasma plasma) |  | mmol |  |
| $\mathrm{Xve}_{\mathrm{some}}$ | `Xve_some` | S-omeprazole mass (venous plasma plasma) |  | mg |  |
| $\mathrm{Mve}_{\mathrm{some}}$ | `Mve_some` | S-omeprazole mass concentration (venous plasma plasma) |  | mg/l |  |
| $\mathrm{Apo}_{\mathrm{some}}$ | `Apo_some` | S-omeprazole amount (portal vein plasma) |  | mmol |  |
| $\mathrm{Xpo}_{\mathrm{some}}$ | `Xpo_some` | S-omeprazole mass (portal vein plasma) |  | mg |  |
| $\mathrm{Mpo}_{\mathrm{some}}$ | `Mpo_some` | S-omeprazole mass concentration (portal vein plasma) |  | mg/l |  |
| $\mathrm{Ahv}_{\mathrm{some}}$ | `Ahv_some` | S-omeprazole amount (hepatic vein plasma) |  | mmol |  |
| $\mathrm{Xhv}_{\mathrm{some}}$ | `Xhv_some` | S-omeprazole mass (hepatic vein plasma) |  | mg |  |
| $\mathrm{Mhv}_{\mathrm{some}}$ | `Mhv_some` | S-omeprazole mass concentration (hepatic vein plasma) |  | mg/l |  |
| $\mathrm{Agu}_{\mathrm{plasma\_rome}}$ | `Agu_plasma_rome` | R-omeprazole amount (gut plasma) |  | mmol |  |
| $\mathrm{Xgu}_{\mathrm{plasma\_rome}}$ | `Xgu_plasma_rome` | R-omeprazole mass (gut plasma) |  | mg |  |
| $\mathrm{Mgu}_{\mathrm{plasma\_rome}}$ | `Mgu_plasma_rome` | R-omeprazole mass concentration (gut plasma) |  | mg/l |  |
| $\mathrm{Aki}_{\mathrm{plasma\_rome}}$ | `Aki_plasma_rome` | R-omeprazole amount (kidney plasma) |  | mmol |  |
| $\mathrm{Xki}_{\mathrm{plasma\_rome}}$ | `Xki_plasma_rome` | R-omeprazole mass (kidney plasma) |  | mg |  |
| $\mathrm{Mki}_{\mathrm{plasma\_rome}}$ | `Mki_plasma_rome` | R-omeprazole mass concentration (kidney plasma) |  | mg/l |  |
| $\mathrm{Ali}_{\mathrm{plasma\_rome}}$ | `Ali_plasma_rome` | R-omeprazole amount (liver plasma) |  | mmol |  |
| $\mathrm{Xli}_{\mathrm{plasma\_rome}}$ | `Xli_plasma_rome` | R-omeprazole mass (liver plasma) |  | mg |  |
| $\mathrm{Mli}_{\mathrm{plasma\_rome}}$ | `Mli_plasma_rome` | R-omeprazole mass concentration (liver plasma) |  | mg/l |  |
| $\mathrm{Alu}_{\mathrm{plasma\_rome}}$ | `Alu_plasma_rome` | R-omeprazole amount (lung plasma) |  | mmol |  |
| $\mathrm{Xlu}_{\mathrm{plasma\_rome}}$ | `Xlu_plasma_rome` | R-omeprazole mass (lung plasma) |  | mg |  |
| $\mathrm{Mlu}_{\mathrm{plasma\_rome}}$ | `Mlu_plasma_rome` | R-omeprazole mass concentration (lung plasma) |  | mg/l |  |
| $\mathrm{Apa}_{\mathrm{plasma\_rome}}$ | `Apa_plasma_rome` | R-omeprazole amount (pancreas plasma) |  | mmol |  |
| $\mathrm{Xpa}_{\mathrm{plasma\_rome}}$ | `Xpa_plasma_rome` | R-omeprazole mass (pancreas plasma) |  | mg |  |
| $\mathrm{Mpa}_{\mathrm{plasma\_rome}}$ | `Mpa_plasma_rome` | R-omeprazole mass concentration (pancreas plasma) |  | mg/l |  |
| $\mathrm{Asp}_{\mathrm{plasma\_rome}}$ | `Asp_plasma_rome` | R-omeprazole amount (spleen plasma) |  | mmol |  |
| $\mathrm{Xsp}_{\mathrm{plasma\_rome}}$ | `Xsp_plasma_rome` | R-omeprazole mass (spleen plasma) |  | mg |  |
| $\mathrm{Msp}_{\mathrm{plasma\_rome}}$ | `Msp_plasma_rome` | R-omeprazole mass concentration (spleen plasma) |  | mg/l |  |
| $\mathrm{Are}_{\mathrm{plasma\_rome}}$ | `Are_plasma_rome` | R-omeprazole amount (rest plasma) |  | mmol |  |
| $\mathrm{Xre}_{\mathrm{plasma\_rome}}$ | `Xre_plasma_rome` | R-omeprazole mass (rest plasma) |  | mg |  |
| $\mathrm{Mre}_{\mathrm{plasma\_rome}}$ | `Mre_plasma_rome` | R-omeprazole mass concentration (rest plasma) |  | mg/l |  |
| $\mathrm{Aar}_{\mathrm{rome}}$ | `Aar_rome` | R-omeprazole amount (arterial plasma plasma) |  | mmol |  |
| $\mathrm{Xar}_{\mathrm{rome}}$ | `Xar_rome` | R-omeprazole mass (arterial plasma plasma) |  | mg |  |
| $\mathrm{Mar}_{\mathrm{rome}}$ | `Mar_rome` | R-omeprazole mass concentration (arterial plasma plasma) |  | mg/l |  |
| $\mathrm{Ave}_{\mathrm{rome}}$ | `Ave_rome` | R-omeprazole amount (venous plasma plasma) |  | mmol |  |
| $\mathrm{Xve}_{\mathrm{rome}}$ | `Xve_rome` | R-omeprazole mass (venous plasma plasma) |  | mg |  |
| $\mathrm{Mve}_{\mathrm{rome}}$ | `Mve_rome` | R-omeprazole mass concentration (venous plasma plasma) |  | mg/l |  |
| $\mathrm{Apo}_{\mathrm{rome}}$ | `Apo_rome` | R-omeprazole amount (portal vein plasma) |  | mmol |  |
| $\mathrm{Xpo}_{\mathrm{rome}}$ | `Xpo_rome` | R-omeprazole mass (portal vein plasma) |  | mg |  |
| $\mathrm{Mpo}_{\mathrm{rome}}$ | `Mpo_rome` | R-omeprazole mass concentration (portal vein plasma) |  | mg/l |  |
| $\mathrm{Ahv}_{\mathrm{rome}}$ | `Ahv_rome` | R-omeprazole amount (hepatic vein plasma) |  | mmol |  |
| $\mathrm{Xhv}_{\mathrm{rome}}$ | `Xhv_rome` | R-omeprazole mass (hepatic vein plasma) |  | mg |  |
| $\mathrm{Mhv}_{\mathrm{rome}}$ | `Mhv_rome` | R-omeprazole mass concentration (hepatic vein plasma) |  | mg/l |  |
| $\mathrm{Agu}_{\mathrm{plasma\_omeoh}}$ | `Agu_plasma_omeoh` | 5-hydroxyomeprazole amount (gut plasma) |  | mmol |  |
| $\mathrm{Xgu}_{\mathrm{plasma\_omeoh}}$ | `Xgu_plasma_omeoh` | 5-hydroxyomeprazole mass (gut plasma) |  | mg |  |
| $\mathrm{Mgu}_{\mathrm{plasma\_omeoh}}$ | `Mgu_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (gut plasma) |  | mg/l |  |
| $\mathrm{Aki}_{\mathrm{plasma\_omeoh}}$ | `Aki_plasma_omeoh` | 5-hydroxyomeprazole amount (kidney plasma) |  | mmol |  |
| $\mathrm{Xki}_{\mathrm{plasma\_omeoh}}$ | `Xki_plasma_omeoh` | 5-hydroxyomeprazole mass (kidney plasma) |  | mg |  |
| $\mathrm{Mki}_{\mathrm{plasma\_omeoh}}$ | `Mki_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (kidney plasma) |  | mg/l |  |
| $\mathrm{Ali}_{\mathrm{plasma\_omeoh}}$ | `Ali_plasma_omeoh` | 5-hydroxyomeprazole amount (liver plasma) |  | mmol |  |
| $\mathrm{Xli}_{\mathrm{plasma\_omeoh}}$ | `Xli_plasma_omeoh` | 5-hydroxyomeprazole mass (liver plasma) |  | mg |  |
| $\mathrm{Mli}_{\mathrm{plasma\_omeoh}}$ | `Mli_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (liver plasma) |  | mg/l |  |
| $\mathrm{Alu}_{\mathrm{plasma\_omeoh}}$ | `Alu_plasma_omeoh` | 5-hydroxyomeprazole amount (lung plasma) |  | mmol |  |
| $\mathrm{Xlu}_{\mathrm{plasma\_omeoh}}$ | `Xlu_plasma_omeoh` | 5-hydroxyomeprazole mass (lung plasma) |  | mg |  |
| $\mathrm{Mlu}_{\mathrm{plasma\_omeoh}}$ | `Mlu_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (lung plasma) |  | mg/l |  |
| $\mathrm{Apa}_{\mathrm{plasma\_omeoh}}$ | `Apa_plasma_omeoh` | 5-hydroxyomeprazole amount (pancreas plasma) |  | mmol |  |
| $\mathrm{Xpa}_{\mathrm{plasma\_omeoh}}$ | `Xpa_plasma_omeoh` | 5-hydroxyomeprazole mass (pancreas plasma) |  | mg |  |
| $\mathrm{Mpa}_{\mathrm{plasma\_omeoh}}$ | `Mpa_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (pancreas plasma) |  | mg/l |  |
| $\mathrm{Asp}_{\mathrm{plasma\_omeoh}}$ | `Asp_plasma_omeoh` | 5-hydroxyomeprazole amount (spleen plasma) |  | mmol |  |
| $\mathrm{Xsp}_{\mathrm{plasma\_omeoh}}$ | `Xsp_plasma_omeoh` | 5-hydroxyomeprazole mass (spleen plasma) |  | mg |  |
| $\mathrm{Msp}_{\mathrm{plasma\_omeoh}}$ | `Msp_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (spleen plasma) |  | mg/l |  |
| $\mathrm{Are}_{\mathrm{plasma\_omeoh}}$ | `Are_plasma_omeoh` | 5-hydroxyomeprazole amount (rest plasma) |  | mmol |  |
| $\mathrm{Xre}_{\mathrm{plasma\_omeoh}}$ | `Xre_plasma_omeoh` | 5-hydroxyomeprazole mass (rest plasma) |  | mg |  |
| $\mathrm{Mre}_{\mathrm{plasma\_omeoh}}$ | `Mre_plasma_omeoh` | 5-hydroxyomeprazole mass concentration (rest plasma) |  | mg/l |  |
| $\mathrm{Aar}_{\mathrm{omeoh}}$ | `Aar_omeoh` | 5-hydroxyomeprazole amount (arterial plasma plasma) |  | mmol |  |
| $\mathrm{Xar}_{\mathrm{omeoh}}$ | `Xar_omeoh` | 5-hydroxyomeprazole mass (arterial plasma plasma) |  | mg |  |
| $\mathrm{Mar}_{\mathrm{omeoh}}$ | `Mar_omeoh` | 5-hydroxyomeprazole mass concentration (arterial plasma plasma) |  | mg/l |  |
| $\mathrm{Ave}_{\mathrm{omeoh}}$ | `Ave_omeoh` | 5-hydroxyomeprazole amount (venous plasma plasma) |  | mmol |  |
| $\mathrm{Xve}_{\mathrm{omeoh}}$ | `Xve_omeoh` | 5-hydroxyomeprazole mass (venous plasma plasma) |  | mg |  |
| $\mathrm{Mve}_{\mathrm{omeoh}}$ | `Mve_omeoh` | 5-hydroxyomeprazole mass concentration (venous plasma plasma) |  | mg/l |  |
| $\mathrm{Apo}_{\mathrm{omeoh}}$ | `Apo_omeoh` | 5-hydroxyomeprazole amount (portal vein plasma) |  | mmol |  |
| $\mathrm{Xpo}_{\mathrm{omeoh}}$ | `Xpo_omeoh` | 5-hydroxyomeprazole mass (portal vein plasma) |  | mg |  |
| $\mathrm{Mpo}_{\mathrm{omeoh}}$ | `Mpo_omeoh` | 5-hydroxyomeprazole mass concentration (portal vein plasma) |  | mg/l |  |
| $\mathrm{Ahv}_{\mathrm{omeoh}}$ | `Ahv_omeoh` | 5-hydroxyomeprazole amount (hepatic vein plasma) |  | mmol |  |
| $\mathrm{Xhv}_{\mathrm{omeoh}}$ | `Xhv_omeoh` | 5-hydroxyomeprazole mass (hepatic vein plasma) |  | mg |  |
| $\mathrm{Mhv}_{\mathrm{omeoh}}$ | `Mhv_omeoh` | 5-hydroxyomeprazole mass concentration (hepatic vein plasma) |  | mg/l |  |
| $\mathrm{Agu}_{\mathrm{plasma\_omesul}}$ | `Agu_plasma_omesul` | omeprazole sulfone amount (gut plasma) |  | mmol |  |
| $\mathrm{Xgu}_{\mathrm{plasma\_omesul}}$ | `Xgu_plasma_omesul` | omeprazole sulfone mass (gut plasma) |  | mg |  |
| $\mathrm{Mgu}_{\mathrm{plasma\_omesul}}$ | `Mgu_plasma_omesul` | omeprazole sulfone mass concentration (gut plasma) |  | mg/l |  |
| $\mathrm{Aki}_{\mathrm{plasma\_omesul}}$ | `Aki_plasma_omesul` | omeprazole sulfone amount (kidney plasma) |  | mmol |  |
| $\mathrm{Xki}_{\mathrm{plasma\_omesul}}$ | `Xki_plasma_omesul` | omeprazole sulfone mass (kidney plasma) |  | mg |  |
| $\mathrm{Mki}_{\mathrm{plasma\_omesul}}$ | `Mki_plasma_omesul` | omeprazole sulfone mass concentration (kidney plasma) |  | mg/l |  |
| $\mathrm{Ali}_{\mathrm{plasma\_omesul}}$ | `Ali_plasma_omesul` | omeprazole sulfone amount (liver plasma) |  | mmol |  |
| $\mathrm{Xli}_{\mathrm{plasma\_omesul}}$ | `Xli_plasma_omesul` | omeprazole sulfone mass (liver plasma) |  | mg |  |
| $\mathrm{Mli}_{\mathrm{plasma\_omesul}}$ | `Mli_plasma_omesul` | omeprazole sulfone mass concentration (liver plasma) |  | mg/l |  |
| $\mathrm{Alu}_{\mathrm{plasma\_omesul}}$ | `Alu_plasma_omesul` | omeprazole sulfone amount (lung plasma) |  | mmol |  |
| $\mathrm{Xlu}_{\mathrm{plasma\_omesul}}$ | `Xlu_plasma_omesul` | omeprazole sulfone mass (lung plasma) |  | mg |  |
| $\mathrm{Mlu}_{\mathrm{plasma\_omesul}}$ | `Mlu_plasma_omesul` | omeprazole sulfone mass concentration (lung plasma) |  | mg/l |  |
| $\mathrm{Apa}_{\mathrm{plasma\_omesul}}$ | `Apa_plasma_omesul` | omeprazole sulfone amount (pancreas plasma) |  | mmol |  |
| $\mathrm{Xpa}_{\mathrm{plasma\_omesul}}$ | `Xpa_plasma_omesul` | omeprazole sulfone mass (pancreas plasma) |  | mg |  |
| $\mathrm{Mpa}_{\mathrm{plasma\_omesul}}$ | `Mpa_plasma_omesul` | omeprazole sulfone mass concentration (pancreas plasma) |  | mg/l |  |
| $\mathrm{Asp}_{\mathrm{plasma\_omesul}}$ | `Asp_plasma_omesul` | omeprazole sulfone amount (spleen plasma) |  | mmol |  |
| $\mathrm{Xsp}_{\mathrm{plasma\_omesul}}$ | `Xsp_plasma_omesul` | omeprazole sulfone mass (spleen plasma) |  | mg |  |
| $\mathrm{Msp}_{\mathrm{plasma\_omesul}}$ | `Msp_plasma_omesul` | omeprazole sulfone mass concentration (spleen plasma) |  | mg/l |  |
| $\mathrm{Are}_{\mathrm{plasma\_omesul}}$ | `Are_plasma_omesul` | omeprazole sulfone amount (rest plasma) |  | mmol |  |
| $\mathrm{Xre}_{\mathrm{plasma\_omesul}}$ | `Xre_plasma_omesul` | omeprazole sulfone mass (rest plasma) |  | mg |  |
| $\mathrm{Mre}_{\mathrm{plasma\_omesul}}$ | `Mre_plasma_omesul` | omeprazole sulfone mass concentration (rest plasma) |  | mg/l |  |
| $\mathrm{Aar}_{\mathrm{omesul}}$ | `Aar_omesul` | omeprazole sulfone amount (arterial plasma plasma) |  | mmol |  |
| $\mathrm{Xar}_{\mathrm{omesul}}$ | `Xar_omesul` | omeprazole sulfone mass (arterial plasma plasma) |  | mg |  |
| $\mathrm{Mar}_{\mathrm{omesul}}$ | `Mar_omesul` | omeprazole sulfone mass concentration (arterial plasma plasma) |  | mg/l |  |
| $\mathrm{Ave}_{\mathrm{omesul}}$ | `Ave_omesul` | omeprazole sulfone amount (venous plasma plasma) |  | mmol |  |
| $\mathrm{Xve}_{\mathrm{omesul}}$ | `Xve_omesul` | omeprazole sulfone mass (venous plasma plasma) |  | mg |  |
| $\mathrm{Mve}_{\mathrm{omesul}}$ | `Mve_omesul` | omeprazole sulfone mass concentration (venous plasma plasma) |  | mg/l |  |
| $\mathrm{Apo}_{\mathrm{omesul}}$ | `Apo_omesul` | omeprazole sulfone amount (portal vein plasma) |  | mmol |  |
| $\mathrm{Xpo}_{\mathrm{omesul}}$ | `Xpo_omesul` | omeprazole sulfone mass (portal vein plasma) |  | mg |  |
| $\mathrm{Mpo}_{\mathrm{omesul}}$ | `Mpo_omesul` | omeprazole sulfone mass concentration (portal vein plasma) |  | mg/l |  |
| $\mathrm{Ahv}_{\mathrm{omesul}}$ | `Ahv_omesul` | omeprazole sulfone amount (hepatic vein plasma) |  | mmol |  |
| $\mathrm{Xhv}_{\mathrm{omesul}}$ | `Xhv_omesul` | omeprazole sulfone mass (hepatic vein plasma) |  | mg |  |
| $\mathrm{Mhv}_{\mathrm{omesul}}$ | `Mhv_omesul` | omeprazole sulfone mass concentration (hepatic vein plasma) |  | mg/l |  |
| $\mathrm{Agu}_{\mathrm{plasma\_omeoth}}$ | `Agu_plasma_omeoth` | other omeprazole metabolites amount (gut plasma) |  | mmol |  |
| $\mathrm{Xgu}_{\mathrm{plasma\_omeoth}}$ | `Xgu_plasma_omeoth` | other omeprazole metabolites mass (gut plasma) |  | mg |  |
| $\mathrm{Mgu}_{\mathrm{plasma\_omeoth}}$ | `Mgu_plasma_omeoth` | other omeprazole metabolites mass concentration (gut plasma) |  | mg/l |  |
| $\mathrm{Aki}_{\mathrm{plasma\_omeoth}}$ | `Aki_plasma_omeoth` | other omeprazole metabolites amount (kidney plasma) |  | mmol |  |
| $\mathrm{Xki}_{\mathrm{plasma\_omeoth}}$ | `Xki_plasma_omeoth` | other omeprazole metabolites mass (kidney plasma) |  | mg |  |
| $\mathrm{Mki}_{\mathrm{plasma\_omeoth}}$ | `Mki_plasma_omeoth` | other omeprazole metabolites mass concentration (kidney plasma) |  | mg/l |  |
| $\mathrm{Ali}_{\mathrm{plasma\_omeoth}}$ | `Ali_plasma_omeoth` | other omeprazole metabolites amount (liver plasma) |  | mmol |  |
| $\mathrm{Xli}_{\mathrm{plasma\_omeoth}}$ | `Xli_plasma_omeoth` | other omeprazole metabolites mass (liver plasma) |  | mg |  |
| $\mathrm{Mli}_{\mathrm{plasma\_omeoth}}$ | `Mli_plasma_omeoth` | other omeprazole metabolites mass concentration (liver plasma) |  | mg/l |  |
| $\mathrm{Alu}_{\mathrm{plasma\_omeoth}}$ | `Alu_plasma_omeoth` | other omeprazole metabolites amount (lung plasma) |  | mmol |  |
| $\mathrm{Xlu}_{\mathrm{plasma\_omeoth}}$ | `Xlu_plasma_omeoth` | other omeprazole metabolites mass (lung plasma) |  | mg |  |
| $\mathrm{Mlu}_{\mathrm{plasma\_omeoth}}$ | `Mlu_plasma_omeoth` | other omeprazole metabolites mass concentration (lung plasma) |  | mg/l |  |
| $\mathrm{Apa}_{\mathrm{plasma\_omeoth}}$ | `Apa_plasma_omeoth` | other omeprazole metabolites amount (pancreas plasma) |  | mmol |  |
| $\mathrm{Xpa}_{\mathrm{plasma\_omeoth}}$ | `Xpa_plasma_omeoth` | other omeprazole metabolites mass (pancreas plasma) |  | mg |  |
| $\mathrm{Mpa}_{\mathrm{plasma\_omeoth}}$ | `Mpa_plasma_omeoth` | other omeprazole metabolites mass concentration (pancreas plasma) |  | mg/l |  |
| $\mathrm{Asp}_{\mathrm{plasma\_omeoth}}$ | `Asp_plasma_omeoth` | other omeprazole metabolites amount (spleen plasma) |  | mmol |  |
| $\mathrm{Xsp}_{\mathrm{plasma\_omeoth}}$ | `Xsp_plasma_omeoth` | other omeprazole metabolites mass (spleen plasma) |  | mg |  |
| $\mathrm{Msp}_{\mathrm{plasma\_omeoth}}$ | `Msp_plasma_omeoth` | other omeprazole metabolites mass concentration (spleen plasma) |  | mg/l |  |
| $\mathrm{Are}_{\mathrm{plasma\_omeoth}}$ | `Are_plasma_omeoth` | other omeprazole metabolites amount (rest plasma) |  | mmol |  |
| $\mathrm{Xre}_{\mathrm{plasma\_omeoth}}$ | `Xre_plasma_omeoth` | other omeprazole metabolites mass (rest plasma) |  | mg |  |
| $\mathrm{Mre}_{\mathrm{plasma\_omeoth}}$ | `Mre_plasma_omeoth` | other omeprazole metabolites mass concentration (rest plasma) |  | mg/l |  |
| $\mathrm{Aar}_{\mathrm{omeoth}}$ | `Aar_omeoth` | other omeprazole metabolites amount (arterial plasma plasma) |  | mmol |  |
| $\mathrm{Xar}_{\mathrm{omeoth}}$ | `Xar_omeoth` | other omeprazole metabolites mass (arterial plasma plasma) |  | mg |  |
| $\mathrm{Mar}_{\mathrm{omeoth}}$ | `Mar_omeoth` | other omeprazole metabolites mass concentration (arterial plasma plasma) |  | mg/l |  |
| $\mathrm{Ave}_{\mathrm{omeoth}}$ | `Ave_omeoth` | other omeprazole metabolites amount (venous plasma plasma) |  | mmol |  |
| $\mathrm{Xve}_{\mathrm{omeoth}}$ | `Xve_omeoth` | other omeprazole metabolites mass (venous plasma plasma) |  | mg |  |
| $\mathrm{Mve}_{\mathrm{omeoth}}$ | `Mve_omeoth` | other omeprazole metabolites mass concentration (venous plasma plasma) |  | mg/l |  |
| $\mathrm{Apo}_{\mathrm{omeoth}}$ | `Apo_omeoth` | other omeprazole metabolites amount (portal vein plasma) |  | mmol |  |
| $\mathrm{Xpo}_{\mathrm{omeoth}}$ | `Xpo_omeoth` | other omeprazole metabolites mass (portal vein plasma) |  | mg |  |
| $\mathrm{Mpo}_{\mathrm{omeoth}}$ | `Mpo_omeoth` | other omeprazole metabolites mass concentration (portal vein plasma) |  | mg/l |  |
| $\mathrm{Ahv}_{\mathrm{omeoth}}$ | `Ahv_omeoth` | other omeprazole metabolites amount (hepatic vein plasma) |  | mmol |  |
| $\mathrm{Xhv}_{\mathrm{omeoth}}$ | `Xhv_omeoth` | other omeprazole metabolites mass (hepatic vein plasma) |  | mg |  |
| $\mathrm{Mhv}_{\mathrm{omeoth}}$ | `Mhv_omeoth` | other omeprazole metabolites mass concentration (hepatic vein plasma) |  | mg/l |  |
| $\mathrm{LI}_{\mathrm{\_f\_cyp2c19}}$ | `LI__f_cyp2c19` | activity of CYP2C19 (genotype, interactions) | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_cyp3a4}}$ | `LI__f_cyp3a4` | activity of CYP3A4 (interactions) | $1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMEIM\_k}}$ | `LI__OMEIM_k` | rate of the omeprazole exchange between plasma and liver | $10$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_Km}}$ | `LI__CYP2C19_Km` | Km CYP2C19 omeprazole (apparent, total concentration) | $0.1$ | mmol/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP3A4\_Km}}$ | `LI__CYP3A4_Km` | Km CYP3A4 omeprazole (apparent, total concentration) | $0.1$ | mmol/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_some\_omeoh}}$ | `LI__f_some_omeoh` | fraction 5-hydroxyomeprazole of the CYP2C19 metabolism of S-omeprazole | $0.1$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_f\_rome\_cyp3a4\_omeoh}}$ | `LI__f_rome_cyp3a4_omeoh` | fraction 5-hydroxyomeprazole of the CYP3A4 metabolism of R-omeprazole | $0.464385319357792$ | \- | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2c19\_active}}$ | `LI__cyp2c19_active` | fraction of active CYP2C19 | $1$ | \- |  |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_kdeg}}$ | `LI__CYP2C19_kdeg` | degradation rate of CYP2C19 | $0.000444230769230769$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_kinact}}$ | `LI__CYP2C19_kinact` | maximal inactivation rate of CYP2C19 by omeprazole | $0.0185056804400849$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_KI}}$ | `LI__CYP2C19_KI` | concentration of half-maximal inactivation of CYP2C19 | $0.002$ | mmol/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_Vmax\_some}}$ | `LI__CYP2C19_Vmax_some` | Vmax CYP2C19 S-omeprazole | $0.0429809444865293$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP2C19\_Vmax\_rome}}$ | `LI__CYP2C19_Vmax_rome` | Vmax CYP2C19 R-omeprazole | $0.0879250267535046$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP3A4\_Vmax\_some}}$ | `LI__CYP3A4_Vmax_some` | Vmax CYP3A4 S-omeprazole | $0.00347040955371226$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_CYP3A4\_Vmax\_rome}}$ | `LI__CYP3A4_Vmax_rome` | Vmax CYP3A4 R-omeprazole | $0.00812409201505695$ | mmol/min/l | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMEOHEX\_k}}$ | `LI__OMEOHEX_k` | rate of the 5-hydroxyomeprazole release from the liver | $0.274485257726021$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMEOHM\_k}}$ | `LI__OMEOHM_k` | rate of the 5-hydroxyomeprazole oxidation in the liver | $0.6$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMEMEX\_k}}$ | `LI__OMEMEX_k` | rate of the metabolite exchange between plasma and liver | $10$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMESUL2C19\_k}}$ | `LI__OMESUL2C19_k` | rate of the CYP2C19 metabolism of omeprazole sulfone | $0.0562470024857024$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMESULM\_k}}$ | `LI__OMESULM_k` | rate of the CYP2C19 independent metabolism of omeprazole sulfone | $0.0629735593807952$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_OMEOTHBIL\_k}}$ | `LI__OMEOTHBIL_k` | rate of the biliary excretion of the other metabolites | $0.00492138159856471$ | 1/min | ✓ |
| $\mathrm{LI}_{\mathrm{\_cyp2c19\_activity}}$ | `LI__cyp2c19_activity` | activity of CYP2C19 |  | \- |  |
| $\mathrm{LI}_{\mathrm{\_SOMECYP2C19\_rate}}$ | `LI__SOMECYP2C19_rate` | rate of the CYP2C19 metabolism of S-omeprazole |  | mmol/min |  |
| $\mathrm{LI}_{\mathrm{\_ROMECYP3A4\_rate}}$ | `LI__ROMECYP3A4_rate` | rate of the CYP3A4 metabolism of R-omeprazole |  | mmol/min |  |
| $\mathrm{KI}_{\mathrm{\_f\_renal\_function}}$ | `KI__f_renal_function` | renal function | $1$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_OMEOHEX\_f}}$ | `KI__OMEOHEX_f` | renal clearance of 5-hydroxyomeprazole relative to the GFR | $1.83915259344785$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_OMEOTHEX\_f}}$ | `KI__OMEOTHEX_f` | renal clearance of the other metabolites relative to the GFR | $0.256693039466168$ | \- | ✓ |
| $\mathrm{KI}_{\mathrm{\_GFR}}$ | `KI__GFR` | glomerular filtration rate |  | ml/min |  |
| $\mathrm{KI}_{\mathrm{\_OMEMETSEX}}$ | `KI__OMEMETSEX` | renal excretion rate of the omeprazole metabolites |  | mmol/min |  |
| $\mathrm{GU}_{\mathrm{\_Qstomach}}$ | `GU__Qstomach` | stomach fluid loss | $0.01$ | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}}$ | `GU__cf_species_dimensionless` | dimensionless species conversion | $1$ | 1/mmol | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_ec}}$ | `GU__f_ec` | enteric-coated form (0 solution or suspension, 1 enteric-coated) | $0$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_f\_unprotected}}$ | `GU__f_unprotected` | unprotected solution (0 buffered or enteric-coated, 1 unprotected) | $0$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_Ka\_dis\_ome}}$ | `GU__Ka_dis_ome` | rate of the gastric emptying of a solution | $30$ | 1/hr | ✓ |
| $\mathrm{GU}_{\mathrm{\_Ka\_ec\_ome}}$ | `GU__Ka_ec_ome` | rate of the gastric emptying and the release of an enteric-coated form | $1.45474229513195$ | 1/hr | ✓ |
| $\mathrm{GU}_{\mathrm{\_fed}}$ | `GU__fed` | fed state (0 fasted, 1 fed) | $0$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_FED\_f\_dissolution}}$ | `GU__FED_f_dissolution` | fed effect on the gastric emptying and dissolution | $0.35$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_FED\_f\_absorption}}$ | `GU__FED_f_absorption` | fed effect on the fraction absorbed | $0.65$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_abs}}$ | `GU__F_ome_abs` | fraction absorbed omeprazole | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_OMEABS\_k}}$ | `GU__OMEABS_k` | rate of omeprazole absorption | $0.0909283349017812$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_OMEOTHEXC\_k}}$ | `GU__OMEOTHEXC_k` | rate of the fecal excretion of the other metabolites | $0.0007$ | 1/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_Mr\_ome}}$ | `GU__Mr_ome` | Molecular weight omeprazole \[g/mole\] | $345.416$ | g/mol | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_pH2}}$ | `GU__F_ome_pH2` | fraction not degraded at pH 2 | $0.35$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_pH6}}$ | `GU__F_ome_pH6` | fraction not degraded at pH 6 | $1$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_KpH}}$ | `GU__F_ome_KpH` | midpoint of the pH effect on the degradation | $4$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_n}}$ | `GU__F_ome_n` | Hill coefficient of the pH effect on the degradation | $2$ | \- | ✓ |
| $\mathrm{GU}_{\mathrm{\_POEC\_some}}$ | `GU__POEC_some` | enteric-coated S-omeprazole in the small intestine \[mg\] | $0$ | mg |  |
| $\mathrm{GU}_{\mathrm{\_POEC\_rome}}$ | `GU__POEC_rome` | enteric-coated R-omeprazole in the small intestine \[mg\] | $0$ | mg |  |
| $\mathrm{GU}_{\mathrm{\_pp\_rate\_k}}$ | `GU__pp_rate_k` | Rate of proton secretion | $0.1$ | mmol/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_ppi\_k}}$ | `GU__ppi_k` | Inhibition rate PP | $5$ | l/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_pp\_synthesis\_k}}$ | `GU__pp_synthesis_k` | Synthesis rate PP | $0.0004$ | mmol/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_pp\_degradation\_k}}$ | `GU__pp_degradation_k` | Degradation rate PP | $0.0004$ | mmol/min | ✓ |
| $\mathrm{GU}_{\mathrm{\_pp\_total}}$ | `GU__pp_total` | total proton pump |  | \- |  |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_pH}}$ | `GU__F_ome_pH` | fraction of an unprotected solution not degraded in the stomach |  | \- |  |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_stomach}}$ | `GU__F_ome_stomach` | fraction of a solution not degraded in the stomach |  | \- |  |
| $\mathrm{GU}_{\mathrm{\_Ka\_emptying}}$ | `GU__Ka_emptying` | rate of the gastric emptying of the form |  | 1/hr |  |
| $\mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}}$ | `GU__F_ome_abs_eff` | fraction absorbed omeprazole (fed state) |  | \- |  |
| $\mathrm{GU}_{\mathrm{\_emptying\_some}}$ | `GU__emptying_some` | gastric emptying S-omeprazole |  | mmol/min |  |
| $\mathrm{GU}_{\mathrm{\_absorption\_some}}$ | `GU__absorption_some` | absorption S-omeprazole |  | mmol/min |  |
| $\mathrm{GU}_{\mathrm{\_emptying\_rome}}$ | `GU__emptying_rome` | gastric emptying R-omeprazole |  | mmol/min |  |
| $\mathrm{GU}_{\mathrm{\_absorption\_rome}}$ | `GU__absorption_rome` | absorption R-omeprazole |  | mmol/min |  |

## Initial assignments and assignment rules

The initial assignments set the values at $t = 0$:

$$
\begin{aligned}
\mathrm{Aurine}_{\mathrm{omeoh}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Aurine}_{\mathrm{omeoth}} &= 0 \cdot \mathrm{Vurine} \\[1ex]
\mathrm{Afeces}_{\mathrm{some}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{Afeces}_{\mathrm{rome}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{Afeces}_{\mathrm{omeoth}} &= 0 \cdot \mathrm{Vfeces} \\[1ex]
\mathrm{GU}_{\mathrm{\_some\_stomach}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vstomach}} \\[1ex]
\mathrm{GU}_{\mathrm{\_rome\_stomach}} &= 0 \cdot \mathrm{GU}_{\mathrm{\_Vstomach}}
\end{aligned}
$$

The assignment rules hold at every time $t$:

$$
\begin{aligned}
f_{\mathrm{shunts}} &= f_{\mathrm{cirrhosis}} \\[1ex]
f_{\mathrm{tissue\_loss}} &= f_{\mathrm{cirrhosis}} \\[1ex]
\mathrm{Cve}_{\mathrm{ome}} &= \mathrm{Cve}_{\mathrm{some}} + \mathrm{Cve}_{\mathrm{rome}} \\[1ex]
\mathrm{Cve}_{\mathrm{omemets}} &= \mathrm{Cve}_{\mathrm{omeoh}} + \mathrm{Cve}_{\mathrm{omesul}} + \mathrm{Cve}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Cve}_{\mathrm{ometot}} &= \mathrm{Cve}_{\mathrm{ome}} + \mathrm{Cve}_{\mathrm{omemets}} \\[1ex]
\mathrm{Aurine}_{\mathrm{omemets}} &= \mathrm{Aurine}_{\mathrm{omeoh}} + \mathrm{Aurine}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Afeces}_{\mathrm{omemets}} &= \mathrm{Afeces}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Afeces}_{\mathrm{ome}} &= \mathrm{Afeces}_{\mathrm{some}} + \mathrm{Afeces}_{\mathrm{rome}} \\[1ex]
\mathrm{FVre} &= 1 - \mathrm{FVgu} - \mathrm{FVki} - \mathrm{FVli} \\
&\quad {} - \mathrm{FVlu} - \mathrm{FVsp} - \mathrm{FVpa} - \mathrm{FVve} \\
&\quad {} - \mathrm{FVar} \\[1ex]
\mathrm{FQre} &= 1 - \mathrm{FQki} - \mathrm{FQh} \\[1ex]
\mathrm{BSA} &= 0.024265 \cdot \mathopen{}\left(\frac{\mathrm{BW}}{1}\right)^{0.5378} \cdot \mathopen{}\left(\frac{\mathrm{HEIGHT}}{1}\right)^{0.3964} \\[1ex]
\mathrm{CO} &= \mathrm{BW} \cdot \mathrm{COBW} \\[1ex]
\mathrm{QC} &= \frac{\mathrm{CO}}{1000} \cdot 60 \\[1ex]
\mathrm{Vgu} &= \mathrm{BW} \cdot \mathrm{FVgu} \\[1ex]
\mathrm{Vki} &= \mathrm{BW} \cdot \mathrm{FVki} \\[1ex]
\mathrm{Vli} &= \mathrm{BW} \cdot \mathrm{FVli} \\[1ex]
\mathrm{Vlu} &= \mathrm{BW} \cdot \mathrm{FVlu} \\[1ex]
\mathrm{Vsp} &= \mathrm{BW} \cdot \mathrm{FVsp} \\[1ex]
\mathrm{Vpa} &= \mathrm{BW} \cdot \mathrm{FVpa} \\[1ex]
\mathrm{Vre} &= \mathrm{BW} \cdot \mathrm{FVre} \\[1ex]
\mathrm{Vve} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVve} - \frac{\mathrm{FVve}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Var} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVar} - \frac{\mathrm{FVar}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Vpo} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVpo} - \frac{\mathrm{FVpo}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Vhv} &= \mathopen{}\left(1 - \mathrm{HCT}\right) \cdot \mathopen{}\left(\mathrm{BW} \cdot \mathrm{FVhv} - \frac{\mathrm{FVhv}}{\mathrm{FVar} + \mathrm{FVve} + \mathrm{FVpo} + \mathrm{FVhv}} \cdot \mathrm{BW} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{FVar} - \mathrm{FVve} - \mathrm{FVpo} - \mathrm{FVhv}\right)\right) \\[1ex]
\mathrm{Qgu} &= \mathrm{QC} \cdot \mathrm{FQgu} \\[1ex]
\mathrm{Qki} &= \mathrm{QC} \cdot \mathrm{FQki} \\[1ex]
\mathrm{Qh} &= \mathrm{QC} \cdot \mathrm{FQh} \\[1ex]
\mathrm{Qlu} &= \mathrm{QC} \cdot \mathrm{FQlu} \\[1ex]
\mathrm{Qsp} &= \mathrm{QC} \cdot \mathrm{FQsp} \\[1ex]
\mathrm{Qpa} &= \mathrm{QC} \cdot \mathrm{FQpa} \\[1ex]
\mathrm{Qha} &= \mathrm{Qh} - \mathrm{Qgu} - \mathrm{Qsp} - \mathrm{Qpa} \\[1ex]
\mathrm{Qre} &= \mathrm{QC} \cdot \mathrm{FQre} \\[1ex]
\mathrm{Qpo} &= \mathrm{Qsp} + \mathrm{Qpa} + \mathrm{Qgu} \\[1ex]
\mathrm{GFR}_{\mathrm{base}} &= f_{\mathrm{GFR\_Qki}} \cdot \mathrm{Qki} \\[1ex]
\mathrm{Vgu}_{\mathrm{plasma}} &= \mathrm{Vgu} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vgu}_{\mathrm{tissue}} &= \mathrm{Vgu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vki}_{\mathrm{plasma}} &= \mathrm{Vki} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vki}_{\mathrm{tissue}} &= \mathrm{Vki} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vli}_{\mathrm{plasma}} &= \mathrm{Vli} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vli}_{\mathrm{tissue}} &= \mathrm{Vli} \cdot \mathopen{}\left(1 - f_{\mathrm{tissue\_loss}}\right) \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vlu}_{\mathrm{plasma}} &= \mathrm{Vlu} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vlu}_{\mathrm{tissue}} &= \mathrm{Vlu} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vpa}_{\mathrm{plasma}} &= \mathrm{Vpa} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vpa}_{\mathrm{tissue}} &= \mathrm{Vpa} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vsp}_{\mathrm{plasma}} &= \mathrm{Vsp} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vsp}_{\mathrm{tissue}} &= \mathrm{Vsp} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Vre}_{\mathrm{plasma}} &= \mathrm{Vre} \cdot \mathrm{Fblood} \cdot \mathopen{}\left(1 - \mathrm{HCT}\right) \\[1ex]
\mathrm{Vre}_{\mathrm{tissue}} &= \mathrm{Vre} \cdot \mathopen{}\left(1 - \mathrm{Fblood}\right) \\[1ex]
\mathrm{Ki}_{\mathrm{some}} &= \frac{0.693}{\mathrm{ti}_{\mathrm{some}}} \cdot 60 \\[1ex]
\mathrm{Agu}_{\mathrm{plasma\_some}} &= \mathrm{Cgu}_{\mathrm{plasma\_some}} \cdot \mathrm{Vgu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xgu}_{\mathrm{plasma\_some}} &= \mathrm{Agu}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mgu}_{\mathrm{plasma\_some}} &= \mathrm{Cgu}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Aki}_{\mathrm{plasma\_some}} &= \mathrm{Cki}_{\mathrm{plasma\_some}} \cdot \mathrm{Vki}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xki}_{\mathrm{plasma\_some}} &= \mathrm{Aki}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mki}_{\mathrm{plasma\_some}} &= \mathrm{Cki}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Ali}_{\mathrm{plasma\_some}} &= \mathrm{Cli}_{\mathrm{plasma\_some}} \cdot \mathrm{Vli}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xli}_{\mathrm{plasma\_some}} &= \mathrm{Ali}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mli}_{\mathrm{plasma\_some}} &= \mathrm{Cli}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Alu}_{\mathrm{plasma\_some}} &= \mathrm{Clu}_{\mathrm{plasma\_some}} \cdot \mathrm{Vlu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xlu}_{\mathrm{plasma\_some}} &= \mathrm{Alu}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mlu}_{\mathrm{plasma\_some}} &= \mathrm{Clu}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Apa}_{\mathrm{plasma\_some}} &= \mathrm{Cpa}_{\mathrm{plasma\_some}} \cdot \mathrm{Vpa}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xpa}_{\mathrm{plasma\_some}} &= \mathrm{Apa}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mpa}_{\mathrm{plasma\_some}} &= \mathrm{Cpa}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Asp}_{\mathrm{plasma\_some}} &= \mathrm{Csp}_{\mathrm{plasma\_some}} \cdot \mathrm{Vsp}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xsp}_{\mathrm{plasma\_some}} &= \mathrm{Asp}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Msp}_{\mathrm{plasma\_some}} &= \mathrm{Csp}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Are}_{\mathrm{plasma\_some}} &= \mathrm{Cre}_{\mathrm{plasma\_some}} \cdot \mathrm{Vre}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xre}_{\mathrm{plasma\_some}} &= \mathrm{Are}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mre}_{\mathrm{plasma\_some}} &= \mathrm{Cre}_{\mathrm{plasma\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Aar}_{\mathrm{some}} &= \mathrm{Car}_{\mathrm{some}} \cdot \mathrm{Var} \\[1ex]
\mathrm{Xar}_{\mathrm{some}} &= \mathrm{Aar}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mar}_{\mathrm{some}} &= \mathrm{Car}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Ave}_{\mathrm{some}} &= \mathrm{Cve}_{\mathrm{some}} \cdot \mathrm{Vve} \\[1ex]
\mathrm{Xve}_{\mathrm{some}} &= \mathrm{Ave}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mve}_{\mathrm{some}} &= \mathrm{Cve}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Apo}_{\mathrm{some}} &= \mathrm{Cpo}_{\mathrm{some}} \cdot \mathrm{Vpo} \\[1ex]
\mathrm{Xpo}_{\mathrm{some}} &= \mathrm{Apo}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mpo}_{\mathrm{some}} &= \mathrm{Cpo}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Ahv}_{\mathrm{some}} &= \mathrm{Chv}_{\mathrm{some}} \cdot \mathrm{Vhv} \\[1ex]
\mathrm{Xhv}_{\mathrm{some}} &= \mathrm{Ahv}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Mhv}_{\mathrm{some}} &= \mathrm{Chv}_{\mathrm{some}} \cdot \mathrm{Mr}_{\mathrm{some}} \\[1ex]
\mathrm{Ki}_{\mathrm{rome}} &= \frac{0.693}{\mathrm{ti}_{\mathrm{rome}}} \cdot 60 \\[1ex]
\mathrm{Agu}_{\mathrm{plasma\_rome}} &= \mathrm{Cgu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vgu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xgu}_{\mathrm{plasma\_rome}} &= \mathrm{Agu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mgu}_{\mathrm{plasma\_rome}} &= \mathrm{Cgu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Aki}_{\mathrm{plasma\_rome}} &= \mathrm{Cki}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vki}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xki}_{\mathrm{plasma\_rome}} &= \mathrm{Aki}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mki}_{\mathrm{plasma\_rome}} &= \mathrm{Cki}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Ali}_{\mathrm{plasma\_rome}} &= \mathrm{Cli}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vli}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xli}_{\mathrm{plasma\_rome}} &= \mathrm{Ali}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mli}_{\mathrm{plasma\_rome}} &= \mathrm{Cli}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Alu}_{\mathrm{plasma\_rome}} &= \mathrm{Clu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vlu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xlu}_{\mathrm{plasma\_rome}} &= \mathrm{Alu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mlu}_{\mathrm{plasma\_rome}} &= \mathrm{Clu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Apa}_{\mathrm{plasma\_rome}} &= \mathrm{Cpa}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vpa}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xpa}_{\mathrm{plasma\_rome}} &= \mathrm{Apa}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mpa}_{\mathrm{plasma\_rome}} &= \mathrm{Cpa}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Asp}_{\mathrm{plasma\_rome}} &= \mathrm{Csp}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vsp}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xsp}_{\mathrm{plasma\_rome}} &= \mathrm{Asp}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Msp}_{\mathrm{plasma\_rome}} &= \mathrm{Csp}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Are}_{\mathrm{plasma\_rome}} &= \mathrm{Cre}_{\mathrm{plasma\_rome}} \cdot \mathrm{Vre}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xre}_{\mathrm{plasma\_rome}} &= \mathrm{Are}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mre}_{\mathrm{plasma\_rome}} &= \mathrm{Cre}_{\mathrm{plasma\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Aar}_{\mathrm{rome}} &= \mathrm{Car}_{\mathrm{rome}} \cdot \mathrm{Var} \\[1ex]
\mathrm{Xar}_{\mathrm{rome}} &= \mathrm{Aar}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mar}_{\mathrm{rome}} &= \mathrm{Car}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Ave}_{\mathrm{rome}} &= \mathrm{Cve}_{\mathrm{rome}} \cdot \mathrm{Vve} \\[1ex]
\mathrm{Xve}_{\mathrm{rome}} &= \mathrm{Ave}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mve}_{\mathrm{rome}} &= \mathrm{Cve}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Apo}_{\mathrm{rome}} &= \mathrm{Cpo}_{\mathrm{rome}} \cdot \mathrm{Vpo} \\[1ex]
\mathrm{Xpo}_{\mathrm{rome}} &= \mathrm{Apo}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mpo}_{\mathrm{rome}} &= \mathrm{Cpo}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Ahv}_{\mathrm{rome}} &= \mathrm{Chv}_{\mathrm{rome}} \cdot \mathrm{Vhv} \\[1ex]
\mathrm{Xhv}_{\mathrm{rome}} &= \mathrm{Ahv}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Mhv}_{\mathrm{rome}} &= \mathrm{Chv}_{\mathrm{rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} \\[1ex]
\mathrm{Agu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cgu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vgu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xgu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Agu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mgu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cgu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Aki}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cki}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vki}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xki}_{\mathrm{plasma\_omeoh}} &= \mathrm{Aki}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mki}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cki}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Ali}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cli}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vli}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xli}_{\mathrm{plasma\_omeoh}} &= \mathrm{Ali}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mli}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cli}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Alu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Clu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vlu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xlu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Alu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mlu}_{\mathrm{plasma\_omeoh}} &= \mathrm{Clu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Apa}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vpa}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xpa}_{\mathrm{plasma\_omeoh}} &= \mathrm{Apa}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mpa}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Asp}_{\mathrm{plasma\_omeoh}} &= \mathrm{Csp}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vsp}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xsp}_{\mathrm{plasma\_omeoh}} &= \mathrm{Asp}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Msp}_{\mathrm{plasma\_omeoh}} &= \mathrm{Csp}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Are}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cre}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Vre}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xre}_{\mathrm{plasma\_omeoh}} &= \mathrm{Are}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mre}_{\mathrm{plasma\_omeoh}} &= \mathrm{Cre}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Aar}_{\mathrm{omeoh}} &= \mathrm{Car}_{\mathrm{omeoh}} \cdot \mathrm{Var} \\[1ex]
\mathrm{Xar}_{\mathrm{omeoh}} &= \mathrm{Aar}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mar}_{\mathrm{omeoh}} &= \mathrm{Car}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Ave}_{\mathrm{omeoh}} &= \mathrm{Cve}_{\mathrm{omeoh}} \cdot \mathrm{Vve} \\[1ex]
\mathrm{Xve}_{\mathrm{omeoh}} &= \mathrm{Ave}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mve}_{\mathrm{omeoh}} &= \mathrm{Cve}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Apo}_{\mathrm{omeoh}} &= \mathrm{Cpo}_{\mathrm{omeoh}} \cdot \mathrm{Vpo} \\[1ex]
\mathrm{Xpo}_{\mathrm{omeoh}} &= \mathrm{Apo}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mpo}_{\mathrm{omeoh}} &= \mathrm{Cpo}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Ahv}_{\mathrm{omeoh}} &= \mathrm{Chv}_{\mathrm{omeoh}} \cdot \mathrm{Vhv} \\[1ex]
\mathrm{Xhv}_{\mathrm{omeoh}} &= \mathrm{Ahv}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Mhv}_{\mathrm{omeoh}} &= \mathrm{Chv}_{\mathrm{omeoh}} \cdot \mathrm{Mr}_{\mathrm{omeoh}} \\[1ex]
\mathrm{Agu}_{\mathrm{plasma\_omesul}} &= \mathrm{Cgu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vgu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xgu}_{\mathrm{plasma\_omesul}} &= \mathrm{Agu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mgu}_{\mathrm{plasma\_omesul}} &= \mathrm{Cgu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Aki}_{\mathrm{plasma\_omesul}} &= \mathrm{Cki}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vki}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xki}_{\mathrm{plasma\_omesul}} &= \mathrm{Aki}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mki}_{\mathrm{plasma\_omesul}} &= \mathrm{Cki}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Ali}_{\mathrm{plasma\_omesul}} &= \mathrm{Cli}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vli}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xli}_{\mathrm{plasma\_omesul}} &= \mathrm{Ali}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mli}_{\mathrm{plasma\_omesul}} &= \mathrm{Cli}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Alu}_{\mathrm{plasma\_omesul}} &= \mathrm{Clu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vlu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xlu}_{\mathrm{plasma\_omesul}} &= \mathrm{Alu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mlu}_{\mathrm{plasma\_omesul}} &= \mathrm{Clu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Apa}_{\mathrm{plasma\_omesul}} &= \mathrm{Cpa}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vpa}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xpa}_{\mathrm{plasma\_omesul}} &= \mathrm{Apa}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mpa}_{\mathrm{plasma\_omesul}} &= \mathrm{Cpa}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Asp}_{\mathrm{plasma\_omesul}} &= \mathrm{Csp}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vsp}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xsp}_{\mathrm{plasma\_omesul}} &= \mathrm{Asp}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Msp}_{\mathrm{plasma\_omesul}} &= \mathrm{Csp}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Are}_{\mathrm{plasma\_omesul}} &= \mathrm{Cre}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Vre}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xre}_{\mathrm{plasma\_omesul}} &= \mathrm{Are}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mre}_{\mathrm{plasma\_omesul}} &= \mathrm{Cre}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Aar}_{\mathrm{omesul}} &= \mathrm{Car}_{\mathrm{omesul}} \cdot \mathrm{Var} \\[1ex]
\mathrm{Xar}_{\mathrm{omesul}} &= \mathrm{Aar}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mar}_{\mathrm{omesul}} &= \mathrm{Car}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Ave}_{\mathrm{omesul}} &= \mathrm{Cve}_{\mathrm{omesul}} \cdot \mathrm{Vve} \\[1ex]
\mathrm{Xve}_{\mathrm{omesul}} &= \mathrm{Ave}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mve}_{\mathrm{omesul}} &= \mathrm{Cve}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Apo}_{\mathrm{omesul}} &= \mathrm{Cpo}_{\mathrm{omesul}} \cdot \mathrm{Vpo} \\[1ex]
\mathrm{Xpo}_{\mathrm{omesul}} &= \mathrm{Apo}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mpo}_{\mathrm{omesul}} &= \mathrm{Cpo}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Ahv}_{\mathrm{omesul}} &= \mathrm{Chv}_{\mathrm{omesul}} \cdot \mathrm{Vhv} \\[1ex]
\mathrm{Xhv}_{\mathrm{omesul}} &= \mathrm{Ahv}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Mhv}_{\mathrm{omesul}} &= \mathrm{Chv}_{\mathrm{omesul}} \cdot \mathrm{Mr}_{\mathrm{omesul}} \\[1ex]
\mathrm{Agu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cgu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vgu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xgu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Agu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mgu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cgu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Aki}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cki}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vki}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xki}_{\mathrm{plasma\_omeoth}} &= \mathrm{Aki}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mki}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cki}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Ali}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cli}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vli}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xli}_{\mathrm{plasma\_omeoth}} &= \mathrm{Ali}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mli}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cli}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Alu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Clu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vlu}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xlu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Alu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mlu}_{\mathrm{plasma\_omeoth}} &= \mathrm{Clu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Apa}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vpa}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xpa}_{\mathrm{plasma\_omeoth}} &= \mathrm{Apa}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mpa}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Asp}_{\mathrm{plasma\_omeoth}} &= \mathrm{Csp}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vsp}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xsp}_{\mathrm{plasma\_omeoth}} &= \mathrm{Asp}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Msp}_{\mathrm{plasma\_omeoth}} &= \mathrm{Csp}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Are}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cre}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Vre}_{\mathrm{plasma}} \\[1ex]
\mathrm{Xre}_{\mathrm{plasma\_omeoth}} &= \mathrm{Are}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mre}_{\mathrm{plasma\_omeoth}} &= \mathrm{Cre}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Aar}_{\mathrm{omeoth}} &= \mathrm{Car}_{\mathrm{omeoth}} \cdot \mathrm{Var} \\[1ex]
\mathrm{Xar}_{\mathrm{omeoth}} &= \mathrm{Aar}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mar}_{\mathrm{omeoth}} &= \mathrm{Car}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Ave}_{\mathrm{omeoth}} &= \mathrm{Cve}_{\mathrm{omeoth}} \cdot \mathrm{Vve} \\[1ex]
\mathrm{Xve}_{\mathrm{omeoth}} &= \mathrm{Ave}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mve}_{\mathrm{omeoth}} &= \mathrm{Cve}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Apo}_{\mathrm{omeoth}} &= \mathrm{Cpo}_{\mathrm{omeoth}} \cdot \mathrm{Vpo} \\[1ex]
\mathrm{Xpo}_{\mathrm{omeoth}} &= \mathrm{Apo}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mpo}_{\mathrm{omeoth}} &= \mathrm{Cpo}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Ahv}_{\mathrm{omeoth}} &= \mathrm{Chv}_{\mathrm{omeoth}} \cdot \mathrm{Vhv} \\[1ex]
\mathrm{Xhv}_{\mathrm{omeoth}} &= \mathrm{Ahv}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{Mhv}_{\mathrm{omeoth}} &= \mathrm{Chv}_{\mathrm{omeoth}} \cdot \mathrm{Mr}_{\mathrm{omeoth}} \\[1ex]
\mathrm{LI}_{\mathrm{\_cyp2c19\_activity}} &= \mathrm{LI}_{\mathrm{\_f\_cyp2c19}} \cdot \mathrm{LI}_{\mathrm{\_cyp2c19\_active}} \\[1ex]
\mathrm{LI}_{\mathrm{\_SOMECYP2C19\_rate}} &= \frac{\mathrm{LI}_{\mathrm{\_cyp2c19\_activity}} \cdot \mathrm{LI}_{\mathrm{\_CYP2C19\_Vmax\_some}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_some}}}{\mathrm{LI}_{\mathrm{\_CYP2C19\_Km}} + \mathrm{LI}_{\mathrm{\_some}}} \\[1ex]
\mathrm{LI}_{\mathrm{\_ROMECYP3A4\_rate}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_cyp3a4}} \cdot \mathrm{LI}_{\mathrm{\_CYP3A4\_Vmax\_rome}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_rome}}}{\mathrm{LI}_{\mathrm{\_CYP3A4\_Km}} + \mathrm{LI}_{\mathrm{\_rome}}} \\[1ex]
\mathrm{KI}_{\mathrm{\_GFR}} &= \mathrm{KI}_{\mathrm{\_f\_renal\_function}} \cdot \mathrm{GFR}_{\mathrm{base}} \\[1ex]
\mathrm{GU}_{\mathrm{\_pp\_total}} &= \mathrm{GU}_{\mathrm{\_pp\_active}} + \mathrm{GU}_{\mathrm{\_pp\_inactive}} \\[1ex]
\mathrm{pH} &= -\log_{10}\mathopen{}\left(\frac{\mathrm{GU}_{\mathrm{\_protons\_stomach}}}{1000}\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_F\_ome\_pH}} &= \mathrm{GU}_{\mathrm{\_F\_ome\_pH2}} + \frac{\mathopen{}\left(\mathrm{GU}_{\mathrm{\_F\_ome\_pH6}} - \mathrm{GU}_{\mathrm{\_F\_ome\_pH2}}\right) \cdot \mathopen{}\left(\max\mathopen{}\left(0, \mathrm{pH} - 2\right)\right)^{\mathrm{GU}_{\mathrm{\_F\_ome\_n}}}}{\mathopen{}\left(\max\mathopen{}\left(0, \mathrm{pH} - 2\right)\right)^{\mathrm{GU}_{\mathrm{\_F\_ome\_n}}} + \mathrm{GU}_{\mathrm{\_F\_ome\_KpH}}^{\mathrm{GU}_{\mathrm{\_F\_ome\_n}}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_F\_ome\_stomach}} &= 1 - \mathrm{GU}_{\mathrm{\_f\_unprotected}} \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_F\_ome\_pH}}\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_Ka\_emptying}} &= \mathopen{}\left(1 + \mathrm{GU}_{\mathrm{\_fed}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_FED\_f\_dissolution}} - 1\right)\right) \cdot \mathopen{}\left(\mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_ec}}\right) \cdot \mathrm{GU}_{\mathrm{\_Ka\_dis\_ome}} + \mathrm{GU}_{\mathrm{\_f\_ec}} \cdot \mathrm{GU}_{\mathrm{\_Ka\_ec\_ome}}\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}} &= \mathrm{GU}_{\mathrm{\_F\_ome\_abs}} \cdot \mathopen{}\left(1 + \mathrm{GU}_{\mathrm{\_fed}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_FED\_f\_absorption}} - 1\right)\right) \\[1ex]
\mathrm{GU}_{\mathrm{\_emptying\_some}} &= \frac{\frac{\mathrm{GU}_{\mathrm{\_Ka\_emptying}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{some}}}{\mathrm{GU}_{\mathrm{\_Mr\_ome}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_absorption\_some}} &= \mathrm{GU}_{\mathrm{\_OMEABS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{some}} \\[1ex]
\mathrm{GU}_{\mathrm{\_emptying\_rome}} &= \frac{\frac{\mathrm{GU}_{\mathrm{\_Ka\_emptying}}}{60} \cdot \mathrm{PODOSE}_{\mathrm{rome}}}{\mathrm{GU}_{\mathrm{\_Mr\_ome}}} \\[1ex]
\mathrm{GU}_{\mathrm{\_absorption\_rome}} &= \mathrm{GU}_{\mathrm{\_OMEABS\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{rome}} \\[1ex]
\mathrm{KI}_{\mathrm{\_OMEMETSEX}} &= v_{\mathrm{KI\_\_OMEOHEX}} + v_{\mathrm{KI\_\_OMEOTHEX}}
\end{aligned}
$$

## Reactions

| Rate | Id | Name | Equation | Modifiers |
| --- | --- | --- | --- | --- |
| $v_{\mathrm{transport\_lu\_some}}$ | `transport_lu_some` | transport S-omeprazole | $\mathrm{Clu}_{\mathrm{plasma\_some}} \rightleftharpoons \mathrm{Clu}_{\mathrm{some}}$ |  |
| $v_{\mathrm{transport\_pa\_some}}$ | `transport_pa_some` | transport S-omeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_some}} \rightleftharpoons \mathrm{Cpa}_{\mathrm{some}}$ |  |
| $v_{\mathrm{transport\_sp\_some}}$ | `transport_sp_some` | transport S-omeprazole | $\mathrm{Csp}_{\mathrm{plasma\_some}} \rightleftharpoons \mathrm{Csp}_{\mathrm{some}}$ |  |
| $v_{\mathrm{transport\_re\_some}}$ | `transport_re_some` | transport S-omeprazole | $\mathrm{Cre}_{\mathrm{plasma\_some}} \rightleftharpoons \mathrm{Cre}_{\mathrm{some}}$ |  |
| $v_{\mathrm{iv\_some}}$ | `iv_some` | iv S-omeprazole | $\varnothing \longrightarrow \mathrm{Cve}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ve\_lu\_some}}$ | `Flow_ve_lu_some` | blood flow S-omeprazole | $\mathrm{Cve}_{\mathrm{some}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_lu\_ar\_some}}$ | `Flow_lu_ar_some` | blood flow S-omeprazole | $\mathrm{Clu}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Car}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ar\_ki\_some}}$ | `Flow_ar_ki_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_ki\_ve\_some}}$ | `Flow_ki_ve_some` | blood flow S-omeprazole | $\mathrm{Cki}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Cve}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ar\_re\_some}}$ | `Flow_ar_re_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_re\_ve\_some}}$ | `Flow_re_ve_some` | blood flow S-omeprazole | $\mathrm{Cre}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Cve}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ar\_gu\_some}}$ | `Flow_ar_gu_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_gu\_po\_some}}$ | `Flow_gu_po_some` | blood flow S-omeprazole | $\mathrm{Cgu}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Cpo}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ar\_sp\_some}}$ | `Flow_ar_sp_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Csp}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_sp\_po\_some}}$ | `Flow_sp_po_some` | blood flow S-omeprazole | $\mathrm{Csp}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Cpo}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_ar\_pa\_some}}$ | `Flow_ar_pa_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Cpa}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_pa\_po\_some}}$ | `Flow_pa_po_some` | blood flow S-omeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Cpo}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_arli\_li\_some}}$ | `Flow_arli_li_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_arli\_hv\_some}}$ | `Flow_arli_hv_some` | blood flow S-omeprazole | $\mathrm{Car}_{\mathrm{some}} \longrightarrow \mathrm{Chv}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_po\_li\_some}}$ | `Flow_po_li_some` | blood flow S-omeprazole | $\mathrm{Cpo}_{\mathrm{some}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{Flow\_po\_hv\_some}}$ | `Flow_po_hv_some` | blood flow S-omeprazole | $\mathrm{Cpo}_{\mathrm{some}} \longrightarrow \mathrm{Chv}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_li\_hv\_some}}$ | `Flow_li_hv_some` | blood flow S-omeprazole | $\mathrm{Cli}_{\mathrm{plasma\_some}} \longrightarrow \mathrm{Chv}_{\mathrm{some}}$ |  |
| $v_{\mathrm{Flow\_hv\_ve\_some}}$ | `Flow_hv_ve_some` | blood flow S-omeprazole | $\mathrm{Chv}_{\mathrm{some}} \longrightarrow \mathrm{Cve}_{\mathrm{some}}$ |  |
| $v_{\mathrm{transport\_lu\_rome}}$ | `transport_lu_rome` | transport R-omeprazole | $\mathrm{Clu}_{\mathrm{plasma\_rome}} \rightleftharpoons \mathrm{Clu}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{transport\_pa\_rome}}$ | `transport_pa_rome` | transport R-omeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_rome}} \rightleftharpoons \mathrm{Cpa}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{transport\_sp\_rome}}$ | `transport_sp_rome` | transport R-omeprazole | $\mathrm{Csp}_{\mathrm{plasma\_rome}} \rightleftharpoons \mathrm{Csp}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{transport\_re\_rome}}$ | `transport_re_rome` | transport R-omeprazole | $\mathrm{Cre}_{\mathrm{plasma\_rome}} \rightleftharpoons \mathrm{Cre}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{iv\_rome}}$ | `iv_rome` | iv R-omeprazole | $\varnothing \longrightarrow \mathrm{Cve}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ve\_lu\_rome}}$ | `Flow_ve_lu_rome` | blood flow R-omeprazole | $\mathrm{Cve}_{\mathrm{rome}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_lu\_ar\_rome}}$ | `Flow_lu_ar_rome` | blood flow R-omeprazole | $\mathrm{Clu}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Car}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ar\_ki\_rome}}$ | `Flow_ar_ki_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_ki\_ve\_rome}}$ | `Flow_ki_ve_rome` | blood flow R-omeprazole | $\mathrm{Cki}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Cve}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ar\_re\_rome}}$ | `Flow_ar_re_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_re\_ve\_rome}}$ | `Flow_re_ve_rome` | blood flow R-omeprazole | $\mathrm{Cre}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Cve}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ar\_gu\_rome}}$ | `Flow_ar_gu_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_gu\_po\_rome}}$ | `Flow_gu_po_rome` | blood flow R-omeprazole | $\mathrm{Cgu}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Cpo}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ar\_sp\_rome}}$ | `Flow_ar_sp_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Csp}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_sp\_po\_rome}}$ | `Flow_sp_po_rome` | blood flow R-omeprazole | $\mathrm{Csp}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Cpo}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_ar\_pa\_rome}}$ | `Flow_ar_pa_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Cpa}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_pa\_po\_rome}}$ | `Flow_pa_po_rome` | blood flow R-omeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Cpo}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_arli\_li\_rome}}$ | `Flow_arli_li_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_arli\_hv\_rome}}$ | `Flow_arli_hv_rome` | blood flow R-omeprazole | $\mathrm{Car}_{\mathrm{rome}} \longrightarrow \mathrm{Chv}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_po\_li\_rome}}$ | `Flow_po_li_rome` | blood flow R-omeprazole | $\mathrm{Cpo}_{\mathrm{rome}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{Flow\_po\_hv\_rome}}$ | `Flow_po_hv_rome` | blood flow R-omeprazole | $\mathrm{Cpo}_{\mathrm{rome}} \longrightarrow \mathrm{Chv}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_li\_hv\_rome}}$ | `Flow_li_hv_rome` | blood flow R-omeprazole | $\mathrm{Cli}_{\mathrm{plasma\_rome}} \longrightarrow \mathrm{Chv}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{Flow\_hv\_ve\_rome}}$ | `Flow_hv_ve_rome` | blood flow R-omeprazole | $\mathrm{Chv}_{\mathrm{rome}} \longrightarrow \mathrm{Cve}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{transport\_lu\_omeoh}}$ | `transport_lu_omeoh` | transport 5-hydroxyomeprazole | $\mathrm{Clu}_{\mathrm{plasma\_omeoh}} \rightleftharpoons \mathrm{Clu}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{transport\_pa\_omeoh}}$ | `transport_pa_omeoh` | transport 5-hydroxyomeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \rightleftharpoons \mathrm{Cpa}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{transport\_sp\_omeoh}}$ | `transport_sp_omeoh` | transport 5-hydroxyomeprazole | $\mathrm{Csp}_{\mathrm{plasma\_omeoh}} \rightleftharpoons \mathrm{Csp}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{transport\_re\_omeoh}}$ | `transport_re_omeoh` | transport 5-hydroxyomeprazole | $\mathrm{Cre}_{\mathrm{plasma\_omeoh}} \rightleftharpoons \mathrm{Cre}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ve\_lu\_omeoh}}$ | `Flow_ve_lu_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cve}_{\mathrm{omeoh}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_lu\_ar\_omeoh}}$ | `Flow_lu_ar_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Clu}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Car}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ar\_ki\_omeoh}}$ | `Flow_ar_ki_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_ki\_ve\_omeoh}}$ | `Flow_ki_ve_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cki}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ar\_re\_omeoh}}$ | `Flow_ar_re_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_re\_ve\_omeoh}}$ | `Flow_re_ve_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cre}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ar\_gu\_omeoh}}$ | `Flow_ar_gu_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_gu\_po\_omeoh}}$ | `Flow_gu_po_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cgu}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ar\_sp\_omeoh}}$ | `Flow_ar_sp_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Csp}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_sp\_po\_omeoh}}$ | `Flow_sp_po_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Csp}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_ar\_pa\_omeoh}}$ | `Flow_ar_pa_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cpa}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_pa\_po\_omeoh}}$ | `Flow_pa_po_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_arli\_li\_omeoh}}$ | `Flow_arli_li_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_arli\_hv\_omeoh}}$ | `Flow_arli_hv_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Car}_{\mathrm{omeoh}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_po\_li\_omeoh}}$ | `Flow_po_li_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cpo}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{Flow\_po\_hv\_omeoh}}$ | `Flow_po_hv_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cpo}_{\mathrm{omeoh}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_li\_hv\_omeoh}}$ | `Flow_li_hv_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Cli}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{Flow\_hv\_ve\_omeoh}}$ | `Flow_hv_ve_omeoh` | blood flow 5-hydroxyomeprazole | $\mathrm{Chv}_{\mathrm{omeoh}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{transport\_lu\_omesul}}$ | `transport_lu_omesul` | transport omeprazole sulfone | $\mathrm{Clu}_{\mathrm{plasma\_omesul}} \rightleftharpoons \mathrm{Clu}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{transport\_pa\_omesul}}$ | `transport_pa_omesul` | transport omeprazole sulfone | $\mathrm{Cpa}_{\mathrm{plasma\_omesul}} \rightleftharpoons \mathrm{Cpa}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{transport\_sp\_omesul}}$ | `transport_sp_omesul` | transport omeprazole sulfone | $\mathrm{Csp}_{\mathrm{plasma\_omesul}} \rightleftharpoons \mathrm{Csp}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{transport\_re\_omesul}}$ | `transport_re_omesul` | transport omeprazole sulfone | $\mathrm{Cre}_{\mathrm{plasma\_omesul}} \rightleftharpoons \mathrm{Cre}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ve\_lu\_omesul}}$ | `Flow_ve_lu_omesul` | blood flow omeprazole sulfone | $\mathrm{Cve}_{\mathrm{omesul}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_lu\_ar\_omesul}}$ | `Flow_lu_ar_omesul` | blood flow omeprazole sulfone | $\mathrm{Clu}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Car}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ar\_ki\_omesul}}$ | `Flow_ar_ki_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_ki\_ve\_omesul}}$ | `Flow_ki_ve_omesul` | blood flow omeprazole sulfone | $\mathrm{Cki}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Cve}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ar\_re\_omesul}}$ | `Flow_ar_re_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_re\_ve\_omesul}}$ | `Flow_re_ve_omesul` | blood flow omeprazole sulfone | $\mathrm{Cre}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Cve}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ar\_gu\_omesul}}$ | `Flow_ar_gu_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_gu\_po\_omesul}}$ | `Flow_gu_po_omesul` | blood flow omeprazole sulfone | $\mathrm{Cgu}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Cpo}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ar\_sp\_omesul}}$ | `Flow_ar_sp_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Csp}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_sp\_po\_omesul}}$ | `Flow_sp_po_omesul` | blood flow omeprazole sulfone | $\mathrm{Csp}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Cpo}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_ar\_pa\_omesul}}$ | `Flow_ar_pa_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Cpa}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_pa\_po\_omesul}}$ | `Flow_pa_po_omesul` | blood flow omeprazole sulfone | $\mathrm{Cpa}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Cpo}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_arli\_li\_omesul}}$ | `Flow_arli_li_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_arli\_hv\_omesul}}$ | `Flow_arli_hv_omesul` | blood flow omeprazole sulfone | $\mathrm{Car}_{\mathrm{omesul}} \longrightarrow \mathrm{Chv}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_po\_li\_omesul}}$ | `Flow_po_li_omesul` | blood flow omeprazole sulfone | $\mathrm{Cpo}_{\mathrm{omesul}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{Flow\_po\_hv\_omesul}}$ | `Flow_po_hv_omesul` | blood flow omeprazole sulfone | $\mathrm{Cpo}_{\mathrm{omesul}} \longrightarrow \mathrm{Chv}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_li\_hv\_omesul}}$ | `Flow_li_hv_omesul` | blood flow omeprazole sulfone | $\mathrm{Cli}_{\mathrm{plasma\_omesul}} \longrightarrow \mathrm{Chv}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{Flow\_hv\_ve\_omesul}}$ | `Flow_hv_ve_omesul` | blood flow omeprazole sulfone | $\mathrm{Chv}_{\mathrm{omesul}} \longrightarrow \mathrm{Cve}_{\mathrm{omesul}}$ |  |
| $v_{\mathrm{transport\_lu\_omeoth}}$ | `transport_lu_omeoth` | transport other omeprazole metabolites | $\mathrm{Clu}_{\mathrm{plasma\_omeoth}} \rightleftharpoons \mathrm{Clu}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{transport\_pa\_omeoth}}$ | `transport_pa_omeoth` | transport other omeprazole metabolites | $\mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \rightleftharpoons \mathrm{Cpa}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{transport\_sp\_omeoth}}$ | `transport_sp_omeoth` | transport other omeprazole metabolites | $\mathrm{Csp}_{\mathrm{plasma\_omeoth}} \rightleftharpoons \mathrm{Csp}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{transport\_re\_omeoth}}$ | `transport_re_omeoth` | transport other omeprazole metabolites | $\mathrm{Cre}_{\mathrm{plasma\_omeoth}} \rightleftharpoons \mathrm{Cre}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ve\_lu\_omeoth}}$ | `Flow_ve_lu_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cve}_{\mathrm{omeoth}} \longrightarrow \mathrm{Clu}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_lu\_ar\_omeoth}}$ | `Flow_lu_ar_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Clu}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Car}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ar\_ki\_omeoth}}$ | `Flow_ar_ki_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cki}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_ki\_ve\_omeoth}}$ | `Flow_ki_ve_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cki}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ar\_re\_omeoth}}$ | `Flow_ar_re_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cre}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_re\_ve\_omeoth}}$ | `Flow_re_ve_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cre}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ar\_gu\_omeoth}}$ | `Flow_ar_gu_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_gu\_po\_omeoth}}$ | `Flow_gu_po_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cgu}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ar\_sp\_omeoth}}$ | `Flow_ar_sp_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Csp}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_sp\_po\_omeoth}}$ | `Flow_sp_po_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Csp}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_ar\_pa\_omeoth}}$ | `Flow_ar_pa_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cpa}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_pa\_po\_omeoth}}$ | `Flow_pa_po_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Cpo}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_arli\_li\_omeoth}}$ | `Flow_arli_li_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_arli\_hv\_omeoth}}$ | `Flow_arli_hv_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Car}_{\mathrm{omeoth}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_po\_li\_omeoth}}$ | `Flow_po_li_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cpo}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{Flow\_po\_hv\_omeoth}}$ | `Flow_po_hv_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cpo}_{\mathrm{omeoth}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_li\_hv\_omeoth}}$ | `Flow_li_hv_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Cli}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Chv}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{Flow\_hv\_ve\_omeoth}}$ | `Flow_hv_ve_omeoth` | blood flow other omeprazole metabolites | $\mathrm{Chv}_{\mathrm{omeoth}} \longrightarrow \mathrm{Cve}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{LI\_\_SOMEIM}}$ | `LI__SOMEIM` | S-omeprazole exchange plasma and liver | $\mathrm{Cli}_{\mathrm{plasma\_some}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_some}}$ |  |
| $v_{\mathrm{LI\_\_ROMEIM}}$ | `LI__ROMEIM` | R-omeprazole exchange plasma and liver | $\mathrm{Cli}_{\mathrm{plasma\_rome}} \rightleftharpoons \mathrm{LI}_{\mathrm{\_rome}}$ |  |
| $v_{\mathrm{LI\_\_SOMECYP2C19}}$ | `LI__SOMECYP2C19` | S-omeprazole to 5-O-desmethylomeprazole (CYP2C19) | $\mathrm{LI}_{\mathrm{\_some}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoth}}$ |  |
| $v_{\mathrm{LI\_\_SOMECYP2C19OH}}$ | `LI__SOMECYP2C19OH` | S-omeprazole to 5-hydroxyomeprazole (CYP2C19) | $\mathrm{LI}_{\mathrm{\_some}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoh}}$ |  |
| $v_{\mathrm{LI\_\_ROMECYP2C19}}$ | `LI__ROMECYP2C19` | R-omeprazole to 5-hydroxyomeprazole (CYP2C19) | $\mathrm{LI}_{\mathrm{\_rome}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoh}}$ |  |
| $v_{\mathrm{LI\_\_SOMECYP3A4}}$ | `LI__SOMECYP3A4` | S-omeprazole to omeprazole sulfone (CYP3A4) | $\mathrm{LI}_{\mathrm{\_some}} \longrightarrow \mathrm{LI}_{\mathrm{\_omesul}}$ |  |
| $v_{\mathrm{LI\_\_ROMECYP3A4}}$ | `LI__ROMECYP3A4` | R-omeprazole to omeprazole sulfone (CYP3A4) | $\mathrm{LI}_{\mathrm{\_rome}} \longrightarrow \mathrm{LI}_{\mathrm{\_omesul}}$ |  |
| $v_{\mathrm{LI\_\_ROMECYP3A4OH}}$ | `LI__ROMECYP3A4OH` | R-omeprazole to 5-hydroxyomeprazole (CYP3A4) | $\mathrm{LI}_{\mathrm{\_rome}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoh}}$ |  |
| $v_{\mathrm{LI\_\_OMEOHEX}}$ | `LI__OMEOHEX` | 5-hydroxyomeprazole release | $\mathrm{LI}_{\mathrm{\_omeoh}} \longrightarrow \mathrm{Cli}_{\mathrm{plasma\_omeoh}}$ |  |
| $v_{\mathrm{LI\_\_OMEOHM}}$ | `LI__OMEOHM` | 5-hydroxyomeprazole oxidation | $\mathrm{LI}_{\mathrm{\_omeoh}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoth}}$ |  |
| $v_{\mathrm{LI\_\_OMESULEX}}$ | `LI__OMESULEX` | omeprazole sulfone exchange liver and plasma | $\mathrm{LI}_{\mathrm{\_omesul}} \rightleftharpoons \mathrm{Cli}_{\mathrm{plasma\_omesul}}$ |  |
| $v_{\mathrm{LI\_\_OMESULM}}$ | `LI__OMESULM` | omeprazole sulfone metabolism | $\mathrm{LI}_{\mathrm{\_omesul}} \longrightarrow \mathrm{LI}_{\mathrm{\_omeoth}}$ |  |
| $v_{\mathrm{LI\_\_OMEOTHEX}}$ | `LI__OMEOTHEX` | other metabolites exchange liver and plasma | $\mathrm{LI}_{\mathrm{\_omeoth}} \rightleftharpoons \mathrm{Cli}_{\mathrm{plasma\_omeoth}}$ |  |
| $v_{\mathrm{LI\_\_OMEOTHBIL}}$ | `LI__OMEOTHBIL` | other metabolites biliary excretion | $\mathrm{LI}_{\mathrm{\_omeoth}} \longrightarrow \mathrm{Cgu}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{KI\_\_OMEOHEX}}$ | `KI__OMEOHEX` | 5-hydroxyomeprazole renal excretion | $\mathrm{Cki}_{\mathrm{plasma\_omeoh}} \longrightarrow \mathrm{Aurine}_{\mathrm{omeoh}}$ |  |
| $v_{\mathrm{KI\_\_OMEOTHEX}}$ | `KI__OMEOTHEX` | other omeprazole metabolites renal excretion | $\mathrm{Cki}_{\mathrm{plasma\_omeoth}} \longrightarrow \mathrm{Aurine}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{GU\_\_pp\_rate}}$ | `GU__pp_rate` | Proton secretion by proton pump | $\varnothing \longrightarrow \mathrm{GU}_{\mathrm{\_protons\_stomach}}$ | $\mathrm{GU}_{\mathrm{\_pp\_active}}$ |
| $v_{\mathrm{GU\_\_gacid\_loss}}$ | `GU__gacid_loss` | Gastric acid loss to intestine | $\mathrm{GU}_{\mathrm{\_protons\_stomach}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{GU\_\_ppi}}$ | `GU__ppi` | PP inhibition | $\mathrm{GU}_{\mathrm{\_pp\_active}} \longrightarrow \mathrm{GU}_{\mathrm{\_pp\_inactive}}$ | $\mathrm{Cgu}_{\mathrm{plasma\_some}}, \mathrm{Cgu}_{\mathrm{plasma\_rome}}$ |
| $v_{\mathrm{GU\_\_pp\_synthesis}}$ | `GU__pp_synthesis` | PP synthesis | $\varnothing \longrightarrow \mathrm{GU}_{\mathrm{\_pp\_active}}$ |  |
| $v_{\mathrm{GU\_\_pp\_active\_degradation}}$ | `GU__pp_active_degradation` | degradation PP active | $\mathrm{GU}_{\mathrm{\_pp\_active}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{GU\_\_pp\_inactive\_degradation}}$ | `GU__pp_inactive_degradation` | degradation PP inactive | $\mathrm{GU}_{\mathrm{\_pp\_inactive}} \longrightarrow \varnothing$ |  |
| $v_{\mathrm{GU\_\_OMEOTHEXC}}$ | `GU__OMEOTHEXC` | excretion other metabolites (feces) | $\mathrm{Cgu}_{\mathrm{omeoth}} \longrightarrow \mathrm{Afeces}_{\mathrm{omeoth}}$ |  |
| $v_{\mathrm{GU\_\_dissolution\_some}}$ | `GU__dissolution_some` | gastric emptying of the solution S-omeprazole | $\mathrm{GU}_{\mathrm{\_some\_stomach}} \longrightarrow \mathrm{Cgu}_{\mathrm{some}}$ |  |
| $v_{\mathrm{GU\_\_degradation\_some}}$ | `GU__degradation_some` | acid degradation S-omeprazole | $\mathrm{GU}_{\mathrm{\_some\_stomach}} \longrightarrow \varnothing$ | $\mathrm{GU}_{\mathrm{\_protons\_stomach}}$ |
| $v_{\mathrm{GU\_\_release\_some}}$ | `GU__release_some` | release from the enteric-coated pellets S-omeprazole | $\mathrm{GU}_{\mathrm{\_some\_stomach}} \longrightarrow \mathrm{Cgu}_{\mathrm{some}}$ |  |
| $v_{\mathrm{GU\_\_SOMEABS}}$ | `GU__SOMEABS` | absorption S-omeprazole | $\mathrm{Cgu}_{\mathrm{some}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_some}}$ |  |
| $v_{\mathrm{GU\_\_SOMEEXC}}$ | `GU__SOMEEXC` | excretion S-omeprazole (feces) | $\mathrm{Cgu}_{\mathrm{some}} \longrightarrow \mathrm{Afeces}_{\mathrm{some}}$ |  |
| $v_{\mathrm{GU\_\_dissolution\_rome}}$ | `GU__dissolution_rome` | gastric emptying of the solution R-omeprazole | $\mathrm{GU}_{\mathrm{\_rome\_stomach}} \longrightarrow \mathrm{Cgu}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{GU\_\_degradation\_rome}}$ | `GU__degradation_rome` | acid degradation R-omeprazole | $\mathrm{GU}_{\mathrm{\_rome\_stomach}} \longrightarrow \varnothing$ | $\mathrm{GU}_{\mathrm{\_protons\_stomach}}$ |
| $v_{\mathrm{GU\_\_release\_rome}}$ | `GU__release_rome` | release from the enteric-coated pellets R-omeprazole | $\mathrm{GU}_{\mathrm{\_rome\_stomach}} \longrightarrow \mathrm{Cgu}_{\mathrm{rome}}$ |  |
| $v_{\mathrm{GU\_\_ROMEABS}}$ | `GU__ROMEABS` | absorption R-omeprazole | $\mathrm{Cgu}_{\mathrm{rome}} \longrightarrow \mathrm{Cgu}_{\mathrm{plasma\_rome}}$ |  |
| $v_{\mathrm{GU\_\_ROMEEXC}}$ | `GU__ROMEEXC` | excretion R-omeprazole (feces) | $\mathrm{Cgu}_{\mathrm{rome}} \longrightarrow \mathrm{Afeces}_{\mathrm{rome}}$ |  |

The rates of the reactions are:

$$
\begin{aligned}
v_{\mathrm{transport\_lu\_some}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_some}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Clu}_{\mathrm{some}}\right) \\[1ex]
v_{\mathrm{transport\_pa\_some}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cpa}_{\mathrm{plasma\_some}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cpa}_{\mathrm{some}}\right) \\[1ex]
v_{\mathrm{transport\_sp\_some}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Csp}_{\mathrm{plasma\_some}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Csp}_{\mathrm{some}}\right) \\[1ex]
v_{\mathrm{transport\_re\_some}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_some}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cre}_{\mathrm{some}}\right) \\[1ex]
v_{\mathrm{iv\_some}} &= \frac{\mathrm{Ki}_{\mathrm{some}} \cdot \mathrm{IVDOSE}_{\mathrm{some}}}{\mathrm{Mr}_{\mathrm{some}}} \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_some}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cve}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_some}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Clu}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_some}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_some}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cki}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_some}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_some}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cre}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_some}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_some}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_ar\_sp\_some}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_sp\_po\_some}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Csp}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_ar\_pa\_some}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_pa\_po\_some}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cpa}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_some}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_some}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Car}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_some}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cpo}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_some}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cpo}_{\mathrm{some}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_some}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Cli}_{\mathrm{plasma\_some}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_some}} &= \mathrm{Qh} \cdot \mathrm{BP}_{\mathrm{some}} \cdot \mathrm{Chv}_{\mathrm{some}} \\[1ex]
v_{\mathrm{transport\_lu\_rome}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_rome}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Clu}_{\mathrm{rome}}\right) \\[1ex]
v_{\mathrm{transport\_pa\_rome}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cpa}_{\mathrm{plasma\_rome}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cpa}_{\mathrm{rome}}\right) \\[1ex]
v_{\mathrm{transport\_sp\_rome}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Csp}_{\mathrm{plasma\_rome}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Csp}_{\mathrm{rome}}\right) \\[1ex]
v_{\mathrm{transport\_re\_rome}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_rome}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cre}_{\mathrm{rome}}\right) \\[1ex]
v_{\mathrm{iv\_rome}} &= \frac{\mathrm{Ki}_{\mathrm{rome}} \cdot \mathrm{IVDOSE}_{\mathrm{rome}}}{\mathrm{Mr}_{\mathrm{rome}}} \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_rome}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cve}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_rome}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Clu}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_rome}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_rome}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cki}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_rome}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_rome}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cre}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_rome}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_rome}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_ar\_sp\_rome}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_sp\_po\_rome}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Csp}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_ar\_pa\_rome}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_pa\_po\_rome}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cpa}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_rome}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_rome}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Car}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_rome}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cpo}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_rome}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cpo}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_rome}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Cli}_{\mathrm{plasma\_rome}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_rome}} &= \mathrm{Qh} \cdot \mathrm{BP}_{\mathrm{rome}} \cdot \mathrm{Chv}_{\mathrm{rome}} \\[1ex]
v_{\mathrm{transport\_lu\_omeoh}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Clu}_{\mathrm{omeoh}}\right) \\[1ex]
v_{\mathrm{transport\_pa\_omeoh}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cpa}_{\mathrm{omeoh}}\right) \\[1ex]
v_{\mathrm{transport\_sp\_omeoh}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Csp}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Csp}_{\mathrm{omeoh}}\right) \\[1ex]
v_{\mathrm{transport\_re\_omeoh}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_omeoh}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cre}_{\mathrm{omeoh}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_omeoh}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cve}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_omeoh}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Clu}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_omeoh}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_omeoh}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cki}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_omeoh}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_omeoh}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cre}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_omeoh}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_omeoh}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_sp\_omeoh}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_sp\_po\_omeoh}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Csp}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_ar\_pa\_omeoh}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_pa\_po\_omeoh}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cpa}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_omeoh}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_omeoh}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Car}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_omeoh}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cpo}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_omeoh}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cpo}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_omeoh}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Cli}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_omeoh}} &= \mathrm{Qh} \cdot \mathrm{BP}_{\mathrm{omeoh}} \cdot \mathrm{Chv}_{\mathrm{omeoh}} \\[1ex]
v_{\mathrm{transport\_lu\_omesul}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Clu}_{\mathrm{omesul}}\right) \\[1ex]
v_{\mathrm{transport\_pa\_omesul}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cpa}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cpa}_{\mathrm{omesul}}\right) \\[1ex]
v_{\mathrm{transport\_sp\_omesul}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Csp}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Csp}_{\mathrm{omesul}}\right) \\[1ex]
v_{\mathrm{transport\_re\_omesul}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_omesul}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cre}_{\mathrm{omesul}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_omesul}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cve}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_omesul}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Clu}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_omesul}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_omesul}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cki}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_omesul}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_omesul}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cre}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_omesul}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_omesul}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_ar\_sp\_omesul}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_sp\_po\_omesul}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Csp}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_ar\_pa\_omesul}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_pa\_po\_omesul}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cpa}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_omesul}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_omesul}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Car}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_omesul}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cpo}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_omesul}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cpo}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_omesul}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Cli}_{\mathrm{plasma\_omesul}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_omesul}} &= \mathrm{Qh} \cdot \mathrm{BP}_{\mathrm{omesul}} \cdot \mathrm{Chv}_{\mathrm{omesul}} \\[1ex]
v_{\mathrm{transport\_lu\_omeoth}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Clu}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Clu}_{\mathrm{omeoth}}\right) \\[1ex]
v_{\mathrm{transport\_pa\_omeoth}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cpa}_{\mathrm{omeoth}}\right) \\[1ex]
v_{\mathrm{transport\_sp\_omeoth}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Csp}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Csp}_{\mathrm{omeoth}}\right) \\[1ex]
v_{\mathrm{transport\_re\_omeoth}} &= \frac{\mathrm{ftissue}_{\mathrm{ome}} \cdot \mathrm{BW}}{\mathrm{BW}_{\mathrm{ref}}} \cdot \mathopen{}\left(\mathrm{Cre}_{\mathrm{plasma\_omeoth}} \cdot \mathrm{Kp}_{\mathrm{ome}} - \mathrm{Cre}_{\mathrm{omeoth}}\right) \\[1ex]
v_{\mathrm{Flow\_ve\_lu\_omeoth}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cve}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_lu\_ar\_omeoth}} &= \mathrm{Qlu} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Clu}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_ar\_ki\_omeoth}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_ki\_ve\_omeoth}} &= \mathrm{Qki} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cki}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_ar\_re\_omeoth}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_re\_ve\_omeoth}} &= \mathrm{Qre} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cre}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_ar\_gu\_omeoth}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_gu\_po\_omeoth}} &= \mathrm{Qgu} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cgu}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_ar\_sp\_omeoth}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_sp\_po\_omeoth}} &= \mathrm{Qsp} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Csp}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_ar\_pa\_omeoth}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_pa\_po\_omeoth}} &= \mathrm{Qpa} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cpa}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_arli\_li\_omeoth}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_arli\_hv\_omeoth}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qha} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Car}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_po\_li\_omeoth}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cpo}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_po\_hv\_omeoth}} &= f_{\mathrm{shunts}} \cdot \mathrm{Qpo} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cpo}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{Flow\_li\_hv\_omeoth}} &= \mathopen{}\left(1 - f_{\mathrm{shunts}}\right) \cdot \mathopen{}\left(\mathrm{Qpo} + \mathrm{Qha}\right) \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Cli}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{Flow\_hv\_ve\_omeoth}} &= \mathrm{Qh} \cdot \mathrm{BP}_{\mathrm{omeoth}} \cdot \mathrm{Chv}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{LI\_\_SOMEIM}} &= \mathrm{LI}_{\mathrm{\_OMEIM\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{Cli}_{\mathrm{plasma\_some}} - \mathrm{LI}_{\mathrm{\_some}}\right) \\[1ex]
v_{\mathrm{LI\_\_ROMEIM}} &= \mathrm{LI}_{\mathrm{\_OMEIM\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{Cli}_{\mathrm{plasma\_rome}} - \mathrm{LI}_{\mathrm{\_rome}}\right) \\[1ex]
v_{\mathrm{LI\_\_SOMECYP2C19}} &= \mathopen{}\left(1 - \mathrm{LI}_{\mathrm{\_f\_some\_omeoh}}\right) \cdot \mathrm{LI}_{\mathrm{\_SOMECYP2C19\_rate}} \\[1ex]
v_{\mathrm{LI\_\_SOMECYP2C19OH}} &= \mathrm{LI}_{\mathrm{\_f\_some\_omeoh}} \cdot \mathrm{LI}_{\mathrm{\_SOMECYP2C19\_rate}} \\[1ex]
v_{\mathrm{LI\_\_ROMECYP2C19}} &= \frac{\mathrm{LI}_{\mathrm{\_cyp2c19\_activity}} \cdot \mathrm{LI}_{\mathrm{\_CYP2C19\_Vmax\_rome}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_rome}}}{\mathrm{LI}_{\mathrm{\_CYP2C19\_Km}} + \mathrm{LI}_{\mathrm{\_rome}}} \\[1ex]
v_{\mathrm{LI\_\_SOMECYP3A4}} &= \frac{\mathrm{LI}_{\mathrm{\_f\_cyp3a4}} \cdot \mathrm{LI}_{\mathrm{\_CYP3A4\_Vmax\_some}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_some}}}{\mathrm{LI}_{\mathrm{\_CYP3A4\_Km}} + \mathrm{LI}_{\mathrm{\_some}}} \\[1ex]
v_{\mathrm{LI\_\_ROMECYP3A4}} &= \mathopen{}\left(1 - \mathrm{LI}_{\mathrm{\_f\_rome\_cyp3a4\_omeoh}}\right) \cdot \mathrm{LI}_{\mathrm{\_ROMECYP3A4\_rate}} \\[1ex]
v_{\mathrm{LI\_\_ROMECYP3A4OH}} &= \mathrm{LI}_{\mathrm{\_f\_rome\_cyp3a4\_omeoh}} \cdot \mathrm{LI}_{\mathrm{\_ROMECYP3A4\_rate}} \\[1ex]
v_{\mathrm{LI\_\_OMEOHEX}} &= \mathrm{LI}_{\mathrm{\_OMEOHEX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_omeoh}} \\[1ex]
v_{\mathrm{LI\_\_OMEOHM}} &= \mathrm{LI}_{\mathrm{\_OMEOHM\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_omeoh}} \\[1ex]
v_{\mathrm{LI\_\_OMESULEX}} &= \mathrm{LI}_{\mathrm{\_OMEMEX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_omesul}} - \mathrm{Cli}_{\mathrm{plasma\_omesul}}\right) \\[1ex]
v_{\mathrm{LI\_\_OMESULM}} &= \mathopen{}\left(\mathrm{LI}_{\mathrm{\_cyp2c19\_activity}} \cdot \mathrm{LI}_{\mathrm{\_OMESUL2C19\_k}} + \mathrm{LI}_{\mathrm{\_OMESULM\_k}}\right) \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_omesul}} \\[1ex]
v_{\mathrm{LI\_\_OMEOTHEX}} &= \mathrm{LI}_{\mathrm{\_OMEMEX\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_omeoth}} - \mathrm{Cli}_{\mathrm{plasma\_omeoth}}\right) \\[1ex]
v_{\mathrm{LI\_\_OMEOTHBIL}} &= \mathrm{LI}_{\mathrm{\_OMEOTHBIL\_k}} \cdot \mathrm{Vli}_{\mathrm{tissue}} \cdot \mathrm{LI}_{\mathrm{\_omeoth}} \\[1ex]
v_{\mathrm{KI\_\_OMEOHEX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_OMEOHEX\_f}} \cdot \mathrm{Cki}_{\mathrm{plasma\_omeoh}} \\[1ex]
v_{\mathrm{KI\_\_OMEOTHEX}} &= \mathrm{KI}_{\mathrm{\_GFR}} \cdot 0.001 \cdot \mathrm{KI}_{\mathrm{\_OMEOTHEX\_f}} \cdot \mathrm{Cki}_{\mathrm{plasma\_omeoth}} \\[1ex]
v_{\mathrm{GU\_\_pp\_rate}} &= \mathrm{GU}_{\mathrm{\_pp\_rate\_k}} \cdot 10^{\frac{-1.1}{\mathrm{GU}_{\mathrm{\_pp\_active}} + 0.1} + 1} \\[1ex]
v_{\mathrm{GU\_\_gacid\_loss}} &= \mathrm{GU}_{\mathrm{\_Qstomach}} \cdot \mathrm{GU}_{\mathrm{\_protons\_stomach}} \\[1ex]
v_{\mathrm{GU\_\_ppi}} &= \mathrm{GU}_{\mathrm{\_ppi\_k}} \cdot \mathrm{GU}_{\mathrm{\_pp\_active}} \cdot \mathopen{}\left(\mathrm{Cgu}_{\mathrm{plasma\_some}} + \mathrm{Cgu}_{\mathrm{plasma\_rome}}\right) \\[1ex]
v_{\mathrm{GU\_\_pp\_synthesis}} &= \mathrm{GU}_{\mathrm{\_pp\_synthesis\_k}} \\[1ex]
v_{\mathrm{GU\_\_pp\_active\_degradation}} &= \mathrm{GU}_{\mathrm{\_pp\_degradation\_k}} \cdot \mathrm{GU}_{\mathrm{\_pp\_active}} \\[1ex]
v_{\mathrm{GU\_\_pp\_inactive\_degradation}} &= \mathrm{GU}_{\mathrm{\_pp\_degradation\_k}} \cdot \mathrm{GU}_{\mathrm{\_pp\_inactive}} \\[1ex]
v_{\mathrm{GU\_\_OMEOTHEXC}} &= \mathrm{GU}_{\mathrm{\_OMEOTHEXC\_k}} \cdot \mathrm{Vgu} \cdot \mathrm{Cgu}_{\mathrm{omeoth}} \\[1ex]
v_{\mathrm{GU\_\_dissolution\_some}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_ec}}\right) \cdot \mathrm{GU}_{\mathrm{\_F\_ome\_stomach}} \cdot \mathrm{GU}_{\mathrm{\_emptying\_some}} \\[1ex]
v_{\mathrm{GU\_\_degradation\_some}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_ec}}\right) \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_F\_ome\_stomach}}\right) \cdot \mathrm{GU}_{\mathrm{\_emptying\_some}} \\[1ex]
v_{\mathrm{GU\_\_release\_some}} &= \frac{\frac{\mathopen{}\left(1 + \mathrm{GU}_{\mathrm{\_fed}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_FED\_f\_dissolution}} - 1\right)\right) \cdot \mathrm{GU}_{\mathrm{\_Ka\_ec\_ome}}}{60} \cdot \mathrm{GU}_{\mathrm{\_POEC\_some}}}{\mathrm{GU}_{\mathrm{\_Mr\_ome}}} \\[1ex]
v_{\mathrm{GU\_\_SOMEABS}} &= \mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}} \cdot \mathrm{GU}_{\mathrm{\_absorption\_some}} \\[1ex]
v_{\mathrm{GU\_\_SOMEEXC}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}}\right) \cdot \mathrm{GU}_{\mathrm{\_absorption\_some}} \\[1ex]
v_{\mathrm{GU\_\_dissolution\_rome}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_ec}}\right) \cdot \mathrm{GU}_{\mathrm{\_F\_ome\_stomach}} \cdot \mathrm{GU}_{\mathrm{\_emptying\_rome}} \\[1ex]
v_{\mathrm{GU\_\_degradation\_rome}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_f\_ec}}\right) \cdot \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_F\_ome\_stomach}}\right) \cdot \mathrm{GU}_{\mathrm{\_emptying\_rome}} \\[1ex]
v_{\mathrm{GU\_\_release\_rome}} &= \frac{\frac{\mathopen{}\left(1 + \mathrm{GU}_{\mathrm{\_fed}} \cdot \mathopen{}\left(\mathrm{GU}_{\mathrm{\_FED\_f\_dissolution}} - 1\right)\right) \cdot \mathrm{GU}_{\mathrm{\_Ka\_ec\_ome}}}{60} \cdot \mathrm{GU}_{\mathrm{\_POEC\_rome}}}{\mathrm{GU}_{\mathrm{\_Mr\_ome}}} \\[1ex]
v_{\mathrm{GU\_\_ROMEABS}} &= \mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}} \cdot \mathrm{GU}_{\mathrm{\_absorption\_rome}} \\[1ex]
v_{\mathrm{GU\_\_ROMEEXC}} &= \mathopen{}\left(1 - \mathrm{GU}_{\mathrm{\_F\_ome\_abs\_eff}}\right) \cdot \mathrm{GU}_{\mathrm{\_absorption\_rome}}
\end{aligned}
$$

## ODE system

The states change in time with the rates of the reactions and the rate rules:

$$
\begin{aligned}
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_some}} - v_{\mathrm{Flow\_gu\_po\_some}} + v_{\mathrm{GU\_\_SOMEABS}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_some}} - v_{\mathrm{Flow\_ki\_ve\_some}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_some}} + v_{\mathrm{Flow\_po\_li\_some}} - v_{\mathrm{Flow\_li\_hv\_some}} - v_{\mathrm{LI\_\_SOMEIM}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_some}} + v_{\mathrm{Flow\_ve\_lu\_some}} - v_{\mathrm{Flow\_lu\_ar\_some}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_pa\_some}} + v_{\mathrm{Flow\_ar\_pa\_some}} - v_{\mathrm{Flow\_pa\_po\_some}}}{\mathrm{Vpa}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_sp\_some}} + v_{\mathrm{Flow\_ar\_sp\_some}} - v_{\mathrm{Flow\_sp\_po\_some}}}{\mathrm{Vsp}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_some}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_some}} + v_{\mathrm{Flow\_ar\_re\_some}} - v_{\mathrm{Flow\_re\_ve\_some}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_some}} - v_{\mathrm{Flow\_ar\_ki\_some}} - v_{\mathrm{Flow\_ar\_re\_some}} - v_{\mathrm{Flow\_ar\_gu\_some}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_sp\_some}} - v_{\mathrm{Flow\_ar\_pa\_some}} - v_{\mathrm{Flow\_arli\_li\_some}} - v_{\mathrm{Flow\_arli\_hv\_some}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( v_{\mathrm{iv\_some}} - v_{\mathrm{Flow\_ve\_lu\_some}} + v_{\mathrm{Flow\_ki\_ve\_some}} + v_{\mathrm{Flow\_re\_ve\_some}} \\
&\quad {} + v_{\mathrm{Flow\_hv\_ve\_some}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}} \Bigl( v_{\mathrm{Flow\_gu\_po\_some}} + v_{\mathrm{Flow\_sp\_po\_some}} + v_{\mathrm{Flow\_pa\_po\_some}} - v_{\mathrm{Flow\_po\_li\_some}} \\
&\quad {} - v_{\mathrm{Flow\_po\_hv\_some}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_some}} + v_{\mathrm{Flow\_po\_hv\_some}} + v_{\mathrm{Flow\_li\_hv\_some}} - v_{\mathrm{Flow\_hv\_ve\_some}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_some}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_pa\_some}}}{\mathrm{Vpa}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_sp\_some}}}{\mathrm{Vsp}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_some}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_rome}} - v_{\mathrm{Flow\_gu\_po\_rome}} + v_{\mathrm{GU\_\_ROMEABS}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_rome}} - v_{\mathrm{Flow\_ki\_ve\_rome}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_rome}} + v_{\mathrm{Flow\_po\_li\_rome}} - v_{\mathrm{Flow\_li\_hv\_rome}} - v_{\mathrm{LI\_\_ROMEIM}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_rome}} + v_{\mathrm{Flow\_ve\_lu\_rome}} - v_{\mathrm{Flow\_lu\_ar\_rome}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_pa\_rome}} + v_{\mathrm{Flow\_ar\_pa\_rome}} - v_{\mathrm{Flow\_pa\_po\_rome}}}{\mathrm{Vpa}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_sp\_rome}} + v_{\mathrm{Flow\_ar\_sp\_rome}} - v_{\mathrm{Flow\_sp\_po\_rome}}}{\mathrm{Vsp}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_rome}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_rome}} + v_{\mathrm{Flow\_ar\_re\_rome}} - v_{\mathrm{Flow\_re\_ve\_rome}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_rome}} - v_{\mathrm{Flow\_ar\_ki\_rome}} - v_{\mathrm{Flow\_ar\_re\_rome}} - v_{\mathrm{Flow\_ar\_gu\_rome}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_sp\_rome}} - v_{\mathrm{Flow\_ar\_pa\_rome}} - v_{\mathrm{Flow\_arli\_li\_rome}} - v_{\mathrm{Flow\_arli\_hv\_rome}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vve}} \Bigl( v_{\mathrm{iv\_rome}} - v_{\mathrm{Flow\_ve\_lu\_rome}} + v_{\mathrm{Flow\_ki\_ve\_rome}} + v_{\mathrm{Flow\_re\_ve\_rome}} \\
&\quad {} + v_{\mathrm{Flow\_hv\_ve\_rome}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}} \Bigl( v_{\mathrm{Flow\_gu\_po\_rome}} + v_{\mathrm{Flow\_sp\_po\_rome}} + v_{\mathrm{Flow\_pa\_po\_rome}} - v_{\mathrm{Flow\_po\_li\_rome}} \\
&\quad {} - v_{\mathrm{Flow\_po\_hv\_rome}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_rome}} + v_{\mathrm{Flow\_po\_hv\_rome}} + v_{\mathrm{Flow\_li\_hv\_rome}} - v_{\mathrm{Flow\_hv\_ve\_rome}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_rome}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_pa\_rome}}}{\mathrm{Vpa}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_sp\_rome}}}{\mathrm{Vsp}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_rome}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_omeoh}} - v_{\mathrm{Flow\_gu\_po\_omeoh}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_omeoh}} - v_{\mathrm{Flow\_ki\_ve\_omeoh}} - v_{\mathrm{KI\_\_OMEOHEX}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_omeoh}} + v_{\mathrm{Flow\_po\_li\_omeoh}} - v_{\mathrm{Flow\_li\_hv\_omeoh}} + v_{\mathrm{LI\_\_OMEOHEX}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_omeoh}} + v_{\mathrm{Flow\_ve\_lu\_omeoh}} - v_{\mathrm{Flow\_lu\_ar\_omeoh}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_pa\_omeoh}} + v_{\mathrm{Flow\_ar\_pa\_omeoh}} - v_{\mathrm{Flow\_pa\_po\_omeoh}}}{\mathrm{Vpa}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_sp\_omeoh}} + v_{\mathrm{Flow\_ar\_sp\_omeoh}} - v_{\mathrm{Flow\_sp\_po\_omeoh}}}{\mathrm{Vsp}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_omeoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_omeoh}} + v_{\mathrm{Flow\_ar\_re\_omeoh}} - v_{\mathrm{Flow\_re\_ve\_omeoh}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_omeoh}} - v_{\mathrm{Flow\_ar\_ki\_omeoh}} - v_{\mathrm{Flow\_ar\_re\_omeoh}} - v_{\mathrm{Flow\_ar\_gu\_omeoh}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_sp\_omeoh}} - v_{\mathrm{Flow\_ar\_pa\_omeoh}} - v_{\mathrm{Flow\_arli\_li\_omeoh}} - v_{\mathrm{Flow\_arli\_hv\_omeoh}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_ve\_lu\_omeoh}} + v_{\mathrm{Flow\_ki\_ve\_omeoh}} + v_{\mathrm{Flow\_re\_ve\_omeoh}} + v_{\mathrm{Flow\_hv\_ve\_omeoh}}}{\mathrm{Vve}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}} \Bigl( v_{\mathrm{Flow\_gu\_po\_omeoh}} + v_{\mathrm{Flow\_sp\_po\_omeoh}} + v_{\mathrm{Flow\_pa\_po\_omeoh}} - v_{\mathrm{Flow\_po\_li\_omeoh}} \\
&\quad {} - v_{\mathrm{Flow\_po\_hv\_omeoh}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_omeoh}} + v_{\mathrm{Flow\_po\_hv\_omeoh}} + v_{\mathrm{Flow\_li\_hv\_omeoh}} - v_{\mathrm{Flow\_hv\_ve\_omeoh}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_omeoh}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_pa\_omeoh}}}{\mathrm{Vpa}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_sp\_omeoh}}}{\mathrm{Vsp}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{omeoh}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_omeoh}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_omesul}} - v_{\mathrm{Flow\_gu\_po\_omesul}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_omesul}} - v_{\mathrm{Flow\_ki\_ve\_omesul}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_omesul}} + v_{\mathrm{Flow\_po\_li\_omesul}} - v_{\mathrm{Flow\_li\_hv\_omesul}} + v_{\mathrm{LI\_\_OMESULEX}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_omesul}} + v_{\mathrm{Flow\_ve\_lu\_omesul}} - v_{\mathrm{Flow\_lu\_ar\_omesul}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_pa\_omesul}} + v_{\mathrm{Flow\_ar\_pa\_omesul}} - v_{\mathrm{Flow\_pa\_po\_omesul}}}{\mathrm{Vpa}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_sp\_omesul}} + v_{\mathrm{Flow\_ar\_sp\_omesul}} - v_{\mathrm{Flow\_sp\_po\_omesul}}}{\mathrm{Vsp}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_omesul}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_omesul}} + v_{\mathrm{Flow\_ar\_re\_omesul}} - v_{\mathrm{Flow\_re\_ve\_omesul}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_omesul}} - v_{\mathrm{Flow\_ar\_ki\_omesul}} - v_{\mathrm{Flow\_ar\_re\_omesul}} - v_{\mathrm{Flow\_ar\_gu\_omesul}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_sp\_omesul}} - v_{\mathrm{Flow\_ar\_pa\_omesul}} - v_{\mathrm{Flow\_arli\_li\_omesul}} - v_{\mathrm{Flow\_arli\_hv\_omesul}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_ve\_lu\_omesul}} + v_{\mathrm{Flow\_ki\_ve\_omesul}} + v_{\mathrm{Flow\_re\_ve\_omesul}} + v_{\mathrm{Flow\_hv\_ve\_omesul}}}{\mathrm{Vve}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}} \Bigl( v_{\mathrm{Flow\_gu\_po\_omesul}} + v_{\mathrm{Flow\_sp\_po\_omesul}} + v_{\mathrm{Flow\_pa\_po\_omesul}} - v_{\mathrm{Flow\_po\_li\_omesul}} \\
&\quad {} - v_{\mathrm{Flow\_po\_hv\_omesul}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_omesul}} + v_{\mathrm{Flow\_po\_hv\_omesul}} + v_{\mathrm{Flow\_li\_hv\_omesul}} - v_{\mathrm{Flow\_hv\_ve\_omesul}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_omesul}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_pa\_omesul}}}{\mathrm{Vpa}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_sp\_omesul}}}{\mathrm{Vsp}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_omesul}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_gu\_omeoth}} - v_{\mathrm{Flow\_gu\_po\_omeoth}}}{\mathrm{Vgu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cki}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_ar\_ki\_omeoth}} - v_{\mathrm{Flow\_ki\_ve\_omeoth}} - v_{\mathrm{KI\_\_OMEOTHEX}}}{\mathrm{Vki}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cli}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_li\_omeoth}} + v_{\mathrm{Flow\_po\_li\_omeoth}} - v_{\mathrm{Flow\_li\_hv\_omeoth}} + v_{\mathrm{LI\_\_OMEOTHEX}}}{\mathrm{Vli}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_lu\_omeoth}} + v_{\mathrm{Flow\_ve\_lu\_omeoth}} - v_{\mathrm{Flow\_lu\_ar\_omeoth}}}{\mathrm{Vlu}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_pa\_omeoth}} + v_{\mathrm{Flow\_ar\_pa\_omeoth}} - v_{\mathrm{Flow\_pa\_po\_omeoth}}}{\mathrm{Vpa}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_sp\_omeoth}} + v_{\mathrm{Flow\_ar\_sp\_omeoth}} - v_{\mathrm{Flow\_sp\_po\_omeoth}}}{\mathrm{Vsp}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{plasma\_omeoth}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{transport\_re\_omeoth}} + v_{\mathrm{Flow\_ar\_re\_omeoth}} - v_{\mathrm{Flow\_re\_ve\_omeoth}}}{\mathrm{Vre}_{\mathrm{plasma}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Car}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Var}} \Bigl( v_{\mathrm{Flow\_lu\_ar\_omeoth}} - v_{\mathrm{Flow\_ar\_ki\_omeoth}} - v_{\mathrm{Flow\_ar\_re\_omeoth}} - v_{\mathrm{Flow\_ar\_gu\_omeoth}} \\
&\quad {} - v_{\mathrm{Flow\_ar\_sp\_omeoth}} - v_{\mathrm{Flow\_ar\_pa\_omeoth}} - v_{\mathrm{Flow\_arli\_li\_omeoth}} - v_{\mathrm{Flow\_arli\_hv\_omeoth}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cve}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{-v_{\mathrm{Flow\_ve\_lu\_omeoth}} + v_{\mathrm{Flow\_ki\_ve\_omeoth}} + v_{\mathrm{Flow\_re\_ve\_omeoth}} + v_{\mathrm{Flow\_hv\_ve\_omeoth}}}{\mathrm{Vve}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpo}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vpo}} \Bigl( v_{\mathrm{Flow\_gu\_po\_omeoth}} + v_{\mathrm{Flow\_sp\_po\_omeoth}} + v_{\mathrm{Flow\_pa\_po\_omeoth}} - v_{\mathrm{Flow\_po\_li\_omeoth}} \\
&\quad {} - v_{\mathrm{Flow\_po\_hv\_omeoth}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{Chv}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{Flow\_arli\_hv\_omeoth}} + v_{\mathrm{Flow\_po\_hv\_omeoth}} + v_{\mathrm{Flow\_li\_hv\_omeoth}} - v_{\mathrm{Flow\_hv\_ve\_omeoth}}}{\mathrm{Vhv}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Clu}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_lu\_omeoth}}}{\mathrm{Vlu}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cpa}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_pa\_omeoth}}}{\mathrm{Vpa}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Csp}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_sp\_omeoth}}}{\mathrm{Vsp}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cre}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{transport\_re\_omeoth}}}{\mathrm{Vre}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{omeoh}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_OMEOHEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Aurine}_{\mathrm{omeoth}}}{\mathrm{d} t} &= v_{\mathrm{KI\_\_OMEOTHEX}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{some}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_SOMEEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{rome}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_ROMEEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Afeces}_{\mathrm{omeoth}}}{\mathrm{d} t} &= v_{\mathrm{GU\_\_OMEOTHEXC}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_dissolution\_some}} + v_{\mathrm{GU\_\_release\_some}} - v_{\mathrm{GU\_\_SOMEABS}} - v_{\mathrm{GU\_\_SOMEEXC}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_dissolution\_rome}} + v_{\mathrm{GU\_\_release\_rome}} - v_{\mathrm{GU\_\_ROMEABS}} - v_{\mathrm{GU\_\_ROMEEXC}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{Cgu}_{\mathrm{omeoth}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_OMEOTHBIL}} - v_{\mathrm{GU\_\_OMEOTHEXC}}}{\mathrm{Vgu}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_some}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_SOMEIM}} - v_{\mathrm{LI\_\_SOMECYP2C19}} - v_{\mathrm{LI\_\_SOMECYP2C19OH}} - v_{\mathrm{LI\_\_SOMECYP3A4}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_rome}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_ROMEIM}} - v_{\mathrm{LI\_\_ROMECYP2C19}} - v_{\mathrm{LI\_\_ROMECYP3A4}} - v_{\mathrm{LI\_\_ROMECYP3A4OH}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_omeoh}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vli}_{\mathrm{tissue}}} \Bigl( v_{\mathrm{LI\_\_SOMECYP2C19OH}} + v_{\mathrm{LI\_\_ROMECYP2C19}} + v_{\mathrm{LI\_\_ROMECYP3A4OH}} - v_{\mathrm{LI\_\_OMEOHEX}} \\
&\quad {} - v_{\mathrm{LI\_\_OMEOHM}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_omesul}}}{\mathrm{d} t} &= \frac{v_{\mathrm{LI\_\_SOMECYP3A4}} + v_{\mathrm{LI\_\_ROMECYP3A4}} - v_{\mathrm{LI\_\_OMESULEX}} - v_{\mathrm{LI\_\_OMESULM}}}{\mathrm{Vli}_{\mathrm{tissue}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_omeoth}}}{\mathrm{d} t} &= \frac{1}{\mathrm{Vli}_{\mathrm{tissue}}} \Bigl( v_{\mathrm{LI\_\_SOMECYP2C19}} + v_{\mathrm{LI\_\_OMEOHM}} + v_{\mathrm{LI\_\_OMESULM}} - v_{\mathrm{LI\_\_OMEOTHEX}} \\
&\quad {} - v_{\mathrm{LI\_\_OMEOTHBIL}} \Bigr) \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_protons\_stomach}}}{\mathrm{d} t} &= \frac{v_{\mathrm{GU\_\_pp\_rate}} - v_{\mathrm{GU\_\_gacid\_loss}}}{\mathrm{GU}_{\mathrm{\_Vstomach}}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_pp\_active}}}{\mathrm{d} t} &= -\mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}} \cdot v_{\mathrm{GU\_\_ppi}} + \mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}} \cdot v_{\mathrm{GU\_\_pp\_synthesis}} - \mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}} \cdot v_{\mathrm{GU\_\_pp\_active\_degradation}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_pp\_inactive}}}{\mathrm{d} t} &= \mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}} \cdot v_{\mathrm{GU\_\_ppi}} - \mathrm{GU}_{\mathrm{\_cf\_species\_dimensionless}} \cdot v_{\mathrm{GU\_\_pp\_inactive\_degradation}} \\[1ex]
\frac{\mathrm{d} \,\mathrm{IVDOSE}_{\mathrm{some}}}{\mathrm{d} t} &= -v_{\mathrm{iv\_some}} \cdot \mathrm{Mr}_{\mathrm{some}} + \mathrm{Ri}_{\mathrm{some}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{cum}_{\mathrm{dose\_some}}}{\mathrm{d} t} &= \mathrm{Ri}_{\mathrm{some}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{some}}}{\mathrm{d} t} &= -\mathrm{GU}_{\mathrm{\_emptying\_some}} \cdot \mathrm{GU}_{\mathrm{\_Mr\_ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{IVDOSE}_{\mathrm{rome}}}{\mathrm{d} t} &= -v_{\mathrm{iv\_rome}} \cdot \mathrm{Mr}_{\mathrm{rome}} + \mathrm{Ri}_{\mathrm{rome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{cum}_{\mathrm{dose\_rome}}}{\mathrm{d} t} &= \mathrm{Ri}_{\mathrm{rome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{PODOSE}_{\mathrm{rome}}}{\mathrm{d} t} &= -\mathrm{GU}_{\mathrm{\_emptying\_rome}} \cdot \mathrm{GU}_{\mathrm{\_Mr\_ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{LI}_{\mathrm{\_cyp2c19\_active}}}{\mathrm{d} t} &= \mathrm{LI}_{\mathrm{\_CYP2C19\_kdeg}} \cdot \mathopen{}\left(1 - \mathrm{LI}_{\mathrm{\_cyp2c19\_active}}\right) - \frac{\mathrm{LI}_{\mathrm{\_CYP2C19\_kinact}} \cdot \mathrm{LI}_{\mathrm{\_cyp2c19\_active}} \cdot \mathopen{}\left(\mathrm{LI}_{\mathrm{\_some}} + \mathrm{LI}_{\mathrm{\_rome}}\right)}{\mathrm{LI}_{\mathrm{\_CYP2C19\_KI}} + \mathrm{LI}_{\mathrm{\_some}} + \mathrm{LI}_{\mathrm{\_rome}}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_POEC\_some}}}{\mathrm{d} t} &= \mathopen{}\left(\mathrm{GU}_{\mathrm{\_f\_ec}} \cdot \mathrm{GU}_{\mathrm{\_emptying\_some}} - v_{\mathrm{GU\_\_release\_some}}\right) \cdot \mathrm{GU}_{\mathrm{\_Mr\_ome}} \qquad \text{(rate rule)} \\[1ex]
\frac{\mathrm{d} \,\mathrm{GU}_{\mathrm{\_POEC\_rome}}}{\mathrm{d} t} &= \mathopen{}\left(\mathrm{GU}_{\mathrm{\_f\_ec}} \cdot \mathrm{GU}_{\mathrm{\_emptying\_rome}} - v_{\mathrm{GU\_\_release\_rome}}\right) \cdot \mathrm{GU}_{\mathrm{\_Mr\_ome}} \qquad \text{(rate rule)}
\end{aligned}
$$
