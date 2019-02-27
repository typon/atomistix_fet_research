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
        self.epsilon_dielectric_region = 25.0
        self.gate_length = 30.0 * Angstrom
        self.metal_region_voltage = 0.0
        self.num_gates = 4
        self.orientation = 'horizontal'
        # Define gate_voltages

        self.ConfigTypes = enum (BULK = (1, DensityOfStates, BulkConfiguration) , DEVICE = (2, DeviceDensityOfStates, DeviceConfiguration))


        try:
            opts, args = getopt.getopt(argv,"higpsno:",["ifile=", "permittivity=", "gate_length=", "size=", "num_gates=", "orientation="])
        except getopt.GetoptError:
            self.usage()
        if not opts:
            print 'No options supplied'
            self.usage()
        for opt, arg in opts:
            if opt == '-h':
                self.usage()
            elif opt in ("-s", "--size"):
                self.size_dielectric_region = float(arg) * Angstrom
            elif opt in ("-p", "--permittivity"):
                self.epsilon_dielectric_region = float(arg)
            elif opt in ("-g", "--gate_length"):
                self.gate_length = float(arg) * Angstrom
            elif opt in ("-n", "--num_gates"):
                self.num_gates = int(arg)
            elif opt in ("-o", "--orientation"):
                self.orientation = arg
            elif opt in ("-i", "--ifile"):
                inputfile = arg
        print 'Input geometry file is:', inputfile


        #run self consistent device calculation for zero bias.
        init_config_obj = []

        #Get full file path
        full_input_path = os.path.abspath (inputfile)
        #Get input file name only
        file_base_name = ntpath.basename(full_input_path)
        print file_base_name
        print full_input_path 



        print "No initial configuration exists, running DFT calculation"

        print "Extracting configuration from file"
        #pdb.set_trace()
        init_config_obj = self.create_device_config(inputfile)

        #setting iether bulk or device config type
        self.configuration_obj = init_config_obj
    
        if (self.num_gates == 2):
            if (self.orientation == 'vertical'):
                self.extract_dimensions_two_gates_vertical()
            else:
                self.extract_dimensions_two_gates()
        elif (self.num_gates == 3):
            self.extract_dimensions_three_gates()
        elif (self.num_gates == 4):
            self.extract_dimensions()
 
    def usage(self):
        print 'python device_analysis.py --ifile=<inputfile>'
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
        print "###########################"

        #s = codeOut.getvalue()
        #print "output:\n%s" % s

        codeOut.close()
        codeErr.close()

        if device_configuration is None:
            return bulk_configuration
        elif bulk_configuration is None:
            return device_configuration
        else:
           print "Error: No configuration specified"
           sys.exit()
            
            
    def extract_dimensions (self):
        lattice = self.configuration_obj.bravaisLattice()
        lattice_vectors = lattice.primitiveVectors()

        self.x_length = lattice_vectors[0][0]
        self.y_length = lattice_vectors[1][1]
        self.z_length = lattice_vectors[2][2]

        coords = self.configuration_obj.cartesianCoordinates()
        print "Coordinates of all atoms..."
        print coords
        print "End of coordinates...\n"

        print "Maximum x-axis coordinate = ", coords.max(axis=0)[0]
        max_x = coords.max(axis=0)[0].inUnitsOf(Angstrom)
        print "Maximum y-axis coordinate = ", coords.max(axis=0)[1]
        max_y = coords.max(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.max(axis=0)[2]
        max_z = coords.max(axis=0)[2].inUnitsOf(Angstrom)
        print "Minumum x-axis coordinate = ", coords.min(axis=0)[0]
        min_x = coords.min(axis=0)[0].inUnitsOf(Angstrom)
        print "Minimum y-axis coordinate = ", coords.min(axis=0)[1]
        min_y = coords.min(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.min(axis=0)[2]
        min_z = coords.min(axis=0)[2].inUnitsOf(Angstrom)

        print "Print dielectric region size = ", self.size_dielectric_region 
        print "\n\n"

        
        #all relative to looking at xy plane

        #print dielectric region 0 (middle right)
        print "dielectric_region_0 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x - 1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", max_y+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"

        #print dielectric region 1 (middle top)
        print "dielectric_region_1 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", max_y + 1, "*Angstrom, ",
        print "ymax = ", (max_y + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 2 (middle left)
        print "dielectric_region_2 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", max_x + 1, "*Angstrom, ",
        print "xmax = ", (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", max_y+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 2 (middle bottom)
        print "dielectric_region_3 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", min_y - 1, "*Angstrom, ",
        print "ymax = ", (min_y - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 2 (bottom right)
        print "dielectric_region_4 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", (min_y - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 2 (top right)
        print "dielectric_region_5 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", max_y+1, "*Angstrom, ",
        print "ymax = ", (max_y+1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"
        #print dielectric region 2 (top left)
        print "dielectric_region_6 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", max_x+1, "*Angstrom, ",
        print "xmax = ", (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", max_y+1, "*Angstrom, ",
        print "ymax = ", (max_y+1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"
        #print dielectric region 2 (bottom left)
        print "dielectric_region_7 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", max_x+1, "*Angstrom, ",
        print "xmax = ", (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", (min_y-1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]"
        print "central_region.setDielectricRegions(dielectric_regions)"



        print "\n"
        print "#Metal regions..."

        #print metal region 0 (right)
        print "metallic_region_0 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmin - 1, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        ymax = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymax, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 1 (top)
        print "metallic_region_1 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom) - 1
        xmax = (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom) + 1
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 2 (left)
        print "metallic_region_2 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmin + 1, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        ymax = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymax, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 3 (bottom)
        print "metallic_region_3 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom) - 1
        xmax = (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom) + 1
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin-1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]"
        print "central_region.setMetallicRegions(metallic_regions)"
        print "\n"



        print "Minimum dimensions of cell..."
        vector_a = (max_x-min_x) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2
        vector_b = (max_y-min_y) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2

        print "vector_a = [", vector_a, ", 0.0, 0.0]*Angstrom"
        print "vector_b = [0.0, ", vector_b,"0.0]*Angstrom"

    def extract_dimensions_two_gates (self):
        lattice = self.configuration_obj.bravaisLattice()
        lattice_vectors = lattice.primitiveVectors()

        self.x_length = lattice_vectors[0][0]
        self.y_length = lattice_vectors[1][1]
        self.z_length = lattice_vectors[2][2]

        coords = self.configuration_obj.cartesianCoordinates()
        print "Coordinates of all atoms..."
        print coords
        print "End of coordinates...\n"

        print "Maximum x-axis coordinate = ", coords.max(axis=0)[0]
        max_x = coords.max(axis=0)[0].inUnitsOf(Angstrom)
        print "Maximum y-axis coordinate = ", coords.max(axis=0)[1]
        max_y = coords.max(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.max(axis=0)[2]
        max_z = coords.max(axis=0)[2].inUnitsOf(Angstrom)
        print "Minumum x-axis coordinate = ", coords.min(axis=0)[0]
        min_x = coords.min(axis=0)[0].inUnitsOf(Angstrom)
        print "Minimum y-axis coordinate = ", coords.min(axis=0)[1]
        min_y = coords.min(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.min(axis=0)[2]
        min_z = coords.min(axis=0)[2].inUnitsOf(Angstrom)

        print "Print dielectric region size = ", self.size_dielectric_region 
        print "\n\n"

        
        #all relative to looking at xy plane

        #print dielectric region 0 (middle top)
        print "dielectric_region_0 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", max_y + 1, "*Angstrom, ",
        print "ymax = ", (max_y + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 1 (middle bottom)
        print "dielectric_region_1 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", min_y - 1, "*Angstrom, ",
        print "ymax = ", (min_y - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        print "\n"

        print "dielectric_regions = [dielectric_region_0, dielectric_region_1]"
        print "central_region.setDielectricRegions(dielectric_regions)"



        print "\n"

        print "#Metal regions..."

        #print metal region 0 (top)
        print "metallic_region_0 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) 
        xmax = (max_x + 1)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 1 (bottom)
        print "metallic_region_1 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) 
        xmax = (max_x + 1)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin-1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "metallic_regions = [metallic_region_0, metallic_region_1]"
        print "central_region.setMetallicRegions(metallic_regions)"
        print "\n"



        print "Minimum dimensions of cell..."
        vector_a = (max_x-min_x) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2
        vector_b = (max_y-min_y) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2

        print "vector_a = [", vector_a, ", 0.0, 0.0]*Angstrom"
        print "vector_b = [0.0, ", vector_b,"0.0]*Angstrom"
        
    def extract_dimensions_three_gates (self):
        lattice = self.configuration_obj.bravaisLattice()
        lattice_vectors = lattice.primitiveVectors()

        self.x_length = lattice_vectors[0][0]
        self.y_length = lattice_vectors[1][1]
        self.z_length = lattice_vectors[2][2]

        coords = self.configuration_obj.cartesianCoordinates()
        print "Coordinates of all atoms..."
        print coords
        print "End of coordinates...\n"

        print "Maximum x-axis coordinate = ", coords.max(axis=0)[0]
        max_x = coords.max(axis=0)[0].inUnitsOf(Angstrom)
        print "Maximum y-axis coordinate = ", coords.max(axis=0)[1]
        max_y = coords.max(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.max(axis=0)[2]
        max_z = coords.max(axis=0)[2].inUnitsOf(Angstrom)
        print "Minumum x-axis coordinate = ", coords.min(axis=0)[0]
        min_x = coords.min(axis=0)[0].inUnitsOf(Angstrom)
        print "Minimum y-axis coordinate = ", coords.min(axis=0)[1]
        min_y = coords.min(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.min(axis=0)[2]
        min_z = coords.min(axis=0)[2].inUnitsOf(Angstrom)

        print "Print dielectric region size = ", self.size_dielectric_region 
        print "\n\n"

        
        #all relative to looking at xy plane

        #print dielectric region 0 (middle right)
        print "dielectric_region_0 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x - 1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", max_y+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"

        #print dielectric region 1 (middle top)
        print "dielectric_region_1 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", max_y + 1, "*Angstrom, ",
        print "ymax = ", (max_y + 1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 2 (middle bottom)
        print "dielectric_region_2 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", min_y - 1, "*Angstrom, ",
        print "ymax = ", (min_y - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 3 (bottom right)
        print "dielectric_region_3 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", (min_y - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 4 (top right)
        print "dielectric_region_4 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1, "*Angstrom, ",
        print "xmax = ", (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        print "ymin = ", max_y+1, "*Angstrom, ",
        print "ymax = ", (max_y+1) + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4]"
        print "central_region.setDielectricRegions(dielectric_regions)"



        print "\n"
        print "#Metal regions..."

        #print metal region 0 (right)
        print "metallic_region_0 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmin - 1, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        ymax = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymax, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 1 (top)
        print "metallic_region_1 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (max_x + 1)
        xmax = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom) - 1
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = max_y + 1 + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 2 (bottom)
        print "metallic_region_2 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (max_x + 1)
        xmax = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom) - 1
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = min_y - 1 - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymin-1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2]"
        print "central_region.setMetallicRegions(metallic_regions)"
        print "\n"



        print "Minimum dimensions of cell..."
        vector_a = (max_x-min_x) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2
        vector_b = (max_y-min_y) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2

        print "vector_a = [", vector_a, ", 0.0, 0.0]*Angstrom"
        print "vector_b = [0.0, ", vector_b,"0.0]*Angstrom"

    def extract_dimensions_two_gates_vertical (self):
        lattice = self.configuration_obj.bravaisLattice()
        lattice_vectors = lattice.primitiveVectors()

        self.x_length = lattice_vectors[0][0]
        self.y_length = lattice_vectors[1][1]
        self.z_length = lattice_vectors[2][2]

        coords = self.configuration_obj.cartesianCoordinates()
        print "Coordinates of all atoms..."
        print coords
        print "End of coordinates...\n"

        print "Maximum x-axis coordinate = ", coords.max(axis=0)[0]
        max_x = coords.max(axis=0)[0].inUnitsOf(Angstrom)
        print "Maximum y-axis coordinate = ", coords.max(axis=0)[1]
        max_y = coords.max(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.max(axis=0)[2]
        max_z = coords.max(axis=0)[2].inUnitsOf(Angstrom)
        print "Minumum x-axis coordinate = ", coords.min(axis=0)[0]
        min_x = coords.min(axis=0)[0].inUnitsOf(Angstrom)
        print "Minimum y-axis coordinate = ", coords.min(axis=0)[1]
        min_y = coords.min(axis=0)[1].inUnitsOf(Angstrom)
        print "Maximum z-axis coordinate = ", coords.min(axis=0)[2]
        min_z = coords.min(axis=0)[2].inUnitsOf(Angstrom)

        print "Print dielectric region size = ", self.size_dielectric_region 
        print "\n\n"

        
        #all relative to looking at xy plane

        #print dielectric region 0 (middle right)
        print "dielectric_region_0 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", min_x-1 - self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom, ",
        print "xmax = ", min_x-1, "*Angstrom,"
        print "\t",
        print "ymin = ", min_y-1, "*Angstrom, ",
        print "ymax = ", max_y+1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        #print dielectric region 1 (middle left)
        print "dielectric_region_1 = BoxRegion("
        print "\t",
        print self.epsilon_dielectric_region, ","
        
        print "\t",
        print "xmin = ", max_x + 1 + self.size_dielectric_region.inUnitsOf(Angstrom), "*Angstrom, ",
        print "xmax = ", max_x+1, "*Angstrom,"
        print "\t",
        print "ymin = ", min_y - 1, "*Angstrom, ",
        print "ymax = ", max_y + 1, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"

        print ")"
        print "\n"

        print "dielectric_regions = [dielectric_region_0, dielectric_region_1]"
        print "central_region.setDielectricRegions(dielectric_regions)"



        print "\n"

        print "#Metal regions..."

        #print metal region 0 (middle right)
        print "metallic_region_0 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (min_x - 2) - self.size_dielectric_region.inUnitsOf(Angstrom)
        xmax = (min_x - 1) - self.size_dielectric_region.inUnitsOf(Angstrom)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = min_y - 1
        ymax = max_y + 1
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymax, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        #print metal region 1 (middle left)
        print "metallic_region_1 = BoxRegion("
        print "\t",
        print self.metal_region_voltage, "*Volt,"
        
        print "\t",
        xmin = (max_x + 1) + self.size_dielectric_region.inUnitsOf(Angstrom)
        xmax = (max_x + 2) + self.size_dielectric_region.inUnitsOf(Angstrom)
        print "xmin = ", xmin, "*Angstrom, ",
        print "xmax = ", xmax, "*Angstrom,"
        print "\t",
        ymin = min_y - 1
        ymax = max_y + 1
        print "ymin = ", ymin, "*Angstrom, ",
        print "ymax = ", ymax, "*Angstrom,"
        print "\t",
        z_min_de = (max_z - self.gate_length.inUnitsOf(Angstrom))/2
        print "zmin = ", z_min_de, "*Angstrom, ",
        print "zmax = ", z_min_de + self.gate_length.inUnitsOf(Angstrom), "*Angstrom,"
        print ")"

        print "metallic_regions = [metallic_region_0, metallic_region_1]"
        print "central_region.setMetallicRegions(metallic_regions)"
        print "\n"



        print "Minimum dimensions of cell..."
        vector_a = (max_x-min_x) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2
        vector_b = (max_y-min_y) + 2 + (self.size_dielectric_region.inUnitsOf(Angstrom))*2 + 2

        print "vector_a = [", vector_a, ", 0.0, 0.0]*Angstrom"
        print "vector_b = [0.0, ", vector_b,"0.0]*Angstrom"
 
    



       

if __name__ == "__main__":

       dev_anal_obj = DeviceAnalysis(sys.argv[1:])

