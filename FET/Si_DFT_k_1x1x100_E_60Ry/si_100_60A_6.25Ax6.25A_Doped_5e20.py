# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.8612]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
left_electrode_coordinates = [[ 15.1284    ,  13.20839296,   0.251586  ],
                              [ 15.1284    ,  17.04840704,   0.251586  ],
                              [ 15.1284    ,  11.99997859,   1.106064  ],
                              [ 15.1284    ,  18.25682141,   1.106064  ],
                              [ 15.1284    ,  15.1284    ,   1.609236  ],
                              [ 11.99997859,  15.1284    ,   2.11240801],
                              [ 18.25682141,  15.1284    ,   2.11240801],
                              [ 13.20839296,  15.1284    ,   2.966886  ],
                              [ 17.04840704,  15.1284    ,   2.966886  ],
                              [ 13.20839296,  11.99997859,   3.47005801],
                              [ 17.04840704,  11.99997859,   3.47005801],
                              [ 13.20839296,  18.25682141,   3.47005801],
                              [ 17.04840704,  18.25682141,   3.47005801],
                              [ 13.20839296,  13.20839296,   4.324536  ],
                              [ 17.04840704,  13.20839296,   4.324536  ],
                              [ 13.20839296,  17.04840704,   4.324536  ],
                              [ 17.04840704,  17.04840704,   4.324536  ],
                              [ 11.99997859,  13.20839296,   5.179014  ],
                              [ 18.25682141,  13.20839296,   5.179014  ],
                              [ 11.99997859,  17.04840704,   5.179014  ],
                              [ 18.25682141,  17.04840704,   5.179014  ],
                              [ 15.1284    ,  13.20839296,   5.682186  ],
                              [ 15.1284    ,  17.04840704,   5.682186  ],
                              [ 15.1284    ,  11.99997859,   6.536664  ],
                              [ 15.1284    ,  18.25682141,   6.536664  ],
                              [ 15.1284    ,  15.1284    ,   7.039836  ],
                              [ 11.99997859,  15.1284    ,   7.54300801],
                              [ 18.25682141,  15.1284    ,   7.54300801],
                              [ 13.20839296,  15.1284    ,   8.397486  ],
                              [ 17.04840704,  15.1284    ,   8.397486  ],
                              [ 13.20839296,  11.99997859,   8.90065801],
                              [ 17.04840704,  11.99997859,   8.90065801],
                              [ 13.20839296,  18.25682141,   8.90065801],
                              [ 17.04840704,  18.25682141,   8.90065801],
                              [ 13.20839296,  13.20839296,   9.755136  ],
                              [ 17.04840704,  13.20839296,   9.755136  ],
                              [ 13.20839296,  17.04840704,   9.755136  ],
                              [ 17.04840704,  17.04840704,   9.755136  ],
                              [ 11.99997859,  13.20839296,  10.609614  ],
                              [ 18.25682141,  13.20839296,  10.609614  ],
                              [ 11.99997859,  17.04840704,  10.609614  ],
                              [ 18.25682141,  17.04840704,  10.609614  ]]*Angstrom

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
vector_c = [0.0, 0.0, 16.2918]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                            Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                            Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                            Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                            Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                            Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
right_electrode_coordinates = [[ 15.1284    ,  13.20839296,   0.251586  ],
                               [ 15.1284    ,  17.04840704,   0.251586  ],
                               [ 15.1284    ,  11.99997859,   1.106064  ],
                               [ 15.1284    ,  18.25682141,   1.106064  ],
                               [ 15.1284    ,  15.1284    ,   1.609236  ],
                               [ 11.99997859,  15.1284    ,   2.11240801],
                               [ 18.25682141,  15.1284    ,   2.11240801],
                               [ 13.20839296,  15.1284    ,   2.966886  ],
                               [ 17.04840704,  15.1284    ,   2.966886  ],
                               [ 13.20839296,  11.99997859,   3.47005801],
                               [ 17.04840704,  11.99997859,   3.47005801],
                               [ 13.20839296,  18.25682141,   3.47005801],
                               [ 17.04840704,  18.25682141,   3.47005801],
                               [ 13.20839296,  13.20839296,   4.324536  ],
                               [ 17.04840704,  13.20839296,   4.324536  ],
                               [ 13.20839296,  17.04840704,   4.324536  ],
                               [ 17.04840704,  17.04840704,   4.324536  ],
                               [ 11.99997859,  13.20839296,   5.179014  ],
                               [ 18.25682141,  13.20839296,   5.179014  ],
                               [ 11.99997859,  17.04840704,   5.179014  ],
                               [ 18.25682141,  17.04840704,   5.179014  ],
                               [ 15.1284    ,  13.20839296,   5.682186  ],
                               [ 15.1284    ,  17.04840704,   5.682186  ],
                               [ 15.1284    ,  11.99997859,   6.536664  ],
                               [ 15.1284    ,  18.25682141,   6.536664  ],
                               [ 15.1284    ,  15.1284    ,   7.039836  ],
                               [ 11.99997859,  15.1284    ,   7.54300801],
                               [ 18.25682141,  15.1284    ,   7.54300801],
                               [ 13.20839296,  15.1284    ,   8.397486  ],
                               [ 17.04840704,  15.1284    ,   8.397486  ],
                               [ 13.20839296,  11.99997859,   8.90065801],
                               [ 17.04840704,  11.99997859,   8.90065801],
                               [ 13.20839296,  18.25682141,   8.90065801],
                               [ 17.04840704,  18.25682141,   8.90065801],
                               [ 13.20839296,  13.20839296,   9.755136  ],
                               [ 17.04840704,  13.20839296,   9.755136  ],
                               [ 13.20839296,  17.04840704,   9.755136  ],
                               [ 17.04840704,  17.04840704,   9.755136  ],
                               [ 11.99997859,  13.20839296,  10.609614  ],
                               [ 18.25682141,  13.20839296,  10.609614  ],
                               [ 11.99997859,  17.04840704,  10.609614  ],
                               [ 18.25682141,  17.04840704,  10.609614  ],
                               [ 15.1284    ,  13.20839296,  11.112786  ],
                               [ 15.1284    ,  17.04840704,  11.112786  ],
                               [ 15.1284    ,  11.99997859,  11.967264  ],
                               [ 15.1284    ,  18.25682141,  11.967264  ],
                               [ 15.1284    ,  15.1284    ,  12.470436  ],
                               [ 11.99997859,  15.1284    ,  12.97360801],
                               [ 18.25682141,  15.1284    ,  12.97360801],
                               [ 13.20839296,  15.1284    ,  13.828086  ],
                               [ 17.04840704,  15.1284    ,  13.828086  ],
                               [ 13.20839296,  11.99997859,  14.33125801],
                               [ 17.04840704,  11.99997859,  14.33125801],
                               [ 13.20839296,  18.25682141,  14.33125801],
                               [ 17.04840704,  18.25682141,  14.33125801],
                               [ 13.20839296,  13.20839296,  15.185736  ],
                               [ 17.04840704,  13.20839296,  15.185736  ],
                               [ 13.20839296,  17.04840704,  15.185736  ],
                               [ 17.04840704,  17.04840704,  15.185736  ],
                               [ 11.99997859,  13.20839296,  16.040214  ],
                               [ 18.25682141,  13.20839296,  16.040214  ],
                               [ 11.99997859,  17.04840704,  16.040214  ],
                               [ 18.25682141,  17.04840704,  16.040214  ]]*Angstrom

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
vector_c = [0.0, 0.0, 59.7366]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen, Hydrogen,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
central_region_coordinates = [[ 15.1284    ,  13.20839296,   0.251586  ],
                              [ 15.1284    ,  17.04840704,   0.251586  ],
                              [ 15.1284    ,  11.99997859,   1.106064  ],
                              [ 15.1284    ,  18.25682141,   1.106064  ],
                              [ 15.1284    ,  15.1284    ,   1.609236  ],
                              [ 11.99997859,  15.1284    ,   2.11240801],
                              [ 18.25682141,  15.1284    ,   2.11240801],
                              [ 13.20839296,  15.1284    ,   2.966886  ],
                              [ 17.04840704,  15.1284    ,   2.966886  ],
                              [ 13.20839296,  11.99997859,   3.47005801],
                              [ 17.04840704,  11.99997859,   3.47005801],
                              [ 13.20839296,  18.25682141,   3.47005801],
                              [ 17.04840704,  18.25682141,   3.47005801],
                              [ 13.20839296,  13.20839296,   4.324536  ],
                              [ 17.04840704,  13.20839296,   4.324536  ],
                              [ 13.20839296,  17.04840704,   4.324536  ],
                              [ 17.04840704,  17.04840704,   4.324536  ],
                              [ 11.99997859,  13.20839296,   5.179014  ],
                              [ 18.25682141,  13.20839296,   5.179014  ],
                              [ 11.99997859,  17.04840704,   5.179014  ],
                              [ 18.25682141,  17.04840704,   5.179014  ],
                              [ 15.1284    ,  13.20839296,   5.682186  ],
                              [ 15.1284    ,  17.04840704,   5.682186  ],
                              [ 15.1284    ,  11.99997859,   6.536664  ],
                              [ 15.1284    ,  18.25682141,   6.536664  ],
                              [ 15.1284    ,  15.1284    ,   7.039836  ],
                              [ 11.99997859,  15.1284    ,   7.54300801],
                              [ 18.25682141,  15.1284    ,   7.54300801],
                              [ 13.20839296,  15.1284    ,   8.397486  ],
                              [ 17.04840704,  15.1284    ,   8.397486  ],
                              [ 13.20839296,  11.99997859,   8.90065801],
                              [ 17.04840704,  11.99997859,   8.90065801],
                              [ 13.20839296,  18.25682141,   8.90065801],
                              [ 17.04840704,  18.25682141,   8.90065801],
                              [ 13.20839296,  13.20839296,   9.755136  ],
                              [ 17.04840704,  13.20839296,   9.755136  ],
                              [ 13.20839296,  17.04840704,   9.755136  ],
                              [ 17.04840704,  17.04840704,   9.755136  ],
                              [ 11.99997859,  13.20839296,  10.609614  ],
                              [ 18.25682141,  13.20839296,  10.609614  ],
                              [ 11.99997859,  17.04840704,  10.609614  ],
                              [ 18.25682141,  17.04840704,  10.609614  ],
                              [ 15.1284    ,  13.20839296,  11.112786  ],
                              [ 15.1284    ,  17.04840704,  11.112786  ],
                              [ 15.1284    ,  11.99997859,  11.967264  ],
                              [ 15.1284    ,  18.25682141,  11.967264  ],
                              [ 15.1284    ,  15.1284    ,  12.470436  ],
                              [ 11.99997859,  15.1284    ,  12.97360801],
                              [ 18.25682141,  15.1284    ,  12.97360801],
                              [ 13.20839296,  15.1284    ,  13.828086  ],
                              [ 17.04840704,  15.1284    ,  13.828086  ],
                              [ 13.20839296,  11.99997859,  14.33125801],
                              [ 17.04840704,  11.99997859,  14.33125801],
                              [ 13.20839296,  18.25682141,  14.33125801],
                              [ 17.04840704,  18.25682141,  14.33125801],
                              [ 13.20839296,  13.20839296,  15.185736  ],
                              [ 17.04840704,  13.20839296,  15.185736  ],
                              [ 13.20839296,  17.04840704,  15.185736  ],
                              [ 17.04840704,  17.04840704,  15.185736  ],
                              [ 11.99997859,  13.20839296,  16.040214  ],
                              [ 18.25682141,  13.20839296,  16.040214  ],
                              [ 11.99997859,  17.04840704,  16.040214  ],
                              [ 18.25682141,  17.04840704,  16.040214  ],
                              [ 15.1284    ,  13.20839296,  16.543386  ],
                              [ 15.1284    ,  17.04840704,  16.543386  ],
                              [ 15.1284    ,  11.99997859,  17.397864  ],
                              [ 15.1284    ,  18.25682141,  17.397864  ],
                              [ 15.1284    ,  15.1284    ,  17.901036  ],
                              [ 11.99997859,  15.1284    ,  18.40420801],
                              [ 18.25682141,  15.1284    ,  18.40420801],
                              [ 13.20839296,  15.1284    ,  19.258686  ],
                              [ 17.04840704,  15.1284    ,  19.258686  ],
                              [ 13.20839296,  11.99997859,  19.76185801],
                              [ 17.04840704,  11.99997859,  19.76185801],
                              [ 13.20839296,  18.25682141,  19.76185801],
                              [ 17.04840704,  18.25682141,  19.76185801],
                              [ 13.20839296,  13.20839296,  20.616336  ],
                              [ 17.04840704,  13.20839296,  20.616336  ],
                              [ 13.20839296,  17.04840704,  20.616336  ],
                              [ 17.04840704,  17.04840704,  20.616336  ],
                              [ 11.99997859,  13.20839296,  21.470814  ],
                              [ 18.25682141,  13.20839296,  21.470814  ],
                              [ 11.99997859,  17.04840704,  21.470814  ],
                              [ 18.25682141,  17.04840704,  21.470814  ],
                              [ 15.1284    ,  13.20839296,  21.973986  ],
                              [ 15.1284    ,  17.04840704,  21.973986  ],
                              [ 15.1284    ,  11.99997859,  22.828464  ],
                              [ 15.1284    ,  18.25682141,  22.828464  ],
                              [ 15.1284    ,  15.1284    ,  23.331636  ],
                              [ 11.99997859,  15.1284    ,  23.83480801],
                              [ 18.25682141,  15.1284    ,  23.83480801],
                              [ 13.20839296,  15.1284    ,  24.689286  ],
                              [ 17.04840704,  15.1284    ,  24.689286  ],
                              [ 13.20839296,  11.99997859,  25.19245801],
                              [ 17.04840704,  11.99997859,  25.19245801],
                              [ 13.20839296,  18.25682141,  25.19245801],
                              [ 17.04840704,  18.25682141,  25.19245801],
                              [ 13.20839296,  13.20839296,  26.046936  ],
                              [ 17.04840704,  13.20839296,  26.046936  ],
                              [ 13.20839296,  17.04840704,  26.046936  ],
                              [ 17.04840704,  17.04840704,  26.046936  ],
                              [ 11.99997859,  13.20839296,  26.901414  ],
                              [ 18.25682141,  13.20839296,  26.901414  ],
                              [ 11.99997859,  17.04840704,  26.901414  ],
                              [ 18.25682141,  17.04840704,  26.901414  ],
                              [ 15.1284    ,  13.20839296,  27.404586  ],
                              [ 15.1284    ,  17.04840704,  27.404586  ],
                              [ 15.1284    ,  11.99997859,  28.259064  ],
                              [ 15.1284    ,  18.25682141,  28.259064  ],
                              [ 15.1284    ,  15.1284    ,  28.762236  ],
                              [ 11.99997859,  15.1284    ,  29.26540801],
                              [ 18.25682141,  15.1284    ,  29.26540801],
                              [ 13.20839296,  15.1284    ,  30.119886  ],
                              [ 17.04840704,  15.1284    ,  30.119886  ],
                              [ 13.20839296,  11.99997859,  30.62305801],
                              [ 17.04840704,  11.99997859,  30.62305801],
                              [ 13.20839296,  18.25682141,  30.62305801],
                              [ 17.04840704,  18.25682141,  30.62305801],
                              [ 13.20839296,  13.20839296,  31.477536  ],
                              [ 17.04840704,  13.20839296,  31.477536  ],
                              [ 13.20839296,  17.04840704,  31.477536  ],
                              [ 17.04840704,  17.04840704,  31.477536  ],
                              [ 11.99997859,  13.20839296,  32.332014  ],
                              [ 18.25682141,  13.20839296,  32.332014  ],
                              [ 11.99997859,  17.04840704,  32.332014  ],
                              [ 18.25682141,  17.04840704,  32.332014  ],
                              [ 15.1284    ,  13.20839296,  32.835186  ],
                              [ 15.1284    ,  17.04840704,  32.835186  ],
                              [ 15.1284    ,  11.99997859,  33.689664  ],
                              [ 15.1284    ,  18.25682141,  33.689664  ],
                              [ 15.1284    ,  15.1284    ,  34.192836  ],
                              [ 11.99997859,  15.1284    ,  34.69600801],
                              [ 18.25682141,  15.1284    ,  34.69600801],
                              [ 13.20839296,  15.1284    ,  35.550486  ],
                              [ 17.04840704,  15.1284    ,  35.550486  ],
                              [ 13.20839296,  11.99997859,  36.05365801],
                              [ 17.04840704,  11.99997859,  36.05365801],
                              [ 13.20839296,  18.25682141,  36.05365801],
                              [ 17.04840704,  18.25682141,  36.05365801],
                              [ 13.20839296,  13.20839296,  36.908136  ],
                              [ 17.04840704,  13.20839296,  36.908136  ],
                              [ 13.20839296,  17.04840704,  36.908136  ],
                              [ 17.04840704,  17.04840704,  36.908136  ],
                              [ 11.99997859,  13.20839296,  37.762614  ],
                              [ 18.25682141,  13.20839296,  37.762614  ],
                              [ 11.99997859,  17.04840704,  37.762614  ],
                              [ 18.25682141,  17.04840704,  37.762614  ],
                              [ 15.1284    ,  13.20839296,  38.265786  ],
                              [ 15.1284    ,  17.04840704,  38.265786  ],
                              [ 15.1284    ,  11.99997859,  39.120264  ],
                              [ 15.1284    ,  18.25682141,  39.120264  ],
                              [ 15.1284    ,  15.1284    ,  39.623436  ],
                              [ 11.99997859,  15.1284    ,  40.12660801],
                              [ 18.25682141,  15.1284    ,  40.12660801],
                              [ 13.20839296,  15.1284    ,  40.981086  ],
                              [ 17.04840704,  15.1284    ,  40.981086  ],
                              [ 13.20839296,  11.99997859,  41.48425801],
                              [ 17.04840704,  11.99997859,  41.48425801],
                              [ 13.20839296,  18.25682141,  41.48425801],
                              [ 17.04840704,  18.25682141,  41.48425801],
                              [ 13.20839296,  13.20839296,  42.338736  ],
                              [ 17.04840704,  13.20839296,  42.338736  ],
                              [ 13.20839296,  17.04840704,  42.338736  ],
                              [ 17.04840704,  17.04840704,  42.338736  ],
                              [ 11.99997859,  13.20839296,  43.193214  ],
                              [ 18.25682141,  13.20839296,  43.193214  ],
                              [ 11.99997859,  17.04840704,  43.193214  ],
                              [ 18.25682141,  17.04840704,  43.193214  ],
                              [ 15.1284    ,  13.20839296,  43.696386  ],
                              [ 15.1284    ,  17.04840704,  43.696386  ],
                              [ 15.1284    ,  11.99997859,  44.550864  ],
                              [ 15.1284    ,  18.25682141,  44.550864  ],
                              [ 15.1284    ,  15.1284    ,  45.054036  ],
                              [ 11.99997859,  15.1284    ,  45.55720801],
                              [ 18.25682141,  15.1284    ,  45.55720801],
                              [ 13.20839296,  15.1284    ,  46.411686  ],
                              [ 17.04840704,  15.1284    ,  46.411686  ],
                              [ 13.20839296,  11.99997859,  46.91485801],
                              [ 17.04840704,  11.99997859,  46.91485801],
                              [ 13.20839296,  18.25682141,  46.91485801],
                              [ 17.04840704,  18.25682141,  46.91485801],
                              [ 13.20839296,  13.20839296,  47.769336  ],
                              [ 17.04840704,  13.20839296,  47.769336  ],
                              [ 13.20839296,  17.04840704,  47.769336  ],
                              [ 17.04840704,  17.04840704,  47.769336  ],
                              [ 11.99997859,  13.20839296,  48.623814  ],
                              [ 18.25682141,  13.20839296,  48.623814  ],
                              [ 11.99997859,  17.04840704,  48.623814  ],
                              [ 18.25682141,  17.04840704,  48.623814  ],
                              [ 15.1284    ,  13.20839296,  49.126986  ],
                              [ 15.1284    ,  17.04840704,  49.126986  ],
                              [ 15.1284    ,  11.99997859,  49.981464  ],
                              [ 15.1284    ,  18.25682141,  49.981464  ],
                              [ 15.1284    ,  15.1284    ,  50.484636  ],
                              [ 11.99997859,  15.1284    ,  50.98780801],
                              [ 18.25682141,  15.1284    ,  50.98780801],
                              [ 13.20839296,  15.1284    ,  51.842286  ],
                              [ 17.04840704,  15.1284    ,  51.842286  ],
                              [ 13.20839296,  11.99997859,  52.34545801],
                              [ 17.04840704,  11.99997859,  52.34545801],
                              [ 13.20839296,  18.25682141,  52.34545801],
                              [ 17.04840704,  18.25682141,  52.34545801],
                              [ 13.20839296,  13.20839296,  53.199936  ],
                              [ 17.04840704,  13.20839296,  53.199936  ],
                              [ 13.20839296,  17.04840704,  53.199936  ],
                              [ 17.04840704,  17.04840704,  53.199936  ],
                              [ 11.99997859,  13.20839296,  54.054414  ],
                              [ 18.25682141,  13.20839296,  54.054414  ],
                              [ 11.99997859,  17.04840704,  54.054414  ],
                              [ 18.25682141,  17.04840704,  54.054414  ],
                              [ 15.1284    ,  13.20839296,  54.557586  ],
                              [ 15.1284    ,  17.04840704,  54.557586  ],
                              [ 15.1284    ,  11.99997859,  55.412064  ],
                              [ 15.1284    ,  18.25682141,  55.412064  ],
                              [ 15.1284    ,  15.1284    ,  55.915236  ],
                              [ 11.99997859,  15.1284    ,  56.41840801],
                              [ 18.25682141,  15.1284    ,  56.41840801],
                              [ 13.20839296,  15.1284    ,  57.272886  ],
                              [ 17.04840704,  15.1284    ,  57.272886  ],
                              [ 13.20839296,  11.99997859,  57.77605801],
                              [ 17.04840704,  11.99997859,  57.77605801],
                              [ 13.20839296,  18.25682141,  57.77605801],
                              [ 17.04840704,  18.25682141,  57.77605801],
                              [ 13.20839296,  13.20839296,  58.630536  ],
                              [ 17.04840704,  13.20839296,  58.630536  ],
                              [ 13.20839296,  17.04840704,  58.630536  ],
                              [ 17.04840704,  17.04840704,  58.630536  ],
                              [ 11.99997859,  13.20839296,  59.485014  ],
                              [ 18.25682141,  13.20839296,  59.485014  ],
                              [ 11.99997859,  17.04840704,  59.485014  ],
                              [ 18.25682141,  17.04840704,  59.485014  ]]*Angstrom

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

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  19.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  19.25682141 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  19.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  19.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.99997859 *Angstrom,  xmax =  0.99997859 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  19.25682141 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.25682141 *Angstrom,  xmax =  29.25682141 *Angstrom,
        ymin =  10.99997859 *Angstrom,  ymax =  0.99997859 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.99997859 *Angstrom,  xmax =  -2.14100000004e-05 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.14100000004e-05 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  29.25682141 *Angstrom,  ymax =  30.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.25682141 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  29.25682141 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.14100000004e-05 *Angstrom,  xmax =  30.25682141 *Angstrom,
        ymin =  0.99997859 *Angstrom,  ymax =  -2.14100000004e-05 *Angstrom,
        zmin =  9.742507 *Angstrom,  zmax =  49.742507 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


#x = (5e20 cm^-3) * (6.25Angstrom * 6.25Angstrom * 16.29Angstrom)
charge = 0.319
temp = 300
