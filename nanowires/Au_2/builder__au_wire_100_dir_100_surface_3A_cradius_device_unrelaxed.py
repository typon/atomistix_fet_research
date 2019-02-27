# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [9.06844024492, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.06844024492, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 2.49509509,  2.49509509,  1.0195625 ],
                              [ 6.57334515,  2.49509509,  1.0195625 ],
                              [ 4.53422012,  4.53422012,  1.0195625 ],
                              [ 2.49509509,  6.57334515,  1.0195625 ],
                              [ 6.57334515,  6.57334515,  1.0195625 ],
                              [ 4.53422012,  2.49509509,  3.0586875 ],
                              [ 2.49509509,  4.53422012,  3.0586875 ],
                              [ 6.57334515,  4.53422012,  3.0586875 ],
                              [ 4.53422012,  6.57334515,  3.0586875 ]]*Angstrom

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
vector_a = [9.06844024492, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.06844024492, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 2.49509509,  2.49509509,  1.0195625 ],
                               [ 6.57334515,  2.49509509,  1.0195625 ],
                               [ 4.53422012,  4.53422012,  1.0195625 ],
                               [ 2.49509509,  6.57334515,  1.0195625 ],
                               [ 6.57334515,  6.57334515,  1.0195625 ],
                               [ 4.53422012,  2.49509509,  3.0586875 ],
                               [ 2.49509509,  4.53422012,  3.0586875 ],
                               [ 6.57334515,  4.53422012,  3.0586875 ],
                               [ 4.53422012,  6.57334515,  3.0586875 ]]*Angstrom

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
vector_a = [9.06844024492, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.06844024492, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 2.49509509,  2.49509509,  1.0195625 ],
                              [ 6.57334515,  2.49509509,  1.0195625 ],
                              [ 4.53422012,  4.53422012,  1.0195625 ],
                              [ 2.49509509,  6.57334515,  1.0195625 ],
                              [ 6.57334515,  6.57334515,  1.0195625 ],
                              [ 4.53422012,  2.49509509,  3.0586875 ],
                              [ 2.49509509,  4.53422012,  3.0586875 ],
                              [ 6.57334515,  4.53422012,  3.0586875 ],
                              [ 4.53422012,  6.57334515,  3.0586875 ],
                              [ 2.49509509,  2.49509509,  5.0978125 ],
                              [ 6.57334515,  2.49509509,  5.0978125 ],
                              [ 4.53422012,  4.53422012,  5.0978125 ],
                              [ 2.49509509,  6.57334515,  5.0978125 ],
                              [ 6.57334515,  6.57334515,  5.0978125 ],
                              [ 4.53422012,  2.49509509,  7.1369375 ],
                              [ 2.49509509,  4.53422012,  7.1369375 ],
                              [ 6.57334515,  4.53422012,  7.1369375 ],
                              [ 4.53422012,  6.57334515,  7.1369375 ]]*Angstrom

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


