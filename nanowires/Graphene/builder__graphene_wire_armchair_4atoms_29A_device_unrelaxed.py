# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 13.6915025657, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon]

# Define coordinates
left_electrode_coordinates = [[ 5.        ,  6.23050089,  0.71043001],
                              [ 5.        ,  8.69150261,  0.71043001],
                              [ 5.        ,  4.05603274,  0.87586028],
                              [ 5.        ,  9.63546982,  1.25542972],
                              [ 5.        ,  4.99999996,  1.42085999],
                              [ 5.        ,  7.46100168,  1.42085999],
                              [ 5.        ,  4.99999996,  2.84172001],
                              [ 5.        ,  7.46100168,  2.84172001],
                              [ 5.        ,  9.63546982,  3.00715028],
                              [ 5.        ,  4.05603274,  3.38671972],
                              [ 5.        ,  6.23050089,  3.55214999],
                              [ 5.        ,  8.69150261,  3.55214999],
                              [ 5.        ,  6.23050089,  4.97301001],
                              [ 5.        ,  8.69150261,  4.97301001],
                              [ 5.        ,  4.05603274,  5.13844028],
                              [ 5.        ,  9.63546982,  5.51800972],
                              [ 5.        ,  4.99999996,  5.68343999],
                              [ 5.        ,  7.46100168,  5.68343999],
                              [ 5.        ,  4.99999996,  7.10430001],
                              [ 5.        ,  7.46100168,  7.10430001],
                              [ 5.        ,  9.63546982,  7.26973028],
                              [ 5.        ,  4.05603274,  7.64929972],
                              [ 5.        ,  6.23050089,  7.81472999],
                              [ 5.        ,  8.69150261,  7.81472999]]*Angstrom

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
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 13.6915025657, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                            Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                            Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                            Hydrogen, Carbon, Carbon]

# Define coordinates
right_electrode_coordinates = [[ 5.        ,  6.23050089,  0.71043001],
                               [ 5.        ,  8.69150261,  0.71043001],
                               [ 5.        ,  4.05603274,  0.87586028],
                               [ 5.        ,  9.63546982,  1.25542972],
                               [ 5.        ,  4.99999996,  1.42085999],
                               [ 5.        ,  7.46100168,  1.42085999],
                               [ 5.        ,  4.99999996,  2.84172001],
                               [ 5.        ,  7.46100168,  2.84172001],
                               [ 5.        ,  9.63546982,  3.00715028],
                               [ 5.        ,  4.05603274,  3.38671972],
                               [ 5.        ,  6.23050089,  3.55214999],
                               [ 5.        ,  8.69150261,  3.55214999],
                               [ 5.        ,  6.23050089,  4.97301001],
                               [ 5.        ,  8.69150261,  4.97301001],
                               [ 5.        ,  4.05603274,  5.13844028],
                               [ 5.        ,  9.63546982,  5.51800972],
                               [ 5.        ,  4.99999996,  5.68343999],
                               [ 5.        ,  7.46100168,  5.68343999],
                               [ 5.        ,  4.99999996,  7.10430001],
                               [ 5.        ,  7.46100168,  7.10430001],
                               [ 5.        ,  9.63546982,  7.26973028],
                               [ 5.        ,  4.05603274,  7.64929972],
                               [ 5.        ,  6.23050089,  7.81472999],
                               [ 5.        ,  8.69150261,  7.81472999]]*Angstrom

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
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 13.6915025657, 0.0]*Angstrom
vector_c = [0.0, 0.0, 29.83806]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon,
                           Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon]

