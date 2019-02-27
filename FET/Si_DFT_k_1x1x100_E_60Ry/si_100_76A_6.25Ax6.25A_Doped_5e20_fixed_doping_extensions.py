# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.8612]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon]

# Define coordinates
left_electrode_coordinates = [[ 11.99997859,  15.1284    ,   0.251586  ],
                              [ 18.25682141,  15.1284    ,   0.251586  ],
                              [ 13.20839296,  15.1284    ,   1.106064  ],
                              [ 17.04840704,  15.1284    ,   1.106064  ],
                              [ 13.20839296,  11.99997859,   1.609236  ],
                              [ 17.04840704,  11.99997859,   1.609236  ],
                              [ 13.20839296,  18.25682141,   1.609236  ],
                              [ 17.04840704,  18.25682141,   1.609236  ],
                              [ 13.20839296,  13.20839296,   2.463714  ],
                              [ 17.04840704,  13.20839296,   2.463714  ],
                              [ 13.20839296,  17.04840704,   2.463714  ],
                              [ 17.04840704,  17.04840704,   2.463714  ],
                              [ 11.99997859,  13.20839296,   3.31819199],
                              [ 18.25682141,  13.20839296,   3.31819199],
                              [ 11.99997859,  17.04840704,   3.31819199],
                              [ 18.25682141,  17.04840704,   3.31819199],
                              [ 15.1284    ,  13.20839296,   3.821364  ],
                              [ 15.1284    ,  17.04840704,   3.821364  ],
                              [ 15.1284    ,  11.99997859,   4.67584199],
                              [ 15.1284    ,  18.25682141,   4.67584199],
                              [ 15.1284    ,  15.1284    ,   5.179014  ],
                              [ 11.99997859,  15.1284    ,   5.682186  ],
                              [ 18.25682141,  15.1284    ,   5.682186  ],
                              [ 13.20839296,  15.1284    ,   6.536664  ],
                              [ 17.04840704,  15.1284    ,   6.536664  ],
                              [ 13.20839296,  11.99997859,   7.039836  ],
                              [ 17.04840704,  11.99997859,   7.039836  ],
                              [ 13.20839296,  18.25682141,   7.039836  ],
                              [ 17.04840704,  18.25682141,   7.039836  ],
                              [ 13.20839296,  13.20839296,   7.894314  ],
                              [ 17.04840704,  13.20839296,   7.894314  ],
                              [ 13.20839296,  17.04840704,   7.894314  ],
                              [ 17.04840704,  17.04840704,   7.894314  ],
                              [ 11.99997859,  13.20839296,   8.74879199],
                              [ 18.25682141,  13.20839296,   8.74879199],
                              [ 11.99997859,  17.04840704,   8.74879199],
                              [ 18.25682141,  17.04840704,   8.74879199],
                              [ 15.1284    ,  13.20839296,   9.251964  ],
                              [ 15.1284    ,  17.04840704,   9.251964  ],
                              [ 15.1284    ,  11.99997859,  10.10644199],
                              [ 15.1284    ,  18.25682141,  10.10644199],
                              [ 15.1284    ,  15.1284    ,  10.609614  ]]*Angstrom

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
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.8612]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                            Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon]

