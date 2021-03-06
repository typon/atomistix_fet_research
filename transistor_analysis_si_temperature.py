#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime
import socket
import os
import sys
import re
import csv
import StringIO
import numpy as np
import getopt
import pdb
import shutil
from pprint import pprint
import ntpath
from NL.IO.NLSaveUtilities import nlinspect

def enum (**enums):
    return type ('Enum', (), enums)

class DeviceAnalysis: 

    def __init__(self, argv):
        self.exchange_correlation = GGA.PBE
        self.k_point_sampling = (1, 1, 100)
        self.default_gate_voltage = 0 * Volt
        self.analysis_type = None
        voltage_range_input = {'gv':False, 'vds':False,}
        self.temp = 300
        # Define gate_voltages

        self.ConfigTypes = enum (BULK = (1, DensityOfStates, BulkConfiguration) , DEVICE = (2, DeviceDensityOfStates, DeviceConfiguration))


        try:
            opts, args = getopt.getopt(argv,"hiagvmt:",["ifile=","analysis=", "gate_v=", "vds=", "model=", "temp="])
        except getopt.GetoptError:
            self.usage()
        if not opts:
            print 'No options supplied'
            self.usage()
        for opt, arg in opts:

            print opt
            if opt == '-h':
                self.usage()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-a", "--analysis"):
                self.analysis_type = arg
            elif opt in ("-g", "--gate_v"):
                gate_voltage_params = arg.split(',')
                if len(gate_voltage_params) is not 4:
                    self.usage()

                self.gate_v_start = float(gate_voltage_params[0])
                self.gate_v_end = float(gate_voltage_params[1])
                self.gate_v_points = float(gate_voltage_params[2])
                self.vds_bias = float(gate_voltage_params[3])
                voltage_range_input['gv'] = True
            elif opt in ("-v", "--vds"):
                vds_params = arg.split(',')
                if len(vds_params) is not 4:
                    self.usage()

                self.vds_start = float(vds_params[0])
                self.vds_end = float(vds_params[1])
                self.vds_points = float(vds_params[2])
                self.gate_v = float(vds_params[3])
                voltage_range_input['vds'] = True
            elif opt in ("-m", "--model"):
				self.model_type = arg
            elif opt in ("-t", "--temp"):
				self.temp = arg

        if self.analysis_type is None:
            print "Please specify analysis type..."
            self.usage()
        if self.analysis_type == 'vds_sweep' and voltage_range_input ['vds'] is False:
            self.usage()
        elif self.analysis_type == 'gate_sweep' and voltage_range_input ['gv'] is False:
            self.usage()
            
        
        
        self.print_sim_info()

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

        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
        self.device_config_path = tmp_path+file_base_name+".analysis.nc"
        print "Device config path = ", self.device_config_path


        #try reading device config first
        try:
            with open(self.device_config_path):
                print "Accessing initial configuration"
                init_config_obj = self.find_zero_volt_config ()
                
                    
                    

        except IOError:
            print 'Oh dear. No device config file exists.'

        if  not init_config_obj:
            print "No initial configuration exists, running DFT calculation"

            print "Extracting configuration from file"
            init_config_obj, basis_set, charge, temp = self.create_device_config(inputfile)

            #setting iether bulk or device config type
            self.set_configuration_type(init_config_obj)

            if (self.config_type == self.ConfigTypes.DEVICE):
                print "device"
                if (self.model_type == 'dft'):
                    self.calculator = self.create_device_calculator_dft (basis_set, charge, temp)
                elif (self.model_type == 'huckel'):
                    self.calculator = self.create_device_calculator_huckel (basis_set, charge, temp)
            elif (self.config_type == self.ConfigTypes.BULK):
                print "bulk"
                self.calculator = self.create_bulk_calculator (basis_set)

            init_config_obj.setCalculator(self.calculator)
            nlprint(init_config_obj)
            init_config_obj.update()

            nlsave(device_config_path, init_config_obj, object_id="Config, GateV %f, Vds %f" % (0.0, 0.0))

            if (self.config_type == self.ConfigTypes.DEVICE):
                configuration_obj = nlread(device_config_path, DeviceConfiguration)
            elif (self.config_type == self.ConfigTypes.BULK):
                configuration_obj = nlread(device_config_path, BulkConfiguration)


            self.configuration_obj = configuration_obj [0]

        else:
            print 'Found initial configuration'
            init_config_obj = init_config_obj [0]
            self.set_configuration_type(init_config_obj)
            self.configuration_obj = init_config_obj

        
        self.extract_dimensions()
 
    def usage(self):
        print 'python device_analysis.py --ifile=<inputfile> --model=<huckel|dft> --analysis=<gate_sweep|vds_sweep|bulk> (--gate_v=<start,end,steps,vds_value> | --vds=<start,end,steps>)'
        sys.exit()
    def print_sim_info(self):
        print "Machine name: ", socket.gethostname()

        print "Starting simulation on: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def gv_obj (self, configuration_obj):
            metallic_regions = configuration_obj.metallicRegions()
            if not metallic_regions:
                print "There are no metallic regions, device is not gated..."
            #return 0 volt value
                return self.default_gate_voltage.inUnitsOf(Volt)
            gate_bias = metallic_regions[0].value().inUnitsOf(Volt)
        #print "Metallic region voltages: "
        #for region in metallic_regions:
        #print region.value().inUnitsOf(Volt),

            return gate_bias
    def vds_obj (self, configuration_obj):
            if self.config_type == self.ConfigTypes.DEVICE:
                electrode_voltages = configuration_obj.calculator().electrodeVoltages()
                return electrode_voltages[0].inUnitsOf(Volt) * 2
            elif self.config_type == self.ConfigTypes.BULK:
        #VDS for bulk is always 0
                return 0


    def find_zero_volt_config(self):

        print "Finding zero volt config..."
        zero_volt_config = []

            #try reading device type first
        zero_volt_config = nlread(self.device_config_path, DeviceConfiguration, 
                                object_id="Config, GateV %f, Vds %f" % (0.0, 0.0), read_state = True)
        if not zero_volt_config:
            zero_volt_config = nlread(self.device_config_path, BulkConfiguration, 
                                object_id="Config, GateV %f, Vds %f" % (0.0, 0.0), read_state = True)

        if (not zero_volt_config):
            print "---------------------------------------"
            print "Warning...No zero volt config found..."
            print "---------------------------------------"



        return zero_volt_config






    def set_configuration_type(self, configuration_obj):
        if 'BulkConfiguration' in str(type(configuration_obj)):
            self.config_type = self.ConfigTypes.BULK
        elif 'DeviceConfiguration' in str(type(configuration_obj)):
            self.config_type = self.ConfigTypes.DEVICE
        else:
           print str(type(configuration_obj))
           print "Error: Not valid configuration type"
           sys.exit()

    def find_closest_state (self, gate_voltage, drain_voltage):

    #holds all objects. need to extract transmissionspectrum objects
        all_nc_keys = nlinspect(self.device_config_path)


        config_objects_ids = []
        for key in all_nc_keys:
            if key[0] == 'DeviceConfiguration':
                config_objects_ids.append (key)



    #config_objects_ids: [0] = DeviceConfiguration
    #                    [1] = object_id
    #                    [2] = Fingerprint

    #Sort the Trans objects by voltage first for printing
    #tuple of (gate_v, vds)
        sorted_voltages = []
        for config_obj in config_objects_ids:
    #extracting the vds and gate voltage
            object_id = config_obj[1]
            search_obj = re.search (r'Config, GateV ([-0-9.]+), Vds ([-0-9.]+)$', object_id, re.M)
            if search_obj:
                gate_v = float(search_obj.group(1))
                vds = float(search_obj.group(2))
                sorted_voltages.append ((gate_v, vds))

    #sort by Vgs
        sorted_voltages.sort(key=lambda tup: tup[0])


        vds_list = [tup[1] for tup in sorted_voltages]
    #find the closest vds tuple first

        closest_vds = min(vds_list, key=lambda x:abs(x-drain_voltage.inUnitsOf(Volt)))

    #get gate voltages with only closest vds

        culled_vgs_list = [tup[0] for tup in sorted_voltages if tup[1] == closest_vds]

        closest_vgs = min(culled_vgs_list, key=lambda x:abs(x-gate_voltage.inUnitsOf(Volt)))

    #get the closest intial state

        
        initial_state = nlread(self.device_config_path, self.config_type[2], 
                                object_id="Config, GateV %f, Vds %f" % (closest_vgs, closest_vds), read_state = True)
        initial_state = initial_state [0]


        vgs_init_state = self.gv_obj (initial_state)
        vds_init_state = self.vds_obj (initial_state)

        print ("Using initial state with VGS = %f, VDS = %f") % (vgs_init_state, vds_init_state)

        return initial_state
    def gate_voltage_sweep (self, voltages, drain_voltage):
        print "Sweeping Gate voltages: ", voltages

        ##Only perform DFT calculations for voltages that are incomplete
        #if self.config_type == self.ConfigTypes.DEVICE:
            #config_objs = nlread(self.device_config_path, DeviceConfiguration)
        #elif self.config_type == self.ConfigTypes.BULK:
            #config_objs = nlread(self.device_config_path, BulkConfiguration)
        ##TODO MAKE THIS INTO ASSERT
        #if not config_objs:
            #print "There must be at least 0 volt config!"
            #sys.exit()
