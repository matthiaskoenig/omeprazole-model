"""Parameters of the omeprazole fits.

The pharmacokinetics (subset PK) are fitted on the plasma concentrations of
omeprazole, its enantiomers and its metabolites and on the excretion of the
metabolites. The fit adjusts the capacities of CYP2C19 and CYP3A4 for S- and
R-omeprazole (IV clearance, the genotypes, the enantiomers, the metabolites),
the mechanism-based inactivation of CYP2C19 (the repeated doses), the tissue
partition, the release of the enteric-coated forms and the absorption, and
the disposition of the metabolites. Fixed as fast processes: the exchange flow
of the tissues (`ftissue_ome`) and the gastric emptying of a buffered solution
(`GU__Ka_dis_ome`), which ran to their upper bounds or spread over a flat
range in the first fits (the absorption `GU__OMEABS_k` and the partition
`Kp_ome` determine the curves). Fixed (literature, see the notes of the
model): the Km of CYP3A4 and of CYP2C19 (in vitro over the unbound
fraction, not identifiable above 50 µM), the KI and the turnover of CYP2C19,
the fraction 5-hydroxyomeprazole of S-omeprazole, the blood to plasma ratio, the complete
absorption, the effects of food, the oxidation of 5-hydroxyomeprazole in the
liver (only its ratio to the release is identifiable) and the fast exchanges
between the liver and the plasma.

The model has a pharmacodynamic part (the proton pumps and the stomach pH),
but no study maps pharmacodynamic data yet: there is no PD subset.
"""

from sbmlsim.fit import FitParameter

#: the pharmacokinetics
parameters_pk: list[FitParameter] = [
    # CYP2C19 and CYP3A4 for S- and R-omeprazole: IV clearance 530-660 ml/min
    # (Caucasian EM), poor metabolizers 50-150 ml/min, S AUC 2.5 fold R
    FitParameter(
        pid="LI__CYP2C19_Vmax_some",
        start_value=0.04,
        lower_bound=1e-4,
        upper_bound=1.0,
        unit="mmole/min/l",
    ),
    FitParameter(
        pid="LI__CYP2C19_Vmax_rome",
        start_value=0.08,
        lower_bound=1e-4,
        upper_bound=1.0,
        unit="mmole/min/l",
    ),
    FitParameter(
        pid="LI__CYP3A4_Vmax_some",
        start_value=0.012,
        lower_bound=1e-4,
        upper_bound=0.5,
        unit="mmole/min/l",
    ),
    FitParameter(
        pid="LI__CYP3A4_Vmax_rome",
        start_value=0.005,
        lower_bound=1e-5,
        upper_bound=0.5,
        unit="mmole/min/l",
    ),
    # repeated doses: AUC x1.7-1.9 after 5-7 days, IV 40 mg CL 446 -> 237 ml/min
    FitParameter(
        pid="LI__CYP2C19_kinact",
        start_value=0.03,
        lower_bound=1e-4,
        upper_bound=1.0,
        unit="1/min",
    ),
    # tissue distribution: Vss 0.17-0.37 l/kg, IV t1/2 0.5-0.9 hr
    FitParameter(
        pid="Kp_ome",
        start_value=0.25,
        lower_bound=0.02,
        upper_bound=5.0,
        unit="dimensionless",
    ),
    # absorption: buffered solution tmax 0.2-0.3 hr, enteric-coated 1.5-3 hr
    FitParameter(
        pid="GU__Ka_ec_ome",
        start_value=2.0,
        lower_bound=0.2,
        upper_bound=20,
        unit="1/hr",
    ),
    FitParameter(
        pid="GU__OMEABS_k",
        start_value=0.05,
        lower_bound=1e-3,
        upper_bound=1.0,
        unit="1/min",
    ),
    # 5-hydroxyomeprazole of poor metabolizers by CYP3A4 from R-omeprazole:
    # urine 5.6 % (PM) vs 13.5 % (EM) of the dose
    FitParameter(
        pid="LI__f_rome_cyp3a4_omeoh",
        start_value=0.2,
        lower_bound=0.01,
        upper_bound=0.9,
        unit="dimensionless",
    ),
    # 5-hydroxyomeprazole: t1/2 about 1 hr, 13.5 % of the dose in the urine
    FitParameter(
        pid="LI__OMEOHEX_k",
        start_value=0.2,
        lower_bound=1e-3,
        upper_bound=10,
        unit="1/min",
    ),
    FitParameter(
        pid="KI__OMEOHEX_f",
        start_value=3.0,
        lower_bound=0.1,
        upper_bound=30,
        unit="dimensionless",
    ),
    # omeprazole sulfone: t1/2 2-2.6 hr (EM), 7.5-11 hr (PM)
    FitParameter(
        pid="LI__OMESUL2C19_k",
        start_value=0.1,
        lower_bound=1e-3,
        upper_bound=10,
        unit="1/min",
    ),
    FitParameter(
        pid="LI__OMESULM_k",
        start_value=0.025,
        lower_bound=1e-4,
        upper_bound=1.0,
        unit="1/min",
    ),
    # other metabolites: urine 75-78 %, feces 17-19 % of the dose
    FitParameter(
        pid="KI__OMEOTHEX_f",
        start_value=2.0,
        lower_bound=0.1,
        upper_bound=50,
        unit="dimensionless",
    ),
    FitParameter(
        pid="LI__OMEOTHBIL_k",
        start_value=0.03,
        lower_bound=1e-4,
        upper_bound=1.0,
        unit="1/min",
    ),
]
