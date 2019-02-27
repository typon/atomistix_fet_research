# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [21.2804212417, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.2804212417, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.76751646075]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[  8.60108554,   6.31457323,   0.72093956],
                              [ 12.6793357 ,   6.31457323,   0.72093956],
                              [  8.60108554,   9.19833142,   0.72093956],
                              [ 12.6793357 ,   9.19833142,   0.72093956],
                              [  8.60108554,  12.08208982,   0.72093956],
                              [ 12.6793357 ,  12.08208982,   0.72093956],
                              [  8.60108554,  14.96584801,   0.72093956],
                              [ 12.6793357 ,  14.96584801,   0.72093956],
                              [  6.56196068,   4.87269424,   2.16281867],
                              [ 10.64021062,   4.87269424,   2.16281867],
                              [ 14.71846056,   4.87269424,   2.16281867],
                              [  6.56196068,   7.75645243,   2.16281867],
                              [ 10.64021062,   7.75645243,   2.16281867],
                              [ 14.71846056,   7.75645243,   2.16281867],
                              [  6.56196068,  10.64021062,   2.16281867],
                              [ 10.64021062,  10.64021062,   2.16281867],
                              [ 14.71846056,  10.64021062,   2.16281867],
                              [  6.56196068,  13.52396881,   2.16281867],
                              [ 10.64021062,  13.52396881,   2.16281867],
                              [ 14.71846056,  13.52396881,   2.16281867],
                              [  6.56196068,  16.407727  ,   2.16281867],
                              [ 10.64021062,  16.407727  ,   2.16281867],
                              [ 14.71846056,  16.407727  ,   2.16281867],
                              [  8.60108554,   6.31457323,   3.60469779],
                              [ 12.6793357 ,   6.31457323,   3.60469779],
                              [  8.60108554,   9.19833142,   3.60469779],
                              [ 12.6793357 ,   9.19833142,   3.60469779],
                              [  8.60108554,  12.08208982,   3.60469779],
                              [ 12.6793357 ,  12.08208982,   3.60469779],
                              [  8.60108554,  14.96584801,   3.60469779],
                              [ 12.6793357 ,  14.96584801,   3.60469779],
                              [  6.56196068,   7.75645243,   5.0465769 ],
                              [ 10.64021062,   7.75645243,   5.0465769 ],
                              [ 14.71846056,   7.75645243,   5.0465769 ],
                              [  6.56196068,  10.64021062,   5.0465769 ],
                              [ 10.64021062,  10.64021062,   5.0465769 ],
                              [ 14.71846056,  10.64021062,   5.0465769 ],
                              [  6.56196068,  13.52396881,   5.0465769 ],
                              [ 10.64021062,  13.52396881,   5.0465769 ],
                              [ 14.71846056,  13.52396881,   5.0465769 ]]*Angstrom

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
vector_a = [21.2804212417, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.2804212417, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.76751646075]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[  8.60108554,   6.31457323,   0.72093956],
                               [ 12.6793357 ,   6.31457323,   0.72093956],
                               [  8.60108554,   9.19833142,   0.72093956],
                               [ 12.6793357 ,   9.19833142,   0.72093956],
                               [  8.60108554,  12.08208982,   0.72093956],
                               [ 12.6793357 ,  12.08208982,   0.72093956],
                               [  8.60108554,  14.96584801,   0.72093956],
                               [ 12.6793357 ,  14.96584801,   0.72093956],
                               [  6.56196068,   4.87269424,   2.16281867],
                               [ 10.64021062,   4.87269424,   2.16281867],
                               [ 14.71846056,   4.87269424,   2.16281867],
                               [  6.56196068,   7.75645243,   2.16281867],
                               [ 10.64021062,   7.75645243,   2.16281867],
                               [ 14.71846056,   7.75645243,   2.16281867],
                               [  6.56196068,  10.64021062,   2.16281867],
                               [ 10.64021062,  10.64021062,   2.16281867],
                               [ 14.71846056,  10.64021062,   2.16281867],
                               [  6.56196068,  13.52396881,   2.16281867],
                               [ 10.64021062,  13.52396881,   2.16281867],
                               [ 14.71846056,  13.52396881,   2.16281867],
                               [  6.56196068,  16.407727  ,   2.16281867],
                               [ 10.64021062,  16.407727  ,   2.16281867],
                               [ 14.71846056,  16.407727  ,   2.16281867],
                               [  8.60108554,   6.31457323,   3.60469779],
                               [ 12.6793357 ,   6.31457323,   3.60469779],
                               [  8.60108554,   9.19833142,   3.60469779],
                               [ 12.6793357 ,   9.19833142,   3.60469779],
                               [  8.60108554,  12.08208982,   3.60469779],
                               [ 12.6793357 ,  12.08208982,   3.60469779],
                               [  8.60108554,  14.96584801,   3.60469779],
                               [ 12.6793357 ,  14.96584801,   3.60469779],
                               [  6.56196068,   7.75645243,   5.0465769 ],
                               [ 10.64021062,   7.75645243,   5.0465769 ],
                               [ 14.71846056,   7.75645243,   5.0465769 ],
                               [  6.56196068,  10.64021062,   5.0465769 ],
                               [ 10.64021062,  10.64021062,   5.0465769 ],
                               [ 14.71846056,  10.64021062,   5.0465769 ],
                               [  6.56196068,  13.52396881,   5.0465769 ],
                               [ 10.64021062,  13.52396881,   5.0465769 ],
                               [ 14.71846056,  13.52396881,   5.0465769 ]]*Angstrom

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
vector_a = [21.2804212417, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.2804212417, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5350329215]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[  8.60108554,   6.31457323,   0.72093956],
                              [ 12.6793357 ,   6.31457323,   0.72093956],
                              [  8.60108554,   9.19833142,   0.72093956],
                              [ 12.6793357 ,   9.19833142,   0.72093956],
                              [  8.60108554,  12.08208982,   0.72093956],
                              [ 12.6793357 ,  12.08208982,   0.72093956],
                              [  8.60108554,  14.96584801,   0.72093956],
                              [ 12.6793357 ,  14.96584801,   0.72093956],
                              [  6.56196068,   4.87269424,   2.16281867],
                              [ 10.64021062,   4.87269424,   2.16281867],
                              [ 14.71846056,   4.87269424,   2.16281867],
                              [  6.56196068,   7.75645243,   2.16281867],
                              [ 10.64021062,   7.75645243,   2.16281867],
                              [ 14.71846056,   7.75645243,   2.16281867],
                              [  6.56196068,  10.64021062,   2.16281867],
                              [ 10.64021062,  10.64021062,   2.16281867],
                              [ 14.71846056,  10.64021062,   2.16281867],
                              [  6.56196068,  13.52396881,   2.16281867],
                              [ 10.64021062,  13.52396881,   2.16281867],
                              [ 14.71846056,  13.52396881,   2.16281867],
                              [  6.56196068,  16.407727  ,   2.16281867],
                              [ 10.64021062,  16.407727  ,   2.16281867],
                              [ 14.71846056,  16.407727  ,   2.16281867],
                              [  8.60108554,   6.31457323,   3.60469779],
                              [ 12.6793357 ,   6.31457323,   3.60469779],
                              [  8.60108554,   9.19833142,   3.60469779],
                              [ 12.6793357 ,   9.19833142,   3.60469779],
                              [  8.60108554,  12.08208982,   3.60469779],
                              [ 12.6793357 ,  12.08208982,   3.60469779],
                              [  8.60108554,  14.96584801,   3.60469779],
                              [ 12.6793357 ,  14.96584801,   3.60469779],
                              [  6.56196068,   7.75645243,   5.0465769 ],
                              [ 10.64021062,   7.75645243,   5.0465769 ],
                              [ 14.71846056,   7.75645243,   5.0465769 ],
                              [  6.56196068,  10.64021062,   5.0465769 ],
                              [ 10.64021062,  10.64021062,   5.0465769 ],
                              [ 14.71846056,  10.64021062,   5.0465769 ],
                              [  6.56196068,  13.52396881,   5.0465769 ],
                              [ 10.64021062,  13.52396881,   5.0465769 ],
                              [ 14.71846056,  13.52396881,   5.0465769 ],
                              [  8.60108554,   6.31457323,   6.48845602],
                              [ 12.6793357 ,   6.31457323,   6.48845602],
                              [  8.60108554,   9.19833142,   6.48845602],
                              [ 12.6793357 ,   9.19833142,   6.48845602],
                              [  8.60108554,  12.08208982,   6.48845602],
                              [ 12.6793357 ,  12.08208982,   6.48845602],
                              [  8.60108554,  14.96584801,   6.48845602],
                              [ 12.6793357 ,  14.96584801,   6.48845602],
                              [  6.56196068,   4.87269424,   7.93033513],
                              [ 10.64021062,   4.87269424,   7.93033513],
                              [ 14.71846056,   4.87269424,   7.93033513],
                              [  6.56196068,   7.75645243,   7.93033513],
                              [ 10.64021062,   7.75645243,   7.93033513],
                              [ 14.71846056,   7.75645243,   7.93033513],
                              [  6.56196068,  10.64021062,   7.93033513],
                              [ 10.64021062,  10.64021062,   7.93033513],
                              [ 14.71846056,  10.64021062,   7.93033513],
                              [  6.56196068,  13.52396881,   7.93033513],
                              [ 10.64021062,  13.52396881,   7.93033513],
                              [ 14.71846056,  13.52396881,   7.93033513],
                              [  6.56196068,  16.407727  ,   7.93033513],
                              [ 10.64021062,  16.407727  ,   7.93033513],
                              [ 14.71846056,  16.407727  ,   7.93033513],
                              [  8.60108554,   6.31457323,   9.37221425],
                              [ 12.6793357 ,   6.31457323,   9.37221425],
                              [  8.60108554,   9.19833142,   9.37221425],
                              [ 12.6793357 ,   9.19833142,   9.37221425],
                              [  8.60108554,  12.08208982,   9.37221425],
                              [ 12.6793357 ,  12.08208982,   9.37221425],
                              [  8.60108554,  14.96584801,   9.37221425],
                              [ 12.6793357 ,  14.96584801,   9.37221425],
                              [  6.56196068,   7.75645243,  10.81409336],
                              [ 10.64021062,   7.75645243,  10.81409336],
                              [ 14.71846056,   7.75645243,  10.81409336],
                              [  6.56196068,  10.64021062,  10.81409336],
                              [ 10.64021062,  10.64021062,  10.81409336],
                              [ 14.71846056,  10.64021062,  10.81409336],
                              [  6.56196068,  13.52396881,  10.81409336],
                              [ 10.64021062,  13.52396881,  10.81409336],
                              [ 14.71846056,  13.52396881,  10.81409336]]*Angstrom

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


