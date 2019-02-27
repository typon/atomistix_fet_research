import sys
import StringIO
import numpy as np
import getopt
import pdb
from pprint import pprint
import ntpath

def enum (**enums):
    return type ('Enum', (), enums)

class DeviceAnalysis: 

    def __init__(self, argv):
        self.exchange_correlation = GGA.PBE
        self.k_point_sampling = (2, 2, 100)

        self.ConfigTypes = enum (BULK = (1, DensityOfStates) , DEVICE = (2, DeviceDensityOfStates))


        try:
            opts, args = getopt.getopt(argv,"hi:",["ifile="])
        except getopt.GetoptError:
            usage()
        if not opts:
            print 'No options supplied'
            usage()
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
        print 'Input geometry file is:', inputfile


        #run self consistent device calculation for zero bias.
        voltage = 0 * Volt
        init_config_obj = []

        #Get full file path
        full_input_path = os.path.abspath (inputfile)
        #Get input file name only
        file_base_name = ntpath.basename(full_input_path)
        print file_base_name
        print full_input_path 

        #extract diretory path

        dir_path = os.path.dirname(full_input_path )

        #Create tmp folder insid ethe directory to hold the NetCDF file and 
        #output data files

        #Temp file path
        tmp_path = dir_path+'/tmp/'
        print "############"
        print "temp PATH = ", tmp_path

        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
        device_config_path = tmp_path+file_base_name+".analysis.nc"
        print device_config_path


        #try reading device config first
        try:
            with open(device_config_path):
                print "Accessing initial device configuration"
                init_config_obj = nlread(device_config_path, BulkConfiguration)
                #configuration empty, therefore device config
                if not init_config_obj:
                    init_config_obj = nlread(device_config_path, DeviceConfiguration)

                self.set_configuration_type(init_config_obj[0])
                
                    
                    

        except IOError:
            print 'Oh dear. No device config file exists.'

        if  not init_config_obj:
            print "No initial configuration exists, running DFT calculation"

            print "Extracting configuration from file"
            #pdb.set_trace()
            init_config_obj, basis_set = self.create_device_config(inputfile)

            #setting iether bulk or device config type
            self.set_configuration_type(init_config_obj)

            print "SADASDASD"
            if (self.config_type == self.ConfigTypes.DEVICE):

                print "device"
                calculator = self.create_device_calculator (basis_set)
            elif (self.config_type == self.ConfigTypes.BULK):
                print "bulk"
                calculator = self.create_bulk_calculator (basis_set)

            init_config_obj.setCalculator(calculator)
            nlprint(init_config_obj)
            init_config_obj.update()

            nlsave(device_config_path, init_config_obj)

            if (self.config_type == self.ConfigTypes.DEVICE):
                configuration_obj = nlread(device_config_path, DeviceConfiguration)
            elif (self.config_type == self.ConfigTypes.BULK):
                configuration_obj = nlread(device_config_path, BulkConfiguration)

            self.configuration_obj = configuration_obj [0]

        else:
            print 'Found initial configuration'
            self.configuration_obj = init_config_obj[0]
        self.extract_dimensions()
        self.device_config_path = device_config_path
 
    def usage(self):
        print 'python device_analysis.py --ifile=<inputfile>'
        sys.exit()

    def set_configuration_type(self, configuration_obj):
        if 'BulkConfiguration' in str(type(configuration_obj)):
            self.config_type = self.ConfigTypes.BULK
        elif 'DeviceConfiguration' in str(type(configuration_obj)):
            self.config_type = self.ConfigTypes.DEVICE
        else:
           print str(type(configuration_obj))
           print "Error: Not valid configuration type"
           sys.exit()

    def frac_to_cart(self, length_real, frac):
        result = length_real*frac;
        return result

    def create_device_config (self, geometry_path):
        # create file-like string to capture output
        codeOut = StringIO.StringIO()
        codeErr = StringIO.StringIO()

        geometry_code = ''

        try:
            with open(geometry_path, 'r') as f:
                geometry_code = f.read()
                #print geometry_code
        except IOError:
            print 'Oh dear. Specified geometry file [',geometry_path,'] does not exist.'

        if (geometry_code == ''):
            print 'Oh dear. No geometry pecified'
            exit(1)

        basis_set = []
        device_configuration = None
        bulk_configuration = None

        # capture output and errors

        sys.stdout = codeOut
        sys.stderr = codeErr

        #print geometry_code
        exec geometry_code

        # restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        #print geometry_code

        #print f(4)

        s = codeErr.getvalue()

        print "error:\n%s\n" % s

        #s = codeOut.getvalue()
        #print "output:\n%s" % s

        codeOut.close()
        codeErr.close()

        if len(basis_set) == 0:
           print "Error: No basis set specified"
           sys.exit()
        if device_configuration is None:
            return bulk_configuration, basis_set
        elif bulk_configuration is None:
            return device_configuration, basis_set
        else:
           print "Error: No configuration specified"
           sys.exit()
            
            
    def create_bulk_calculator (self, basis_set):

        bulk_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )
        calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=bulk_numerical_accuracy_parameters,
            )

        return calculator


    def create_device_calculator (self, basis_set):

        #----------------------------------------
        # Numerical Accuracy Settings
        #----------------------------------------
        left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        #----------------------------------------
        # Poisson Solver Settings
        #----------------------------------------
        left_electrode_poisson_solver = FastFourier2DSolver(
            boundary_conditions=[[PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        right_electrode_poisson_solver = FastFourier2DSolver(
            boundary_conditions=[[PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        #----------------------------------------
        # Electrode Calculators
        #----------------------------------------
        left_electrode_calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
            poisson_solver=left_electrode_poisson_solver,
            )

        right_electrode_calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
            poisson_solver=right_electrode_poisson_solver,
            )

        #----------------------------------------
        # Device Calculator
        #----------------------------------------
        calculator = DeviceLCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=device_numerical_accuracy_parameters,
            electrode_calculators=
                [left_electrode_calculator, right_electrode_calculator],
            )


        return calculator
            
    def create_device_calculator (self, basis_set):


        # -------------------------------------------------------------
        # Calculator
        # -------------------------------------------------------------


        #----------------------------------------
        # Exchange-Correlation
        #----------------------------------------

        #----------------------------------------
        # Numerical Accuracy Settings
        #----------------------------------------
        left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )

        #----------------------------------------
        # Poisson Solver Settings
        #----------------------------------------
        left_electrode_poisson_solver = FastFourier2DSolver(
            boundary_conditions=[[PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        right_electrode_poisson_solver = FastFourier2DSolver(
            boundary_conditions=[[PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        #----------------------------------------
        # Electrode Calculators
        #----------------------------------------
        left_electrode_calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
            poisson_solver=left_electrode_poisson_solver,
            )

        right_electrode_calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
            poisson_solver=right_electrode_poisson_solver,
            )

        #----------------------------------------
        # Device Calculator
        #----------------------------------------
        calculator = DeviceLCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=device_numerical_accuracy_parameters,
            electrode_calculators=
                [left_electrode_calculator, right_electrode_calculator],
            )


        return calculator

    def extract_dimensions (self):
        lattice = self.configuration_obj.bravaisLattice()
        lattice_vectors = lattice.primitiveVectors()

        self.x_length = lattice_vectors[0][0]
        self.y_length = lattice_vectors[1][1]
        self.z_length = lattice_vectors[2][2]

        coords = self.configuration_obj.fractionalCoordinates()
        #sort by the third axis, in this case z. f2= axis3, f1=axis2, f0=axis1
        
        #need to copy the array to make it work
        coords = coords.copy()
        coords.view('f8,f8,f8').sort(order=['f2'], axis=0)

        #figuring out the projection lines for 100 

        z_coord_first_atom = coords[0][2]
        z_coord_last_atom = coords[-1][2]
        self.projection_point_x_1 = numpy.array([0, 0.5, z_coord_first_atom])
        self.projection_point_y_1 = numpy.array([0.5, 0, z_coord_first_atom])
        self.projection_point_x_0 = numpy.array([0, 0.5, z_coord_last_atom])
        self.projection_point_y_0 = numpy.array([0.5, 0, z_coord_last_atom])


        print self.projection_point_x_1

        
        print coords




    def generate_diff_pot (self):
        print "Generating Difference Potential"

        diff = ElectrostaticDifferencePotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, diff)


    def generate_v_eff (self):
        print "Generating Veff"

        v_eff = EffectivePotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, v_eff)

    def generate_e_diff_density (self):
        print "Generating Electron Difference Density"

        electron_diff_density = ElectronDifferenceDensity (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, electron_diff_density)


    def generate_e_density (self):
        print "Generating Electron Density"

        electron_density = ElectronDensity (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, electron_density)


    def generate_dos_real_space (self):
        print "Generate DOS real space"

        energies = np.linspace(-5, 5, num = 100) * eV 

        for nrg in energies:
            
            ldos = LocalDeviceDensityOfStates(
            configuration=self.configuration_obj,
            energy=nrg,
            kpoints=MonkhorstPackGrid(2,2),
            contributions=All,
            energy_zero_parameter=AverageFermiLevel,
            infinitesimal=1e-06*eV,
            self_energy_calculator=KrylovSelfEnergy(),

            )
            #ldos = LocalDeviceDensityOfStates(configuration_obj , nrg,  contributions=All)
            nlsave(self.device_config_path,ldos, object_id="LDDOS %f" % nrg.inUnitsOf(eV))

    def graph_diff_pot (self):
        print "Graphing Difference Potential"

    
        diff_potential_obj = nlread(self.device_config_path, ElectrostaticDifferencePotential)
        if not diff_potential_obj:
            self.generate_diff_pot()
            diff_potential_obj = nlread(self.device_config_path, ElectrostaticDifferencePotential)[0]
        else:
            diff_potential_obj = diff_potential_obj[0]



        proj_x_arr = []
        proj_y_arr = []

        #proj_x = diff_potential_obj.axisProjection ('Line', 'A', Spin.Sum, projection_point_x)
        #proj_y = diff_potential_obj.axisProjection ('Line', 'B', Spin.Sum, projection_point_y)
        proj_x_arr.append(diff_potential_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(diff_potential_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(diff_potential_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(diff_potential_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

        #proj_x = diff_potential_obj.axisProjection ('Average', 'A', Spin.Sum)
        #proj_y = diff_potential_obj.axisProjection ('Average', 'B', Spin.Sum)
        #proj_z = diff_potential_obj.axisProjection ('Average', 'C', Spin.Sum)

        #proj [0] = fractional coords
        #proj [1] = potential at the coordinate

     
        outfile = open (self.device_config_path + 'diffpot.plot', 'w')
        outfile.write ('x, \g(d)V\-(H), \g(d)V\-(H), y, \g(d)V\-(H), \g(d)V\-(H)\n')
        outfile.write ('Angstrom, eV, eV, Angstrom, eV, eV\n')
        outfile.write ('x, \g(d)V\-(H)_X_2_atoms, \g(d)V\-(H)_X_3_atoms, y, \g(d)V\-(H)_Y_2_atoms, \g(d)V\-(H)_Y_2_atoms\n')

        for i in range(len(proj_x_arr[0][0])):
        
            x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
            y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][i]).inUnitsOf(Angstrom))
            x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
            y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][i]).inUnitsOf(Angstrom))
            x_energy_0 = str(proj_x_arr[0][1][i].inUnitsOf(eV))
            y_energy_0 = str(proj_y_arr[0][1][i].inUnitsOf(eV))
            x_energy_1 = str(proj_x_arr[1][1][i].inUnitsOf(eV))
            y_energy_1 = str(proj_y_arr[1][1][i].inUnitsOf(eV))


            #printing VEFF for x direction
            outfile.write (x_angstrom_0 + ',')
            outfile.write (x_energy_0 + ',')
            outfile.write (x_energy_1 + ',')
            outfile.write (y_angstrom_0 + ',')
            outfile.write (y_energy_0 + ',')
            outfile.write (y_energy_1)
            outfile.write ('\n')


        

        outfile.close()
        

    def graph_v_eff (self):
        print "Graphing Veff"

        effective_potential_obj = nlread(self.device_config_path, EffectivePotential)
        if not effective_potential_obj:
            self.generate_v_eff ()
            effective_potential_obj = nlread(self.device_config_path, EffectivePotential)[0]
        else:
            effective_potential_obj = effective_potential_obj[0] 

        proj_x_arr = []
        proj_y_arr = []

        #proj_x = diff_potential_obj.axisProjection ('Line', 'A', Spin.Sum, projection_point_x)
        #proj_y = diff_potential_obj.axisProjection ('Line', 'B', Spin.Sum, projection_point_y)
        proj_x_arr.append(effective_potential_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(effective_potential_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(effective_potential_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(effective_potential_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

     
        outfile = open (self.device_config_path + 'veff.plot', 'w')
        outfile.write ('x, V\-(eff), V\-(eff), y, V\-(eff), V\-(eff)\n')
        outfile.write ('Angstrom, eV, eV, Angstrom, eV, eV\n')
        outfile.write ('x, V\-(eff_X_2_atoms), V\-(eff_X_3_atoms), y, V\-(eff_Y_2_atoms), V\-(eff_Y_3_atoms)\n')

        for i in range(len(proj_x_arr[0][0])):
            x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
            y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][i]).inUnitsOf(Angstrom))
            x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
            y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][i]).inUnitsOf(Angstrom))
            x_energy_0 = str(proj_x_arr[0][1][i].inUnitsOf(eV))
            y_energy_0 = str(proj_y_arr[0][1][i].inUnitsOf(eV))
            x_energy_1 = str(proj_x_arr[1][1][i].inUnitsOf(eV))
            y_energy_1 = str(proj_y_arr[1][1][i].inUnitsOf(eV))


            #printing VEFF for x direction
            outfile.write (x_angstrom_0 + ',')
            outfile.write (x_energy_0 + ',')
            outfile.write (x_energy_1 + ',')
            outfile.write (y_angstrom_0 + ',')
            outfile.write (y_energy_0 + ',')
            outfile.write (y_energy_1)
            outfile.write ('\n')


        outfile.close()
        

    def graph_e_density (self):
        print "Graphing E density"

        edensity_obj = nlread(self.device_config_path, ElectronDensity)[0]
        if not edensity_obj:
            self.generate_e_density()
            edensity_obj = nlread(self.device_config_path, ElectronDensity)[0]
        else:
            edensity_obj = edensity_obj[0]

        
        proj_x_arr = []
        proj_y_arr = []

        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

        outfile = open (self.device_config_path + 'edensity.plot', 'w')
        outfile.write ('x, n, n, y, n, n\n')
        outfile.write ('Angstrom, Angstrom\+(-3), Angstrom\+(-3), Angstrom, Angstrom\+(-3), Angstrom\+(-3)\n')
        outfile.write ('x, n_x_2_atoms, n_x_3_atoms, y, n_y_2_atoms, n_y_3_atoms\n')

        for i in range(len(proj_x_arr[0][0])):
        
            x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
            y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][i]).inUnitsOf(Angstrom))
            x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
            y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][i]).inUnitsOf(Angstrom))
            x_density_0 = str(proj_x_arr[0][1][i].inUnitsOf(Angstrom**-3))
            y_density_0 = str(proj_y_arr[0][1][i].inUnitsOf(Angstrom**-3))
            x_density_1 = str(proj_x_arr[1][1][i].inUnitsOf(Angstrom**-3))
            y_density_1 = str(proj_y_arr[1][1][i].inUnitsOf(Angstrom**-3))


            #printing VEFF for x direction
            outfile.write (x_angstrom_0 + ',')
            outfile.write (x_density_0 + ',')
            outfile.write (x_density_1 + ',')
            outfile.write (y_angstrom_0 + ',')
            outfile.write (y_density_0 + ',')
            outfile.write (y_density_1)
            outfile.write ('\n')


        outfile.close()

    def graph_e_diff_density (self):
        print "Graphing E diff density"

        edensity_obj = nlread(self.device_config_path, ElectronDifferenceDensity)
        if not edensity_obj:
            self.generate_e_diff_density()
            edensity_obj = nlread(self.device_config_path, ElectronDifferenceDensity)[0]
        else:
            edensity_obj = edensity_obj[0]
        
        proj_x_arr = []
        proj_y_arr = []

        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

        outfile = open (self.device_config_path + 'ediffdensity.plot', 'w')
        outfile.write ('x, \g(d)n, \g(d)n, y, \g(d)n, \g(d)n\n')
        outfile.write ('Angstrom, Angstrom\+(-3), Angstrom\+(-3), Angstrom, Angstrom\+(-3), Angstrom\+(-3)\n')
        outfile.write ('x, \g(d)n_x_2_atoms, \g(d)n_x_3_atoms, y, \g(d)n_y_2_atoms, \g(d)n_y_3_atoms\n')

        for i in range(len(proj_x_arr[0][0])):
        
            x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
            y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][i]).inUnitsOf(Angstrom))
            x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
            y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][i]).inUnitsOf(Angstrom))
            x_density_0 = str(proj_x_arr[0][1][i].inUnitsOf(Angstrom**-3))
            y_density_0 = str(proj_y_arr[0][1][i].inUnitsOf(Angstrom**-3))
            x_density_1 = str(proj_x_arr[1][1][i].inUnitsOf(Angstrom**-3))
            y_density_1 = str(proj_y_arr[1][1][i].inUnitsOf(Angstrom**-3))


            #printing VEFF for x direction
            outfile.write (x_angstrom_0 + ',')
            outfile.write (x_density_0 + ',')
            outfile.write (x_density_1 + ',')
            outfile.write (y_angstrom_0 + ',')
            outfile.write (y_density_0 + ',')
            outfile.write (y_density_1)
            outfile.write ('\n')


        outfile.close()
    def graph_dos_real_space (self):
        
        #print "NUMBER OF LDDSO BJECTS"
        #print len(nlread(self.device_config_path, LocalDeviceDensityOfStates))
        dos_objects = nlread(self.device_config_path, LocalDeviceDensityOfStates)

        outfile = open (self.device_config_path + 'lddos.plot', 'w')
        outfile.write ('Energy, x, LDDOS, y, LDDOS\n')
        outfile.write ('eV, Angstrom, arb, eV, Angstrom, arb\n')
        outfile.write ('Energy_x, x, LDDOS_x, y, LDDOS_y\n')


        for obj in dos_objects:
            energy = obj.energy()[0]
            proj_x = obj.axisProjection ('Sum', 'A', Spin.Sum)
            proj_y = obj.axisProjection ('Sum', 'B', Spin.Sum)

            print proj_x[0][0]
            print len(proj_x[0])
            print len(proj_x[1])
            for i in range(len(proj_x[0])):
                
                x_angstrom = self.frac_to_cart(self.x_length, proj_x[0][i]).inUnitsOf(Angstrom)
                y_angstrom = self.frac_to_cart(self.y_length, proj_y[0][i]).inUnitsOf(Angstrom)
                
                outfile.write (str(energy.inUnitsOf(eV)) + ',')
                outfile.write (str(x_angstrom) + ',')
                outfile.write (str(proj_x[1][i].inUnitsOf(Hartree**-1 * Angstrom**-3)) + ',')
                # For y coords
                outfile.write (str(y_angstrom) + ',')
                outfile.write (str(proj_y[1][i].inUnitsOf(Hartree**-1 * Angstrom**-3)) + '\n')

        #printing z fractional coords
        #outfile.write ('START_DATA|X|z|2\n')
        #for i in proj_z[0]:
            #outfile.write (str(i) + '\n')
        #outfile.write ('END_DATA\n')
        ##printing energies for y direction
        #outfile.write ('START_DATA|Y|n_z|0|2|kv-\n')
        #for i in proj_z[1]:
            #outfile.write (str(i.inUnitsOf(Angstrom**-3)) + '\n')
        #outfile.write ('END_DATA\n')

        outfile.close()
    def graph_dos_real_space_atk (self):
        
        #print "NUMBER OF LDDSO BJECTS"
        #print len(nlread(self.device_config_path, LocalDeviceDensityOfStates))
        lddos_list = nlread(self.device_config_path, LocalDeviceDensityOfStates)
        if not lddos_list:
            self.generate_dos_real_space()
            lddos_list = nlread(self.device_config_path, LocalDeviceDensityOfStates)



        #Find the z-spacing
        dX, dY, dZ = lddos_list[0].volumeElement().convertTo(Ang)
        dz = dZ.norm()
        shape = lddos_list[0].shape()
        z = dz * numpy.arange(shape[2])

        # calculate average lddos along z for each spectrum
        energies = []
        lddos_z = []
        for lddos in lddos_list:
            energies = energies + [lddos.energy().inUnitsOf(eV)]
            avg_z = numpy.apply_over_axes(numpy.mean,lddos[:,:,:],[0,1]).flatten()
            lddos_z = lddos_z + [avg_z]

        # plot as contour plot
        # make variables
        energies = numpy.array(energies)
        X, Y = numpy.meshgrid(z, energies)
        Z = numpy.array(lddos_z).reshape(numpy.shape(X))
        #print "X = "
        #print X
        #print "Y = "
        #print Y
        #print "Z = "
        #print Z
        #print "X min, max"
        #print numpy.amax(X)
        #print numpy.amin(X)
        #print "Y min, max"
        #print numpy.amax(Y)
        #print numpy.amin(Y)
        #print "Z min, max"
        #print numpy.amax(Z)
        #print numpy.amin(Z)

        import pylab
        #plot the LDDOS(E, z)
        pylab.xlabel('z (Angstrom)',fontsize=12,family='sans-serif')
        pylab.ylabel('Energy (eV)',fontsize=12,family='sans-serif')

        contour_values = numpy.linspace(0 , numpy.amax(Z), 25)
        pylab.contourf(X, Y, Z, contour_values)
        pylab.colorbar()
        pylab.axis([numpy.amin(X), numpy.amax(X), numpy.amin(Y), numpy.amax(Y)])

        pylab.title(self.device_config_path + ": E vs. z")
        pylab.savefig(self.device_config_path + 'lddos.png',dpi=100)


        #pylab.show()
    def graph_density_of_states (self):
        print "Graphing Density of States"

        #dos_obj = nlread(self.device_config_path, DeviceDensityOfStates)
        dos_obj = nlread(self.device_config_path, self.config_type[1])
    
        if not dos_obj:
            self.generate_density_of_states ()
            dos_obj = nlread(self.device_config_path, self.config_type[1])[0]
        else:
            print "Using existing generated DOS"
            dos_obj = dos_obj[0] 


        outfile = open (self.device_config_path + 'dos.plot', 'w')
        outfile.write ('TITLE|Energy vs. Density of States\n')
        outfile.write ('Units|eV|1/eV\n')
        outfile.write ('X_AXIS_LABEL|Energy\n')
        outfile.write ('Y_AXIS_LABEL|Projected Density of States\n')
        outfile.write ('X_UNIT|eV\n')
        outfile.write ('Y_UNIT|eV^{-1}\n')




        energies = dos_obj.energies()
        print len(dos_obj.elements())
        num_atoms = len(dos_obj.elements())
        dos_projections = [dos_obj.evaluate(projection_list = ProjectionList([i])) \
                      for i in range(0,num_atoms)]
        #print dos_projection
        #Add up the DOS projections for each atom to get final Projected DOS
        final_dos = [sum(i) for i in zip (*dos_projections)]

        #Writing the energies in the x axis
        outfile.write ('START_DATA|X|Energy|0\n')

        j = 0
        for i in final_dos:
            outfile.write (str(energies[j].inUnitsOf(eV))+'\n')
            j = j + 1
        outfile.write ('END_DATA\n')
        #Writing the density of states now, in the y axis
        outfile.write ('START_DATA|Y|Projected Density of States|0|0|r.-\n')
        for i in final_dos:
            outfile.write (str(i.inUnitsOf(eV**-1)) + '\n')
        outfile.write ('END_DATA\n')
       
        
        outfile.close()

    def generate_density_of_states (self):
        print "Generating DOS"


       # -------------------------------------------------------------
        # Device density of states
        # -------------------------------------------------------------
        if self.config_type == self.ConfigTypes.DEVICE:

            dos = DeviceDensityOfStates(
                configuration=self.configuration_obj,
                energies=numpy.linspace(-1,1,300)*eV,
                kpoints=MonkhorstPackGrid(4,4),
                contributions=All,
                energy_zero_parameter=AverageFermiLevel,
                infinitesimal=5e-07*eV,
                self_energy_calculator=KrylovSelfEnergy(),
             )
        elif self.config_type == self.ConfigTypes.BULK:
            dos = DensityOfStates(
                configuration=self.configuration_obj,
                kpoints=MonkhorstPackGrid(4,4,1),
                #default = All
                #bands_above_fermi_level=All,
                energy_zero_parameter=FermiLevel,
             )


        nlsave(self.device_config_path, dos)

    def generate_bulk_bandstructure (self):
        print "Generating BULK Bandstructure"

        bandstructure_obj = nlread(self.device_config_path, Bandstructure)
        if not bandstructure_obj:
            bandstructure = Bandstructure (
                configuration=self.configuration_obj,
                route=['G', 'Z', 'R', 'X', 'G', 'M', 'X'],
                points_per_segment=40,
                bands_above_fermi_level=5
            )
            nlsave(self.device_config_path, bandstructure)
        else:
            print "Already generated Bandstructure"

     
    def analyze(self):
       
        print "Starting analysis..."

        #works for both bulk and device
        self.graph_density_of_states ()

        if (self.config_type == self.ConfigTypes.BULK):
            self.generate_bulk_bandstructure()

        if (self.config_type == self.ConfigTypes.DEVICE):
            self.graph_dos_real_space_atk ()


        #self.generate_device_density_of_states ()
        #self.generate_v_eff ()
        #self.generate_diff_pot()
        #self.generate_e_diff_density ()
        #self.generate_e_density ()
        #self.generate_dos_real_space ()
        #self.graph_v_eff ()
        #self.graph_dos_real_space ()
        #self.graph_dos_real_space_atk ()
        #self.graph_diff_pot()
        #self.graph_e_density ()
        #self.graph_e_diff_density ()
        #self.graph_density_of_states ()
    def plot(self):
        print "Plotting data..."
        

if __name__ == "__main__":
        dev_anal_obj = DeviceAnalysis(sys.argv[1:])
        dev_anal_obj.analyze()