# Define coordinates
central_region_coordinates = [[  5.        ,   6.23050089,   0.71043001],
                              [  5.        ,   8.69150261,   0.71043001],
                              [  5.        ,   4.05603274,   0.87586028],
                              [  5.        ,   9.63546982,   1.25542972],
                              [  5.        ,   4.99999996,   1.42085999],
                              [  5.        ,   7.46100168,   1.42085999],
                              [  5.        ,   4.99999996,   2.84172001],
                              [  5.        ,   7.46100168,   2.84172001],
                              [  5.        ,   9.63546982,   3.00715028],
                              [  5.        ,   4.05603274,   3.38671972],
                              [  5.        ,   6.23050089,   3.55214999],
                              [  5.        ,   8.69150261,   3.55214999],
                              [  5.        ,   6.23050089,   4.97301001],
                              [  5.        ,   8.69150261,   4.97301001],
                              [  5.        ,   4.05603274,   5.13844028],
                              [  5.        ,   9.63546982,   5.51800972],
                              [  5.        ,   4.99999996,   5.68343999],
                              [  5.        ,   7.46100168,   5.68343999],
                              [  5.        ,   4.99999996,   7.10430001],
                              [  5.        ,   7.46100168,   7.10430001],
                              [  5.        ,   9.63546982,   7.26973028],
                              [  5.        ,   4.05603274,   7.64929972],
                              [  5.        ,   6.23050089,   7.81472999],
                              [  5.        ,   8.69150261,   7.81472999],
                              [  5.        ,   6.23050089,   9.23559001],
                              [  5.        ,   8.69150261,   9.23559001],
                              [  5.        ,   4.05603274,   9.40102028],
                              [  5.        ,   9.63546982,   9.78058972],
                              [  5.        ,   4.99999996,   9.94601999],
                              [  5.        ,   7.46100168,   9.94601999],
                              [  5.        ,   4.99999996,  11.36688001],
                              [  5.        ,   7.46100168,  11.36688001],
                              [  5.        ,   9.63546982,  11.53231028],
                              [  5.        ,   4.05603274,  11.91187972],
                              [  5.        ,   6.23050089,  12.07730999],
                              [  5.        ,   8.69150261,  12.07730999],
                              [  5.        ,   6.23050089,  13.49817001],
                              [  5.        ,   8.69150261,  13.49817001],
                              [  5.        ,   4.05603274,  13.66360028],
                              [  5.        ,   9.63546982,  14.04316972],
                              [  5.        ,   4.99999996,  14.20859999],
                              [  5.        ,   7.46100168,  14.20859999],
                              [  5.        ,   4.99999996,  15.62946001],
                              [  5.        ,   7.46100168,  15.62946001],
                              [  5.        ,   9.63546982,  15.79489028],
                              [  5.        ,   4.05603274,  16.17445972],
                              [  5.        ,   6.23050089,  16.33988999],
                              [  5.        ,   8.69150261,  16.33988999],
                              [  5.        ,   6.23050089,  17.76075001],
                              [  5.        ,   8.69150261,  17.76075001],
                              [  5.        ,   4.05603274,  17.92618028],
                              [  5.        ,   9.63546982,  18.30574972],
                              [  5.        ,   4.99999996,  18.47117999],
                              [  5.        ,   7.46100168,  18.47117999],
                              [  5.        ,   4.99999996,  19.89204001],
                              [  5.        ,   7.46100168,  19.89204001],
                              [  5.        ,   9.63546982,  20.05747028],
                              [  5.        ,   4.05603274,  20.43703972],
                              [  5.        ,   6.23050089,  20.60246999],
                              [  5.        ,   8.69150261,  20.60246999],
                              [  5.        ,   6.23050089,  22.02333001],
                              [  5.        ,   8.69150261,  22.02333001],
                              [  5.        ,   4.05603274,  22.18876028],
                              [  5.        ,   9.63546982,  22.56832972],
                              [  5.        ,   4.99999996,  22.73375999],
                              [  5.        ,   7.46100168,  22.73375999],
                              [  5.        ,   4.99999996,  24.15462001],
                              [  5.        ,   7.46100168,  24.15462001],
                              [  5.        ,   9.63546982,  24.32005028],
                              [  5.        ,   4.05603274,  24.69961972],
                              [  5.        ,   6.23050089,  24.86504999],
                              [  5.        ,   8.69150261,  24.86504999],
                              [  5.        ,   6.23050089,  26.28591001],
                              [  5.        ,   8.69150261,  26.28591001],
                              [  5.        ,   4.05603274,  26.45134028],
                              [  5.        ,   9.63546982,  26.83090972],
                              [  5.        ,   4.99999996,  26.99633999],
                              [  5.        ,   7.46100168,  26.99633999],
                              [  5.        ,   4.99999996,  28.41720001],
                              [  5.        ,   7.46100168,  28.41720001],
                              [  5.        ,   9.63546982,  28.58263028],
                              [  5.        ,   4.05603274,  28.96219972],
                              [  5.        ,   6.23050089,  29.12762999],
                              [  5.        ,   8.69150261,  29.12762999]]*Angstrom

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
    GGABasis.Carbon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]

