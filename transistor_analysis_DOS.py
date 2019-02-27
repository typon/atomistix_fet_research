#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pylab 
import collections
from datetime import datetime
import time
import multiprocessing
import socket
import os
import sys
import re
import csv
import StringIO
import numpy as np
import scipy
from operator import add
import getopt
import pdb
import shutil
from pprint import pprint
import ntpath
import itertools
from NL.IO.NLSaveUtilities import nlinspect
from NanoLanguage import *
import NLEngine
electron_charge = 1.6021766e-19 * Coulomb

def enum (**enums):
    return type ('Enum', (), enums)

class Semaphore:
    def __init__(self, device_config_path):
        processId = str(os.getpid())
        self.fileName = device_config_path + '.sem.' + processId + '.lock'
    def touch (self, fileName):
        with open(fileName, 'a'):
            os.utime(fileName, None)
    def lock (self):
        exists = True
        while (exists):
            exists = os.path.exists(self.fileName)
            print 'waiting for ', self.fileName
        self.touch(self.fileName)
    def release (self):
        exists = os.path.exists(self.fileName)
        if (exists):
            os.remove(self.fileName)
class DeviceAnalysis: 

    def __init__(self, argv):
        self.exchange_correlation = GGA.PBE
        self.k_point_sampling = (1, 1, 100)
        self.default_gate_voltage = 0 * Volt
        self.analysis_type = None
        self.voltage_range_input = {'gv':False, 'vds':False,}
        self.band_route = None
        self.band_zero = "FermiLevel"
        self.nprocessors = 4
        self.dos_energy_range = []
        self.calc_types = []
        self.ang_momenta = []
        self.band_dims = 1
        # Define gate_voltages

        self.ConfigTypes = enum (BULK = (1, DensityOfStates, BulkConfiguration) , DEVICE = (2, DeviceDensityOfStates, DeviceConfiguration))
        self.objects_enum = {"Veff": EffectivePotential, "Vext": ExternalPotential, "DiffPot": ElectrostaticDifferencePotential, "Edens": ElectronDensity,
                             "Dos": DensityOfStates, "LDDOS": LocalDeviceDensityOfStates, "Ediffdens": ElectronDifferenceDensity, "VDrop": ElectrostaticDifferencePotential,
                             "ChemPot": ChemicalPotential, "Band": Bandstructure, "VDropEff": EffectivePotential, "FT": ''}


        try:
            opts, args = getopt.getopt(argv,"hiagvmndckbzlq:",["ifile=","analysis=", "gate_v=", "vds=", "model=", 
                                                              "nprocs=", "dos_energy_range=", "calcs=", "k_points=", 
                                                              "band_route=", "band_zero=", "angular_momenta=", "band_dims="])
        except getopt.GetoptError, exc:
            print exc.msg
            self.usage()
        if not opts:
            print 'No options supplied'
            self.usage()
        for opt, arg in opts:

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
                self.voltage_range_input['gv'] = True
            elif opt in ("-v", "--vds"):
                vds_params = arg.split(',')
                if len(vds_params) is not 4:
                    self.usage()

                self.vds_start = float(vds_params[0])
                self.vds_end = float(vds_params[1])
                self.vds_points = float(vds_params[2])
                self.gate_v = float(vds_params[3])
                self.voltage_range_input['vds'] = True
            elif opt in ("-m", "--model"):
                self.model_type = arg
            elif opt in ("-n", "--nprocs"):
                self.nprocessors = int(arg)
            elif opt in ("-d", "--dos_energy_range"):
                dos_energy_params = arg.split(',')
                if len(dos_energy_params) is not 3:
                    self.usage()

                start = float(dos_energy_params[0])
                end = float(dos_energy_params[1])
                pts = float(dos_energy_params[2])
                self.dos_energy_range = np.linspace(start, end, num = pts)
            elif opt in ("-c", "--calcs"):

                self.calc_types = arg.split(',')
                print self.calc_types
            elif opt in ("-k", "--k_points"):
                k_points = arg.split(',')
                if len(k_points) is not 3:
                    self.usage()
                k_points_list = [int(i) for i in k_points]
 
                self.k_point_sampling = tuple(k_points_list) 
            elif opt in ("-b", "--band_route"):
                self.band_route = arg.split(',')
            elif opt in ("-b", "--band_zero"):
                self.band_zero = arg
            elif opt in ("-l", "--angular_momenta"):
                
                self.ang_momenta = arg.split(',')
                self.ang_momenta = [int(x) for x in self.ang_momenta]
            elif opt in ("-q", "--band_dims"):
                
                self.band_dims = int(arg)
                 

 

        if self.analysis_type is None:
            print "Please specify analysis type..."
            self.usage()
        if self.analysis_type == 'vds_sweep' and self.voltage_range_input ['vds'] is False:
            self.usage()
        elif self.analysis_type == 'gate_sweep' and self.voltage_range_input ['gv'] is False:
            self.usage()
        elif len(self.dos_energy_range) == 0:
            print "Please include dos energy range"
            self.usage()
        elif len(self.calc_types) == 0:
            print "Please include Calc"
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

        analysis_tmp_path = dir_path+'/tmp/internals/'

        if not os.path.exists(analysis_tmp_path):
            os.makedirs(analysis_tmp_path)
        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
        self.analysis_config_path = analysis_tmp_path+file_base_name+".internals"
        self.device_config_path = tmp_path+file_base_name+".analysis.nc"
        print "Device config path = ", self.device_config_path
        self.sem_device = Semaphore(self.device_config_path)
        self.sem_int = Semaphore(self.analysis_config_path)


        #try reading device config first
        try:
            with open(self.device_config_path):
                print "Accessing initial configuration"
                init_config_obj = self.find_zero_volt_config ()
                #configuration empty, therefore device config


                
                    
                    

        except IOError:
            print 'Oh dear. No device config file exists.'

        if  not init_config_obj:
            print "No initial configuration exists, running DFT calculation"

            print "Extracting configuration from file"
            init_config_obj, basis_set = self.create_device_config(inputfile)

            #setting iether bulk or device config type
            self.set_configuration_type(init_config_obj)

            if (self.config_type == self.ConfigTypes.DEVICE):
                print "device"
                if (self.model_type == 'dft'):
                    self.calculator = self.create_device_calculator_dft (basis_set)
                elif (self.model_type == 'huckel'):
                    self.calculator = self.create_device_calculator_huckel (basis_set)
            elif (self.config_type == self.ConfigTypes.BULK):
                print "bulk"
                if (self.model_type == 'dft'):
                    self.calculator = self.create_bulk_calculator (basis_set)
                elif (self.model_type == 'huckel'):
                    self.calculator = self.create_bulk_huckel_calculator (basis_set)

            init_config_obj.setCalculator(self.calculator)
            nlprint(init_config_obj)
            init_config_obj.update()

            self.sem_device.lock()
            nlsave(self.device_config_path, init_config_obj, object_id="Config, GateV %f, Vds %f" % (0.0, 0.0))
            self.sem_device.release()

            if (self.config_type == self.ConfigTypes.DEVICE):
                configuration_obj = nlread(self.device_config_path, DeviceConfiguration)
            elif (self.config_type == self.ConfigTypes.BULK):
                configuration_obj = nlread(self.device_config_path, BulkConfiguration)


            self.configuration_obj = configuration_obj [0]

        else:
            print 'Found initial configuration'
            init_config_obj = init_config_obj [0]
            self.set_configuration_type(init_config_obj)
            self.configuration_obj = init_config_obj

        
        self.extract_dimensions()
 
    def usage(self):
        print 'python transistor_analysis_DOS.py \
--ifile=<inputfile> \
--model=<huckel|dft> \
--analysis=<gate_sweep|vds_sweep|bulk> \
(--gate_v=<start,end,steps,vds_value> | --vds=<start,end,steps>) \
--dos_energy_range=<start,end,num_pts> \
--calcs=<Veff|Vext|DiffPot|Edens|Dos|LDDOS|Ediffdens|VDrop|Efield|Trans|Bands|ChemPot|VDropEff|MoveTrans|None> \
--k_points=<start,end,steps> \
--band_zero=FermiLevel|Absolute \
--band_route=<route seperated with zero> \
--angular_momenta=<comma separated list of angular momenta>'
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
        #there are some configs
        zero_volt_config = nlread(self.device_config_path, DeviceConfiguration, 
                                object_id="Config, GateV %f, Vds %f" % (0.0, 0.0), read_state = True)
        if not zero_volt_config:
            zero_volt_config = nlread(self.device_config_path, BulkConfiguration, 
                #there are no metallic regions, therefore device not gated
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
            if key[0] == ('DeviceConfiguration') or key[0] == ('BulkConfiguration'):
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
        

 
        

        

    def gate_voltage_sweep (self, voltages, drain_voltage, asymmetric_voltage=False):
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
            if (asymmetric_voltage):
                new_regions = [metallic_regions[0](value = gate_voltage)]
                new_regions.extend([m for m in metallic_regions[1:]])
            else:
                new_regions = [m(value = gate_voltage) for m in metallic_regions]
            new_config.setMetallicRegions(new_regions)

            # Make a copy of the calculator and attach it to the configuration
            # Restart from the previous scf state
            #find closest state
            init_state = self.find_closest_state(gate_voltage, drain_voltage)

            new_config.setCalculator(calculator(),
                 initial_state=init_state)
            new_config.update()
            self.sem_device.lock()
            nlsave(self.device_config_path, new_config, 
                object_id="Config, GateV %f, Vds %f" % (self.gv_obj(new_config), self.vds_obj(new_config)))
            self.sem_device.release()
                

    def vds_sweep (self, gate_voltage, vds_voltages):

        
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
            self.sem_device.lock()
            nlsave(self.device_config_path, zero_volt_config, object_id="Config, GateV %f, Vds %f" % (self.gv_obj(zero_volt_config), self.vds_obj(zero_volt_config)))
            self.sem_device.release()
 


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

        if s:
            print "###########################"
            print "error: %s\n" % s
            print "###########################"

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
            
    def create_bulk_huckel_calculator (self, basis_set):

        print "Creating Bulk calculator..."
        if (self.voltage_range_input['gv']):
            print "...with Multipole boundary conditions on A/B"
            poisson_solver = MultigridSolver(
                #boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                     #[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                     #[PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
                #boundary_conditions=[[DirichletBoundaryCondition,DirichletBoundaryCondition],
                                     #[DirichletBoundaryCondition,DirichletBoundaryCondition],
                                     #[PeriodicBoundaryCondition,PeriodicBoundaryCondition]]

                boundary_conditions=[[MultipoleBoundaryCondition,MultipoleBoundaryCondition],
                                     [MultipoleBoundaryCondition,MultipoleBoundaryCondition],
                                     [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
                )
        else:
            print "...with Periodic boundary conditions on A/B/C"
            poisson_solver = MultigridSolver(
                boundary_conditions=[[PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                     [PeriodicBoundaryCondition,PeriodicBoundaryCondition],
                                     [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
                )
        bulk_numerical_accuracy_parameters = NumericalAccuracyParameters(
            density_mesh_cutoff = 150.0*Rydberg,
            k_point_sampling=self.k_point_sampling
            )
            
        calculator = HuckelCalculator(
            basis_set=basis_set,
            poisson_solver=poisson_solver,
            numerical_accuracy_parameters=bulk_numerical_accuracy_parameters,
            )


        return calculator
            
    def create_bulk_calculator (self, basis_set):

        print "Creating Bulk calculator..."
        if (self.voltage_range_input['gv']):
            print "...with Dirichlet boundary conditions on A/B"
            poisson_solver = MultigridSolver(
                #boundary_conditions=[[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                     #[NeumannBoundaryCondition,NeumannBoundaryCondition],
                                     #[PeriodicBoundaryCondition,PeriodicBoundaryCondition]]
                boundary_conditions=[[DirichletBoundaryCondition,DirichletBoundaryCondition],
                                     [DirichletBoundaryCondition,DirichletBoundaryCondition],
                                     [PeriodicBoundaryCondition,PeriodicBoundaryCondition]]

                )
        else:
            print "...with Periodic boundary conditions on A/B/C"
            poisson_solver = FastFourierSolver()

        bulk_numerical_accuracy_parameters = NumericalAccuracyParameters(
            density_mesh_cutoff = 150.0*Rydberg,
            k_point_sampling=self.k_point_sampling
            )
        calculator = LCAOCalculator(
            poisson_solver=poisson_solver,
            basis_set=basis_set,
            exchange_correlation=self.exchange_correlation,
            numerical_accuracy_parameters=bulk_numerical_accuracy_parameters,
            )

        return calculator

    def create_device_calculator_huckel (self, basis_set):


        #----------------------------------------
        # Numerical Accuracy Settings
        #----------------------------------------
        left_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            )
        #----------------------------------------
        # Iteration Control Settings
        #----------------------------------------
        left_electrode_iteration_control_parameters = IterationControlParameters()

        right_electrode_iteration_control_parameters = IterationControlParameters()

        #device_iteration_control_parameters = IterationControlParameters()
        device_iteration_control_parameters = IterationControlParameters(
            damping_factor=0.10,
            preconditioner=Kerker(0.02*Hartree, 0.5*Hartree, 0.01),
            mixing_variable=HamiltonianVariable,
            number_of_history_steps=12, 
        )

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
            numerical_accuracy_parameters=left_electrode_numerical_accuracy_parameters,
            iteration_control_parameters=left_electrode_iteration_control_parameters,
            poisson_solver=left_electrode_poisson_solver,
            )

        right_electrode_calculator = HuckelCalculator(
            basis_set=basis_set,
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

    def create_device_calculator_dft (self, basis_set):


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
            density_mesh_cutoff = 150.0*Rydberg,
            )

        right_electrode_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff = 150.0*Rydberg,
            )

        device_numerical_accuracy_parameters = NumericalAccuracyParameters(
            k_point_sampling=self.k_point_sampling,
            density_mesh_cutoff = 150.0*Rydberg,
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
            
        return points
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

        self.z_coord_first_atom = coords[0][2]
        self.z_coord_last_atom = coords[-1][2]


        x_coords_list = [x[0] for x in coords]
        x_coords_list = sorted(set(x_coords_list))

        self.x_coord_first_atom = self.frac_to_cart(self.x_length,  x_coords_list[0])
        self.x_coord_last_atom = self.frac_to_cart(self.x_length,  x_coords_list[-1])

        middle_x_index = int(len(x_coords_list)/2)
        self.x_coord_middle_atom = self.frac_to_cart(self.x_length,  x_coords_list[middle_x_index])

        middle_z_index = int(len(coords)/2)
        self.z_coord_middle_atom = self.frac_to_cart(self.z_length,  coords [middle_z_index][2])

        
        

        


        self.projection_point_x_1 = numpy.array([0, 0.5, self.z_coord_first_atom])
        self.projection_point_y_1 = numpy.array([0.5, 0, self.z_coord_first_atom])
        self.projection_point_x_0 = numpy.array([0, 0.5, self.z_coord_last_atom])
        self.projection_point_y_0 = numpy.array([0.5, 0, self.z_coord_last_atom])


        for coord in coords:
            x_coord = coord[0]
            

        #print coords




    def nlread_object (self, obj_name, gv, vds, nrg=0*eV, ang_momenta=[], dimensions=1, route=None, ftVars=None):

        result = (False, None)
        if (obj_name == 'LDDOS'):
            obj_id = "LDDOS %f, GateV %f, Vds %f" % (nrg, gv, vds)
        elif (obj_name == 'Band'):
            if not ang_momenta:
                ang_momenta_str = 'all'
            else:
                ang_momenta_str = str(ang_momenta)
            
            if (dimensions == 1):
                dimensions_str = ''
            elif (dimensions > 1):
                dimensions_str = ', dim = %d' % dimensions

            if (route):
                route_str = ',route = '
                for point in route:
                    route_str = route_str + ('%s ' % point)

            else:
                route_str = ''
                

            obj_id = "Band, GateV %f, Vds %f, l = %s%s%s" % (gv, vds, ang_momenta_str, dimensions_str, route_str)
        elif (obj_name == 'FT'):
            obj_id = "FT, %s" % ftVars
        else:
            obj_id = obj_name + ", GateV %f, Vds %f" % (gv, vds)
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"

        obj_type = self.objects_enum[obj_name]
        if (obj_name == "Dos"):
            obj_type = self.config_type[1]
        try: 
            #obj = nlread(path, obj_type, object_id=obj_id)
            obj = nlread(path, object_id=obj_id)
            obj = obj[0]
            result = (True, obj)
        except:
            result = (False, None)
        


        return result



    def generate_transmission_spectrum (self):
        print "Generating Transmission Spectrum "

        transmission_spectrum = TransmissionSpectrum(
                configuration=self.configuration_obj,
                energies=numpy.linspace(-2,2,101)*eV,
                self_energy_calculator=KrylovSelfEnergy(),
                )

        nlsave(self.device_config_path, transmission_spectrum, object_id="Trans, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))




    def generate_diff_pot (self):
        print "Generating Difference Potential"

        diff = ElectrostaticDifferencePotential (
            configuration = self.configuration_obj,
        )

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        self.sem_int.lock()
        obj_id = "DiffPot, GateV %f, Vds %f" % (gv, vds)
        obj_id = obj_id.replace(" ", "_")
        path = self.analysis_config_path + obj_id + ".nc"
        nlsave(path, diff, object_id=obj_id)
        self.sem_int.release()

    def generate_v_ext (self):
        print "Generating V external"

        v_ext = ExternalPotential (
            configuration = self.configuration_obj,
        )

        self.sem_int.lock()
        obj_id = "Vext, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        obj_id = obj_id.replace(" ", "_")
        path = self.analysis_config_path + obj_id + ".nc"
        nlsave(path, v_ext, object_id=obj_id)
        self.sem_int.release()


    def generate_v_eff (self):
        print "Generating Veff"

        v_eff = EffectivePotential (
            configuration = self.configuration_obj,
        )

        self.sem_int.lock()
        obj_id = "Veff, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, v_eff, object_id=obj_id)
        self.sem_int.release()

    def generate_e_diff_density (self):
        print "Generating Electron Difference Density"

        electron_diff_density = ElectronDifferenceDensity (
            configuration = self.configuration_obj,
        )

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        self.sem_int.lock()
        obj_id = "Ediffdens, GateV %f, Vds %f" % (gv, vds)
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, electron_diff_density, object_id=obj_id)
        self.sem_int.release()


    def generate_e_density (self):
        print "Generating Electron Density"

        electron_density = ElectronDensity (
            configuration = self.configuration_obj,
        )

        self.sem_int.lock()
        obj_id = "Edens, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, electron_density, object_id=obj_id)
        self.sem_int.release()

    def generate_chem_potential (self):
        print "Generating Chemical Potential..."

        chemical_potential = ChemicalPotential (
            configuration = self.configuration_obj,
        )

        self.sem_int.lock()
        obj_id = "ChemPot, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, chemical_potential, object_id=obj_id)
        self.sem_int.release()



    def generate_dos_real_space (self):
        print "Generate DOS real space"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
 
        energies = [round(x, 6) for x in self.dos_energy_range]
        num_energies = len(energies)
        done_nrg = []

        lddos_list = []
        #Try reading all the LDDOS objects at once, since reaidng individually takes a long time.
        #if not (len(lddos_list) == num_energies):
        for nrg in energies:
            print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
            result, lddos_obj = self.nlread_object("LDDOS", gv, vds, nrg=nrg)
            #lddos_obj = nlread(path, LocalDeviceDensityOfStates, object_id=obj_id)
            if lddos_obj:
                rounded_nrg = round(lddos_obj.energy().inUnitsOf(eV)[0], 6)
                done_nrg.append(rounded_nrg)

            

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
            self.sem_int.lock()
            obj_id = "LDDOS %f, GateV %f, Vds %f" % (nrg.inUnitsOf(eV), self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
            path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
            nlsave(path, ldos, object_id=obj_id)
            self.sem_int.release()


    def generate_voltage_drop (self):
        print "Generating Voltage Drop Object"

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        result, zero_volt_drop_obj = self.nlread_object("DiffPot", 0.0, 0.0)
        if (not result):
            self.set_default_voltages(gate_v=0*Volt, vds = 0*Volt)
            self.generate_diff_pot()
            result, zero_volt_drop_obj = self.nlread_object("DiffPot", 0.0, 0.0)


        self.set_default_voltages(gate_v=gv*Volt, vds = vds*Volt)
        result, volt_drop_obj = self.nlread_object("DiffPot", gv, vds)
        if (not result):
            self.generate_diff_pot()
            result, volt_drop_obj = self.nlread_object("DiffPot", gv, vds)

        vdrop_obj = zero_volt_drop_obj - volt_drop_obj

        self.sem_int.lock()
        obj_id = "VDrop, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        obj_id = obj_id.replace(" ", "_")
        path = self.analysis_config_path + obj_id + ".nc"
        nlsave(path, vdrop_obj, object_id=obj_id)
        self.sem_int.release()


    def graph_voltage_drop (self):
        print "Graphing Voltage drop..."

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)


        #try reading Vdrop object first 
        result, volt_drop_obj = self.nlread_object("VDrop", gv, vds)
        if (not result):
            self.generate_voltage_drop()
            result, volt_drop_obj = self.nlread_object("VDrop", gv, vds)



        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_vdrop.plot", 'w')
        outfile.write ('z, y, \g(d)V\-(H), x, y, \g(d)V\-(H)\n')
        outfile.write ('Angstrom, Angstrom, V, Angstrom, Angstrom, V\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))

        #volt_drop_arr = volt_drop_obj.toArray()
        #get array of y values in Angstrom
        x_vol_elem = volt_drop_obj.volumeElement()[0][0]
        y_vol_elem = volt_drop_obj.volumeElement()[1][1]
        z_vol_elem = volt_drop_obj.volumeElement()[2][2]

        num_x_elems = volt_drop_obj.shape()[0]
        num_y_elems = volt_drop_obj.shape()[1]
        num_z_elems = volt_drop_obj.shape()[2]

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_voltage_list = []
        xy_voltage_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_voltage = volt_drop_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_voltage_list.append(str(yz_voltage.inUnitsOf(eV)))


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_voltage = volt_drop_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_voltage_list.append(str(xy_voltage.inUnitsOf(eV)))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_voltage_list,
                                               x_coord_list, y_coord_list_2, xy_voltage_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',')
        writer.writerows (final_list)

        outfile.close()

    def generate_voltage_drop_eff (self):
        print "Generating Voltage Drop Effective Object"

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        result, zero_volt_drop_obj = self.nlread_object("Veff", 0.0, 0.0)
        if (not result):
            self.set_default_voltages(gate_v=0*Volt, vds = 0*Volt)
            self.generate_v_eff()
            result, zero_volt_drop_obj = self.nlread_object("Veff", 0.0, 0.0)


        self.set_default_voltages(gate_v=gv*Volt, vds = vds*Volt)
        result, volt_drop_obj = self.nlread_object("Veff", gv, vds)
        if (not result):
            self.generate_v_eff()
            result, volt_drop_obj = self.nlread_object("Veff", gv, vds)

        vdrop_obj = volt_drop_obj - zero_volt_drop_obj

        self.sem_int.lock()
        obj_id = "VDropEff, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        obj_id = obj_id.replace(" ", "_")
        path = self.analysis_config_path + obj_id + ".nc"
        nlsave(path, vdrop_obj, object_id=obj_id)
        self.sem_int.release()


    def graph_voltage_drop_eff (self):
        print "Graphing Voltage drop effective..."

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)


        #try reading Vdrop object first 
        result, volt_drop_obj = self.nlread_object("VDropEff", gv, vds)
        if (not result):
            self.generate_voltage_drop_eff()
            result, volt_drop_obj = self.nlread_object("VDropEff", gv, vds)



        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_vdropeff.plot", 'w')
        outfile.write ('z, y, \g(d)V\-(eff), x, y, \g(d)V\-(eff)\n')
        outfile.write ('Angstrom, Angstrom, V, Angstrom, Angstrom, V\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))

        #volt_drop_arr = volt_drop_obj.toArray()
        #get array of y values in Angstrom
        x_vol_elem = volt_drop_obj.volumeElement()[0][0]
        y_vol_elem = volt_drop_obj.volumeElement()[1][1]
        z_vol_elem = volt_drop_obj.volumeElement()[2][2]

        num_x_elems = volt_drop_obj.shape()[0]
        num_y_elems = volt_drop_obj.shape()[1]
        num_z_elems = volt_drop_obj.shape()[2]

        vdrop_array = volt_drop_obj.toArray()

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_voltage_list = []
        xy_voltage_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        x_index_frac = x_coord/self.x_length
        #get the actual index of the x-coordinate
        x_index = int(x_index_frac * np.shape(vdrop_array)[0])

        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_voltage = vdrop_array[x_index][y][z]
                yz_voltage = yz_voltage * Hartree

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_voltage_list.append(str(yz_voltage.inUnitsOf(eV)))

                #print y


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        z_index_frac = z_coord/self.z_length
        #get the actual index of the x-coordinate
        z_index = int(z_index_frac * np.shape(vdrop_array)[2])


        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_voltage = vdrop_array[x][y][z_index]
                xy_voltage = xy_voltage * Hartree

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_voltage_list.append(str(xy_voltage.inUnitsOf(eV)))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_voltage_list,
                                               x_coord_list, y_coord_list_2, xy_voltage_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',')
        writer.writerows (final_list)

        outfile.close()



    def graph_efield (self):
        print "Graphing Electric Field ..."

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)


        #try reading Vdrop object first 
        result, volt_drop_obj = self.nlread_object("VDrop", gv, vds)
        if (not result):
            self.generate_voltage_drop()
            result, volt_drop_obj = self.nlread_object("VDrop", gv, vds)



        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_efield.plot", 'w')
        outfile.write ('z, y, \\ab(E), x, y, \\ab(E)\n')
        outfile.write ('Angstrom, Angstrom, V/cm, Angstrom, Angstrom, V/cm\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))

        #volt_drop_arr = volt_drop_obj.toArray()
        #get array of y values in Angstrom
        x_vol_elem = volt_drop_obj.volumeElement()[0][0]
        y_vol_elem = volt_drop_obj.volumeElement()[1][1]
        z_vol_elem = volt_drop_obj.volumeElement()[2][2]

        num_x_elems = volt_drop_obj.shape()[0]
        num_y_elems = volt_drop_obj.shape()[1]
        num_z_elems = volt_drop_obj.shape()[2]

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_field_list = []
        xy_field_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_field = volt_drop_obj.derivatives (x_coord, y_coord, z_coord, Spin.Sum)[2].inUnitsOf(eV/(Meter))/100

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_field_list.append(str(yz_field))


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_field = volt_drop_obj.derivatives (x_coord, y_coord, z_coord, Spin.Sum)[2].inUnitsOf(eV/(Meter))/100

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_field_list.append(str(xy_field))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_field_list,
                                               x_coord_list, y_coord_list_2, xy_field_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',')
        writer.writerows (final_list)

        outfile.close()





    def graph_diff_pot (self):
        print "Graphing Difference Potential"

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        result, diff_potential_obj = self.nlread_object("DiffPot", gv, vds)
        if (not result):
            self.generate_diff_pot()
            result, diff_potential_obj = self.nlread_object("DiffPot", gv, vds)
 



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

     
        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_diffpot.plot", 'w')
        outfile.write ('z, y, \g(d)V\-(H), x, y, \g(d)V\-(H)\n')
        outfile.write ('Angstrom, Angstrom, eV, Angstrom, Angstrom, eV\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))


        #volt_drop_arr = volt_drop_obj.toArray()
        #get array of y values in Angstrom
        x_vol_elem = diff_potential_obj.volumeElement()[0][0]
        y_vol_elem = diff_potential_obj.volumeElement()[1][1]
        z_vol_elem = diff_potential_obj.volumeElement()[2][2]

        num_x_elems = diff_potential_obj.shape()[0]
        num_y_elems = diff_potential_obj.shape()[1]
        num_z_elems = diff_potential_obj.shape()[2]

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_diff_pot_list = []
        xy_diff_pot_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_diff_pot = diff_potential_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_diff_pot_list.append(str(yz_diff_pot.inUnitsOf(eV)))


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_diff_pot = diff_potential_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_diff_pot_list.append(str(xy_diff_pot.inUnitsOf(eV)))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_diff_pot_list,
                                               x_coord_list, y_coord_list_2, xy_diff_pot_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',',lineterminator='\n' )
        writer.writerows (final_list)

        outfile.close()


        
    def graph_v_ext (self):
        print "Graphing Vext"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        result, ext_pot_obj = self.nlread_object("Vext", gv, vds)
        if (not result):
            self.generate_v_ext ()
            result, ext_pot_obj = self.nlread_object("Vext", gv, vds)
                
 
        proj_x_arr = []
        proj_y_arr = []

        #proj_x = diff_potential_obj.axisProjection ('Line', 'A', Spin.Sum, projection_point_x)
        #proj_y = diff_potential_obj.axisProjection ('Line', 'B', Spin.Sum, projection_point_y)
        proj_x_arr.append(ext_pot_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(ext_pot_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(ext_pot_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(ext_pot_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

     
        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_vext.plot", 'w')
        outfile.write ('x, V\-(ext), V\-(ext), y, V\-(ext), V\-(ext)\n')
        outfile.write ('Angstrom, eV, eV, Angstrom, eV, eV\n')
        outfile.write ('x, V\-(ext_X_2_atoms), V\-(ext_X_3_atoms), y, V\-(ext_Y_2_atoms), V\-(ext_Y_3_atoms)\n')

        length_x_coords = len(proj_x_arr[0][0])
        length_y_coords = len(proj_y_arr[0][0])
        j = 0
        i = 0
        max_index = max(length_x_coords,length_x_coords)
        k = 0
        done_x = False
        done_y = False
        while (k < max_index):
            if (not done_y):
                y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][j]).inUnitsOf(Angstrom))
                y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][j]).inUnitsOf(Angstrom))
                y_energy_0 = str(proj_y_arr[0][1][j].inUnitsOf(eV))
                y_energy_1 = str(proj_y_arr[1][1][j].inUnitsOf(eV))
            if (not done_x):
                x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
                x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
                x_energy_0 = str(proj_x_arr[0][1][i].inUnitsOf(eV))
                x_energy_1 = str(proj_x_arr[1][1][i].inUnitsOf(eV))

            j = j+1
            i = i+1
            k = k+1
            if (i >= length_x_coords):
                done_x = True
                x_angstrom_0 = '-'
                x_energy_0 = '-'
                x_energy_1 = '-'
            if (j >= length_y_coords):
                done_y = True
                y_angstrom_0 = '-'
                y_energy_0 = '-'
                y_energy_1 = '-'
                


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

                                            
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        result, effective_potential_obj = self.nlread_object("Veff", gv, vds)
        if (not result):
            self.generate_v_eff ()
            result, effective_potential_obj = self.nlread_object("Veff", gv, vds)
                
        
       
        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_veff.plot", 'w')
        outfile.write ('z, y, V\-(eff), x, y, V\-(eff)\n')
        outfile.write ('Angstrom, Angstrom, V, Angstrom, Angstrom, V\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))

        #get array of y values in Angstrom
        x_vol_elem = effective_potential_obj.volumeElement()[0][0]
        y_vol_elem = effective_potential_obj.volumeElement()[1][1]
        z_vol_elem = effective_potential_obj.volumeElement()[2][2]

        num_x_elems = effective_potential_obj.shape()[0]
        num_y_elems = effective_potential_obj.shape()[1]
        num_z_elems = effective_potential_obj.shape()[2]

        eff_pot_array = effective_potential_obj.toArray()

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_voltage_list = []
        xy_voltage_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        x_index_frac = x_coord/self.x_length
        #get the actual index of the x-coordinate
        x_index = int(x_index_frac * np.shape(eff_pot_array)[0])

        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_voltage = eff_pot_array[x_index][y][z]
                yz_voltage = yz_voltage * Hartree

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_voltage_list.append(str(yz_voltage.inUnitsOf(eV)))

                #print y


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        z_index_frac = z_coord/self.z_length
        #get the actual index of the x-coordinate
        z_index = int(z_index_frac * np.shape(eff_pot_array)[2])


        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_voltage = eff_pot_array[x][y][z_index]
                xy_voltage = xy_voltage * Hartree

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_voltage_list.append(str(xy_voltage.inUnitsOf(eV)))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_voltage_list,
                                               x_coord_list, y_coord_list_2, xy_voltage_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',')
        writer.writerows (final_list)

        outfile.close()


 

    def graph_e_density (self):
        print "Graphing E density"

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)


        #try reading Vdrop object first 
        result, e_dens_obj = self.nlread_object("Edens", gv, vds)
        if (not result):
            self.generate_e_density()
            result, e_dens_obj = self.nlread_object("Edens", gv, vds)



        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_edens.plot", 'w')
        outfile.write ('z, y, n, x, y, n\n')
        outfile.write ('Angstrom, Angstrom, cm\+(-3), Angstrom, Angstrom, cm\+(-3)\n')
        outfile.write ('x = %f, x = %f, x = %f, z = %f, z = %f, z = %f\n' % (self.x_coord_middle_atom, self.x_coord_middle_atom, self.x_coord_middle_atom,
                                                                             self.z_coord_middle_atom, self.z_coord_middle_atom, self.z_coord_middle_atom))


        #volt_drop_arr = volt_drop_obj.toArray()
        #get array of y values in Angstrom
        x_vol_elem = e_dens_obj.volumeElement()[0][0]
        y_vol_elem = e_dens_obj.volumeElement()[1][1]
        z_vol_elem = e_dens_obj.volumeElement()[2][2]

        num_x_elems = e_dens_obj.shape()[0]
        num_y_elems = e_dens_obj.shape()[1]
        num_z_elems = e_dens_obj.shape()[2]

        x_coord_list = []
        y_coord_list_1 = []
        z_coord_list = []
        yz_e_dens_list = []
        xy_e_dens_list = []
        #draw picture for x = middle atom
        x_coord = self.x_coord_middle_atom
        for z in range(num_z_elems):
            z_coord = z * z_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                yz_e_dens = e_dens_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                y_coord_list_1.append(str(y_coord.inUnitsOf(Angstrom)))
                z_coord_list.append(str(z_coord.inUnitsOf(Angstrom)))
                yz_e_dens_list.append(str(yz_e_dens.inUnitsOf(Meter**-3)/10**6))


        y_coord_list_2 = []
        z_coord = self.z_coord_middle_atom
        for x in range(num_x_elems):
            x_coord = x * x_vol_elem
            for y in range(num_y_elems):
                y_coord = y * y_vol_elem

                xy_e_dens = e_dens_obj.evaluate (x_coord, y_coord, z_coord, Spin.Sum)

                x_coord_list.append(str(x_coord.inUnitsOf(Angstrom)))
                y_coord_list_2.append(str(y_coord.inUnitsOf(Angstrom)))
                xy_e_dens_list.append(str(xy_e_dens.inUnitsOf(Meter**-3)/10**6))


        final_zipped =  itertools.izip_longest(z_coord_list, y_coord_list_1, yz_e_dens_list,
                                               x_coord_list, y_coord_list_2, xy_e_dens_list)
                                    
        final_list = [x for x in (map(lambda x: '-' if x == None else x, pair) for pair in final_zipped)]


        writer = csv.writer (outfile, delimiter=',')
        writer.writerows (final_list)

        outfile.close()


    def graph_e_diff_density (self):
        print "Graphing E diff density"


        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        result, edensity_obj = self.nlread_object("Ediffdens", gv, vds)
        if (not result):
            self.generate_e_diff_density()
            result, edensity_obj = self.nlread_object("Ediffdens", gv, vds)
         
       
        proj_x_arr = []
        proj_y_arr = []

        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_0))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_0))
        proj_x_arr.append(edensity_obj.axisProjection ('Line', 'A', Spin.Sum, self.projection_point_x_1))
        proj_y_arr.append(edensity_obj.axisProjection ('Line', 'B', Spin.Sum, self.projection_point_y_1))

        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_ediffdensity.plot", 'w')
        outfile.write ('x, \g(d)n, \g(d)n, y, \g(d)n, \g(d)n\n')
        outfile.write ('Angstrom, cm\+(-3), cm\+(-3), Angstrom, cm\+(-3), cm\+(-3)\n')
        outfile.write ('x, \g(d)n_x_2_atoms, \g(d)n_x_3_atoms, y, \g(d)n_y_2_atoms, \g(d)n_y_3_atoms\n')

        length_x_coords = len(proj_x_arr[0][0])
        length_y_coords = len(proj_y_arr[0][0])
        j = 0
        i = 0
        max_index = max(length_x_coords,length_x_coords)
        k = 0
        done_x = False
        done_y = False
        while (k < max_index):
            if (not done_y):
                y_angstrom_0 = str(self.frac_to_cart(self.y_length, proj_y_arr[0][0][j]).inUnitsOf(Angstrom))
                y_angstrom_1 = str(self.frac_to_cart(self.y_length, proj_y_arr[1][0][j]).inUnitsOf(Angstrom))
                #y_density_0 = str(proj_y_arr[0][1][j].inUnitsOf(Angstrom**-3))
                #y_density_1 = str(proj_y_arr[1][1][j].inUnitsOf(Angstrom**-3))
                y_density_0 = str(proj_y_arr[0][1][j].inUnitsOf(Meter**-3)/10**6)
                y_density_1 = str(proj_y_arr[1][1][j].inUnitsOf(Meter**-3)/10**6)
            if (not done_x):
                x_angstrom_0 = str(self.frac_to_cart(self.x_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
                x_angstrom_1 = str(self.frac_to_cart(self.x_length, proj_x_arr[1][0][i]).inUnitsOf(Angstrom))
                #x_density_0 = str(proj_x_arr[0][1][i].inUnitsOf(Angstrom**-3))
                #x_density_1 = str(proj_x_arr[1][1][i].inUnitsOf(Angstrom**-3))
                x_density_0 = str(proj_x_arr[0][1][i].inUnitsOf(Meter**-3)/10**6)
                x_density_1 = str(proj_x_arr[1][1][i].inUnitsOf(Meter**-3)/10**6)

            j = j+1
            i = i+1
            k = k+1
            if (i >= length_x_coords):
                done_x = True
                x_angstrom_0 = '-'
                x_density_0 = '-'
                x_density_1 = '-'
            if (j >= length_y_coords):
                done_y = True
                y_angstrom_0 = '-'
                y_density_0 = '-'
                y_density_1 = '-'

            #printing VEFF for x direction
            outfile.write (x_angstrom_0 + ',')
            outfile.write (x_density_0 + ',')
            outfile.write (x_density_1 + ',')
            outfile.write (y_angstrom_0 + ',')
            outfile.write (y_density_0 + ',')
            outfile.write (y_density_1)
            outfile.write ('\n')


        outfile.close()


    def lddos_worker (self, axis, obj, result_dict):
        #print "Starting worker for axis: ", axis
        start_time = time.time()
        dd={}


        st = time.time()
        axisProj = obj.axisProjection ('Average', axis, Spin.Sum)
        #print "Time taken for axisProj = ", str (time.time() - st)



        st = time.time()
        fracs = [float(x) for x in axisProj[0]]
        #print "Time taken for fracs = ", str (time.time() - st)
        st = time.time()
        vals = [x.inUnitsOf(Hartree**-1 * Angstrom**-3) for x in axisProj[1]]
        #print "Time taken for vals comprehension = ", str (time.time() - st)
        #dd[axis] = axisProj
        #print dd
        #print dd
        #result_dict.update(dd)
        st = time.time()
        result_dict[axis] = (fracs, vals)
        #print "Time taken for appending to dict = ", str (time.time() - st)
        end_time = time.time()
        print "Time taken for LDDOS_WORKER = ", str (end_time - start_time)
        #print "Ending worker for axis: ", axis

    def lddos_multi_nrg_worker (self, obj, result_string_lst):
        nprocs = 3
        procs = []
        manager = multiprocessing.Manager()
        result_dict=manager.dict()

        energy = obj.energy()[0]

        #start
        axis = ['A','B','C']
        for i in range(nprocs):
            
            p = multiprocessing.Process (target=self.lddos_worker,
                                        args=(axis[i],obj, result_dict))
            procs.append(p)
            p.start()

            
        for p in procs:
            p.join()

        
        start_time = time.time()

        proj_x = []
        proj_x.append(result_dict[axis[0]][0])
        proj_x.append(result_dict[axis[0]][1])

        proj_y = []
        proj_y.append(result_dict[axis[1]][0])
        proj_y.append(result_dict[axis[1]][1])

        proj_z = []
        proj_z.append(result_dict[axis[2]][0])
        proj_z.append(result_dict[axis[2]][1])

        #proj_x = obj.axisProjection ('Average', 'A', Spin.Sum)
        #proj_y = obj.axisProjection ('Average', 'B', Spin.Sum)
        #proj_z = obj.axisProjection ('Average', 'C', Spin.Sum)

        print "Printing LDDOS for Energy = ", str(energy.inUnitsOf(eV)),
        print "\n"



        length_x_coords = len(proj_x[0])
        length_y_coords = len(proj_y[0])
        length_z_coords = len(proj_z[0])
        j = 0
        i = 0
        k = 0
        max_index = max(length_x_coords,length_x_coords, length_z_coords)
        l = 0
        done_x = False
        done_y = False
        done_z = False

        
        #setting up the dictionary to store all the values in
        energy_float = float(energy.inUnitsOf(eV))
        final_str_list = []
        while (l < max_index):

            if (not done_x):
                x_angstrom = str(self.frac_to_cart(self.x_length, proj_x[0][i]).inUnitsOf(Angstrom))
                x_states = (str(proj_x[1][i]))


            if (not done_y):
                y_angstrom = str(self.frac_to_cart(self.y_length, proj_y[0][j]).inUnitsOf(Angstrom))
                y_states = (str(proj_y[1][j]))

            if (not done_z):
                z_angstrom = str(self.frac_to_cart(self.z_length, proj_z[0][k]).inUnitsOf(Angstrom))
                z_states = (str(proj_z[1][k]))

            i = i + 1
            j = j + 1
            k = k + 1
            l = l + 1

            if (i >= length_x_coords):
                done_x = True
                x_angstrom = '-'
                x_states = '-'
            if (j >= length_y_coords):
                done_y = True
                y_angstrom = '-'
                y_states = '-'
            if (k >= length_z_coords):
                done_z = True
                z_angstrom = '-'
                z_states = '-'

            if (done_y and done_x and done_z):
                continue

            energy_str = str(energy.inUnitsOf(eV))
            #For x coords
            final_string = (x_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (x_states + ',')
            # For y coords
            final_string = final_string + (y_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (y_states + ',')
            # For z coords
            final_string = final_string + (z_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (z_states)

            final_string = final_string + '\n'

            final_str_list.append(final_string)

        end_time = time.time()
        #print "Time taken to print one energy point: ", str (end_time - start_time)

        result_string_lst[energy_float] = final_str_list



    def graph_dos_real_space (self):
        print "Graphing LDDOS Real Space"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        start = time.time()
 
        #@TODO UNCOMMENT THIS
        self.generate_dos_real_space()
        energies = [round(x, 6) for x in self.dos_energy_range]

 
        #print "NUMBER OF LDDSO BJECTS"
        #print len(nlread(self.device_config_path, LocalDeviceDensityOfStates))
        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + '_V_lddos.plot', 'w')
        outfile.write ('x, Energy, States, y, Energy, States, z, Energy, States\n')
        outfile.write ('Angstrom, eV, arb. units, Angstrom, eV, arb. units, Angstrom, eV, arb. units\n')
        outfile.write ('x, Energy, Number of States, y, Energy, Number of States, z, Energy, Number of States\n')

        final_out_dict = {}
        nprocs = self.nprocessors

        #start
        #endj
        
        for nrg_idx in range(0, len(energies), nprocs):

            lddos_list = []

            for k in range(nprocs):
                
                nrg = energies[nrg_idx + k]
                print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
                result, lddos_obj = self.nlread_object("LDDOS", gv, vds, nrg=nrg)
                lddos_list.append(lddos_obj)
 
            for k in range(0, len(lddos_list), nprocs):


                procs = []
                manager = multiprocessing.Manager()
                result_string_lst=manager.dict()

                start_loop_time = time.time()

                for i in range(nprocs):
                    
                    p = multiprocessing.Process (target=self.lddos_multi_nrg_worker,
                                                args=(lddos_list[k+i], result_string_lst))
                    procs.append(p)
                    p.start()

                    
                for p in procs:
                    p.join()


        
                #append result dictionary to total dict with all energies
                final_out_dict.update(result_string_lst)


                time_per_iter = time.time() - start_loop_time
                print "Time Taken: ", time_per_iter
                print "\n"



        od = collections.OrderedDict(sorted(final_out_dict.items()))
        for k, v in od.iteritems():
            for line in v:
                outfile.write (line)

            

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
        end = time.time()
        total = end -start
        print "Total Time Passed for Graphing real Space DOS Function ", total
 
    def graph_dos_real_space_atk (self):
        
        #print "NUMBER OF LDDSO BJECTS"
        #te = nlread(self.device_config_path, LocalDeviceDensityOfStates)
        #self.generate_dos_real_space()
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
 
        energies = np.linspace(-5, 5, num = 10)
        energies = [round(x, 6) for x in energies]

        lddos_list = []
        for nrg in energies:
            print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
            obj_id = "LDDOS %f, GateV %f, Vds %f" % (nrg, gv, vds)
            obj_id = obj_id.replace(" ", "_")
            path = self.analysis_config_path + obj_id + ".nc"
            lddos_obj = nlread(path, LocalDeviceDensityOfStates, object_id=obj_id)

            lddos_list.append(lddos_obj[0])

    
      


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

        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + '_V_lddos.plot', 'w')
        outfile.write ('z, Energy, States\n')
        outfile.write ('Angstrom, eV, arb. units\n')
        outfile.write ('z, Energy, Number of States\n')

        for z_coord in Z:
            print z_coord

        #plot the LDDOS(E, z)
        pylab.xlabel('z (Angstrom)',fontsize=12,family='sans-serif')
        pylab.ylabel('Energy (eV)',fontsize=12,family='sans-serif')

        contour_values = numpy.linspace(0 , numpy.amax(Z), 25)
        pylab.contourf(X, Y, Z, contour_values)
        pylab.colorbar()
        pylab.axis([numpy.amin(X), numpy.amax(X), numpy.amin(Y), numpy.amax(Y)])

        pylab.title(self.device_config_path + ": E vs. z")
        pylab.savefig(self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + '_V_lddos.png',dpi=100)


        #pylab.show()
    def graph_density_of_states (self):
        print "Graphing Density of States"


        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        print "DOS, GateV %f, Vds %f" % (gv, vds)

        result, dos_obj = self.nlread_object("Dos", gv, vds)
        if (not result):
            self.generate_density_of_states ()
            result, dos_obj = self.nlread_object("Dos", gv, vds)

        if not self.ang_momenta:
            ang_momenta_str = 'all'
        else:
            ang_momenta_str = str(self.ang_momenta)
            ang_momenta_str = ang_momenta_str.replace('[','')
            ang_momenta_str = ang_momenta_str.replace(']','')


        outfile = open (self.device_config_path + 
                        "_VG_" + str(gv) + 
                        "_VDS_"+ str(vds) + 
                        "_l=" + ang_momenta_str + 
                        "_dos.plot", 'w')
        outfile.write ('Energy, Density of States\n')
        outfile.write ('eV, 1/eV\n')


        energies = dos_obj.energies()
        num_atoms = len(dos_obj.elements())

        #dos_obj.nlprint()
        #sys.exit()

        if self.ang_momenta:
            final_dos = dos_obj.evaluate(projection_list = ProjectionList(angular_momenta = self.ang_momenta))
        else:
            final_dos = dos_obj.evaluate()
            
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

        #self.print_currents_file ()


    def graph_chem_potential (self):
        print "Graphing chemical potential..."

        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        result, chem_pot_obj = self.nlread_object("ChemPot", gv, vds)
        if (not result):
            self.generate_chem_potential ()
            result, chem_pot_obj = self.nlread_object("ChemPot", gv, vds)


 
 



    def print_currents_file (self, currents_plot_file=None):
        if currents_plot_file is None:
            currents_plot_file = self.device_config_path + 'currents.plot'     

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
                        
            current_in_uA = trans_object.current().inUnitsOf(Ampere) * 10**6

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
                energies=numpy.linspace(-5,5,300)*eV,
                kpoints=MonkhorstPackGrid(4,4),
                contributions=All,
                energy_zero_parameter=AverageFermiLevel,
                infinitesimal=5e-07*eV,
                self_energy_calculator=KrylovSelfEnergy(),
             )
        elif self.config_type == self.ConfigTypes.BULK:
            dos = DensityOfStates(
                configuration=self.configuration_obj,
                kpoints=MonkhorstPackGrid(4,4,100),
                energy_zero_parameter=FermiLevel,
             )


        self.sem_int.lock()
        obj_id = "Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, dos, object_id=obj_id)
        self.sem_int.release()

    def generate_bulk_bandstructure (self, route=None, k_points_list=[], ang_momenta=[], dimensions=1):
        print "Generating BULK Bandstructure"

        #ang_momenta list isn't empty, therefore specify projection list
        if ang_momenta:
            projection_list = ProjectionList(angular_momenta = ang_momenta)
        else:
            projection_list = ProjectionList()


        if route:
            bandstructure = Bandstructure (
                configuration=self.configuration_obj,
                route=route,
                points_per_segment=100,
                bands_above_fermi_level=10,
                projection_list = projection_list
            )
        else:
            bandstructure = Bandstructure (
                configuration=self.configuration_obj,
                kpoints = k_points_list,
                bands_above_fermi_level=2,
                projection_list = projection_list
            )

        if not ang_momenta:
            ang_momenta_str = 'all'
        else:
            ang_momenta_str = str(ang_momenta)
        self.sem_int.lock()
        if (dimensions == 1):
            dimensions_str = ''
        elif (dimensions > 1):
            dimensions_str = ', dim = %d' % dimensions

        if (route):

            route_str = ',route = '
            for point in route:
                route_str = route_str + ('%s ' % point)
        else:
            route_str = ''
            

        obj_id = "Band, GateV %f, Vds %f, l = %s%s%s" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj), ang_momenta_str, dimensions_str, route_str)
        path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
        nlsave(path, bandstructure, object_id=obj_id)
        self.sem_int.release()

     
    def graph_bulk_bandstructure (self):
        print "Graphing bandstructure..."
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        surface = '100'

        if (self.band_dims == 1):
            n0 = 500

            bands_k_points_list = [[0, 0, x] for x in numpy.linspace (-0.5,0.5,num=n0, endpoint = True)]
        elif (self.band_dims == 2):
            if (surface == '100'):
                n0 = 150
                n1 = 150
                kx = list(numpy.linspace (-1,1,num=n0, endpoint = True))
                ky = list(numpy.linspace (-1,1,num=n1, endpoint = True))

                #bands_k_points_list = np.array(list(itertools.product(kx,ky,kz)))
                bands_k_points_list = np.array(list(itertools.product(kx,ky)))
                bands_k_points_list = [[i[0],i[1],0] for i in bands_k_points_list]
            elif (surface == '110'):
                n0 = 50
                n1 = 50

                
                
                
 
        elif (self.band_dims == 3):

            n0 = 20
            n1 = 20
            n2 = 20
            kx = list(numpy.linspace (-0.5,0.5,num=n0, endpoint = True))
            ky = list(numpy.linspace (-0.5,0.5,num=n1, endpoint = True))
            kz = list(numpy.linspace (-0.5,0.5,num=n2, endpoint = True))

            bands_k_points_list = np.array(list(itertools.product(kx,ky,kz)))
            
            

        result, bandstructure_obj = self.nlread_object("Band", gv, vds, ang_momenta=self.ang_momenta, dimensions=self.band_dims, route=self.band_route)
        if (not result):
            self.generate_bulk_bandstructure(route=self.band_route, k_points_list=bands_k_points_list, ang_momenta=self.ang_momenta, dimensions=self.band_dims)
            result, bandstructure_obj = self.nlread_object("Band", gv, vds, ang_momenta=self.ang_momenta, dimensions=self.band_dims, route=self.band_route)

        energies = bandstructure_obj.evaluate().inUnitsOf(eV)
        energy_zero = bandstructure_obj.energyZero()

        if not self.ang_momenta:
            ang_momenta_str = 'all'
        else:
            ang_momenta_str = str(self.ang_momenta)
            ang_momenta_str = ang_momenta_str.replace('[','')
            ang_momenta_str = ang_momenta_str.replace(']','')



        outfile = open (self.device_config_path + 
                        'VG_' + str(gv) +   
                        '_VDS_' + str(vds) +
                        '_zero_' + self.band_zero + 
                        '_l=' + ang_momenta_str + 
                        '_dims=' + str(self.band_dims) +
                        '_bands.plot', 'w')


        if (self.band_dims == 1):
            outfile.write ('k\-(z), Energy\n')
            outfile.write ('2\g(p)/L, eV\n')


            #get the number of bands
            num_bands = np.shape(energies)[1]
            bands = range(num_bands)
            #bands = [3, 4]

            energies = energies[:,bands].transpose()

            for band in range(len(bands)):
                outfile.write ("#Band %d\n" % band)
                x_index = 0
                xs = []
                all_nrgs = energies[band] 
                #x resets every n0
                for z in range(0, n0):
                    outfile.write ("%f,%f\n" % (bands_k_points_list[z][2], all_nrgs[z]))

            outfile.close()
        elif (self.band_dims == 2):
            outfile.write ('k\-(x), k\-(y), Energy\n')
            outfile.write ('2\g(p)/L\-(x), 2\g(p)/L\-(y), eV\n')


            #if (surface == '110'):


            #get the number of bands
            num_bands = np.shape(energies)[1]
            bands = range(num_bands)
            #bands = [3, 4]

            energies = energies[:,bands].transpose()

            for band in range(len(bands)):
                outfile.write ("#Band %d\n" % band)
                x_index = 0
                y_index = 0
                xs = []
                ys = []
                all_nrgs = energies[band] 
                #x resets every n1*n2 points
                for x in range(0,len(all_nrgs), n1):
                    #y resets every n2 points
                    for y in range(x, x + n1):
                        xIndex = x_index % n0
                        yIndex = y_index % n1
                    

                        x_coord = kx[xIndex]
                        y_coord = ky[yIndex]



            


                        outfile.write ("%f,%f,%f\n" % (kx[xIndex], ky[yIndex], all_nrgs[y]))
                        y_index = y_index + 1
                    x_index = x_index + 1



            outfile.close()
 
        elif (self.band_dims == 3):
            outfile.write ('k\-(x), k\-(y), k\-(z), Energy\n')
            outfile.write ('2\g(p)/L\-(x), 2\g(p)/L\-(y), 2\g(p)/L\-(z), eV\n')


            #get the number of bands
            num_bands = np.shape(energies)[1]
            bands = range(num_bands)
            bands = [3]

            energies = energies[:,bands].transpose()

            for band in range(len(bands)):
                outfile.write ("#Band %d\n" % band)
                x_index = 0
                y_index = 0
                z_index = 0
                xs = []
                ys = []
                zs = []
                all_nrgs = energies[band] 
                #x resets every n1*n2 points
                for x in range(0,len(all_nrgs), n1*n2):
                    #y resets every n2 points
                    for y in range(x, x + (n1 * n2), n2):
                        #z resets every 1 point
                        for z in range(y, y + n2):
                            #xs.append (all_nrgs[x])
                            #ys.append (all_nrgs[y])
                            #zs.append (all_nrgs[y])
                            xIndex = x_index % n0
                            yIndex = y_index % n1
                            zIndex = z_index % n2
                            
                            outfile.write ("%f,%f,%f,%f\n" % (kx[xIndex], ky[yIndex], kz[zIndex], all_nrgs[z]))
                            z_index = z_index + 1
                            
                        y_index = y_index + 1
                    x_index = x_index + 1



            outfile.close()
    def makeGridValues(self, datagrid, cell, origin, unit):
        n0, n1, n2 = datagrid.shape
        gA, gB, gC = cell
        u0 = NLEngine.Cartesian3DDouble(gA[0],gA[1],gA[2])
        u1 = NLEngine.Cartesian3DDouble(gB[0],gB[1],gB[2])
        u2 = NLEngine.Cartesian3DDouble(gC[0],gC[1],gC[2])
        cell_origin = NLEngine.Cartesian3DDouble(origin[0],origin[1],origin[2])

        grid_descriptor = NLEngine.GridDescriptor(n0,n1,n2, 
                                                  NLEngine.UnitCell(u0,u1,u2,cell_origin))
        grid3d = NLEngine.RealGrid3D(grid_descriptor,
                                     NLEngine.doubleSequenceToRealVector(datagrid.flatten()),True)

        return GridValues(grid3d,unit)

    def generate_ft_object (self, gv1, gv2, gv3, gv4, vds, ftVars):
        print "Generating FT Object"
        biases = [gv1, gv2, gv3, gv4]
        result, ft_obj = self.nlread_object("FT", gv1, vds, ftVars=ftVars)
        if (not result):

            object_id1 = "Trans, GateV %f, Vds %f" % (gv1, vds)
            trans_obj1 = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv1, vds))[0]
            if not trans_obj1:
                print "Trans obj 1 with gv [%s] is missing" % gv1 
            trans_obj2 = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv2, vds))[0]
            if not trans_obj2:
                print "Trans obj 2 with gv [%s] is missing" % gv2 
            trans_obj3 = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv3, vds))[0]
            if not trans_obj3:
                print "Trans obj 3 with gv [%s] is missing" % gv3 
            trans_obj4 = nlread(self.device_config_path, TransmissionSpectrum, object_id="Trans, GateV %f, Vds %f" % (gv4, vds))[0]
            if not trans_obj4:
                print "Trans obj 4 with gv [%s] is missing" % gv4 

            

            diff_pot_objs = []
            edens_objs = []
            for bias in biases:
                print "Setting default Bias  = %f" % bias
                self.set_default_voltages(gate_v=bias, vds=vds)

                result1, diff_pot_obj = self.nlread_object("DiffPot", bias, vds)
                if (not result1):
                    self.generate_diff_pot()
                    result1, diff_pot_obj = self.nlread_object("DiffPot", bias, vds)
         
                result2, ediff_dens_obj = self.nlread_object("Ediffdens", bias, vds)
                if (not result2):
                    self.generate_e_diff_density()
                    result2, ediff_dens_obj = self.nlread_object("Ediffdens", bias, vds)

                if result1 and result2:
                    diff_pot_objs.append(diff_pot_obj)
                    edens_objs.append(ediff_dens_obj)
                else:
                    print "Please run the DiffPot and Ediffdens analyses for bias %f, vds %f" % (bias, vds)
                    sys.exit()

                


            #edens1 = edens_obj1[:,:,:].sum()
            #edens2 = edens_obj2[:,:,:].sum()

            dX, dY, dZ = edens_objs[0].volumeElement().inUnitsOf(Ang)
            volume = numpy.abs(numpy.dot(dX,numpy.cross(dY,dZ) ))*Ang**3

            #unitCell = self.configuration_obj.unitCell()
            #vol = unitCell[0][0] * unitCell[1][1] * unitCell[2][2]

            #charge1 = vol * edens1 * electron_charge
            #charge2 = vol * edens2 * electron_charge

            # E = CV^2 * 0.5

            # Calculate the electrostatic energy
            energies = []
            for i in range(len(biases)):
                induced_potential = diff_pot_objs[i]-diff_pot_objs[0]
                induced_density = edens_objs[i]-edens_objs[0]
                energy = 0.5*(induced_density[:,:,:]*induced_potential[:,:,:]).sum()*volume
                energies += [energy.inUnitsOf(eV)]

            # Fit a parabola
            energies = numpy.array(energies)
            pol = numpy.polyfit(biases, energies, 2)
            Cg = 2.0*pol[0]*elementary_charge/Volt

            #Cg = (charge2-charge1)/ (gv2 - gv1)

            I1 = trans_obj1.current()
            I2 = trans_obj2.current()

            gm = (I2 - I1)/ (gv2-gv1)

            ft = (1/(2*np.pi)) * (gm/Cg)
            ft = ft.inUnitsOf(Second**-1)
            ft = abs(ft)

            cell = self.configuration_obj.bravaisLattice().primitiveVectors().inUnitsOf(Bohr)
            #cell = np.array([[1,0,0],[0,1,0],[0,0,1]]) * Angstrom
            origin = [0,0,0] 
            
            final_array = np.zeros([1,3,5])
            final_array[0][0][0] = ft 
            final_array[0][0][1] = float(Cg)
            final_array[0][0][2] = float(gm)
            final_array[0][1][0] = float(energies[0])
            final_array[0][1][1] = float(energies[1])
            final_array[0][1][2] = float(energies[2])
            final_array[0][1][3] = float(energies[3])
            final_array[0][2][0] = gv1.inUnitsOf(Volt)
            final_array[0][2][1] = gv2.inUnitsOf(Volt)
            final_array[0][2][2] = gv3.inUnitsOf(Volt)
            final_array[0][2][3] = gv4.inUnitsOf(Volt)

            #ft = np.ones([1,1,1]) * ft
            ft_obj = self.makeGridValues(final_array,cell,origin,Angstrom)

            obj_id = "FT, %s" % ftVars
            path = self.analysis_config_path + obj_id.replace(" ", "_") + ".nc"
            nlsave(path, ft_obj, object_id=obj_id)
        else:
            print "FT object exists"



        
    def extract_ft (self, gv1, gv2, gv3, gv4, vds):

        print "Wrting FT to file..."

        ftVars = "%fV%fV%fV%fV%fV" % (gv1, gv2, gv3, gv4, vds)
        result, ft_obj = self.nlread_object("FT", gv1, vds, ftVars=ftVars)
        if (not result):
            self.generate_ft_object(gv1, gv2, gv3, gv4, vds, ftVars)
            result, ft_obj = self.nlread_object("FT", gv1, vds, ftVars=ftVars)


    
        outfile = open (self.device_config_path + 
                            '_VG1_' + str(gv1.inUnitsOf(Volt)) +   
                        '_VDS_' + str(vds.inUnitsOf(Volt)) +
                        'FT.plot', 'w')
        outfile.write ('V\-(GS), f\-(T)\n')
        outfile.write ('V, GHz\n')

        zero = 0*Angstrom
        ft_obj = ft_obj.toArray()
        ft_val = ft_obj[0][0][0]
        Cg = (float(ft_obj[0][0][1]) * 1.6e-19) * 1e18
        gm = float(ft_obj[0][0][2])* 1e6
        energies = [None]*4
        energies[0] = ft_obj[0][1][0]
        energies[1] = ft_obj[0][1][1]
        energies[2] = ft_obj[0][1][2]
        energies[3] = ft_obj[0][1][3]

        ft_val = ft_val / 1e9

        outfile.write ('%f,%f\n' % (gv1, ft_val))
        outfile.write ('Capacitance (aF)\n')
        outfile.write ('%f,%f\n' % (gv1, Cg))
        outfile.write ('Gm (uS)\n')
        outfile.write ('%f,%f\n' % (gv1, gm))
        outfile.write ('Energies\n')
        outfile.write ('%f,%f\n' % (gv1, energies[0]))
        outfile.write ('%f,%f\n' % (gv2, energies[1]))
        outfile.write ('%f,%f\n' % (gv3, energies[2]))
        outfile.write ('%f,%f\n' % (gv4, energies[3]))

        outfile.close()
         

    def transfer_transmission_spectrums (self):
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

            path = self.device_config_path 

            try: 
                trans_obj = nlread(path, object_id=object_id)[0]

            except:
                print "Trans object not found"

            new_path = self.analysis_config_path + object_id.replace(" ", "_") + ".nc"

            self.sem_int.lock()
            nlsave(new_path, trans_obj, object_id=object_id)
            self.sem_int.release()

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


        default_config = None

        obj_id = "Config, GateV %f, Vds %f" % (gate_v.inUnitsOf(Volt), vds.inUnitsOf(Volt))
        default_config = nlread(self.device_config_path, self.config_type[2], 
                                object_id=obj_id)

        if (default_config is None) or (not default_config):
            #TODO MAKE THIS INTO ASSERT
            print "No config found with this voltage! Run the init first! Vds = ", vds, " GateV = ", gate_v
            sys.exit()
        
        default_config = default_config[0]
        self.configuration_obj = default_config
            

    def analyze(self):
       
        print "Starting analysis..."

        if ('None' in self.calc_types):
            print "No calculations specified..."
            return 
        else:
            if ('Veff' in self.calc_types):
                self.graph_v_eff ()
            if ('Vext' in self.calc_types):
                self.graph_v_ext ()
            if ('DiffPot' in self.calc_types):
                self.graph_diff_pot ()
            if ('Edens' in self.calc_types):
                self.graph_e_density ()
            if ('Dos' in self.calc_types):
                self.graph_density_of_states ()
            if ('LDDOS' in self.calc_types):
                self.graph_dos_real_space ()
            if ('Ediffdens' in self.calc_types):
                self.graph_e_diff_density ()
            if ('VDrop' in self.calc_types):
                self.graph_voltage_drop ()
            if ('VDropEff' in self.calc_types):
                self.graph_voltage_drop_eff ()
            if ('Efield' in self.calc_types):
                self.graph_efield ()
            if ('Trans' in self.calc_types):
                self.graph_transmission_spectrum()
            if ('Bands' in self.calc_types):
                self.graph_bulk_bandstructure()
            if ('ChemPot' in self.calc_types):
                self.graph_chem_potential()
            if ('MoveTrans' in self.calc_types):
                self.transfer_transmission_spectrums()
                


