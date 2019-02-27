from admittance import displacementAdmittance, conductanceAdmittance, admittance
# Read in device configuration
device_configuration = nlread('CNT_10_10.nc', DeviceConfiguration)[0]

# Define parameters for the calculation
T = 300*Kelvin
N = 50
omega_list =  numpy.linspace(0,1,11)*eV

# Get chemical potentials
chemical_potential_class = ChemicalPotential(device_configuration)
chemical_potentials = chemical_potential_class.evaluate()
average_fermi_level = 0.5*numpy.sum(chemical_potentials)

# Get Hamiltonian and Overlap
H, S = calculateHamiltonianAndOverlap(device_configuration)

# Calculate SelfEnergies
S_L = calculateSelfEnergy(device_configuration, average_fermi_level,
                              contribution=Left).inUnitsOf(Hartree)
S_R = calculateSelfEnergy(device_configuration, average_fermi_level,
                              contribution=Right).inUnitsOf(Hartree)

# Make Self energies same shape as Gr
Sigma_L = 0*S
n = S_L.shape[0]
Sigma_L[:n,:n] = S_L
Sigma_L = Sigma_L*Hartree

Sigma_R = 0*S
m = S_R.shape[0]
Sigma_R[-m:,-m:] = S_R
Sigma_R = Sigma_R*Hartree

B=[]
G=[]
for omega in omega_list:
    print 'omega ', omega
    YD = displacementAdmittance(average_fermi_level, omega, T, N, H, S, Sigma_L, Sigma_R)
    YC = conductanceAdmittance(average_fermi_level, omega, T, N, H, S, Sigma_L, Sigma_R)
    Y = admittance(YD,YC)
    G += [Y[0,1].real]
    B += [Y[0,1].imag]

# Plot the data
import pylab
f, axarr = pylab.subplots(2, sharex=True)
axarr[0].plot(omega_list.inUnitsOf(eV), G)
axarr[0].set_ylabel('$\mathrm{G}(\omega,\mathrm{N})/\mathrm{G}_0$')
axarr[1].plot(omega_list.inUnitsOf(eV), B)
axarr[1].set_xlabel('$\hbar \omega$ [eV]')
axarr[1].set_ylabel('$\mathrm{B}(\omega,\mathrm{N})/\mathrm{G}_0$')
pylab.show()