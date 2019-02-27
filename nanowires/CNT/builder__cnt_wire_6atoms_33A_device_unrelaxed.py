# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [14.7001670461, 0.0, 0.0]*Angstrom
vector_b = [0.0, 14.7001670461, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
left_electrode_coordinates = [[ 7.35008352,  5.00000001,  0.71042989],
                              [ 5.31485142,  6.17504169,  0.71042989],
                              [ 9.38531562,  6.17504169,  0.71042989],
                              [ 5.31485142,  8.52512535,  0.71042989],
                              [ 9.38531562,  8.52512535,  0.71042989],
                              [ 7.35008352,  9.70016704,  0.71042989],
                              [ 6.17504169,  5.31485142,  1.42086011],
                              [ 8.52512535,  5.31485142,  1.42086011],
                              [ 5.00000001,  7.35008352,  1.42086011],
                              [ 9.70016704,  7.35008352,  1.42086011],
                              [ 6.17504169,  9.38531562,  1.42086011],
                              [ 8.52512535,  9.38531562,  1.42086011],
                              [ 6.17504169,  5.31485142,  2.84171989],
                              [ 8.52512535,  5.31485142,  2.84171989],
                              [ 5.00000001,  7.35008352,  2.84171989],
                              [ 9.70016704,  7.35008352,  2.84171989],
                              [ 6.17504169,  9.38531562,  2.84171989],
                              [ 8.52512535,  9.38531562,  2.84171989],
                              [ 7.35008352,  5.00000001,  3.55215011],
                              [ 5.31485142,  6.17504169,  3.55215011],
                              [ 9.38531562,  6.17504169,  3.55215011],
                              [ 5.31485142,  8.52512535,  3.55215011],
                              [ 9.38531562,  8.52512535,  3.55215011],
                              [ 7.35008352,  9.70016704,  3.55215011],
                              [ 7.35008352,  5.00000001,  4.97300989],
                              [ 5.31485142,  6.17504169,  4.97300989],
                              [ 9.38531562,  6.17504169,  4.97300989],
                              [ 5.31485142,  8.52512535,  4.97300989],
                              [ 9.38531562,  8.52512535,  4.97300989],
                              [ 7.35008352,  9.70016704,  4.97300989],
                              [ 6.17504169,  5.31485142,  5.68344011],
                              [ 8.52512535,  5.31485142,  5.68344011],
                              [ 5.00000001,  7.35008352,  5.68344011],
                              [ 9.70016704,  7.35008352,  5.68344011],
                              [ 6.17504169,  9.38531562,  5.68344011],
                              [ 8.52512535,  9.38531562,  5.68344011],
                              [ 6.17504169,  5.31485142,  7.10429989],
                              [ 8.52512535,  5.31485142,  7.10429989],
                              [ 5.00000001,  7.35008352,  7.10429989],
                              [ 9.70016704,  7.35008352,  7.10429989],
                              [ 6.17504169,  9.38531562,  7.10429989],
                              [ 8.52512535,  9.38531562,  7.10429989],
                              [ 7.35008352,  5.00000001,  7.81473011],
                              [ 5.31485142,  6.17504169,  7.81473011],
                              [ 9.38531562,  6.17504169,  7.81473011],
                              [ 5.31485142,  8.52512535,  7.81473011],
                              [ 9.38531562,  8.52512535,  7.81473011],
                              [ 7.35008352,  9.70016704,  7.81473011]]*Angstrom

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
vector_a = [14.7001670461, 0.0, 0.0]*Angstrom
vector_b = [0.0, 14.7001670461, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
right_electrode_coordinates = [[ 7.35008352,  5.00000001,  0.71042989],
                               [ 5.31485142,  6.17504169,  0.71042989],
                               [ 9.38531562,  6.17504169,  0.71042989],
                               [ 5.31485142,  8.52512535,  0.71042989],
                               [ 9.38531562,  8.52512535,  0.71042989],
                               [ 7.35008352,  9.70016704,  0.71042989],
                               [ 6.17504169,  5.31485142,  1.42086011],
                               [ 8.52512535,  5.31485142,  1.42086011],
                               [ 5.00000001,  7.35008352,  1.42086011],
                               [ 9.70016704,  7.35008352,  1.42086011],
                               [ 6.17504169,  9.38531562,  1.42086011],
                               [ 8.52512535,  9.38531562,  1.42086011],
                               [ 6.17504169,  5.31485142,  2.84171989],
                               [ 8.52512535,  5.31485142,  2.84171989],
                               [ 5.00000001,  7.35008352,  2.84171989],
                               [ 9.70016704,  7.35008352,  2.84171989],
                               [ 6.17504169,  9.38531562,  2.84171989],
                               [ 8.52512535,  9.38531562,  2.84171989],
                               [ 7.35008352,  5.00000001,  3.55215011],
                               [ 5.31485142,  6.17504169,  3.55215011],
                               [ 9.38531562,  6.17504169,  3.55215011],
                               [ 5.31485142,  8.52512535,  3.55215011],
                               [ 9.38531562,  8.52512535,  3.55215011],
                               [ 7.35008352,  9.70016704,  3.55215011],
                               [ 7.35008352,  5.00000001,  4.97300989],
                               [ 5.31485142,  6.17504169,  4.97300989],
                               [ 9.38531562,  6.17504169,  4.97300989],
                               [ 5.31485142,  8.52512535,  4.97300989],
                               [ 9.38531562,  8.52512535,  4.97300989],
                               [ 7.35008352,  9.70016704,  4.97300989],
                               [ 6.17504169,  5.31485142,  5.68344011],
                               [ 8.52512535,  5.31485142,  5.68344011],
                               [ 5.00000001,  7.35008352,  5.68344011],
                               [ 9.70016704,  7.35008352,  5.68344011],
                               [ 6.17504169,  9.38531562,  5.68344011],
                               [ 8.52512535,  9.38531562,  5.68344011],
                               [ 6.17504169,  5.31485142,  7.10429989],
                               [ 8.52512535,  5.31485142,  7.10429989],
                               [ 5.00000001,  7.35008352,  7.10429989],
                               [ 9.70016704,  7.35008352,  7.10429989],
                               [ 6.17504169,  9.38531562,  7.10429989],
                               [ 8.52512535,  9.38531562,  7.10429989],
                               [ 7.35008352,  5.00000001,  7.81473011],
                               [ 5.31485142,  6.17504169,  7.81473011],
                               [ 9.38531562,  6.17504169,  7.81473011],
                               [ 5.31485142,  8.52512535,  7.81473011],
                               [ 9.38531562,  8.52512535,  7.81473011],
                               [ 7.35008352,  9.70016704,  7.81473011]]*Angstrom

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
vector_a = [14.7001670461, 0.0, 0.0]*Angstrom
vector_b = [0.0, 14.7001670461, 0.0]*Angstrom
vector_c = [0.0, 0.0, 34.10064]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
central_region_coordinates = [[  7.35008352,   5.00000001,   0.71042989],
                              [  5.31485142,   6.17504169,   0.71042989],
                              [  9.38531562,   6.17504169,   0.71042989],
                              [  5.31485142,   8.52512535,   0.71042989],
                              [  9.38531562,   8.52512535,   0.71042989],
                              [  7.35008352,   9.70016704,   0.71042989],
                              [  6.17504169,   5.31485142,   1.42086011],
                              [  8.52512535,   5.31485142,   1.42086011],
                              [  5.00000001,   7.35008352,   1.42086011],
                              [  9.70016704,   7.35008352,   1.42086011],
                              [  6.17504169,   9.38531562,   1.42086011],
                              [  8.52512535,   9.38531562,   1.42086011],
                              [  6.17504169,   5.31485142,   2.84171989],
                              [  8.52512535,   5.31485142,   2.84171989],
                              [  5.00000001,   7.35008352,   2.84171989],
                              [  9.70016704,   7.35008352,   2.84171989],
                              [  6.17504169,   9.38531562,   2.84171989],
                              [  8.52512535,   9.38531562,   2.84171989],
                              [  7.35008352,   5.00000001,   3.55215011],
                              [  5.31485142,   6.17504169,   3.55215011],
                              [  9.38531562,   6.17504169,   3.55215011],
                              [  5.31485142,   8.52512535,   3.55215011],
                              [  9.38531562,   8.52512535,   3.55215011],
                              [  7.35008352,   9.70016704,   3.55215011],
                              [  7.35008352,   5.00000001,   4.97300989],
                              [  5.31485142,   6.17504169,   4.97300989],
                              [  9.38531562,   6.17504169,   4.97300989],
                              [  5.31485142,   8.52512535,   4.97300989],
                              [  9.38531562,   8.52512535,   4.97300989],
                              [  7.35008352,   9.70016704,   4.97300989],
                              [  6.17504169,   5.31485142,   5.68344011],
                              [  8.52512535,   5.31485142,   5.68344011],
                              [  5.00000001,   7.35008352,   5.68344011],
                              [  9.70016704,   7.35008352,   5.68344011],
                              [  6.17504169,   9.38531562,   5.68344011],
                              [  8.52512535,   9.38531562,   5.68344011],
                              [  6.17504169,   5.31485142,   7.10429989],
                              [  8.52512535,   5.31485142,   7.10429989],
                              [  5.00000001,   7.35008352,   7.10429989],
                              [  9.70016704,   7.35008352,   7.10429989],
                              [  6.17504169,   9.38531562,   7.10429989],
                              [  8.52512535,   9.38531562,   7.10429989],
                              [  7.35008352,   5.00000001,   7.81473011],
                              [  5.31485142,   6.17504169,   7.81473011],
                              [  9.38531562,   6.17504169,   7.81473011],
                              [  5.31485142,   8.52512535,   7.81473011],
                              [  9.38531562,   8.52512535,   7.81473011],
                              [  7.35008352,   9.70016704,   7.81473011],
                              [  7.35008352,   5.00000001,   9.23558989],
                              [  5.31485142,   6.17504169,   9.23558989],
                              [  9.38531562,   6.17504169,   9.23558989],
                              [  5.31485142,   8.52512535,   9.23558989],
                              [  9.38531562,   8.52512535,   9.23558989],
                              [  7.35008352,   9.70016704,   9.23558989],
                              [  6.17504169,   5.31485142,   9.94602011],
                              [  8.52512535,   5.31485142,   9.94602011],
                              [  5.00000001,   7.35008352,   9.94602011],
                              [  9.70016704,   7.35008352,   9.94602011],
                              [  6.17504169,   9.38531562,   9.94602011],
                              [  8.52512535,   9.38531562,   9.94602011],
                              [  6.17504169,   5.31485142,  11.36687989],
                              [  8.52512535,   5.31485142,  11.36687989],
                              [  5.00000001,   7.35008352,  11.36687989],
                              [  9.70016704,   7.35008352,  11.36687989],
                              [  6.17504169,   9.38531562,  11.36687989],
                              [  8.52512535,   9.38531562,  11.36687989],
                              [  7.35008352,   5.00000001,  12.07731011],
                              [  5.31485142,   6.17504169,  12.07731011],
                              [  9.38531562,   6.17504169,  12.07731011],
                              [  5.31485142,   8.52512535,  12.07731011],
                              [  9.38531562,   8.52512535,  12.07731011],
                              [  7.35008352,   9.70016704,  12.07731011],
                              [  7.35008352,   5.00000001,  13.49816989],
                              [  5.31485142,   6.17504169,  13.49816989],
                              [  9.38531562,   6.17504169,  13.49816989],
                              [  5.31485142,   8.52512535,  13.49816989],
                              [  9.38531562,   8.52512535,  13.49816989],
                              [  7.35008352,   9.70016704,  13.49816989],
                              [  6.17504169,   5.31485142,  14.20860011],
                              [  8.52512535,   5.31485142,  14.20860011],
                              [  5.00000001,   7.35008352,  14.20860011],
                              [  9.70016704,   7.35008352,  14.20860011],
                              [  6.17504169,   9.38531562,  14.20860011],
                              [  8.52512535,   9.38531562,  14.20860011],
                              [  6.17504169,   5.31485142,  15.62945989],
                              [  8.52512535,   5.31485142,  15.62945989],
                              [  5.00000001,   7.35008352,  15.62945989],
                              [  9.70016704,   7.35008352,  15.62945989],
                              [  6.17504169,   9.38531562,  15.62945989],
                              [  8.52512535,   9.38531562,  15.62945989],
                              [  7.35008352,   5.00000001,  16.33989011],
                              [  5.31485142,   6.17504169,  16.33989011],
                              [  9.38531562,   6.17504169,  16.33989011],
                              [  5.31485142,   8.52512535,  16.33989011],
                              [  9.38531562,   8.52512535,  16.33989011],
                              [  7.35008352,   9.70016704,  16.33989011],
                              [  7.35008352,   5.00000001,  17.76074989],
                              [  5.31485142,   6.17504169,  17.76074989],
                              [  9.38531562,   6.17504169,  17.76074989],
                              [  5.31485142,   8.52512535,  17.76074989],
                              [  9.38531562,   8.52512535,  17.76074989],
                              [  7.35008352,   9.70016704,  17.76074989],
                              [  6.17504169,   5.31485142,  18.47118011],
                              [  8.52512535,   5.31485142,  18.47118011],
                              [  5.00000001,   7.35008352,  18.47118011],
                              [  9.70016704,   7.35008352,  18.47118011],
                              [  6.17504169,   9.38531562,  18.47118011],
                              [  8.52512535,   9.38531562,  18.47118011],
                              [  6.17504169,   5.31485142,  19.89203989],
                              [  8.52512535,   5.31485142,  19.89203989],
                              [  5.00000001,   7.35008352,  19.89203989],
                              [  9.70016704,   7.35008352,  19.89203989],
                              [  6.17504169,   9.38531562,  19.89203989],
                              [  8.52512535,   9.38531562,  19.89203989],
                              [  7.35008352,   5.00000001,  20.60247011],
                              [  5.31485142,   6.17504169,  20.60247011],
                              [  9.38531562,   6.17504169,  20.60247011],
                              [  5.31485142,   8.52512535,  20.60247011],
                              [  9.38531562,   8.52512535,  20.60247011],
                              [  7.35008352,   9.70016704,  20.60247011],
                              [  7.35008352,   5.00000001,  22.02332989],
                              [  5.31485142,   6.17504169,  22.02332989],
                              [  9.38531562,   6.17504169,  22.02332989],
                              [  5.31485142,   8.52512535,  22.02332989],
                              [  9.38531562,   8.52512535,  22.02332989],
                              [  7.35008352,   9.70016704,  22.02332989],
                              [  6.17504169,   5.31485142,  22.73376011],
                              [  8.52512535,   5.31485142,  22.73376011],
                              [  5.00000001,   7.35008352,  22.73376011],
                              [  9.70016704,   7.35008352,  22.73376011],
                              [  6.17504169,   9.38531562,  22.73376011],
                              [  8.52512535,   9.38531562,  22.73376011],
                              [  6.17504169,   5.31485142,  24.15461989],
                              [  8.52512535,   5.31485142,  24.15461989],
                              [  5.00000001,   7.35008352,  24.15461989],
                              [  9.70016704,   7.35008352,  24.15461989],
                              [  6.17504169,   9.38531562,  24.15461989],
                              [  8.52512535,   9.38531562,  24.15461989],
                              [  7.35008352,   5.00000001,  24.86505011],
                              [  5.31485142,   6.17504169,  24.86505011],
                              [  9.38531562,   6.17504169,  24.86505011],
                              [  5.31485142,   8.52512535,  24.86505011],
                              [  9.38531562,   8.52512535,  24.86505011],
                              [  7.35008352,   9.70016704,  24.86505011],
                              [  7.35008352,   5.00000001,  26.28590989],
                              [  5.31485142,   6.17504169,  26.28590989],
                              [  9.38531562,   6.17504169,  26.28590989],
                              [  5.31485142,   8.52512535,  26.28590989],
                              [  9.38531562,   8.52512535,  26.28590989],
                              [  7.35008352,   9.70016704,  26.28590989],
                              [  6.17504169,   5.31485142,  26.99634011],
                              [  8.52512535,   5.31485142,  26.99634011],
                              [  5.00000001,   7.35008352,  26.99634011],
                              [  9.70016704,   7.35008352,  26.99634011],
                              [  6.17504169,   9.38531562,  26.99634011],
                              [  8.52512535,   9.38531562,  26.99634011],
                              [  6.17504169,   5.31485142,  28.41719989],
                              [  8.52512535,   5.31485142,  28.41719989],
                              [  5.00000001,   7.35008352,  28.41719989],
                              [  9.70016704,   7.35008352,  28.41719989],
                              [  6.17504169,   9.38531562,  28.41719989],
                              [  8.52512535,   9.38531562,  28.41719989],
                              [  7.35008352,   5.00000001,  29.12763011],
                              [  5.31485142,   6.17504169,  29.12763011],
                              [  9.38531562,   6.17504169,  29.12763011],
                              [  5.31485142,   8.52512535,  29.12763011],
                              [  9.38531562,   8.52512535,  29.12763011],
                              [  7.35008352,   9.70016704,  29.12763011],
                              [  7.35008352,   5.00000001,  30.54848989],
                              [  5.31485142,   6.17504169,  30.54848989],
                              [  9.38531562,   6.17504169,  30.54848989],
                              [  5.31485142,   8.52512535,  30.54848989],
                              [  9.38531562,   8.52512535,  30.54848989],
                              [  7.35008352,   9.70016704,  30.54848989],
                              [  6.17504169,   5.31485142,  31.25892011],
                              [  8.52512535,   5.31485142,  31.25892011],
                              [  5.00000001,   7.35008352,  31.25892011],
                              [  9.70016704,   7.35008352,  31.25892011],
                              [  6.17504169,   9.38531562,  31.25892011],
                              [  8.52512535,   9.38531562,  31.25892011],
                              [  6.17504169,   5.31485142,  32.67977989],
                              [  8.52512535,   5.31485142,  32.67977989],
                              [  5.00000001,   7.35008352,  32.67977989],
                              [  9.70016704,   7.35008352,  32.67977989],
                              [  6.17504169,   9.38531562,  32.67977989],
                              [  8.52512535,   9.38531562,  32.67977989],
                              [  7.35008352,   5.00000001,  33.39021011],
                              [  5.31485142,   6.17504169,  33.39021011],
                              [  9.38531562,   6.17504169,  33.39021011],
                              [  5.31485142,   8.52512535,  33.39021011],
                              [  9.38531562,   8.52512535,  33.39021011],
                              [  7.35008352,   9.70016704,  33.39021011]]*Angstrom

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
    ]