if __name__ == "__main__":

        #gate_voltage_list=[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1]*Volt
        #gate_voltage_list

        dev_anal_obj = DeviceAnalysis(sys.argv[1:])
        analysis_type = dev_anal_obj.analysis_type

        if analysis_type == "bulk":
            vds = 0.0 * Volt

            gate_voltage_list = [0.0] * Volt
            #set the gate potential
            if (dev_anal_obj.voltage_range_input['gv']):
                gate_voltage_list= np.linspace(dev_anal_obj.gate_v_start, dev_anal_obj.gate_v_end, num = dev_anal_obj.gate_v_points, endpoint=True) * Volt

            dev_anal_obj.gate_voltage_sweep (gate_voltage_list, vds, asymmetric_voltage=True)

            for gv in gate_voltage_list:
                dev_anal_obj.set_default_voltages(gate_v=gv, vds=vds)
                dev_anal_obj.analyze()
 

        elif analysis_type == "vds_sweep":
            dev_anal_obj.analyze()
            vds_voltage_list = np.linspace(dev_anal_obj.vds_start, dev_anal_obj.vds_end, num = dev_anal_obj.vds_points, endpoint=False) * Volt

            #
            print "Sweeping VDS voltages: ", vds_voltage_list
            #Gate voltage for which VDS voltage sbeing swept
            gate_voltage = dev_anal_obj.gate_v * Volt


            dev_anal_obj.gate_voltage_sweep ([gate_voltage], 0.0*Volt)

            

            dev_anal_obj.set_default_voltages(gate_v=gate_voltage, vds = 0.0*Volt)
            dev_anal_obj.vds_sweep (gate_voltage, vds_voltage_list)
            for vds in vds_voltage_list:
                dev_anal_obj.set_default_voltages(gate_v=gate_voltage, vds = vds)
                dev_anal_obj.analyze()
        elif analysis_type == "gate_sweep":
            #dev_anal_obj.analyze()
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
        elif analysis_type == "extract_ft":
            gate_voltage_list= np.linspace(dev_anal_obj.gate_v_start, dev_anal_obj.gate_v_end, num = dev_anal_obj.gate_v_points) * Volt
            vds = dev_anal_obj.vds_bias*Volt

                
            #calculate -5mv, 0mv, +5mv voltage above and below the given voltages:

            for gv in gate_voltage_list:
                small_new_step_v_range = [gv-0.01*Volt, gv-0.005*Volt, gv, gv+0.005*Volt, gv+0.01*Volt]
                small_new_step_v_range = [round(x.inUnitsOf(Volt), 6) for x in small_new_step_v_range ]
                small_new_step_v_range =  small_new_step_v_range * Volt

                small_new_gate_voltage_list = []
                for num in small_new_step_v_range:
                    int_part = int(num)
                    decimal_part = abs(float(num) - int(num))
                    decimal_part_str = format(decimal_part, '.6f')
                    decimal_index = decimal_part_str.find('.')
                    decimal_part_str = decimal_part_str[decimal_index+1:]
                    # all the the decimals are identical, convert them to 6 long
                    if (len(set(decimal_part_str)) == 1):
                        decimal_part_str = decimal_part_str[0]*6
                        num_str = str(int_part) + '.' + decimal_part_str
                        num = float(num_str) * Volt

                    small_new_gate_voltage_list.append (num)


                dev_anal_obj.gate_voltage_sweep (small_new_gate_voltage_list, vds)
                for small_range_gv in small_new_gate_voltage_list:
                    dev_anal_obj.set_default_voltages(gate_v=small_range_gv, vds=vds)
                    dev_anal_obj.calc_types = ['Trans']
                    dev_anal_obj.analyze()

                gv1 = small_new_gate_voltage_list[0]
                gv2 = small_new_gate_voltage_list[1]
                gv3 = small_new_gate_voltage_list[2]
                gv4 = small_new_gate_voltage_list[3]
                dev_anal_obj.extract_ft(gv1, gv2, gv3, gv4, vds)


        #set gate voltage for which to sweep vds
        #sweep over VDS's 
        #sweep over gate voltage with certain vds


