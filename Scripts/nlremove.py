from NanoLanguage import *
from NL.IO.NLSaveUtilities import nlinspect
import sys

"""
---------------------------------------------------------------------------------------
Usage:

atkpython nlremove.py too_big_nc_file.nc smaller_nc_file.nc gID000 gID001 ...

If only one argument is passed (one NC file), the object IDs in the file are printed
---------------------------------------------------------------------------------------
"""

def nlremove(input_filename,output_filename,ids_to_remove):
    """
    Function to remove a set of object IDs from a NetCDF file

    @param    input_filename    The name of the original NC file
    @type     string

    @param    output_filename   The name of the output NC file
    @type     string

    @param    ids_to_remove     Object IDs to remove
    @type     list of strings, or string
    """
    
    if in_filename == "":
        print "No input NetCDF file specified - not much to do here..."
        return

    # Allow a single object ID to be removed by passing it as a simple string
    if type(ids_to_remove) == str:
        ids_to_remove = [ids_to_remove]

    if input_filename == output_filename:
        print "Input and output NC files must be different"
        return

    file_contents = nlinspect(input_filename)
    if file_contents is None:
        print "Input file %s not found, or not a valid NetCDF file" % input_filename
        return

    # Present contents of file, for reference
    
    # Make a nice table presentation
    l1 = max([len(s) for s in file_contents[:,1]])+2
    l2 = max([len(s) for s in file_contents[:,0]])+2
    table = "{0: <%d} {1: <%d}" % (l1,l2)

    print "Contents of", input_filename
    print table.format("ID","Object"),"Remove?"
    print "----------------------------------------------------------------------------------------"
    for ix in range(len(file_contents)):
        print table.format(file_contents[ix][1],file_contents[ix][0]),
        if file_contents[ix][1] in ids_to_remove:
            print "Yes"
        else:
            print "No"
    print

    # If no objects are specified for removal, exit now
    if ids_to_remove == []:
        print "No objects to remove - output file will not be created"
        return

    print "Writing objects to", output_filename

    # Read and write all objects, one by one
    for id in file_contents[:,1]:
        object = nlread(input_filename, object_id=id)[0]
        if id in ids_to_remove:
            print table.format(id,"- skipping")
        else:
            nlsave(output_filename,object,object_id=id)
            print table.format(id,"- done")

# ----------------------------------------------------------------------

# Initialize to empty values
in_filename = ""
out_filename = ""
ids_to_remove = []

# If command line arguments are provided for output file and object IDs, read them
if len(sys.argv)>1:
    in_filename = sys.argv[1]
if len(sys.argv)>2:
    out_filename = sys.argv[2]
if len(sys.argv)>3:
    #ids_to_remove.append('Dos, GateV 0.000000, Vds 0.000000')
    #ids_to_remove.append('Bands, GateV 0.000000, Vds 0.000000')

    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.000000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.100000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.200000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.300000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.400000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.700000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.800000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 0.900000')
    #ids_to_remove.append('Trans, GateV 0.000000, Vds 1.000000')

    print "Nothign"




# GO!
nlremove(in_filename,out_filename,ids_to_remove)
