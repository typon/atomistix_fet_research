# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [12.23475, 0.0, 0.0]*Angstrom
vector_b = [6.117375, 6.117375, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ -0.       ,  -0.       ,   1.0195625],
                              [  4.07825  ,  -0.       ,   1.0195625],
                              [  8.1565   ,  -0.       ,   1.0195625],
                              [  2.039125 ,   2.039125 ,   1.0195625],
                              [  6.117375 ,   2.039125 ,   1.0195625],
                              [ 10.195625 ,   2.039125 ,   1.0195625],
                              [  4.07825  ,   4.07825  ,   1.0195625],
                              [  8.1565   ,   4.07825  ,   1.0195625],
                              [ 12.23475  ,   4.07825  ,   1.0195625],
                              [  2.039125 ,   0.       ,   3.0586875],
                              [  6.117375 ,  -0.       ,   3.0586875],
                              [ 10.195625 ,  -0.       ,   3.0586875],
                              [  4.07825  ,   2.039125 ,   3.0586875],
                              [  8.1565   ,   2.039125 ,   3.0586875],
                              [ 12.23475  ,   2.039125 ,   3.0586875],
                              [  6.117375 ,   4.07825  ,   3.0586875],
                              [ 10.195625 ,   4.07825  ,   3.0586875],
                              [ 14.273875 ,   4.07825  ,   3.0586875]]*Angstrom

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
vector_a = [12.23475, 0.0, 0.0]*Angstrom
vector_b = [6.117375, 6.117375, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.42971994036]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium,
                            Hafnium, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen]

# Define coordinates
right_electrode_coordinates = [[ -0.        ,  -0.        ,   0.73828666],
                               [  6.117375  ,   0.        ,   0.73828666],
                               [  3.0586875 ,   1.52934375,   0.73828666],
                               [  9.1760625 ,   1.52934375,   0.73828666],
                               [  6.117375  ,   3.0586875 ,   0.73828666],
                               [ 12.23475   ,   3.0586875 ,   0.73828666],
                               [  9.1760625 ,   4.58803125,   0.73828666],
                               [ 15.2934375 ,   4.58803125,   0.73828666],
                               [  2.039125  ,  -0.        ,   1.47657331],
                               [  8.1565    ,   0.        ,   1.47657331],
                               [  5.0978125 ,   1.52934375,   1.47657331],
                               [ 11.2151875 ,   1.52934375,   1.47657331],
                               [  8.1565    ,   3.0586875 ,   1.47657331],
                               [ 14.273875  ,   3.0586875 ,   1.47657331],
                               [  5.0978125 ,   4.58803125,   1.47657331],
                               [ 11.2151875 ,   4.58803125,   1.47657331],
                               [  4.07825   ,  -0.        ,   2.21485997],
                               [ 10.195625  ,  -0.        ,   2.21485997],
                               [  7.1369375 ,   1.52934375,   2.21485997],
                               [ 13.2543125 ,   1.52934375,   2.21485997],
                               [  4.07825   ,   3.0586875 ,   2.21485997],
                               [ 10.195625  ,   3.0586875 ,   2.21485997],
                               [  7.1369375 ,   4.58803125,   2.21485997],
                               [ 13.2543125 ,   4.58803125,   2.21485997],
                               [  2.039125  ,  -0.        ,   3.69143328],
                               [  8.1565    ,   0.        ,   3.69143328],
                               [  5.0978125 ,   1.52934375,   3.69143328],
                               [ 11.2151875 ,   1.52934375,   3.69143328],
                               [  8.1565    ,   3.0586875 ,   3.69143328],
                               [ 14.273875  ,   3.0586875 ,   3.69143328],
                               [  5.0978125 ,   4.58803125,   3.69143328],
                               [ 11.2151875 ,   4.58803125,   3.69143328]]*Angstrom

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
vector_a = [12.23475, 0.0, 0.0]*Angstrom
vector_b = [6.117375, 6.117375, 0.0]*Angstrom
vector_c = [0.0, 0.0, 17.0823557538]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Hafnium, Hafnium, Hafnium, Hafnium,
                           Hafnium, Hafnium, Hafnium, Hafnium, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Hafnium, Hafnium, Hafnium,
                           Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
