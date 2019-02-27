# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [9.04984855697, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.04984855697, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88902617589]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silver, Silver, Silver, Silver, Silver]

# Define coordinates
left_electrode_coordinates = [[ 4.52492428,  4.52492428,  0.72225654],
                              [ 2.48207428,  3.08041119,  2.16676963],
                              [ 6.56777428,  3.08041119,  2.16676963],
                              [ 2.48207428,  5.96943737,  2.16676963],
                              [ 6.56777428,  5.96943737,  2.16676963]]*Angstrom

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
vector_a = [9.04984855697, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.04984855697, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88902617589]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
right_electrode_coordinates = [[ 4.52492428,  1.6358981 ,  0.72225654],
                               [ 4.52492428,  4.52492428,  0.72225654],
                               [ 4.52492428,  7.41395045,  0.72225654],
                               [ 2.48207428,  3.08041119,  2.16676963],
                               [ 6.56777428,  3.08041119,  2.16676963],
                               [ 2.48207428,  5.96943737,  2.16676963],
                               [ 6.56777428,  5.96943737,  2.16676963]]*Angstrom

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
vector_a = [9.04984855697, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.04984855697, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5561047036]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
central_region_coordinates = [[  4.52492428,   4.52492428,   0.72225654],
                              [  2.48207428,   3.08041119,   2.16676963],
                              [  6.56777428,   3.08041119,   2.16676963],
                              [  2.48207428,   5.96943737,   2.16676963],
                              [  6.56777428,   5.96943737,   2.16676963],
                              [  4.52492428,   1.6358981 ,   3.61128272],
                              [  4.52492428,   4.52492428,   3.61128272],
                              [  4.52492428,   7.41395045,   3.61128272],
                              [  2.48207428,   3.08041119,   5.05579581],
                              [  6.56777428,   3.08041119,   5.05579581],
                              [  2.48207428,   5.96943737,   5.05579581],
                              [  6.56777428,   5.96943737,   5.05579581],
                              [  4.52492428,   4.52492428,   6.5003089 ],
                              [  2.48207428,   3.08041119,   7.94482198],
                              [  6.56777428,   3.08041119,   7.94482198],
                              [  2.48207428,   5.96943737,   7.94482198],
                              [  6.56777428,   5.96943737,   7.94482198],
                              [  4.52492428,   1.6358981 ,   9.38933507],
                              [  4.52492428,   4.52492428,   9.38933507],
                              [  4.52492428,   7.41395045,   9.38933507],
                              [  2.48207428,   3.08041119,  10.83384816],
                              [  6.56777428,   3.08041119,  10.83384816],
                              [  2.48207428,   5.96943737,  10.83384816],
                              [  6.56777428,   5.96943737,  10.83384816]]*Angstrom

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

