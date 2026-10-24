"""The tolerances of the integrator for the omeprazole model."""

from sbmlsim.model.tolerances import AbsoluteTolerance


def absolute_tolerance(value: float, species: float) -> AbsoluteTolerance:
    """Get the absolute tolerance of the integrator for the omeprazole model.

    The species of omeprazole and its metabolites are small: the plasma
    concentrations are about 1e-6 to 1e-2 mM (1e-5 mM after the microdose of
    Oh2012), the amounts of a similar scale in mmole. The targets of the rate
    rules are the doses in mg (`PODOSE_<sid>`, `IVDOSE_<sid>`, the
    enteric-coated pellets `GU__POEC_<sid>`, the infused dose
    `cum_dose_<sid>`) and the fraction of active CYP2C19
    (`LI__cyp2c19_active`, 0-1); the protons in the stomach (10 mM) and the
    proton pumps (1) are species of a larger scale.

    Args:
        value: tolerance of the targets of the rate rules [mg, -].
        species: tolerance of the species, of their concentrations [mM] and
            amounts [mmole].

    Returns:
        The absolute tolerance per kind of state.
    """
    return AbsoluteTolerance(amount=species, concentration=species, other=value)


#: the absolute tolerance of the simulation experiments
ABSOLUTE_TOLERANCE = absolute_tolerance(1e-10, species=1e-14)