# Define coordinates
right_electrode_coordinates = [[ 11.99997859,  15.1284    ,   0.251586  ],
                               [ 18.25682141,  15.1284    ,   0.251586  ],
                               [ 13.20839296,  15.1284    ,   1.106064  ],
                               [ 17.04840704,  15.1284    ,   1.106064  ],
                               [ 13.20839296,  11.99997859,   1.609236  ],
                               [ 17.04840704,  11.99997859,   1.609236  ],
                               [ 13.20839296,  18.25682141,   1.609236  ],
                               [ 17.04840704,  18.25682141,   1.609236  ],
                               [ 13.20839296,  13.20839296,   2.463714  ],
                               [ 17.04840704,  13.20839296,   2.463714  ],
                               [ 13.20839296,  17.04840704,   2.463714  ],
                               [ 17.04840704,  17.04840704,   2.463714  ],
                               [ 11.99997859,  13.20839296,   3.31819199],
                               [ 18.25682141,  13.20839296,   3.31819199],
                               [ 11.99997859,  17.04840704,   3.31819199],
                               [ 18.25682141,  17.04840704,   3.31819199],
                               [ 15.1284    ,  13.20839296,   3.821364  ],
                               [ 15.1284    ,  17.04840704,   3.821364  ],
                               [ 15.1284    ,  11.99997859,   4.67584199],
                               [ 15.1284    ,  18.25682141,   4.67584199],
                               [ 15.1284    ,  15.1284    ,   5.179014  ],
                               [ 11.99997859,  15.1284    ,   5.682186  ],
                               [ 18.25682141,  15.1284    ,   5.682186  ],
                               [ 13.20839296,  15.1284    ,   6.536664  ],
                               [ 17.04840704,  15.1284    ,   6.536664  ],
                               [ 13.20839296,  11.99997859,   7.039836  ],
                               [ 17.04840704,  11.99997859,   7.039836  ],
                               [ 13.20839296,  18.25682141,   7.039836  ],
                               [ 17.04840704,  18.25682141,   7.039836  ],
                               [ 13.20839296,  13.20839296,   7.894314  ],
                               [ 17.04840704,  13.20839296,   7.894314  ],
                               [ 13.20839296,  17.04840704,   7.894314  ],
                               [ 17.04840704,  17.04840704,   7.894314  ],
                               [ 11.99997859,  13.20839296,   8.74879199],
                               [ 18.25682141,  13.20839296,   8.74879199],
                               [ 11.99997859,  17.04840704,   8.74879199],
                               [ 18.25682141,  17.04840704,   8.74879199],
                               [ 15.1284    ,  13.20839296,   9.251964  ],
                               [ 15.1284    ,  17.04840704,   9.251964  ],
                               [ 15.1284    ,  11.99997859,  10.10644199],
                               [ 15.1284    ,  18.25682141,  10.10644199],
                               [ 15.1284    ,  15.1284    ,  10.609614  ]]*Angstrom

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
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 76.0284]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon]