central_region_coordinates = [[ -0.        ,  -0.        ,   1.0195625 ],
                              [  4.07825   ,  -0.        ,   1.0195625 ],
                              [  8.1565    ,  -0.        ,   1.0195625 ],
                              [  2.039125  ,   2.039125  ,   1.0195625 ],
                              [  6.117375  ,   2.039125  ,   1.0195625 ],
                              [ 10.195625  ,   2.039125  ,   1.0195625 ],
                              [  4.07825   ,   4.07825   ,   1.0195625 ],
                              [  8.1565    ,   4.07825   ,   1.0195625 ],
                              [ 12.23475   ,   4.07825   ,   1.0195625 ],
                              [  2.039125  ,   0.        ,   3.0586875 ],
                              [  6.117375  ,  -0.        ,   3.0586875 ],
                              [ 10.195625  ,  -0.        ,   3.0586875 ],
                              [  4.07825   ,   2.039125  ,   3.0586875 ],
                              [  8.1565    ,   2.039125  ,   3.0586875 ],
                              [ 12.23475   ,   2.039125  ,   3.0586875 ],
                              [  6.117375  ,   4.07825   ,   3.0586875 ],
                              [ 10.195625  ,   4.07825   ,   3.0586875 ],
                              [ 14.273875  ,   4.07825   ,   3.0586875 ],
                              [ -0.        ,  -0.        ,   5.0978125 ],
                              [  4.07825   ,  -0.        ,   5.0978125 ],
                              [  8.1565    ,  -0.        ,   5.0978125 ],
                              [  2.039125  ,   2.039125  ,   5.0978125 ],
                              [  6.117375  ,   2.039125  ,   5.0978125 ],
                              [ 10.195625  ,   2.039125  ,   5.0978125 ],
                              [  4.07825   ,   4.07825   ,   5.0978125 ],
                              [  8.1565    ,   4.07825   ,   5.0978125 ],
                              [ 12.23475   ,   4.07825   ,   5.0978125 ],
                              [  2.039125  ,   0.        ,   7.1369375 ],
                              [  6.117375  ,  -0.        ,   7.1369375 ],
                              [ 10.195625  ,  -0.        ,   7.1369375 ],
                              [  4.07825   ,   2.039125  ,   7.1369375 ],
                              [  8.1565    ,   2.039125  ,   7.1369375 ],
                              [ 12.23475   ,   2.039125  ,   7.1369375 ],
                              [  6.117375  ,   4.07825   ,   7.1369375 ],
                              [ 10.195625  ,   4.07825   ,   7.1369375 ],
                              [ 14.273875  ,   4.07825   ,   7.1369375 ],
                              [ -0.        ,  -0.        ,   9.1760625 ],
                              [  4.07825   ,  -0.        ,   9.1760625 ],
                              [  8.1565    ,  -0.        ,   9.1760625 ],
                              [  2.039125  ,   2.039125  ,   9.1760625 ],
                              [  6.117375  ,   2.039125  ,   9.1760625 ],
                              [ 10.195625  ,   2.039125  ,   9.1760625 ],
                              [  4.07825   ,   4.07825   ,   9.1760625 ],
                              [  8.1565    ,   4.07825   ,   9.1760625 ],
                              [ 12.23475   ,   4.07825   ,   9.1760625 ],
                              [ -0.        ,  -0.        ,  11.1760625 ],
                              [  6.117375  ,   0.        ,  11.1760625 ],
                              [  3.0586875 ,   1.52934375,  11.1760625 ],
                              [  9.1760625 ,   1.52934375,  11.1760625 ],
                              [  6.117375  ,   3.0586875 ,  11.1760625 ],
                              [ 12.23475   ,   3.0586875 ,  11.1760625 ],
                              [  9.1760625 ,   4.58803125,  11.1760625 ],
                              [ 15.2934375 ,   4.58803125,  11.1760625 ],
                              [  2.039125  ,  -0.        ,  11.91434916],
                              [  8.1565    ,   0.        ,  11.91434916],
                              [  5.0978125 ,   1.52934375,  11.91434916],
                              [ 11.2151875 ,   1.52934375,  11.91434916],
                              [  8.1565    ,   3.0586875 ,  11.91434916],
                              [ 14.273875  ,   3.0586875 ,  11.91434916],
                              [  5.0978125 ,   4.58803125,  11.91434916],
                              [ 11.2151875 ,   4.58803125,  11.91434916],
                              [ -0.        ,  -0.        ,  13.39092247],
                              [  6.117375  ,   0.        ,  13.39092247],
                              [  3.0586875 ,   1.52934375,  13.39092247],
                              [  9.1760625 ,   1.52934375,  13.39092247],
                              [  6.117375  ,   3.0586875 ,  13.39092247],
                              [ 12.23475   ,   3.0586875 ,  13.39092247],
                              [  9.1760625 ,   4.58803125,  13.39092247],
                              [ 15.2934375 ,   4.58803125,  13.39092247],
                              [  2.039125  ,  -0.        ,  14.12920913],
                              [  8.1565    ,   0.        ,  14.12920913],
                              [  5.0978125 ,   1.52934375,  14.12920913],
                              [ 11.2151875 ,   1.52934375,  14.12920913],
                              [  8.1565    ,   3.0586875 ,  14.12920913],
                              [ 14.273875  ,   3.0586875 ,  14.12920913],
                              [  5.0978125 ,   4.58803125,  14.12920913],
                              [ 11.2151875 ,   4.58803125,  14.12920913],
                              [  4.07825   ,  -0.        ,  14.86749578],
                              [ 10.195625  ,  -0.        ,  14.86749578],
                              [  7.1369375 ,   1.52934375,  14.86749578],
                              [ 13.2543125 ,   1.52934375,  14.86749578],
                              [  4.07825   ,   3.0586875 ,  14.86749578],
                              [ 10.195625  ,   3.0586875 ,  14.86749578],
                              [  7.1369375 ,   4.58803125,  14.86749578],
                              [ 13.2543125 ,   4.58803125,  14.86749578],
                              [  2.039125  ,  -0.        ,  16.3440691 ],
                              [  8.1565    ,   0.        ,  16.3440691 ],
                              [  5.0978125 ,   1.52934375,  16.3440691 ],
                              [ 11.2151875 ,   1.52934375,  16.3440691 ],
                              [  8.1565    ,   3.0586875 ,  16.3440691 ],
                              [ 14.273875  ,   3.0586875 ,  16.3440691 ],
                              [  5.0978125 ,   4.58803125,  16.3440691 ],
                              [ 11.2151875 ,   4.58803125,  16.3440691 ]]*Angstrom

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

