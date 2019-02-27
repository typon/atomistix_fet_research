# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [26.1262050405, 0.0, 0.0]*Angstrom
vector_b = [0.0, 26.1262050405, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[  8.9848526 ,   6.94572764,   1.0195625 ],
                              [ 13.06310252,   6.94572764,   1.0195625 ],
                              [ 17.14135244,   6.94572764,   1.0195625 ],
                              [  6.94572764,   8.9848526 ,   1.0195625 ],
                              [ 11.02397756,   8.9848526 ,   1.0195625 ],
                              [ 15.10222748,   8.9848526 ,   1.0195625 ],
                              [ 19.1804774 ,   8.9848526 ,   1.0195625 ],
                              [  8.9848526 ,  11.02397756,   1.0195625 ],
                              [ 13.06310252,  11.02397756,   1.0195625 ],
                              [ 17.14135244,  11.02397756,   1.0195625 ],
                              [  6.94572764,  13.06310252,   1.0195625 ],
                              [ 11.02397756,  13.06310252,   1.0195625 ],
                              [ 15.10222748,  13.06310252,   1.0195625 ],
                              [ 19.1804774 ,  13.06310252,   1.0195625 ],
                              [  8.9848526 ,  15.10222748,   1.0195625 ],
                              [ 13.06310252,  15.10222748,   1.0195625 ],
                              [ 17.14135244,  15.10222748,   1.0195625 ],
                              [  6.94572764,  17.14135244,   1.0195625 ],
                              [ 11.02397756,  17.14135244,   1.0195625 ],
                              [ 15.10222748,  17.14135244,   1.0195625 ],
                              [ 19.1804774 ,  17.14135244,   1.0195625 ],
                              [  8.9848526 ,  19.1804774 ,   1.0195625 ],
                              [ 13.06310252,  19.1804774 ,   1.0195625 ],
                              [ 17.14135244,  19.1804774 ,   1.0195625 ],
                              [  6.94572764,   6.94572764,   3.0586875 ],
                              [ 11.02397756,   6.94572764,   3.0586875 ],
                              [ 15.10222748,   6.94572764,   3.0586875 ],
                              [ 19.1804774 ,   6.94572764,   3.0586875 ],
                              [  8.9848526 ,   8.9848526 ,   3.0586875 ],
                              [ 13.06310252,   8.9848526 ,   3.0586875 ],
                              [ 17.14135244,   8.9848526 ,   3.0586875 ],
                              [  6.94572764,  11.02397756,   3.0586875 ],
                              [ 11.02397756,  11.02397756,   3.0586875 ],
                              [ 15.10222748,  11.02397756,   3.0586875 ],
                              [ 19.1804774 ,  11.02397756,   3.0586875 ],
                              [  8.9848526 ,  13.06310252,   3.0586875 ],
                              [ 13.06310252,  13.06310252,   3.0586875 ],
                              [ 17.14135244,  13.06310252,   3.0586875 ],
                              [  6.94572764,  15.10222748,   3.0586875 ],
                              [ 11.02397756,  15.10222748,   3.0586875 ],
                              [ 15.10222748,  15.10222748,   3.0586875 ],
                              [ 19.1804774 ,  15.10222748,   3.0586875 ],
                              [  8.9848526 ,  17.14135244,   3.0586875 ],
                              [ 13.06310252,  17.14135244,   3.0586875 ],
                              [ 17.14135244,  17.14135244,   3.0586875 ],
                              [  6.94572764,  19.1804774 ,   3.0586875 ],
                              [ 11.02397756,  19.1804774 ,   3.0586875 ],
                              [ 15.10222748,  19.1804774 ,   3.0586875 ],
                              [ 19.1804774 ,  19.1804774 ,   3.0586875 ]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [26.1262050405, 0.0, 0.0]*Angstrom
vector_b = [0.0, 26.1262050405, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[  8.9848526 ,   6.94572764,   1.0195625 ],
                               [ 13.06310252,   6.94572764,   1.0195625 ],
                               [ 17.14135244,   6.94572764,   1.0195625 ],
                               [  6.94572764,   8.9848526 ,   1.0195625 ],
                               [ 11.02397756,   8.9848526 ,   1.0195625 ],
                               [ 15.10222748,   8.9848526 ,   1.0195625 ],
                               [ 19.1804774 ,   8.9848526 ,   1.0195625 ],
                               [  8.9848526 ,  11.02397756,   1.0195625 ],
                               [ 13.06310252,  11.02397756,   1.0195625 ],
                               [ 17.14135244,  11.02397756,   1.0195625 ],
                               [  6.94572764,  13.06310252,   1.0195625 ],
                               [ 11.02397756,  13.06310252,   1.0195625 ],
                               [ 15.10222748,  13.06310252,   1.0195625 ],
                               [ 19.1804774 ,  13.06310252,   1.0195625 ],
                               [  8.9848526 ,  15.10222748,   1.0195625 ],
                               [ 13.06310252,  15.10222748,   1.0195625 ],
                               [ 17.14135244,  15.10222748,   1.0195625 ],
                               [  6.94572764,  17.14135244,   1.0195625 ],
                               [ 11.02397756,  17.14135244,   1.0195625 ],
                               [ 15.10222748,  17.14135244,   1.0195625 ],
                               [ 19.1804774 ,  17.14135244,   1.0195625 ],
                               [  8.9848526 ,  19.1804774 ,   1.0195625 ],
                               [ 13.06310252,  19.1804774 ,   1.0195625 ],
                               [ 17.14135244,  19.1804774 ,   1.0195625 ],
                               [  6.94572764,   6.94572764,   3.0586875 ],
                               [ 11.02397756,   6.94572764,   3.0586875 ],
                               [ 15.10222748,   6.94572764,   3.0586875 ],
                               [ 19.1804774 ,   6.94572764,   3.0586875 ],
                               [  8.9848526 ,   8.9848526 ,   3.0586875 ],
                               [ 13.06310252,   8.9848526 ,   3.0586875 ],
                               [ 17.14135244,   8.9848526 ,   3.0586875 ],
                               [  6.94572764,  11.02397756,   3.0586875 ],
                               [ 11.02397756,  11.02397756,   3.0586875 ],
                               [ 15.10222748,  11.02397756,   3.0586875 ],
                               [ 19.1804774 ,  11.02397756,   3.0586875 ],
                               [  8.9848526 ,  13.06310252,   3.0586875 ],
                               [ 13.06310252,  13.06310252,   3.0586875 ],
                               [ 17.14135244,  13.06310252,   3.0586875 ],
                               [  6.94572764,  15.10222748,   3.0586875 ],
                               [ 11.02397756,  15.10222748,   3.0586875 ],
                               [ 15.10222748,  15.10222748,   3.0586875 ],
                               [ 19.1804774 ,  15.10222748,   3.0586875 ],
                               [  8.9848526 ,  17.14135244,   3.0586875 ],
                               [ 13.06310252,  17.14135244,   3.0586875 ],
                               [ 17.14135244,  17.14135244,   3.0586875 ],
                               [  6.94572764,  19.1804774 ,   3.0586875 ],
                               [ 11.02397756,  19.1804774 ,   3.0586875 ],
                               [ 15.10222748,  19.1804774 ,   3.0586875 ],
                               [ 19.1804774 ,  19.1804774 ,   3.0586875 ]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Central region
# -------------------------------------------------------------

# Set up lattice
vector_a = [26.1262050405, 0.0, 0.0]*Angstrom
vector_b = [0.0, 26.1262050405, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[  8.9848526 ,   6.94572764,   1.0195625 ],
                              [ 13.06310252,   6.94572764,   1.0195625 ],
                              [ 17.14135244,   6.94572764,   1.0195625 ],
                              [  6.94572764,   8.9848526 ,   1.0195625 ],
                              [ 11.02397756,   8.9848526 ,   1.0195625 ],
                              [ 15.10222748,   8.9848526 ,   1.0195625 ],
                              [ 19.1804774 ,   8.9848526 ,   1.0195625 ],
                              [  8.9848526 ,  11.02397756,   1.0195625 ],
                              [ 13.06310252,  11.02397756,   1.0195625 ],
                              [ 17.14135244,  11.02397756,   1.0195625 ],
                              [  6.94572764,  13.06310252,   1.0195625 ],
                              [ 11.02397756,  13.06310252,   1.0195625 ],
                              [ 15.10222748,  13.06310252,   1.0195625 ],
                              [ 19.1804774 ,  13.06310252,   1.0195625 ],
                              [  8.9848526 ,  15.10222748,   1.0195625 ],
                              [ 13.06310252,  15.10222748,   1.0195625 ],
                              [ 17.14135244,  15.10222748,   1.0195625 ],
                              [  6.94572764,  17.14135244,   1.0195625 ],
                              [ 11.02397756,  17.14135244,   1.0195625 ],
                              [ 15.10222748,  17.14135244,   1.0195625 ],
                              [ 19.1804774 ,  17.14135244,   1.0195625 ],
                              [  8.9848526 ,  19.1804774 ,   1.0195625 ],
                              [ 13.06310252,  19.1804774 ,   1.0195625 ],
                              [ 17.14135244,  19.1804774 ,   1.0195625 ],
                              [  6.94572764,   6.94572764,   3.0586875 ],
                              [ 11.02397756,   6.94572764,   3.0586875 ],
                              [ 15.10222748,   6.94572764,   3.0586875 ],
                              [ 19.1804774 ,   6.94572764,   3.0586875 ],
                              [  8.9848526 ,   8.9848526 ,   3.0586875 ],
                              [ 13.06310252,   8.9848526 ,   3.0586875 ],
                              [ 17.14135244,   8.9848526 ,   3.0586875 ],
                              [  6.94572764,  11.02397756,   3.0586875 ],
                              [ 11.02397756,  11.02397756,   3.0586875 ],
                              [ 15.10222748,  11.02397756,   3.0586875 ],
                              [ 19.1804774 ,  11.02397756,   3.0586875 ],
                              [  8.9848526 ,  13.06310252,   3.0586875 ],
                              [ 13.06310252,  13.06310252,   3.0586875 ],
                              [ 17.14135244,  13.06310252,   3.0586875 ],
                              [  6.94572764,  15.10222748,   3.0586875 ],
                              [ 11.02397756,  15.10222748,   3.0586875 ],
                              [ 15.10222748,  15.10222748,   3.0586875 ],
                              [ 19.1804774 ,  15.10222748,   3.0586875 ],
                              [  8.9848526 ,  17.14135244,   3.0586875 ],
                              [ 13.06310252,  17.14135244,   3.0586875 ],
                              [ 17.14135244,  17.14135244,   3.0586875 ],
                              [  6.94572764,  19.1804774 ,   3.0586875 ],
                              [ 11.02397756,  19.1804774 ,   3.0586875 ],
                              [ 15.10222748,  19.1804774 ,   3.0586875 ],
                              [ 19.1804774 ,  19.1804774 ,   3.0586875 ],
                              [  8.9848526 ,   6.94572764,   5.0978125 ],
                              [ 13.06310252,   6.94572764,   5.0978125 ],
                              [ 17.14135244,   6.94572764,   5.0978125 ],
                              [  6.94572764,   8.9848526 ,   5.0978125 ],
                              [ 11.02397756,   8.9848526 ,   5.0978125 ],
                              [ 15.10222748,   8.9848526 ,   5.0978125 ],
                              [ 19.1804774 ,   8.9848526 ,   5.0978125 ],
                              [  8.9848526 ,  11.02397756,   5.0978125 ],
                              [ 13.06310252,  11.02397756,   5.0978125 ],
                              [ 17.14135244,  11.02397756,   5.0978125 ],
                              [  6.94572764,  13.06310252,   5.0978125 ],
                              [ 11.02397756,  13.06310252,   5.0978125 ],
                              [ 15.10222748,  13.06310252,   5.0978125 ],
                              [ 19.1804774 ,  13.06310252,   5.0978125 ],
                              [  8.9848526 ,  15.10222748,   5.0978125 ],
                              [ 13.06310252,  15.10222748,   5.0978125 ],
                              [ 17.14135244,  15.10222748,   5.0978125 ],
                              [  6.94572764,  17.14135244,   5.0978125 ],
                              [ 11.02397756,  17.14135244,   5.0978125 ],
                              [ 15.10222748,  17.14135244,   5.0978125 ],
                              [ 19.1804774 ,  17.14135244,   5.0978125 ],
                              [  8.9848526 ,  19.1804774 ,   5.0978125 ],
                              [ 13.06310252,  19.1804774 ,   5.0978125 ],
                              [ 17.14135244,  19.1804774 ,   5.0978125 ],
                              [  6.94572764,   6.94572764,   7.1369375 ],
                              [ 11.02397756,   6.94572764,   7.1369375 ],
                              [ 15.10222748,   6.94572764,   7.1369375 ],
                              [ 19.1804774 ,   6.94572764,   7.1369375 ],
                              [  8.9848526 ,   8.9848526 ,   7.1369375 ],
                              [ 13.06310252,   8.9848526 ,   7.1369375 ],
                              [ 17.14135244,   8.9848526 ,   7.1369375 ],
                              [  6.94572764,  11.02397756,   7.1369375 ],
                              [ 11.02397756,  11.02397756,   7.1369375 ],
                              [ 15.10222748,  11.02397756,   7.1369375 ],
                              [ 19.1804774 ,  11.02397756,   7.1369375 ],
                              [  8.9848526 ,  13.06310252,   7.1369375 ],
                              [ 13.06310252,  13.06310252,   7.1369375 ],
                              [ 17.14135244,  13.06310252,   7.1369375 ],
                              [  6.94572764,  15.10222748,   7.1369375 ],
                              [ 11.02397756,  15.10222748,   7.1369375 ],
                              [ 15.10222748,  15.10222748,   7.1369375 ],
                              [ 19.1804774 ,  15.10222748,   7.1369375 ],
                              [  8.9848526 ,  17.14135244,   7.1369375 ],
                              [ 13.06310252,  17.14135244,   7.1369375 ],
                              [ 17.14135244,  17.14135244,   7.1369375 ],
                              [  6.94572764,  19.1804774 ,   7.1369375 ],
                              [ 11.02397756,  19.1804774 ,   7.1369375 ],
                              [ 15.10222748,  19.1804774 ,   7.1369375 ],
                              [ 19.1804774 ,  19.1804774 ,   7.1369375 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

