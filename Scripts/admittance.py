from NanoLanguage import *
# Implement AC conductance as in Yamamoto et. al., PRB 81, 115448 (2010)

eps = 1e-5*eV

def fermiFunction(E, T):
    return 1/(1+numpy.exp(E/T))

def conductanceTransmissionAC(omega, energy, H, S, sigma_a, sigma_b, gamma_a, gamma_b, diagonal_element):
    """Eq. (4) All energies in Hartree """
    G0 = numpy.linalg.inv(energy*S-H-sigma_a -sigma_b)
    G0_dagger = numpy.conj(G0.transpose())
    G1 = numpy.linalg.inv((omega+energy)*S-H-sigma_a -sigma_b)

    T = numpy.trace(numpy.dot(numpy.dot(numpy.dot(G1, gamma_b),G0_dagger), gamma_a))
    if diagonal_element:
        T -= 1j*numpy.trace(numpy.dot(G1, gamma_a))
        T += 1j*numpy.trace(numpy.dot(gamma_a,G0_dagger))
    return T

def displacementTransmissionAC(omega, energy, H, S, sigma_a, sigma_b, gamma_a):
    """Eq. (6) All energies in Hartree """
    G0 = numpy.linalg.inv(energy*S-H-sigma_a -sigma_b)
    G0_dagger = numpy.conj(G0.transpose())
    G1 = numpy.linalg.inv((omega+energy)*S-H-sigma_a -sigma_b)

    T = -1j*numpy.trace(numpy.dot(numpy.dot(G1, gamma_a),G0_dagger))
    return T

def conductanceAdmittance(Ef, omega, T, N, H, S, Sigma_L, Sigma_R):
    """Eq. (3) """
    if omega < eps:
        omega = eps
    TE = boltzmann_constant*T
    # Convert everything to Hartree
    Sigma_L = Sigma_L.inUnitsOf(Hartree)
    Sigma_R = Sigma_R.inUnitsOf(Hartree)
    H = H.inUnitsOf(Hartree)
    Ef = Ef.inUnitsOf(Hartree)
    omega = omega.inUnitsOf(Hartree)
    TE = TE.inUnitsOf(Hartree)

    E0 = Ef-omega-8*TE
    E1 = Ef+omega+8*TE
    energies = numpy.linspace(E0, E1, N)
    f0 = fermiFunction(energies-Ef, TE)
    f1 = fermiFunction(energies-(Ef-omega), TE)
    # Calculate gamma's
    Gamma_L = 1j*(Sigma_L-numpy.conj(Sigma_L.transpose()))
    Gamma_R = 1j*(Sigma_R-numpy.conj(Sigma_R.transpose()))

    # Calculate conductance admittance
    T_LL = numpy.array([conductanceTransmissionAC(omega, e, H, S, Sigma_L, Sigma_R, Gamma_L, Gamma_L, True) for e in energies])
    YC_LL = numpy.sum(T_LL*(f0-f1))*(energies[1]-energies[0])/omega

    T_RR = numpy.array([conductanceTransmissionAC(omega, e, H, S, Sigma_L, Sigma_R, Gamma_R, Gamma_R, True) for e in energies])
    YC_RR = numpy.sum(T_RR*(f0-f1))*(energies[1]-energies[0])/omega

    T_LR = numpy.array([conductanceTransmissionAC(omega, e, H, S, Sigma_L, Sigma_R, Gamma_L, Gamma_R, False) for e in energies])
    YC_LR = numpy.sum(T_LR*(f0-f1))*(energies[1]-energies[0])/omega

    T_RL = numpy.array([conductanceTransmissionAC(omega, e, H, S, Sigma_R, Sigma_L, Gamma_R, Gamma_L, False) for e in energies])
    YC_RL = numpy.sum(T_RL*(f0-f1))*(energies[1]-energies[0])/omega

    return numpy.array([[YC_LL, YC_LR],[YC_RL, YC_RR]])

def displacementAdmittance(Ef, omega, T, N, H, S, Sigma_L, Sigma_R):
    """Eq. (5) """
    if omega < eps:
        omega = eps
    TE = boltzmann_constant*T
    # Convert everything to Hartree
    Sigma_L = Sigma_L.inUnitsOf(Hartree)
    Sigma_R = Sigma_R.inUnitsOf(Hartree)
    H = H.inUnitsOf(Hartree)
    Ef = Ef.inUnitsOf(Hartree)
    omega = omega.inUnitsOf(Hartree)
    TE = TE.inUnitsOf(Hartree)

    E0 = Ef-omega-8*TE
    E1 = Ef+omega+8*TE
    energies = numpy.linspace(E0, E1, N)
    f0 = fermiFunction(energies-Ef, TE)
    f1 = fermiFunction(energies-(Ef-omega), TE)

    # Calculate displacement current
    Gamma_L = 1j*(Sigma_L-numpy.conj(Sigma_L.transpose()))
    TD_L = numpy.array([displacementTransmissionAC(omega, e, H, S, Sigma_L, Sigma_R, Gamma_L) for e in energies])
    YD_L = numpy.sum(TD_L*(f0-f1))*(energies[1]-energies[0])

    Gamma_R = 1j*(Sigma_R-numpy.conj(Sigma_R.transpose()))
    TD_R = numpy.array([displacementTransmissionAC(omega, e, H, S, Sigma_L, Sigma_R, Gamma_R) for e in energies])
    YD_R = numpy.sum(TD_R*(f0-f1))*(energies[1]-energies[0])
    return numpy.array([YD_L, YD_R])

def admittance(YD, YC):
    """Eq. (2) """
    P_sum = YD[0]+YD[1]
    P1_sum = YC[0,0]+ YC[1,1]+ YC[0,1]+ YC[1,0]
    P = numpy.zeros(2, dtype=complex)
    P[0] = -(YC[0,0]+YC[0,1])/P_sum
    P[1] = -(YC[1,0]+YC[1,1])/P_sum
    Y = numpy.zeros(4, dtype=complex).reshape(2,2)
    Y[0,0] = YC[0,0]+P[0]*YD[0]
    Y[0,1] = YC[0,1]+P[0]*YD[1]
    Y[1,0] = YC[1,0]+P[1]*YD[0]
    Y[1,1] = YC[1,1]+P[1]*YD[1]
    return Y