# -*- coding: UTF-8 -*-
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
import getopt
import pdb
import shutil
from pprint import pprint
import ntpath
from NL.IO.NLSaveUtilities import nlinspect

def enum (**enums):
    return type ('Enum', (), enums)

class IntefaceAnalysis: 

    def __init__(self, argv):
        self.exchange_correlation = GGA.PBE
        self.k_point_sampling = (3, 3, 3)
        self.default_gate_voltage = 0 * Volt
        self.analysis_type = None
        self.state = "None"
        self.relax = False
        voltage_range_input = {'gv':False, 'vds':False,}
        # Define gate_voltages

        self.ConfigTypes = enum (BULK = (1, DensityOfStates, BulkConfiguration) , DEVICE = (2, DeviceDensityOfStates, DeviceConfiguration))


        try:
            opts, args = getopt.getopt(argv,"hiasr:",["ifile=","analysis=","state=","relax="])
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
            elif opt in ("-s", "--state"):
                self.state = arg
            elif opt in ("-r", "--relax"):
                if (arg == "True"):
                    self.relax = True
                elif (arg == "False"):
                    self.relax = False
            elif opt in ("-a", "--analysis"):
                self.analysis_type = arg

        if self.analysis_type is None:
            print "Please specify analysis type..."
            self.usage()
        
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
        device_config_path = tmp_path+file_base_name+".analysis.nc"
        print "Device config path = ", device_config_path

        self.device_config_path = device_config_path


        #read constraints 
        obj, basis_set,constraints = self.create_device_config(inputfile)
        self.constraints = constraints


        #try reading device config first
        try:
            with open(device_config_path):
                print "Accessing initial device configuration"
                init_config_obj = nlread(device_config_path, BulkConfiguration)
                if not init_config_obj:
                    init_config_obj = nlread(device_config_path, DeviceConfiguration)    

        except IOError:
            print 'Oh dear. No device config file exists.'

        if  not init_config_obj:
            print "No initial configuration exists, running DFT calculation"

            print "Extracting configuration from file"
            #pdb.set_trace()
            init_config_obj, basis_set, self.constraints = self.create_device_config(inputfile)

            #setting iether bulk or device config type
            self.set_configuration_type(init_config_obj)

            if (self.config_type == self.ConfigTypes.DEVICE):
                print "device"
                self.calculator = self.create_device_calculator_dft (basis_set)
            elif (self.config_type == self.ConfigTypes.BULK):
                print "bulk"
                self.calculator = self.create_bulk_calculator (basis_set)

            init_config_obj.setCalculator(self.calculator)
            nlprint(init_config_obj)
            init_config_obj.update()

            nlsave(device_config_path, init_config_obj, object_id="UnrelaxedConfig, GateV %f, Vds %f" % (0.0, 0.0))

            if (self.config_type == self.ConfigTypes.DEVICE):
                configuration_obj = nlread(device_config_path, DeviceConfiguration)
            elif (self.config_type == self.ConfigTypes.BULK):
                configuration_obj = nlread(device_config_path, BulkConfiguration)


            self.configuration_obj = configuration_obj [0]

        else:
            print 'Found initial configuration'
            self.set_configuration_type(init_config_obj[0])
            self.set_default_obj (state="UnrelaxedConfig")
        
 
    def usage(self):
        print 'atkpython interface_anaysis.py --ifile=<inputfile> --analysis=<interface>'
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

    def find_unrelaxed_config (self, obj):

        default_config = nlread(self.device_config_path, self.config_type[2], 
                                object_id="UnrelaxedConfig, GateV %f, Vds %f" % (0.0,0.0))

        if not default_config:
            #TODO MAKE THIS INTO ASSERT
            print "No config found with this voltage or state! Run the init first! Vds = ", vds, " GateV = ", gate_v, " State = ", state
            sys.exit()
        
        default_config = default_config[0]
        self.state = 'UnrelaxedConfig'

        return default_config
 
    def set_default_obj (self, gate_v = 0*Volt, vds = 0*Volt, state='UnrelaxedConfig'):
        default_config = None


        self.state = state
        default_config = nlread(self.device_config_path, self.config_type[2], 
                                object_id="%s, GateV %f, Vds %f" % (state, gate_v.inUnitsOf(Volt), vds.inUnitsOf(Volt)))

        if not default_config:
            #TODO MAKE THIS INTO ASSERT
            print "No config found with this voltage or state! Run the init first! Vds = ", vds, " GateV = ", gate_v, " State = ", state
            sys.exit()
        
        default_config = default_config[0]
        self.configuration_obj = default_config
 
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
        constraints = []
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
            return bulk_configuration, basis_set, constraints
        elif bulk_configuration is None:
            return device_configuration, basis_set, constraints
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

    def gv_obj (self, configuration_obj):
            metallic_regions = configuration_obj.metallicRegions()
            if not metallic_regions:
                print "There are no metallic regions, device is not gated..."
                #return 0 volt value
                return self.default_gate_voltage.inUnitsOf(Volt)
            gate_bias = metallic_regions[0].value().inUnitsOf(Volt)
            print "Metallic region voltages: "
            for region in metallic_regions:
                print region.value().inUnitsOf(Volt),
            
            return gate_bias
    def vds_obj (self, configuration_obj):
            if self.config_type == self.ConfigTypes.DEVICE:
                electrode_voltages = configuration_obj.calculator().electrodeVoltages()
                return electrode_voltages[0].inUnitsOf(Volt) * 2
            elif self.config_type == self.ConfigTypes.BULK:
                #VDS for bulk is always 0
                return 0
 
    def generate_diff_pot (self):
        print "Generating Difference Potential"

        diff = ElectrostaticDifferencePotential (
            configuration = self.configuration_obj,
        )

        nlsave(self.device_config_path, diff, object_id="DiffPot, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


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

        nlsave(self.device_config_path, electron_density, object_id="Edens, State %s, GateV %f, Vds %f" % (self.state, self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))


    def generate_dos_real_space (self):
        print "Generate DOS real space"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)

        energies = np.linspace(-5, 5, num = 100)
        energies = [round(x, 6) for x in energies]
        num_energies = len(energies)
        done_nrg = []

        lddos_list = []
        for nrg in energies:
            print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
            lddos_obj = nlread(self.device_config_path, LocalDeviceDensityOfStates, object_id="LDDOS %f, State %s, GateV %f, Vds %f" % (nrg, self.state, gv, vds))
            if lddos_obj:
                lddos_list.append(lddos_obj[0])
        if lddos_list:
           #generate for the erngies that are not done.
            for lddos in lddos_list:
                rounded_nrg = round(lddos.energy().inUnitsOf(eV)[0], 6)
                done_nrg.append(rounded_nrg)
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
            nlsave(self.device_config_path,ldos, object_id="LDDOS %f, State %s, GateV %f, Vds %f" % (nrg.inUnitsOf(eV), self.state, self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

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

        edensity_obj = nlread(self.device_config_path, ElectronDensity, object_id="Edens, State %s, GateV %f, Vds %f" % (self.state, self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        if not edensity_obj:
            self.generate_e_density()
            edensity_obj = nlread(self.device_config_path, ElectronDensity, object_id="Edens, State %s, GateV %f, Vds %f" % (self.state, self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))

        edensity_obj = edensity_obj[0]

        
        proj_x_arr = []
        proj_y_arr = []
        proj_z_arr = []

        proj_z_arr.append(edensity_obj.axisProjection ('Line', 'C', Spin.Sum))

        outfile = open (self.device_config_path + 'edensity_' + self.state + '.plot', 'w')
        outfile.write ('z, n\n')
        outfile.write ('Å,Å\+(-3)\n')

        for i in range(len(proj_z_arr[0][0])):
        
            z_angstrom_0 = str(self.frac_to_cart(self.z_length, proj_z_arr[0][0][i]).inUnitsOf(Angstrom))
            z_density_0 = str(proj_z_arr[0][1][i].inUnitsOf(Angstrom**-3))


            #printing VEFF for x direction
            outfile.write (z_angstrom_0 + ',')
            outfile.write (z_density_0)
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
        
            z_angstrom_0 = str(self.frac_to_cart(self.z_length, proj_x_arr[0][0][i]).inUnitsOf(Angstrom))
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
    def lddos_worker (self, axis, obj, result_dict):
        dd={}
        axisProj = obj.axisProjection ('Average', axis, Spin.Sum)
        fracs = [float(x) for x in axisProj[0]]
        vals = [x.inUnitsOf(Hartree**-1 * Angstrom**-3) for x in axisProj[1]]
        result_dict[axis] = (fracs, vals)
    def lddos_multi_nrg_worker (self, obj, result_string_lst):
        nprocs = 3
        procs = []
        manager = multiprocessing.Manager()
        result_dict=manager.dict()
        start_loop_time = time.time()
        energy = obj.energy()[0]
        axis = ['A','B','C']
        for i in range(nprocs):
            p = multiprocessing.Process (target=self.lddos_worker,
                                        args=(axis[i],obj, result_dict))
            procs.append(p)
            p.start()
        for p in procs:
            p.join()
        proj_x = []
        proj_x.append(result_dict[axis[0]][0])
        proj_x.append(result_dict[axis[0]][1])
        proj_y = []
        proj_y.append(result_dict[axis[1]][0])
        proj_y.append(result_dict[axis[1]][1])
        proj_z = []
        proj_z.append(result_dict[axis[2]][0])
        proj_z.append(result_dict[axis[2]][1])
        print "Printing LDDOS for Energy = ", str(energy.inUnitsOf(eV)),
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
            final_string = (x_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (x_states + ',')
            final_string = final_string + (y_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (y_states + ',')
            final_string = final_string + (z_angstrom + ',')
            final_string = final_string + (energy_str + ',')
            final_string = final_string + (z_states + ',')
            final_string = final_string + '\n'
            final_str_list.append(final_string)
        result_string_lst[energy_float] = final_str_list
    def graph_dos_real_space (self):
        print "Graphing LDDOS Real Space"
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        start = time.time()
        self.generate_dos_real_space()
        energies = np.linspace(-5, 5, num = 100)
        energies = [round(x, 6) for x in energies]
        lddos_list = []
        for nrg in energies:
            print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
            lddos_obj = nlread(self.device_config_path, LocalDeviceDensityOfStates, object_id="LDDOS %f, State %s, GateV %f, Vds %f" % (nrg, self.state, gv, vds))
            lddos_list.append(lddos_obj[0])
        
        #print "NUMBER OF LDDSO BJECTS"
        #print len(nlread(self.device_config_path, LocalDeviceDensityOfStates))

        outfile = open (self.device_config_path + "_VG_" + str(gv) + "V_VDS_"+ str(vds) + '_V_lddos.plot', 'w')
        outfile.write ('x, Energy, States, y, Energy, States, z, Energy, States\n')
        outfile.write ('Angstrom, eV, arb. units, Angstrom, eV, arb. units, Angstrom, eV, arb. units\n')
        outfile.write ('x, Energy, Number of States, y, Energy, Number of States, z, Energy, Number of States\n')


        nprocs = 4
        final_out_dict = {}
        for k in range(0, len(lddos_list), 4):

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
                # For y coords
            time_per_iter = time.time() - start_loop_time
            print "Time Taken: ", time_per_iter

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
        #print len(nlread(self.device_config_path, LocalDeviceDensityOfStates))
        self.generate_dos_real_space()
        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        energies = np.linspace(-5, 5, num = 100)
        energies = [round(x, 6) for x in energies]
        lddos_list = []
        for nrg in energies:
            print "Reading LDDOS with energy: ", nrg, ", VGS = ", gv, " VDS = ", vds
            lddos_obj = nlread(self.device_config_path, LocalDeviceDensityOfStates, object_id="LDDOS %f, State %s, GateV %f, Vds %f" % (nrg, self.state, gv, vds))

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

        import pylab
        #plot the LDDOS(E, z)
        pylab.xlabel('z (Angstrom)',fontsize=12,family='sans-serif')
        pylab.ylabel('Energy (eV)',fontsize=12,family='sans-serif')

        contour_values = numpy.linspace(0 , numpy.amax(Z), 25)
        pylab.contourf(X, Y, Z, contour_values)
        pylab.colorbar()
        pylab.axis([numpy.amin(X), numpy.amax(X), numpy.amin(Y), numpy.amax(Y)])

        pylab.title(self.device_config_path + ": E vs. z")
        pylab.savefig(self.device_config_path +self.state+ "_VG_" + str(gv) + "V_VDS_"+ str(vds) + '_V_lddos.png',dpi=100)


        #pylab.show()
    def graph_density_of_states (self):
        print "Graphing Density of States"


        gv = self.gv_obj(self.configuration_obj)
        vds = self.vds_obj(self.configuration_obj)
        print "Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj))
        dos_objects = []
        #get the DOS object for the gate voltage we're working wiht
        try:
            dos_objects = nlread(self.device_config_path, self.config_type[1], object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        except:
    
            self.generate_density_of_states ()
            dos_objects = nlread(self.device_config_path, self.config_type[1], object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        if not dos_objects:
            self.generate_density_of_states ()
            dos_objects = nlread(self.device_config_path, self.config_type[1], object_id="Dos, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
        else:
            print "Using existing generated DOS"

        dos_obj = dos_objects[0] 
        outfile = open (self.device_config_path +self.state+ "_VG_" + str(gv) + "V_VDS_"+ str(vds) + "_V_dos.plot", 'w')
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

    def generate_density_of_states (self):
        print "Generating DOS"
               # -------------------------------------------------------------
        # Device density of states
        # -------------------------------------------------------------
        if self.config_type == self.ConfigTypes.DEVICE:

            dos = DeviceDensityOfStates(
                configuration=self.configuration_obj,
                energies=numpy.linspace(-5,5,200)*eV,
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

    def relax_structure (self):
        print "Relaxing structure"

        relaxed_obj = nlread(self.device_config_path, BulkConfiguration, object_id="RelaxedConfig, GateV %f, Vds %f" % (self.gv_obj(self.configuration_obj), self.vds_obj(self.configuration_obj)))
            
        if not relaxed_obj:
            relaxed_obj = OptimizeGeometry(
                configuration=self.configuration_obj,
                max_forces=0.01*eV/Ang,
                max_steps=200,
                max_step_length=0.5*Ang,
                constraints=self.constraints,
                trajectory_filename=self.device_config_path + "_traj.nc",
                disable_stress=True,
                optimizer_method=QuasiNewton(),

            )
            nlsave(self.device_config_path, relaxed_obj, object_id="RelaxedConfig, GateV %f, Vds %f" % (0.0, 0.0))
        else:
            print "Already generated relaxed structure..."

     
    def analyze(self, run_dos_real_space=False):
       
        self.extract_dimensions()
        print "Starting analysis..."

        if (self.config_type == self.ConfigTypes.BULK):
            self.generate_bulk_bandstructure()
            self.graph_e_density ()
            self.graph_density_of_states ()

        if (run_dos_real_space):
            #self.graph_dos_real_space ()
            self.graph_density_of_states ()

        self.graph_v_eff ()
        self.graph_e_density ()
        #self.graph_diff_pot()
        #self.graph_e_diff_density ()
        #self.graph_density_of_states ()
        

if __name__ == "__main__":

        int_anal_obj = IntefaceAnalysis(sys.argv[1:])
        analysis_type = int_anal_obj.analysis_type
        state = int_anal_obj.state
        relax = int_anal_obj.relax

        if analysis_type == "interface":
            
            if relax:
                int_anal_obj.relax_structure()
                int_anal_obj.set_default_obj (state="RelaxedConfig")
                int_anal_obj.analyze(run_dos_real_space = True)
            else:
                int_anal_obj.set_default_obj (state=state)
                int_anal_obj.analyze(run_dos_real_space = True)
                
                

