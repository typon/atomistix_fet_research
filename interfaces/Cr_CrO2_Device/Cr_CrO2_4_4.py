# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [4.421, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.842, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.917]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Oxygen, Chromium, Oxygen, Oxygen, Chromium, Oxygen, Chromium,
                           Oxygen, Oxygen, Chromium, Oxygen, Oxygen]

# Define coordinates
left_electrode_coordinates = [[ 0.879779,  0.879779,  0.72925 ],
                              [ 2.2105  ,  2.2105  ,  0.72925 ],
                              [ 3.541221,  3.541221,  0.72925 ],
                              [ 0.879779,  5.300779,  0.72925 ],
                              [ 2.2105  ,  6.6315  ,  0.72925 ],
                              [ 3.541221,  7.962221,  0.72925 ],
                              [ 0.      ,  0.      ,  2.18775 ],
                              [ 3.090279,  1.330721,  2.18775 ],
                              [ 1.330721,  3.090279,  2.18775 ],
                              [ 0.      ,  4.421   ,  2.18775 ],
                              [ 3.090279,  5.751721,  2.18775 ],
                              [ 1.330721,  7.511279,  2.18775 ]]*Angstrom

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
vector_a = [4.421, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.842, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07972328473]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                            Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                            Chromium, Chromium]

# Define coordinates
right_electrode_coordinates = [[ 3.15785714,  0.63157143,  1.01993082],
                               [ 0.63157143,  1.89471429,  1.01993082],
                               [ 2.52628571,  3.15785714,  1.01993082],
                               [-0.        ,  4.421     ,  1.01993082],
                               [ 1.89471429,  5.68414286,  1.01993082],
                               [ 3.78942857,  6.94728571,  1.01993082],
                               [ 1.26314286,  8.21042857,  1.01993082],
                               [-0.        ,  0.        ,  3.05979246],
                               [ 1.89471429,  1.26314286,  3.05979246],
                               [ 3.78942857,  2.52628571,  3.05979246],
                               [ 1.26314286,  3.78942857,  3.05979246],
                               [ 3.15785714,  5.05257143,  3.05979246],
                               [ 0.63157143,  6.31571429,  3.05979246],
                               [ 2.52628571,  7.57885714,  3.05979246]]*Angstrom

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
vector_a = [4.421, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.842, 0.0]*Angstrom
vector_c = [0.0, 0.0, 17.2011273907]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Oxygen, Chromium, Oxygen, Oxygen, Chromium, Oxygen, Chromium,
                           Oxygen, Oxygen, Chromium, Oxygen, Oxygen, Oxygen, Chromium,
                           Oxygen, Oxygen, Chromium, Oxygen, Chromium, Oxygen, Oxygen,
                           Chromium, Oxygen, Oxygen, Oxygen, Chromium, Oxygen, Oxygen,
                           Chromium, Oxygen, Chromium, Chromium, Chromium, Chromium, Chromium,
                           Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                           Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                           Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                           Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
                           Chromium, Chromium, Chromium, Chromium, Chromium, Chromium]

# Define coordinates
central_region_coordinates = [[  0.879779  ,   0.879779  ,   0.72925   ],
                              [  2.2105    ,   2.2105    ,   0.72925   ],
                              [  3.541221  ,   3.541221  ,   0.72925   ],
                              [  0.879779  ,   5.300779  ,   0.72925   ],
                              [  2.2105    ,   6.6315    ,   0.72925   ],
                              [  3.541221  ,   7.962221  ,   0.72925   ],
                              [  0.        ,   0.        ,   2.18775   ],
                              [  3.090279  ,   1.330721  ,   2.18775   ],
                              [  1.330721  ,   3.090279  ,   2.18775   ],
                              [  0.        ,   4.421     ,   2.18775   ],
                              [  3.090279  ,   5.751721  ,   2.18775   ],
                              [  1.330721  ,   7.511279  ,   2.18775   ],
                              [  0.879779  ,   0.879779  ,   3.64625   ],
                              [  2.2105    ,   2.2105    ,   3.64625   ],
                              [  3.541221  ,   3.541221  ,   3.64625   ],
                              [  0.879779  ,   5.300779  ,   3.64625   ],
                              [  2.2105    ,   6.6315    ,   3.64625   ],
                              [  3.541221  ,   7.962221  ,   3.64625   ],
                              [  0.        ,   0.        ,   5.10475   ],
                              [  3.090279  ,   1.330721  ,   5.10475   ],
                              [  1.330721  ,   3.090279  ,   5.10475   ],
                              [  0.        ,   4.421     ,   5.10475   ],
                              [  3.090279  ,   5.751721  ,   5.10475   ],
                              [  1.330721  ,   7.511279  ,   5.10475   ],
                              [  0.879779  ,   0.879779  ,   6.56325   ],
                              [  2.2105    ,   2.2105    ,   6.56325   ],
                              [  3.541221  ,   3.541221  ,   6.56325   ],
                              [  0.879779  ,   5.300779  ,   6.56325   ],
                              [  2.2105    ,   6.6315    ,   6.56325   ],
                              [  3.541221  ,   7.962221  ,   6.56325   ],
                              [  0.        ,   0.        ,   8.02175   ],
                              [  1.89471429,   1.26314286,   8.02175   ],
                              [  3.78942857,   2.52628571,   8.02175   ],
                              [  1.26314286,   3.78942857,   8.02175   ],
                              [  3.15785714,   5.05257143,   8.02175   ],
                              [  0.63157143,   6.31571429,   8.02175   ],
                              [  2.52628571,   7.57885714,   8.02175   ],
                              [  3.15785714,   0.63157143,  10.06161164],
                              [  0.63157143,   1.89471429,  10.06161164],
                              [  2.52628571,   3.15785714,  10.06161164],
                              [  0.        ,   4.421     ,  10.06161164],
                              [  1.89471429,   5.68414286,  10.06161164],
                              [  3.78942857,   6.94728571,  10.06161164],
                              [  1.26314286,   8.21042857,  10.06161164],
                              [ -0.        ,   0.        ,  12.10147328],
                              [  1.89471429,   1.26314286,  12.10147328],
                              [  3.78942857,   2.52628571,  12.10147328],
                              [  1.26314286,   3.78942857,  12.10147328],
                              [  3.15785714,   5.05257143,  12.10147328],
                              [  0.63157143,   6.31571429,  12.10147328],
                              [  2.52628571,   7.57885714,  12.10147328],
                              [  3.15785714,   0.63157143,  14.14133493],
                              [  0.63157143,   1.89471429,  14.14133493],
                              [  2.52628571,   3.15785714,  14.14133493],
                              [ -0.        ,   4.421     ,  14.14133493],
                              [  1.89471429,   5.68414286,  14.14133493],
                              [  3.78942857,   6.94728571,  14.14133493],
                              [  1.26314286,   8.21042857,  14.14133493],
                              [ -0.        ,   0.        ,  16.18119657],
                              [  1.89471429,   1.26314286,  16.18119657],
                              [  3.78942857,   2.52628571,  16.18119657],
                              [  1.26314286,   3.78942857,  16.18119657],
                              [  3.15785714,   5.05257143,  16.18119657],
                              [  0.63157143,   6.31571429,  16.18119657],
                              [  2.52628571,   7.57885714,  16.18119657]]*Angstrom

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