#
#
        ##find only configs with particular vds bias
        #configs_vds_bias = []
        #for config in config_objs:
            #electrode_voltages = config.calculator().electrodeVoltages()
            #if abs(electrode_voltages[0].inUnitsOf(Volt)) == abs((drain_voltage.inUnitsOf(Volt)/2)):
                #configs_vds_bias.append(config)
        #
#
        #if not configs_vds_bias:
            #print "There are no configs with vds = ", drain_voltage
            #sys.exit(1)

        ##there are some configs
        #voltages = [x.inUnitsOf(Volt) for x in voltages]

        #find zero volt vds config first
        configs = []
        zero_volt_config = nlread(self.device_config_path, self.config_type[2], 
                                object_id="Config, GateV %f, Vds %f" % (0.0, drain_voltage.inUnitsOf(Volt)), read_state = False)
        if not zero_volt_config:
            print "There are no configs with vds = ", drain_voltage
            sys.exit(1)

        #now remove any gv bias configs for drain_voltage
        valid_voltages = []
        for voltage in voltages:
            config = nlread(self.device_config_path, self.config_type[2], 
                         object_id="Config, GateV %f, Vds %f" % (voltage.inUnitsOf(Volt), drain_voltage.inUnitsOf(Volt)), read_state = False)
            if not config:
                valid_voltages.append(voltage)
                


        #for config in configs_vds_bias:
