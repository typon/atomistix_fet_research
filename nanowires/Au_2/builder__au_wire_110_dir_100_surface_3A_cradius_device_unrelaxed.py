# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [9.03334676493, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.03334676493, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.76751646075]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 2.47754838,  3.07479424,  0.72093956],
                              [ 6.55579839,  3.07479424,  0.72093956],
                              [ 2.47754838,  5.95855253,  0.72093956],
                              [ 6.55579839,  5.95855253,  0.72093956],
                              [ 4.51667338,  1.63291519,  2.16281867],
                              [ 4.51667338,  4.51667338,  2.16281867],
                              [ 4.51667338,  7.40043158,  2.16281867],
                              [ 2.47754838,  3.07479424,  3.60469779],
                              [ 6.55579839,  3.07479424,  3.60469779],
                              [ 2.47754838,  5.95855253,  3.60469779],
                              [ 6.55579839,  5.95855253,  3.60469779],
                              [ 4.51667338,  4.51667338,  5.0465769 ]]*Angstrom

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
vector_a = [9.03334676493, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.03334676493, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.76751646075]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 2.47754838,  3.07479424,  0.72093956],
                               [ 6.55579839,  3.07479424,  0.72093956],
                               [ 2.47754838,  5.95855253,  0.72093956],
                               [ 6.55579839,  5.95855253,  0.72093956],
                               [ 4.51667338,  1.63291519,  2.16281867],
                               [ 4.51667338,  4.51667338,  2.16281867],
                               [ 4.51667338,  7.40043158,  2.16281867],
                               [ 2.47754838,  3.07479424,  3.60469779],
                               [ 6.55579839,  3.07479424,  3.60469779],
                               [ 2.47754838,  5.95855253,  3.60469779],
                               [ 6.55579839,  5.95855253,  3.60469779],
                               [ 4.51667338,  4.51667338,  5.0465769 ]]*Angstrom

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
vector_a = [9.03334676493, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.03334676493, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5350329215]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[  2.47754838,   3.07479424,   0.72093956],
                              [  6.55579839,   3.07479424,   0.72093956],
                              [  2.47754838,   5.95855253,   0.72093956],
                              [  6.55579839,   5.95855253,   0.72093956],
                              [  4.51667338,   1.63291519,   2.16281867],
                              [  4.51667338,   4.51667338,   2.16281867],
                              [  4.51667338,   7.40043158,   2.16281867],
                              [  2.47754838,   3.07479424,   3.60469779],
                              [  6.55579839,   3.07479424,   3.60469779],
                              [  2.47754838,   5.95855253,   3.60469779],
                              [  6.55579839,   5.95855253,   3.60469779],
                              [  4.51667338,   4.51667338,   5.0465769 ],
                              [  2.47754838,   3.07479424,   6.48845602],
                              [  6.55579839,   3.07479424,   6.48845602],
                              [  2.47754838,   5.95855253,   6.48845602],
                              [  6.55579839,   5.95855253,   6.48845602],
                              [  4.51667338,   1.63291519,   7.93033513],
                              [  4.51667338,   4.51667338,   7.93033513],
                              [  4.51667338,   7.40043158,   7.93033513],
                              [  2.47754838,   3.07479424,   9.37221425],
                              [  6.55579839,   3.07479424,   9.37221425],
                              [  2.47754838,   5.95855253,   9.37221425],
                              [  6.55579839,   5.95855253,   9.37221425],
                              [  4.51667338,   4.51667338,  10.81409336]]*Angstrom

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