# Define coordinates
central_region_coordinates = [[ 11.99997859,  15.1284    ,   0.251586  ],
                              [ 18.25682141,  15.1284    ,   0.251586  ],
                              [ 13.20839296,  15.1284    ,   1.106064  ],
                              [ 17.04840704,  15.1284    ,   1.106064  ],
                              [ 13.20839296,  11.99997859,   1.609236  ],
                              [ 17.04840704,  11.99997859,   1.609236  ],
                              [ 13.20839296,  18.25682141,   1.609236  ],
                              [ 17.04840704,  18.25682141,   1.609236  ],
                              [ 13.20839296,  13.20839296,   2.463714  ],
                              [ 17.04840704,  13.20839296,   2.463714  ],
                              [ 13.20839296,  17.04840704,   2.463714  ],
                              [ 17.04840704,  17.04840704,   2.463714  ],
                              [ 11.99997859,  13.20839296,   3.31819199],
                              [ 18.25682141,  13.20839296,   3.31819199],
                              [ 11.99997859,  17.04840704,   3.31819199],
                              [ 18.25682141,  17.04840704,   3.31819199],
                              [ 15.1284    ,  13.20839296,   3.821364  ],
                              [ 15.1284    ,  17.04840704,   3.821364  ],
                              [ 15.1284    ,  11.99997859,   4.67584199],
                              [ 15.1284    ,  18.25682141,   4.67584199],
                              [ 15.1284    ,  15.1284    ,   5.179014  ],
                              [ 11.99997859,  15.1284    ,   5.682186  ],
                              [ 18.25682141,  15.1284    ,   5.682186  ],
                              [ 13.20839296,  15.1284    ,   6.536664  ],
                              [ 17.04840704,  15.1284    ,   6.536664  ],
                              [ 13.20839296,  11.99997859,   7.039836  ],
                              [ 17.04840704,  11.99997859,   7.039836  ],
                              [ 13.20839296,  18.25682141,   7.039836  ],
                              [ 17.04840704,  18.25682141,   7.039836  ],
                              [ 13.20839296,  13.20839296,   7.894314  ],
                              [ 17.04840704,  13.20839296,   7.894314  ],
                              [ 13.20839296,  17.04840704,   7.894314  ],
                              [ 17.04840704,  17.04840704,   7.894314  ],
                              [ 11.99997859,  13.20839296,   8.74879199],
                              [ 18.25682141,  13.20839296,   8.74879199],
                              [ 11.99997859,  17.04840704,   8.74879199],
                              [ 18.25682141,  17.04840704,   8.74879199],
                              [ 15.1284    ,  13.20839296,   9.251964  ],
                              [ 15.1284    ,  17.04840704,   9.251964  ],
                              [ 15.1284    ,  11.99997859,  10.10644199],
                              [ 15.1284    ,  18.25682141,  10.10644199],
                              [ 15.1284    ,  15.1284    ,  10.609614  ],
                              [ 11.99997859,  15.1284    ,  11.112786  ],
                              [ 18.25682141,  15.1284    ,  11.112786  ],
                              [ 13.20839296,  15.1284    ,  11.967264  ],
                              [ 17.04840704,  15.1284    ,  11.967264  ],
                              [ 13.20839296,  11.99997859,  12.470436  ],
                              [ 17.04840704,  11.99997859,  12.470436  ],
                              [ 13.20839296,  18.25682141,  12.470436  ],
                              [ 17.04840704,  18.25682141,  12.470436  ],
                              [ 13.20839296,  13.20839296,  13.324914  ],
                              [ 17.04840704,  13.20839296,  13.324914  ],
                              [ 13.20839296,  17.04840704,  13.324914  ],
                              [ 17.04840704,  17.04840704,  13.324914  ],
                              [ 11.99997859,  13.20839296,  14.17939199],
                              [ 18.25682141,  13.20839296,  14.17939199],
                              [ 11.99997859,  17.04840704,  14.17939199],
                              [ 18.25682141,  17.04840704,  14.17939199],
                              [ 15.1284    ,  13.20839296,  14.682564  ],
                              [ 15.1284    ,  17.04840704,  14.682564  ],
                              [ 15.1284    ,  11.99997859,  15.53704199],
                              [ 15.1284    ,  18.25682141,  15.53704199],
                              [ 15.1284    ,  15.1284    ,  16.040214  ],
                              [ 11.99997859,  15.1284    ,  16.543386  ],
                              [ 18.25682141,  15.1284    ,  16.543386  ],
                              [ 13.20839296,  15.1284    ,  17.397864  ],
                              [ 17.04840704,  15.1284    ,  17.397864  ],
                              [ 13.20839296,  11.99997859,  17.901036  ],
                              [ 17.04840704,  11.99997859,  17.901036  ],
                              [ 13.20839296,  18.25682141,  17.901036  ],
                              [ 17.04840704,  18.25682141,  17.901036  ],
                              [ 13.20839296,  13.20839296,  18.755514  ],
                              [ 17.04840704,  13.20839296,  18.755514  ],
                              [ 13.20839296,  17.04840704,  18.755514  ],
                              [ 17.04840704,  17.04840704,  18.755514  ],
                              [ 11.99997859,  13.20839296,  19.60999199],
                              [ 18.25682141,  13.20839296,  19.60999199],
                              [ 11.99997859,  17.04840704,  19.60999199],
                              [ 18.25682141,  17.04840704,  19.60999199],
                              [ 15.1284    ,  13.20839296,  20.113164  ],
                              [ 15.1284    ,  17.04840704,  20.113164  ],
                              [ 15.1284    ,  11.99997859,  20.96764199],
                              [ 15.1284    ,  18.25682141,  20.96764199],
                              [ 15.1284    ,  15.1284    ,  21.470814  ],
                              [ 11.99997859,  15.1284    ,  21.973986  ],
                              [ 18.25682141,  15.1284    ,  21.973986  ],
                              [ 13.20839296,  15.1284    ,  22.828464  ],
                              [ 17.04840704,  15.1284    ,  22.828464  ],
                              [ 13.20839296,  11.99997859,  23.331636  ],
                              [ 17.04840704,  11.99997859,  23.331636  ],
                              [ 13.20839296,  18.25682141,  23.331636  ],
                              [ 17.04840704,  18.25682141,  23.331636  ],
                              [ 13.20839296,  13.20839296,  24.186114  ],
                              [ 17.04840704,  13.20839296,  24.186114  ],
                              [ 13.20839296,  17.04840704,  24.186114  ],
                              [ 17.04840704,  17.04840704,  24.186114  ],
                              [ 11.99997859,  13.20839296,  25.04059199],
                              [ 18.25682141,  13.20839296,  25.04059199],
                              [ 11.99997859,  17.04840704,  25.04059199],
                              [ 18.25682141,  17.04840704,  25.04059199],
                              [ 15.1284    ,  13.20839296,  25.543764  ],
                              [ 15.1284    ,  17.04840704,  25.543764  ],
                              [ 15.1284    ,  11.99997859,  26.39824199],
                              [ 15.1284    ,  18.25682141,  26.39824199],
                              [ 15.1284    ,  15.1284    ,  26.901414  ],
                              [ 11.99997859,  15.1284    ,  27.404586  ],
                              [ 18.25682141,  15.1284    ,  27.404586  ],
                              [ 13.20839296,  15.1284    ,  28.259064  ],
                              [ 17.04840704,  15.1284    ,  28.259064  ],
                              [ 13.20839296,  11.99997859,  28.762236  ],
                              [ 17.04840704,  11.99997859,  28.762236  ],
                              [ 13.20839296,  18.25682141,  28.762236  ],
                              [ 17.04840704,  18.25682141,  28.762236  ],
                              [ 13.20839296,  13.20839296,  29.616714  ],
                              [ 17.04840704,  13.20839296,  29.616714  ],
                              [ 13.20839296,  17.04840704,  29.616714  ],
                              [ 17.04840704,  17.04840704,  29.616714  ],
                              [ 11.99997859,  13.20839296,  30.47119199],
                              [ 18.25682141,  13.20839296,  30.47119199],
                              [ 11.99997859,  17.04840704,  30.47119199],
                              [ 18.25682141,  17.04840704,  30.47119199],
                              [ 15.1284    ,  13.20839296,  30.974364  ],
                              [ 15.1284    ,  17.04840704,  30.974364  ],
                              [ 15.1284    ,  11.99997859,  31.82884199],
                              [ 15.1284    ,  18.25682141,  31.82884199],
                              [ 15.1284    ,  15.1284    ,  32.332014  ],
                              [ 11.99997859,  15.1284    ,  32.835186  ],
                              [ 18.25682141,  15.1284    ,  32.835186  ],
                              [ 13.20839296,  15.1284    ,  33.689664  ],
                              [ 17.04840704,  15.1284    ,  33.689664  ],
                              [ 13.20839296,  11.99997859,  34.192836  ],
                              [ 17.04840704,  11.99997859,  34.192836  ],
                              [ 13.20839296,  18.25682141,  34.192836  ],
                              [ 17.04840704,  18.25682141,  34.192836  ],
                              [ 13.20839296,  13.20839296,  35.047314  ],
                              [ 17.04840704,  13.20839296,  35.047314  ],
                              [ 13.20839296,  17.04840704,  35.047314  ],
                              [ 17.04840704,  17.04840704,  35.047314  ],
                              [ 11.99997859,  13.20839296,  35.90179199],
                              [ 18.25682141,  13.20839296,  35.90179199],
                              [ 11.99997859,  17.04840704,  35.90179199],
                              [ 18.25682141,  17.04840704,  35.90179199],
                              [ 15.1284    ,  13.20839296,  36.404964  ],
                              [ 15.1284    ,  17.04840704,  36.404964  ],
                              [ 15.1284    ,  11.99997859,  37.25944199],
                              [ 15.1284    ,  18.25682141,  37.25944199],
                              [ 15.1284    ,  15.1284    ,  37.762614  ],
                              [ 11.99997859,  15.1284    ,  38.265786  ],
                              [ 18.25682141,  15.1284    ,  38.265786  ],
                              [ 13.20839296,  15.1284    ,  39.120264  ],
                              [ 17.04840704,  15.1284    ,  39.120264  ],
                              [ 13.20839296,  11.99997859,  39.623436  ],
                              [ 17.04840704,  11.99997859,  39.623436  ],
                              [ 13.20839296,  18.25682141,  39.623436  ],
                              [ 17.04840704,  18.25682141,  39.623436  ],
                              [ 13.20839296,  13.20839296,  40.477914  ],
                              [ 17.04840704,  13.20839296,  40.477914  ],
                              [ 13.20839296,  17.04840704,  40.477914  ],
                              [ 17.04840704,  17.04840704,  40.477914  ],
                              [ 11.99997859,  13.20839296,  41.33239199],
                              [ 18.25682141,  13.20839296,  41.33239199],
                              [ 11.99997859,  17.04840704,  41.33239199],
                              [ 18.25682141,  17.04840704,  41.33239199],
                              [ 15.1284    ,  13.20839296,  41.835564  ],
                              [ 15.1284    ,  17.04840704,  41.835564  ],
                              [ 15.1284    ,  11.99997859,  42.69004199],
                              [ 15.1284    ,  18.25682141,  42.69004199],
                              [ 15.1284    ,  15.1284    ,  43.193214  ],
                              [ 11.99997859,  15.1284    ,  43.696386  ],
                              [ 18.25682141,  15.1284    ,  43.696386  ],
                              [ 13.20839296,  15.1284    ,  44.550864  ],
                              [ 17.04840704,  15.1284    ,  44.550864  ],
                              [ 13.20839296,  11.99997859,  45.054036  ],
                              [ 17.04840704,  11.99997859,  45.054036  ],
                              [ 13.20839296,  18.25682141,  45.054036  ],
                              [ 17.04840704,  18.25682141,  45.054036  ],
                              [ 13.20839296,  13.20839296,  45.908514  ],
                              [ 17.04840704,  13.20839296,  45.908514  ],
                              [ 13.20839296,  17.04840704,  45.908514  ],
                              [ 17.04840704,  17.04840704,  45.908514  ],
                              [ 11.99997859,  13.20839296,  46.76299199],
                              [ 18.25682141,  13.20839296,  46.76299199],
                              [ 11.99997859,  17.04840704,  46.76299199],
                              [ 18.25682141,  17.04840704,  46.76299199],
                              [ 15.1284    ,  13.20839296,  47.266164  ],
                              [ 15.1284    ,  17.04840704,  47.266164  ],
                              [ 15.1284    ,  11.99997859,  48.12064199],
                              [ 15.1284    ,  18.25682141,  48.12064199],
                              [ 15.1284    ,  15.1284    ,  48.623814  ],
                              [ 11.99997859,  15.1284    ,  49.126986  ],
                              [ 18.25682141,  15.1284    ,  49.126986  ],
                              [ 13.20839296,  15.1284    ,  49.981464  ],
                              [ 17.04840704,  15.1284    ,  49.981464  ],
                              [ 13.20839296,  11.99997859,  50.484636  ],
                              [ 17.04840704,  11.99997859,  50.484636  ],
                              [ 13.20839296,  18.25682141,  50.484636  ],
                              [ 17.04840704,  18.25682141,  50.484636  ],
                              [ 13.20839296,  13.20839296,  51.339114  ],
                              [ 17.04840704,  13.20839296,  51.339114  ],
                              [ 13.20839296,  17.04840704,  51.339114  ],
                              [ 17.04840704,  17.04840704,  51.339114  ],
                              [ 11.99997859,  13.20839296,  52.19359199],
                              [ 18.25682141,  13.20839296,  52.19359199],
                              [ 11.99997859,  17.04840704,  52.19359199],
                              [ 18.25682141,  17.04840704,  52.19359199],
                              [ 15.1284    ,  13.20839296,  52.696764  ],
                              [ 15.1284    ,  17.04840704,  52.696764  ],
                              [ 15.1284    ,  11.99997859,  53.55124199],
                              [ 15.1284    ,  18.25682141,  53.55124199],
                              [ 15.1284    ,  15.1284    ,  54.054414  ],
                              [ 11.99997859,  15.1284    ,  54.557586  ],
                              [ 18.25682141,  15.1284    ,  54.557586  ],
                              [ 13.20839296,  15.1284    ,  55.412064  ],
                              [ 17.04840704,  15.1284    ,  55.412064  ],
                              [ 13.20839296,  11.99997859,  55.915236  ],
                              [ 17.04840704,  11.99997859,  55.915236  ],
                              [ 13.20839296,  18.25682141,  55.915236  ],
                              [ 17.04840704,  18.25682141,  55.915236  ],
                              [ 13.20839296,  13.20839296,  56.769714  ],
                              [ 17.04840704,  13.20839296,  56.769714  ],
                              [ 13.20839296,  17.04840704,  56.769714  ],
                              [ 17.04840704,  17.04840704,  56.769714  ],
                              [ 11.99997859,  13.20839296,  57.62419199],
                              [ 18.25682141,  13.20839296,  57.62419199],
                              [ 11.99997859,  17.04840704,  57.62419199],
                              [ 18.25682141,  17.04840704,  57.62419199],
                              [ 15.1284    ,  13.20839296,  58.127364  ],
                              [ 15.1284    ,  17.04840704,  58.127364  ],
                              [ 15.1284    ,  11.99997859,  58.98184199],
                              [ 15.1284    ,  18.25682141,  58.98184199],
                              [ 15.1284    ,  15.1284    ,  59.485014  ],
                              [ 11.99997859,  15.1284    ,  59.988186  ],
                              [ 18.25682141,  15.1284    ,  59.988186  ],
                              [ 13.20839296,  15.1284    ,  60.842664  ],
                              [ 17.04840704,  15.1284    ,  60.842664  ],
                              [ 13.20839296,  11.99997859,  61.345836  ],
                              [ 17.04840704,  11.99997859,  61.345836  ],
                              [ 13.20839296,  18.25682141,  61.345836  ],
                              [ 17.04840704,  18.25682141,  61.345836  ],
                              [ 13.20839296,  13.20839296,  62.200314  ],
                              [ 17.04840704,  13.20839296,  62.200314  ],
                              [ 13.20839296,  17.04840704,  62.200314  ],
                              [ 17.04840704,  17.04840704,  62.200314  ],
                              [ 11.99997859,  13.20839296,  63.05479199],
                              [ 18.25682141,  13.20839296,  63.05479199],
                              [ 11.99997859,  17.04840704,  63.05479199],
                              [ 18.25682141,  17.04840704,  63.05479199],
                              [ 15.1284    ,  13.20839296,  63.557964  ],
                              [ 15.1284    ,  17.04840704,  63.557964  ],
                              [ 15.1284    ,  11.99997859,  64.41244199],
                              [ 15.1284    ,  18.25682141,  64.41244199],
                              [ 15.1284    ,  15.1284    ,  64.915614  ],
                              [ 11.99997859,  15.1284    ,  65.418786  ],
                              [ 18.25682141,  15.1284    ,  65.418786  ],
                              [ 13.20839296,  15.1284    ,  66.273264  ],
                              [ 17.04840704,  15.1284    ,  66.273264  ],
                              [ 13.20839296,  11.99997859,  66.776436  ],
                              [ 17.04840704,  11.99997859,  66.776436  ],
                              [ 13.20839296,  18.25682141,  66.776436  ],
                              [ 17.04840704,  18.25682141,  66.776436  ],
                              [ 13.20839296,  13.20839296,  67.630914  ],
                              [ 17.04840704,  13.20839296,  67.630914  ],
                              [ 13.20839296,  17.04840704,  67.630914  ],
                              [ 17.04840704,  17.04840704,  67.630914  ],
                              [ 11.99997859,  13.20839296,  68.48539199],
                              [ 18.25682141,  13.20839296,  68.48539199],
                              [ 11.99997859,  17.04840704,  68.48539199],
                              [ 18.25682141,  17.04840704,  68.48539199],
                              [ 15.1284    ,  13.20839296,  68.988564  ],
                              [ 15.1284    ,  17.04840704,  68.988564  ],
                              [ 15.1284    ,  11.99997859,  69.84304199],
                              [ 15.1284    ,  18.25682141,  69.84304199],
                              [ 15.1284    ,  15.1284    ,  70.346214  ],
                              [ 11.99997859,  15.1284    ,  70.849386  ],
                              [ 18.25682141,  15.1284    ,  70.849386  ],
                              [ 13.20839296,  15.1284    ,  71.703864  ],
                              [ 17.04840704,  15.1284    ,  71.703864  ],
                              [ 13.20839296,  11.99997859,  72.207036  ],
                              [ 17.04840704,  11.99997859,  72.207036  ],
                              [ 13.20839296,  18.25682141,  72.207036  ],
                              [ 17.04840704,  18.25682141,  72.207036  ],
                              [ 13.20839296,  13.20839296,  73.061514  ],
                              [ 17.04840704,  13.20839296,  73.061514  ],
                              [ 13.20839296,  17.04840704,  73.061514  ],
                              [ 17.04840704,  17.04840704,  73.061514  ],
                              [ 11.99997859,  13.20839296,  73.91599199],
                              [ 18.25682141,  13.20839296,  73.91599199],
                              [ 11.99997859,  17.04840704,  73.91599199],
                              [ 18.25682141,  17.04840704,  73.91599199],
                              [ 15.1284    ,  13.20839296,  74.419164  ],
                              [ 15.1284    ,  17.04840704,  74.419164  ],
                              [ 15.1284    ,  11.99997859,  75.27364199],
                              [ 15.1284    ,  18.25682141,  75.27364199],
                              [ 15.1284    ,  15.1284    ,  75.776814  ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )
# Add tags
central_region.addTags('left_electrode_extension',  [ 2,  3,  8,  9, 10, 11, 16, 17, 20, 23, 24, 29, 30,
                                                     31, 32, 37, 38, 41, 44, 45, 50, 51, 52, 53, 58, 59,
                                                     62, 65, 66, 71, 72, 73, 74, 79, 80])
central_region.addTags('right_electrode_extension', [212, 213, 218, 219, 220, 221, 226, 227, 230, 233,
                                                     234, 239, 240, 241, 242, 247, 248, 251, 254, 255,
                                                     260, 261, 262, 263, 268, 269, 272, 275, 276, 281,
                                                     282, 283, 284, 289, 290, 293])

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  19.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  19.25682141 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  19.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  19.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.99997859 *Angstrom,  xmax =  -2.14100000004e-05 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.14100000004e-05 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  29.25682141 *Angstrom,  ymax =  30.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.25682141 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.14100000004e-05 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  -2.14100000004e-05 *Angstrom,
        zmin =  22.888407 *Angstrom,  zmax =  52.888407 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]



#Angstrom cubed
electrode_volume = 416.365
#per cm cubed
electrode_doping_density = 5e+20
#device Atom
atom_type = Silicon
passivation_atom_type = Hydrogen

temp = 300