#
            #metallic_regions = config.metallicRegions()
            #gate_bias = metallic_regions[0].value().inUnitsOf(Volt)
            ##this bias has already been compiled
            #if gate_bias in voltages:
                #voltages.remove (gate_bias)
                
               
        


        print "Gate Voltages being swept: ", valid_voltages

        # Read in the old configuration
        #TODO get the most appropirate voltage
        new_config = zero_volt_config[0]
        calculator = new_config.calculator()
        metallic_regions = new_config.metallicRegions()


        # Perform loop over gate voltages
        for gate_voltage in valid_voltages:
            print ("Running self consistent calculation with VGS = %f, VDS = %f") % (gate_voltage, drain_voltage)
            # Set the gate voltages to the new values
            new_regions = [m(value = gate_voltage) for m in metallic_regions]
            new_config.setMetallicRegions(new_regions)

            # Make a copy of the calculator and attach it to the configuration
            # Restart from the previous scf state
            #find closest state
            init_state = self.find_closest_state(gate_voltage, drain_voltage)

            new_config.setCalculator(calculator(),
                 initial_state=init_state)
            new_config.update()
            nlsave(self.device_config_path, new_config, 
                object_id="Config, GateV %f, Vds %f" % (self.gv_obj(new_config), self.vds_obj(new_config)))
                

    def vds_sweep (self, gate_voltage, vds_voltages):

        #pdb.set_trace()
        
        #Only perform DFT calculations for voltages that are incomplete
        if self.config_type == self.ConfigTypes.DEVICE:
            config_objs = nlread(self.device_config_path, DeviceConfiguration, read_state=False)
        elif self.config_type == self.ConfigTypes.BULK:
            config_objs = nlread(self.device_config_path, BulkConfiguration, read_state=False)
        #TODO MAKE THIS INTO ASSERT
        if not config_objs:
            print "There must be at least 0 volt config!"
            sys.exit()

        #Figure out if this configuration with current gate voltage is already done

        #now remove any gv bias configs for drain_voltage
        valid_voltages = []
        for voltage in vds_voltages:
            obj_id = "Config, GateV %f, Vds %f" % (gate_voltage.inUnitsOf(Volt), voltage.inUnitsOf(Volt))
            config = nlread(self.device_config_path, self.config_type[2], 
                         object_id=obj_id, read_state=False)
            if not config:
                valid_voltages.append(voltage)


        zero_volt_config = self.configuration_obj
        calculator = zero_volt_config.calculator()
        print "Gate Voltage: ", self.gv_obj (zero_volt_config)
        print "VDS voltages being swept: ", valid_voltages
        # Perform loop over gate voltages
        for voltage in valid_voltages:

            print ("Running self consistent calculation with VGS = %f, VDS = %f") % (gate_voltage, voltage)
            init_state = self.find_closest_state(gate_voltage, voltage)


            # Set the gate voltages to the new values
            zero_volt_config.setCalculator(
              calculator(electrode_voltages=(voltage/2, -voltage/2)), 
              initial_state=init_state)

            # Make a copy of the calculator and attach it to the configuration
            # Restart from the previous scf state
            zero_volt_config.update()
            nlsave(self.device_config_path, zero_volt_config, object_id="Config, GateV %f, Vds %f" % (self.gv_obj(zero_volt_config), self.vds_obj(zero_volt_config)))
 


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
        charge = None
        temp = None

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

        if s:
            print "###########################"
            print "error: %s\n" % s
            print "###########################"

        #s = codeOut.getvalue()
        #print "output:\n%s" % s

        codeOut.close()
        codeErr.close()

        if temp is None:
            print "Please specify temperature ..."
            sys.exit()
        if charge is None:
            print "Please specify doping charge..."
            sys.exit()
        if len(basis_set) == 0:
           print "Error: No basis set specified"
           sys.exit()
        if device_configuration is None:
            return bulk_configuration, basis_set, charge, temp
        elif bulk_configuration is None:
            return device_configuration, basis_set, charge, temp
        else:
           print "Error: No configuration specified"
           sys.exit()
            
            
    def create_bulk_calculator (self, basis_set):

        if self.analysis_type == "bulk":
            self.k_point_sampling = (5, 5, 100)
            
        bulk_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling
            )
        calculator = LCAOCalculator(
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=bulk_numerical_accuracy_parameters,
            )

        return calculator

    def create_device_calculator_huckel (self, basis_set, charge, temp):


        #----------------------------------------
        # Numerical Accuracy Settings
        #----------------------------------------
        left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff=20.0*Hartree,
            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff=20.0*Hartree,
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff=20.0*Hartree,
            )
        #----------------------------------------
        # Iteration Control Settings
        #----------------------------------------
        left_electrode_iteration_control_parameters = IterationControlParameters()

        right_electrode_iteration_control_parameters = IterationControlParameters()

        device_iteration_control_parameters = IterationControlParameters()
        #device_iteration_control_parameters = IterationControlParameters(
            #damping_factor=0.25,
            #preconditioner=Kerker(0.02*Hartree, 0.5*Hartree, 0.01),
            #mixing_variable=HamiltonianVariable,
            #number_of_history_steps=12, 
        #)

        # Poisson Solver Settings
        #----------------------------------------
        left_electrode_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        right_electrode_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        device_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [DirichletBoundaryCondition,DirichletBoundaryCondition]]
            )

        #----------------------------------------
        # Electrode Calculators
        #----------------------------------------
        left_electrode_calculator = HuckelCalculator(
            basis_set=basis_set,
            charge=charge * -1 ,
            numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
            iteration_control_parameters=left_electrode_iteration_control_parameters,
            poisson_solver=left_electrode_poisson_solver,
            )

        right_electrode_calculator = HuckelCalculator(
            basis_set=basis_set,
            charge=charge,
            numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
            iteration_control_parameters=right_electrode_iteration_control_parameters,
            poisson_solver=right_electrode_poisson_solver,
            )

        #----------------------------------------
        # Device Calculator
        #----------------------------------------
        calculator = DeviceHuckelCalculator(
            basis_set=basis_set,
            numerical_accuracy_parameters=device_numerical_accuracy_parameters,
            iteration_control_parameters=device_iteration_control_parameters,
            poisson_solver=device_poisson_solver,
            electrode_calculators=
                [left_electrode_calculator, right_electrode_calculator],
            )



        return calculator

    def create_device_calculator_dft (self, basis_set, charge, temp):


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
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff = 60.0*Rydberg,
            electron_temperature=temp*Kelvin,

            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff = 60.0*Rydberg,
            electron_temperature=temp*Kelvin,
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff = 60.0*Rydberg,
            electron_temperature=temp*Kelvin,
            )

        #----------------------------------------
        # Poisson Solver Settings
        #----------------------------------------
        left_electrode_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        right_electrode_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
            )

        device_poisson_solver = MultigridSolver(
            boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [NeumannBoundaryCondition,NeumannBoundaryCondition],
                                 [DirichletBoundaryCondition,DirichletBoundaryCondition]]
            )


        #----------------------------------------
        # Electrode Calculators
        #----------------------------------------
        left_electrode_calculator = LCAOCalculator(
            charge=charge * -1 ,
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
            poisson_solver=left_electrode_poisson_solver,
            )

        right_electrode_calculator = LCAOCalculator(
            charge=charge * -1,
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=right_electrode_numerical_accuracy_parameters,
            poisson_solver=right_electrode_poisson_solver,
            )

        #----------------------------------------
        # Device Calculator
        #----------------------------------------
        calculator = DeviceLCAOCalculator(
            poisson_solver=device_poisson_solver,
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=device_numerical_accuracy_parameters,
            electrode_calculators=
                [left_electrode_calculator, right_electrode_calculator],
            )



        return calculator

    def symmetry_points (self):
        lattice = self.configuration_obj.bravaisLattice()
        points = []
        for point in lattice.symmetryPoints().keys():
            points.append(point)
            
        self.route = points
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



    def generate_transmission_spectrum (self):
        print "Generating Transmission Spectrum "

        transmission_spectrum = TransmissionSpectrum(
                configuration=self.configuration_obj,
                energies=numpy.linspace(-4,4,301)*eV,
                #self_energy_calculator=DirectSelfEnergy(),
                )

        nlsave(self.device_config_path, transmission_spectrum, object_id="Trans, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


    def generate_diff_pot (self):
        print "Generating Difference Potential"

        diff = ElectrostaticDifferencePotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, diff, object_id="DiffPot, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

    def generate_v_ext (self):
        print "Generating V external"

        v_ext = ExternalPotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, v_ext, object_id="Vext, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


    def generate_v_eff (self):
        print "Generating Veff"

        v_eff = EffectivePotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, v_eff, object_id="Veff, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

    def generate_e_diff_density (self):
        print "Generating Electron Difference Density"

        electron_diff_density = ElectronDifferenceDensity (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, electron_diff_density, object_id="Ediffdens, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


    def generate_e_density (self):
        print "Generating Electron Density"

        electron_density = ElectronDensity (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, electron_density, object_id="Edens, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


    def generate_dos_real_space (self):
        print "Generate DOS real space"

        energies = np.linspace(-5, 5, num = 100)
        done_nrg = []

        #lddos_list = nlread(self.device_config_path, LocalDeviceDensityOfStates)
        lddos_list = nlread(self.device_config_path, LocalDeviceDensityOfStates)
        if lddos_list:
           #generate for the erngies that are not done.
            for lddos in lddos_list:
                done_nrg.append(lddos.energy().inUnitsOf(eV)[0])
        #else:
              #do all energies, nothing exists so far
           
        #only do energies which are not already done
        energies = [x for x in energies if x not in done_nrg]
        energies = [x*eV for x in energies] 

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
            nlsave(self.device_config_path,ldos, object_id="LDDOS %f, GateV %f, Vds %f" % (nrg.inUnitsOf(eV), self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

    def graph_diff_pot (self):
        print "Graphing Difference Potential"

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
    
        diff_potential_obj = nlread(self.device_config_path, ElectrostaticDifferencePotential, object_id="DiffPot, GateV %f, Vds %f" % (gv, vds))
        if not diff_potential_obj:
            self.generate_diff_pot()
            diff_potential_obj = nlread(self.device_config_path, ElectrostaticDifferencePotential, object_id="DiffPot, GateV %f, Vds %f" % (gv, vds))[0]
        else:
            diff_potential_obj = diff_potential_obj[0]

        return 


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
        
    def graph_v_ext (self):
        print "Graphing Vext"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        ext_pot_obj = nlread(self.device_config_path, ExternalPotential, object_id="Vext, GateV %f, Vds %f" % (gv, vds))

        if not ext_pot_obj:
            self.generate_v_ext ()
            ext_pot_obj = nlread(self.device_config_path, ExternalPotential, object_id="Vext, GateV %f, Vds %f" % (gv, vds))[0]
        else:
            ext_pot_obj = ext_pot_obj [0] 


    def graph_v_eff (self):
        print "Graphing Veff"

                                            
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        effective_potential_obj = nlread(self.device_config_path, EffectivePotential, object_id="Veff, GateV %f, Vds %f" % (gv, vds))
        if not effective_potential_obj:
            self.generate_v_eff ()
            effective_potential_obj = nlread(self.device_config_path, EffectivePotential, object_id="Veff, GateV %f, Vds %f" % (gv, vds))[0]
        else:
            effective_potential_obj = effective_potential_obj[0] 

        return 
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


        print "Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        #get the DOS object for the gate voltage we're working wiht
        dos_objects = nlread(self.device_config_path, self.config_type[1], object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

        if not dos_objects:
            self.generate_density_of_states ()
            dos_objects = nlread(self.device_config_path, self.config_type[1], object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        else:
            print "Using existing generated DOS"
        dos_obj = dos_objects[0] 

        outfile = open (self.device_config_path + 'dos.plot', 'w')
        outfile.write ('Energy, Density of States\n')
        outfile.write ('eV, 1/eV\n')


        energies = dos_obj.energies()
        num_atoms = len(dos_obj.elements())
        dos_projections = [dos_obj.evaluate(projection_list = ProjectionList([i])) \
                      for i in range(0,num_atoms)]
        #print dos_projection
        #Add up the DOS projections for each atom to get final Projected DOS
        final_dos = [sum(i) for i in zip (*dos_projections)]


        j = 0
        for i in final_dos:
            outfile.write (str(energies[j].inUnitsOf(eV))+',')
            outfile.write (str(i.inUnitsOf(eV**-1)) + '\n')
            j = j + 1
       
        
        outfile.close()
    def graph_transmission_spectrum (self):
        print "Graphing Transmission spectrum"


        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        print "Trans, GateV %f, Vds %f" % (gv, vds)
        #get the DOS object for the gate voltage we're working wiht
        trans_objects = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv, vds))
    
        if not trans_objects:
            self.generate_transmission_spectrum ()
            #trans_objects = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv, vds))
        else:
            print "Using existing transmission spectrum"


    def print_currents_file (self, currents_plot_file=None):
        if currents_plot_file is None:
            currents_plot_file = self.device_config_path + 'temp_currents.plot'     

        if os.path.isfile(currents_plot_file):
            print "Currents file exists, moving file and creating new file..."
            found = True
            num = 1
            while (found and num < 3):

                bak_file_name = currents_plot_file + '.' + str(num)
                if os.path.isfile(bak_file_name):
                    num = num + 1
                else:
                    shutil.copy (currents_plot_file, bak_file_name)
                    found = False

        outfile = open (currents_plot_file, 'w')
        outfile.write ("V\-(GS), V\-(DS), Current\n")
        outfile.write ("V, V, µA\n")
 
        #holds all objects. need to extract transmissionspectrum objects
        all_nc_keys = nlinspect(self.device_config_path)

        
        trans_objects_ids = []
        for key in all_nc_keys:
            if key[0] == 'TransmissionSpectrum':
                trans_objects_ids.append (key)
                

        #trans_objects_ids: [0] = TransmissionSpectrum.
                           #[1] = object_id
                           #[2] = Fingerprint

        #Sort the Trans objects by voltage first for printing
        #tuple of (gate_v, vds)
        sorted_voltages = []
        for trans_obj in trans_objects_ids:
            #extracting the vds and gate voltage
            object_id = trans_obj[1]
            search_obj = re.search (r'Trans, GateV ([-0-9.]+), Vds ([-0-9.]+)$', object_id, re.M)
            if search_obj:
                gate_v = float(search_obj.group(1))
                vds = float(search_obj.group(2))
                sorted_voltages.append ((gate_v, vds))

        #sort by Vds
        sorted_voltages.sort(key=lambda tup: tup[0])

        
        for trans_obj in trans_objects_ids:
            #extracting the vds and gate voltage
            object_id = trans_obj[1]
            search_obj = re.search (r'Trans, GateV ([-0-9.]+), Vds ([-0-9.]+)$', object_id, re.M)
            if search_obj:
                gate_v = float(search_obj.group(1))
                vds = float(search_obj.group(2))
                sorted_voltages.append ((gate_v, vds))

            trans_objects = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gate_v, vds))
            trans_object = trans_objects [0]
            print trans_object.energyZero()
                        
            current_in_uA = trans_object.current(electrode_temperatures=[self.temp,self.temp]).inUnitsOf(Ampere) * 10**6

            outfile.write (str(gate_v) + "," + str (vds) + "," + str (current_in_uA) + "\n")

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
                kpoints=MonkhorstPackGrid(4,4,4),
                #default = All
                #bands_above_fermi_level=All,
                energy_zero_parameter=FermiLevel,
             )


        nlsave(self.device_config_path, dos, object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

    def generate_bulk_bandstructure (self):
        print "Generating BULK Bandstructure"

        self.symmetry_points()
        bandstructure_obj = nlread(self.device_config_path, Bandstructure)
        self.band_rout = self.route
            
        if not bandstructure_obj:
            bandstructure = Bandstructure (
                configuration=self.configuration_obj,
                route=self.band_rout,
                points_per_segment=100,
                bands_above_fermi_level=5
            )
            nlsave(self.device_config_path, bandstructure, object_id="Bands, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        else:
            print "Already generated Bandstructure"

     
    def set_default_voltages (self, gate_v = 0*Volt, vds = 0*Volt):
        
        #config_objs = []
        #if self.config_type == self.ConfigTypes.DEVICE:
            #config_objs = nlread(self.device_config_path, DeviceConfiguration)
        #elif self.config_type == self.ConfigTypes.BULK:
            #config_objs = nlread(self.device_config_path, BulkConfiguration)
        ##TODO MAKE THIS INTO ASSERT
        #if not config_objs:
            #print "There must be some configs at all!"
            #sys.exit()

        #pdb.set_trace()

        default_config = None

        default_config = nlread(self.device_config_path, self.config_type[2], 
                                object_id="Config, GateV %f, Vds %f" % (gate_v.inUnitsOf(Volt), vds.inUnitsOf(Volt)))

        if (default_config is None) or (not default_config):
            #TODO MAKE THIS INTO ASSERT
            print "No config found with this voltage! Run the init first! Vds = ", vds, " GateV = ", gate_v
            sys.exit()
        
        default_config = default_config[0]
        self.configuration_obj = default_config
            

    def analyze(self, run_dos_real_space=False):
       
        print "Starting analysis..."

        #works for both bulk and device
        #self.graph_density_of_states ()

        if (self.config_type == self.ConfigTypes.BULK):
            self.generate_bulk_bandstructure()

        if (self.config_type == self.ConfigTypes.DEVICE):

            self.graph_transmission_spectrum()
            if run_dos_real_space is True:
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
        #self.graph_v_ext()
        #self.graph_e_density ()
        #self.graph_e_diff_density ()
        #self.graph_density_of_states ()
    def plot(self):
        print "Plotting data..."
    def sort_csv (self, file_name):
        
        with open (file_name, 'r') as csv_con:
            reader = csv.reader (csv_con, delimiter=',')
            file_matrix = list(reader)

        print file_matrix

        exit(1)


if __name__ == "__main__":

        #gate_voltage_list=[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1]*Volt
        #gate_voltage_list

        dev_anal_obj = DeviceAnalysis(sys.argv[1:])
        analysis_type = dev_anal_obj.analysis_type

        if analysis_type == "bulk":
            dev_anal_obj.analyze(run_dos_real_space = True)
        elif analysis_type == "vds_sweep":
            dev_anal_obj.analyze()
            vds_voltage_list = np.linspace(dev_anal_obj.vds_start, dev_anal_obj.vds_end, num = dev_anal_obj.vds_points, endpoint=False) * Volt

            #
            print "Sweeping VDS voltages: ", vds_voltage_list
            #Gate voltage for which VDS voltage sbeing swept
            gate_voltage = dev_anal_obj.gate_v * Volt

            #pdb.set_trace()

            dev_anal_obj.gate_voltage_sweep ([gate_voltage], 0.0*Volt)

            

            dev_anal_obj.set_default_voltages(gate_v=gate_voltage, vds = 0.0*Volt)
            dev_anal_obj.vds_sweep (gate_voltage, vds_voltage_list)
            for vds in vds_voltage_list:
                dev_anal_obj.set_default_voltages(gate_v=gate_voltage, vds = vds)
                dev_anal_obj.analyze()
            dev_anal_obj.print_currents_file ()
        elif analysis_type == "gate_sweep":
			
            dev_anal_obj.analyze()
            gate_voltage_list= np.linspace(dev_anal_obj.gate_v_start, dev_anal_obj.gate_v_end, num = dev_anal_obj.gate_v_points, endpoint=False) * Volt
            vds_voltage_list=[dev_anal_obj.vds_bias]*Volt
            dev_anal_obj.set_default_voltages(gate_v=0.0 * Volt, vds = 0.0*Volt)
            gate_voltage = 0.0 * Volt
            dev_anal_obj.vds_sweep (gate_voltage, vds_voltage_list)
            print "#####"
            print "Sweeping Gate Voltages: ", gate_voltage_list
            print "VDS Voltage: ", vds_voltage_list
            print "#####"
            for vds in vds_voltage_list:
                dev_anal_obj.gate_voltage_sweep (gate_voltage_list, vds)

            for gv in gate_voltage_list:
                dev_anal_obj.set_default_voltages(gate_v=gv, vds=vds_voltage_list[0])
                dev_anal_obj.analyze()
            dev_anal_obj.print_currents_file ()



        #set gate voltage for which to sweep vds
        #sweep over VDS's 
        #sweep over gate voltage with certain vds


