# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [8.66707852768, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.66707852768, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.07663998448]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver]

# Define coordinates
left_electrode_coordinates = [[ 3.15409927,  3.15409927,  1.17944   ],
                              [ 5.94468426,  3.90183426,  1.17944   ],
                              [ 3.90183426,  5.94468426,  1.17944   ],
                              [ 3.58580427,  1.54295427,  3.53831999],
                              [ 6.37638926,  2.29068926,  3.53831999],
                              [ 1.54295427,  3.58580427,  3.53831999],
                              [ 4.33353926,  4.33353926,  3.53831999],
                              [ 7.12412426,  5.08127426,  3.53831999],
                              [ 2.29068926,  6.37638926,  3.53831999],
                              [ 5.08127426,  7.12412426,  3.53831999],
                              [ 4.76524427,  2.72239427,  5.89719999],
                              [ 2.72239427,  4.76524427,  5.89719999],
                              [ 5.51297926,  5.51297926,  5.89719999]]*Angstrom

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
vector_a = [8.66707852768, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.66707852768, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.07663998448]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver, Silver, Silver, Silver, Silver]

# Define coordinates
right_electrode_coordinates = [[ 3.15409927,  3.15409927,  1.17944   ],
                               [ 5.94468426,  3.90183426,  1.17944   ],
                               [ 3.90183426,  5.94468426,  1.17944   ],
                               [ 3.58580427,  1.54295427,  3.53831999],
                               [ 6.37638926,  2.29068926,  3.53831999],
                               [ 1.54295427,  3.58580427,  3.53831999],
                               [ 4.33353926,  4.33353926,  3.53831999],
                               [ 7.12412426,  5.08127426,  3.53831999],
                               [ 2.29068926,  6.37638926,  3.53831999],
                               [ 5.08127426,  7.12412426,  3.53831999],
                               [ 4.76524427,  2.72239427,  5.89719999],
                               [ 2.72239427,  4.76524427,  5.89719999],
                               [ 5.51297926,  5.51297926,  5.89719999]]*Angstrom

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
vector_a = [8.66707852768, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.66707852768, 0.0]*Angstrom
vector_c = [0.0, 0.0, 14.153279969]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver]

# Define coordinates
central_region_coordinates = [[  3.15409927,   3.15409927,   1.17944   ],
                              [  5.94468426,   3.90183426,   1.17944   ],
                              [  3.90183426,   5.94468426,   1.17944   ],
                              [  3.58580427,   1.54295427,   3.53831999],
                              [  6.37638926,   2.29068926,   3.53831999],
                              [  1.54295427,   3.58580427,   3.53831999],
                              [  4.33353926,   4.33353926,   3.53831999],
                              [  7.12412426,   5.08127426,   3.53831999],
                              [  2.29068926,   6.37638926,   3.53831999],
                              [  5.08127426,   7.12412426,   3.53831999],
                              [  4.76524427,   2.72239427,   5.89719999],
                              [  2.72239427,   4.76524427,   5.89719999],
                              [  5.51297926,   5.51297926,   5.89719999],
                              [  3.15409927,   3.15409927,   8.25607998],
                              [  5.94468426,   3.90183426,   8.25607998],
                              [  3.90183426,   5.94468426,   8.25607998],
                              [  3.58580427,   1.54295427,  10.61495998],
                              [  6.37638926,   2.29068926,  10.61495998],
                              [  1.54295427,   3.58580427,  10.61495998],
                              [  4.33353926,   4.33353926,  10.61495998],
                              [  7.12412426,   5.08127426,  10.61495998],
                              [  2.29068926,   6.37638926,  10.61495998],
                              [  5.08127426,   7.12412426,  10.61495998],
                              [  4.76524427,   2.72239427,  12.97383997],
                              [  2.72239427,   4.76524427,  12.97383997],
                              [  5.51297926,   5.51297926,  12.97383997]]*Angstrom

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
    GGABasis.Silver_DoubleZetaPolarized,
    ]

