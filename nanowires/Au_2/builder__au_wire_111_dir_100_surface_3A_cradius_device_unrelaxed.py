# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.65127469112, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 3.14834801,  3.14834801,  1.17728939],
                              [ 5.93384451,  3.89471952,  1.17728939],
                              [ 3.89471952,  5.93384451,  1.17728939],
                              [ 3.57926575,  1.54014075,  3.5318681 ],
                              [ 6.36476234,  2.28651235,  3.5318681 ],
                              [ 1.54014075,  3.57926575,  3.5318681 ],
                              [ 4.32563735,  4.32563735,  3.5318681 ],
                              [ 7.11113394,  5.07200894,  3.5318681 ],
                              [ 2.28651235,  6.36476234,  3.5318681 ],
                              [ 5.07200894,  7.11113394,  3.5318681 ],
                              [ 4.75655518,  2.71743018,  5.88644681],
                              [ 2.71743018,  4.75655518,  5.88644681],
                              [ 5.50292668,  5.50292668,  5.88644681]]*Angstrom

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
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.65127469112, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 3.14834801,  3.14834801,  1.17728939],
                               [ 5.93384451,  3.89471952,  1.17728939],
                               [ 3.89471952,  5.93384451,  1.17728939],
                               [ 3.57926575,  1.54014075,  3.5318681 ],
                               [ 6.36476234,  2.28651235,  3.5318681 ],
                               [ 1.54014075,  3.57926575,  3.5318681 ],
                               [ 4.32563735,  4.32563735,  3.5318681 ],
                               [ 7.11113394,  5.07200894,  3.5318681 ],
                               [ 2.28651235,  6.36476234,  3.5318681 ],
                               [ 5.07200894,  7.11113394,  3.5318681 ],
                               [ 4.75655518,  2.71743018,  5.88644681],
                               [ 2.71743018,  4.75655518,  5.88644681],
                               [ 5.50292668,  5.50292668,  5.88644681]]*Angstrom

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
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.65127469112, 0.0]*Angstrom
vector_c = [0.0, 0.0, 14.1274724119]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[  3.14834801,   3.14834801,   1.17728939],
                              [  5.93384451,   3.89471952,   1.17728939],
                              [  3.89471952,   5.93384451,   1.17728939],
                              [  3.57926575,   1.54014075,   3.5318681 ],
                              [  6.36476234,   2.28651235,   3.5318681 ],
                              [  1.54014075,   3.57926575,   3.5318681 ],
                              [  4.32563735,   4.32563735,   3.5318681 ],
                              [  7.11113394,   5.07200894,   3.5318681 ],
                              [  2.28651235,   6.36476234,   3.5318681 ],
                              [  5.07200894,   7.11113394,   3.5318681 ],
                              [  4.75655518,   2.71743018,   5.88644681],
                              [  2.71743018,   4.75655518,   5.88644681],
                              [  5.50292668,   5.50292668,   5.88644681],
                              [  3.14834801,   3.14834801,   8.2410256 ],
                              [  5.93384451,   3.89471952,   8.2410256 ],
                              [  3.89471952,   5.93384451,   8.2410256 ],
                              [  3.57926575,   1.54014075,  10.59560431],
                              [  6.36476234,   2.28651235,  10.59560431],
                              [  1.54014075,   3.57926575,  10.59560431],
                              [  4.32563735,   4.32563735,  10.59560431],
                              [  7.11113394,   5.07200894,  10.59560431],
                              [  2.28651235,   6.36476234,  10.59560431],
                              [  5.07200894,   7.11113394,  10.59560431],
                              [  4.75655518,   2.71743018,  12.95018302],
                              [  2.71743018,   4.75655518,  12.95018302],
                              [  5.50292668,   5.50292668,  12.95018302]]*Angstrom

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


