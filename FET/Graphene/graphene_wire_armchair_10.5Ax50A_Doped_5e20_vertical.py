# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 34.5014, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon]

# Define coordinates
left_electrode_coordinates = [[ 12.        ,  12.94394701,   0.71043   ],
                              [ 12.        ,  15.40494872,   0.71043   ],
                              [ 12.        ,  17.86595043,   0.71043   ],
                              [ 12.        ,  20.32695214,   0.71043   ],
                              [ 12.        ,  22.50142024,   0.87586026],
                              [ 12.        ,  11.99997976,   1.25542974],
                              [ 12.        ,  14.17444786,   1.42086   ],
                              [ 12.        ,  16.63544957,   1.42086   ],
                              [ 12.        ,  19.09645128,   1.42086   ],
                              [ 12.        ,  21.55745299,   1.42086   ],
                              [ 12.        ,  14.17444786,   2.84172   ],
                              [ 12.        ,  16.63544957,   2.84172   ],
                              [ 12.        ,  19.09645128,   2.84172   ],
                              [ 12.        ,  21.55745299,   2.84172   ],
                              [ 12.        ,  11.99997976,   3.00715026],
                              [ 12.        ,  22.50142024,   3.38671974],
                              [ 12.        ,  12.94394701,   3.55215   ],
                              [ 12.        ,  15.40494872,   3.55215   ],
                              [ 12.        ,  17.86595043,   3.55215   ],
                              [ 12.        ,  20.32695214,   3.55215   ],
                              [ 12.        ,  12.94394701,   4.97301   ],
                              [ 12.        ,  15.40494872,   4.97301   ],
                              [ 12.        ,  17.86595043,   4.97301   ],
                              [ 12.        ,  20.32695214,   4.97301   ],
                              [ 12.        ,  22.50142024,   5.13844026],
                              [ 12.        ,  11.99997976,   5.51800974],
                              [ 12.        ,  14.17444786,   5.68344   ],
                              [ 12.        ,  16.63544957,   5.68344   ],
                              [ 12.        ,  19.09645128,   5.68344   ],
                              [ 12.        ,  21.55745299,   5.68344   ],
                              [ 12.        ,  14.17444786,   7.1043    ],
                              [ 12.        ,  16.63544957,   7.1043    ],
                              [ 12.        ,  19.09645128,   7.1043    ],
                              [ 12.        ,  21.55745299,   7.1043    ],
                              [ 12.        ,  11.99997976,   7.26973026],
                              [ 12.        ,  22.50142024,   7.64929974],
                              [ 12.        ,  12.94394701,   7.81473   ],
                              [ 12.        ,  15.40494872,   7.81473   ],
                              [ 12.        ,  17.86595043,   7.81473   ],
                              [ 12.        ,  20.32695214,   7.81473   ]]*Angstrom

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
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 34.5014, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.52516]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                            Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                            Carbon, Carbon, Carbon]

# Define coordinates
right_electrode_coordinates = [[ 12.        ,  12.94394701,   0.71043   ],
                               [ 12.        ,  15.40494872,   0.71043   ],
                               [ 12.        ,  17.86595043,   0.71043   ],
                               [ 12.        ,  20.32695214,   0.71043   ],
                               [ 12.        ,  22.50142024,   0.87586026],
                               [ 12.        ,  11.99997976,   1.25542974],
                               [ 12.        ,  14.17444786,   1.42086   ],
                               [ 12.        ,  16.63544957,   1.42086   ],
                               [ 12.        ,  19.09645128,   1.42086   ],
                               [ 12.        ,  21.55745299,   1.42086   ],
                               [ 12.        ,  14.17444786,   2.84172   ],
                               [ 12.        ,  16.63544957,   2.84172   ],
                               [ 12.        ,  19.09645128,   2.84172   ],
                               [ 12.        ,  21.55745299,   2.84172   ],
                               [ 12.        ,  11.99997976,   3.00715026],
                               [ 12.        ,  22.50142024,   3.38671974],
                               [ 12.        ,  12.94394701,   3.55215   ],
                               [ 12.        ,  15.40494872,   3.55215   ],
                               [ 12.        ,  17.86595043,   3.55215   ],
                               [ 12.        ,  20.32695214,   3.55215   ],
                               [ 12.        ,  12.94394701,   4.97301   ],
                               [ 12.        ,  15.40494872,   4.97301   ],
                               [ 12.        ,  17.86595043,   4.97301   ],
                               [ 12.        ,  20.32695214,   4.97301   ],
                               [ 12.        ,  22.50142024,   5.13844026],
                               [ 12.        ,  11.99997976,   5.51800974],
                               [ 12.        ,  14.17444786,   5.68344   ],
                               [ 12.        ,  16.63544957,   5.68344   ],
                               [ 12.        ,  19.09645128,   5.68344   ],
                               [ 12.        ,  21.55745299,   5.68344   ],
                               [ 12.        ,  14.17444786,   7.1043    ],
                               [ 12.        ,  16.63544957,   7.1043    ],
                               [ 12.        ,  19.09645128,   7.1043    ],
                               [ 12.        ,  21.55745299,   7.1043    ],
                               [ 12.        ,  11.99997976,   7.26973026],
                               [ 12.        ,  22.50142024,   7.64929974],
                               [ 12.        ,  12.94394701,   7.81473   ],
                               [ 12.        ,  15.40494872,   7.81473   ],
                               [ 12.        ,  17.86595043,   7.81473   ],
                               [ 12.        ,  20.32695214,   7.81473   ]]*Angstrom

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
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 34.5014, 0.0]*Angstrom
vector_c = [0.0, 0.0, 51.15096]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
central_region_coordinates = [[ 12.        ,  12.94394701,   0.71043   ],
                              [ 12.        ,  15.40494872,   0.71043   ],
                              [ 12.        ,  17.86595043,   0.71043   ],
                              [ 12.        ,  20.32695214,   0.71043   ],
                              [ 12.        ,  22.50142024,   0.87586026],
                              [ 12.        ,  11.99997976,   1.25542974],
                              [ 12.        ,  14.17444786,   1.42086   ],
                              [ 12.        ,  16.63544957,   1.42086   ],
                              [ 12.        ,  19.09645128,   1.42086   ],
                              [ 12.        ,  21.55745299,   1.42086   ],
                              [ 12.        ,  14.17444786,   2.84172   ],
                              [ 12.        ,  16.63544957,   2.84172   ],
                              [ 12.        ,  19.09645128,   2.84172   ],
                              [ 12.        ,  21.55745299,   2.84172   ],
                              [ 12.        ,  11.99997976,   3.00715026],
                              [ 12.        ,  22.50142024,   3.38671974],
                              [ 12.        ,  12.94394701,   3.55215   ],
                              [ 12.        ,  15.40494872,   3.55215   ],
                              [ 12.        ,  17.86595043,   3.55215   ],
                              [ 12.        ,  20.32695214,   3.55215   ],
                              [ 12.        ,  12.94394701,   4.97301   ],
                              [ 12.        ,  15.40494872,   4.97301   ],
                              [ 12.        ,  17.86595043,   4.97301   ],
                              [ 12.        ,  20.32695214,   4.97301   ],
                              [ 12.        ,  22.50142024,   5.13844026],
                              [ 12.        ,  11.99997976,   5.51800974],
                              [ 12.        ,  14.17444786,   5.68344   ],
                              [ 12.        ,  16.63544957,   5.68344   ],
                              [ 12.        ,  19.09645128,   5.68344   ],
                              [ 12.        ,  21.55745299,   5.68344   ],
                              [ 12.        ,  14.17444786,   7.1043    ],
                              [ 12.        ,  16.63544957,   7.1043    ],
                              [ 12.        ,  19.09645128,   7.1043    ],
                              [ 12.        ,  21.55745299,   7.1043    ],
                              [ 12.        ,  11.99997976,   7.26973026],
                              [ 12.        ,  22.50142024,   7.64929974],
                              [ 12.        ,  12.94394701,   7.81473   ],
                              [ 12.        ,  15.40494872,   7.81473   ],
                              [ 12.        ,  17.86595043,   7.81473   ],
                              [ 12.        ,  20.32695214,   7.81473   ],
                              [ 12.        ,  12.94394701,   9.23559   ],
                              [ 12.        ,  15.40494872,   9.23559   ],
                              [ 12.        ,  17.86595043,   9.23559   ],
                              [ 12.        ,  20.32695214,   9.23559   ],
                              [ 12.        ,  22.50142024,   9.40102026],
                              [ 12.        ,  11.99997976,   9.78058974],
                              [ 12.        ,  14.17444786,   9.94602   ],
                              [ 12.        ,  16.63544957,   9.94602   ],
                              [ 12.        ,  19.09645128,   9.94602   ],
                              [ 12.        ,  21.55745299,   9.94602   ],
                              [ 12.        ,  14.17444786,  11.36688   ],
                              [ 12.        ,  16.63544957,  11.36688   ],
                              [ 12.        ,  19.09645128,  11.36688   ],
                              [ 12.        ,  21.55745299,  11.36688   ],
                              [ 12.        ,  11.99997976,  11.53231026],
                              [ 12.        ,  22.50142024,  11.91187974],
                              [ 12.        ,  12.94394701,  12.07731   ],
                              [ 12.        ,  15.40494872,  12.07731   ],
                              [ 12.        ,  17.86595043,  12.07731   ],
                              [ 12.        ,  20.32695214,  12.07731   ],
                              [ 12.        ,  12.94394701,  13.49817   ],
                              [ 12.        ,  15.40494872,  13.49817   ],
                              [ 12.        ,  17.86595043,  13.49817   ],
                              [ 12.        ,  20.32695214,  13.49817   ],
                              [ 12.        ,  22.50142024,  13.66360026],
                              [ 12.        ,  11.99997976,  14.04316974],
                              [ 12.        ,  14.17444786,  14.2086    ],
                              [ 12.        ,  16.63544957,  14.2086    ],
                              [ 12.        ,  19.09645128,  14.2086    ],
                              [ 12.        ,  21.55745299,  14.2086    ],
                              [ 12.        ,  14.17444786,  15.62946   ],
                              [ 12.        ,  16.63544957,  15.62946   ],
                              [ 12.        ,  19.09645128,  15.62946   ],
                              [ 12.        ,  21.55745299,  15.62946   ],
                              [ 12.        ,  11.99997976,  15.79489026],
                              [ 12.        ,  22.50142024,  16.17445974],
                              [ 12.        ,  12.94394701,  16.33989   ],
                              [ 12.        ,  15.40494872,  16.33989   ],
                              [ 12.        ,  17.86595043,  16.33989   ],
                              [ 12.        ,  20.32695214,  16.33989   ],
                              [ 12.        ,  12.94394701,  17.76075   ],
                              [ 12.        ,  15.40494872,  17.76075   ],
                              [ 12.        ,  17.86595043,  17.76075   ],
                              [ 12.        ,  20.32695214,  17.76075   ],
                              [ 12.        ,  22.50142024,  17.92618026],
                              [ 12.        ,  11.99997976,  18.30574974],
                              [ 12.        ,  14.17444786,  18.47118   ],
                              [ 12.        ,  16.63544957,  18.47118   ],
                              [ 12.        ,  19.09645128,  18.47118   ],
                              [ 12.        ,  21.55745299,  18.47118   ],
                              [ 12.        ,  14.17444786,  19.89204   ],
                              [ 12.        ,  16.63544957,  19.89204   ],
                              [ 12.        ,  19.09645128,  19.89204   ],
                              [ 12.        ,  21.55745299,  19.89204   ],
                              [ 12.        ,  11.99997976,  20.05747026],
                              [ 12.        ,  22.50142024,  20.43703974],
                              [ 12.        ,  12.94394701,  20.60247   ],
                              [ 12.        ,  15.40494872,  20.60247   ],
                              [ 12.        ,  17.86595043,  20.60247   ],
                              [ 12.        ,  20.32695214,  20.60247   ],
                              [ 12.        ,  12.94394701,  22.02333   ],
                              [ 12.        ,  15.40494872,  22.02333   ],
                              [ 12.        ,  17.86595043,  22.02333   ],
                              [ 12.        ,  20.32695214,  22.02333   ],
                              [ 12.        ,  22.50142024,  22.18876026],
                              [ 12.        ,  11.99997976,  22.56832974],
                              [ 12.        ,  14.17444786,  22.73376   ],
                              [ 12.        ,  16.63544957,  22.73376   ],
                              [ 12.        ,  19.09645128,  22.73376   ],
                              [ 12.        ,  21.55745299,  22.73376   ],
                              [ 12.        ,  14.17444786,  24.15462   ],
                              [ 12.        ,  16.63544957,  24.15462   ],
                              [ 12.        ,  19.09645128,  24.15462   ],
                              [ 12.        ,  21.55745299,  24.15462   ],
                              [ 12.        ,  11.99997976,  24.32005026],
                              [ 12.        ,  22.50142024,  24.69961974],
                              [ 12.        ,  12.94394701,  24.86505   ],
                              [ 12.        ,  15.40494872,  24.86505   ],
                              [ 12.        ,  17.86595043,  24.86505   ],
                              [ 12.        ,  20.32695214,  24.86505   ],
                              [ 12.        ,  12.94394701,  26.28591   ],
                              [ 12.        ,  15.40494872,  26.28591   ],
                              [ 12.        ,  17.86595043,  26.28591   ],
                              [ 12.        ,  20.32695214,  26.28591   ],
                              [ 12.        ,  22.50142024,  26.45134026],
                              [ 12.        ,  11.99997976,  26.83090974],
                              [ 12.        ,  14.17444786,  26.99634   ],
                              [ 12.        ,  16.63544957,  26.99634   ],
                              [ 12.        ,  19.09645128,  26.99634   ],
                              [ 12.        ,  21.55745299,  26.99634   ],
                              [ 12.        ,  14.17444786,  28.4172    ],
                              [ 12.        ,  16.63544957,  28.4172    ],
                              [ 12.        ,  19.09645128,  28.4172    ],
                              [ 12.        ,  21.55745299,  28.4172    ],
                              [ 12.        ,  11.99997976,  28.58263026],
                              [ 12.        ,  22.50142024,  28.96219974],
                              [ 12.        ,  12.94394701,  29.12763   ],
                              [ 12.        ,  15.40494872,  29.12763   ],
                              [ 12.        ,  17.86595043,  29.12763   ],
                              [ 12.        ,  20.32695214,  29.12763   ],
                              [ 12.        ,  12.94394701,  30.54849   ],
                              [ 12.        ,  15.40494872,  30.54849   ],
                              [ 12.        ,  17.86595043,  30.54849   ],
                              [ 12.        ,  20.32695214,  30.54849   ],
                              [ 12.        ,  22.50142024,  30.71392026],
                              [ 12.        ,  11.99997976,  31.09348974],
                              [ 12.        ,  14.17444786,  31.25892   ],
                              [ 12.        ,  16.63544957,  31.25892   ],
                              [ 12.        ,  19.09645128,  31.25892   ],
                              [ 12.        ,  21.55745299,  31.25892   ],
                              [ 12.        ,  14.17444786,  32.67978   ],
                              [ 12.        ,  16.63544957,  32.67978   ],
                              [ 12.        ,  19.09645128,  32.67978   ],
                              [ 12.        ,  21.55745299,  32.67978   ],
                              [ 12.        ,  11.99997976,  32.84521026],
                              [ 12.        ,  22.50142024,  33.22477974],
                              [ 12.        ,  12.94394701,  33.39021   ],
                              [ 12.        ,  15.40494872,  33.39021   ],
                              [ 12.        ,  17.86595043,  33.39021   ],
                              [ 12.        ,  20.32695214,  33.39021   ],
                              [ 12.        ,  12.94394701,  34.81107   ],
                              [ 12.        ,  15.40494872,  34.81107   ],
                              [ 12.        ,  17.86595043,  34.81107   ],
                              [ 12.        ,  20.32695214,  34.81107   ],
                              [ 12.        ,  22.50142024,  34.97650026],
                              [ 12.        ,  11.99997976,  35.35606974],
                              [ 12.        ,  14.17444786,  35.5215    ],
                              [ 12.        ,  16.63544957,  35.5215    ],
                              [ 12.        ,  19.09645128,  35.5215    ],
                              [ 12.        ,  21.55745299,  35.5215    ],
                              [ 12.        ,  14.17444786,  36.94236   ],
                              [ 12.        ,  16.63544957,  36.94236   ],
                              [ 12.        ,  19.09645128,  36.94236   ],
                              [ 12.        ,  21.55745299,  36.94236   ],
                              [ 12.        ,  11.99997976,  37.10779026],
                              [ 12.        ,  22.50142024,  37.48735974],
                              [ 12.        ,  12.94394701,  37.65279   ],
                              [ 12.        ,  15.40494872,  37.65279   ],
                              [ 12.        ,  17.86595043,  37.65279   ],
                              [ 12.        ,  20.32695214,  37.65279   ],
                              [ 12.        ,  12.94394701,  39.07365   ],
                              [ 12.        ,  15.40494872,  39.07365   ],
                              [ 12.        ,  17.86595043,  39.07365   ],
                              [ 12.        ,  20.32695214,  39.07365   ],
                              [ 12.        ,  22.50142024,  39.23908026],
                              [ 12.        ,  11.99997976,  39.61864974],
                              [ 12.        ,  14.17444786,  39.78408   ],
                              [ 12.        ,  16.63544957,  39.78408   ],
                              [ 12.        ,  19.09645128,  39.78408   ],
                              [ 12.        ,  21.55745299,  39.78408   ],
                              [ 12.        ,  14.17444786,  41.20494   ],
                              [ 12.        ,  16.63544957,  41.20494   ],
                              [ 12.        ,  19.09645128,  41.20494   ],
                              [ 12.        ,  21.55745299,  41.20494   ],
                              [ 12.        ,  11.99997976,  41.37037026],
                              [ 12.        ,  22.50142024,  41.74993974],
                              [ 12.        ,  12.94394701,  41.91537   ],
                              [ 12.        ,  15.40494872,  41.91537   ],
                              [ 12.        ,  17.86595043,  41.91537   ],
                              [ 12.        ,  20.32695214,  41.91537   ],
                              [ 12.        ,  12.94394701,  43.33623   ],
                              [ 12.        ,  15.40494872,  43.33623   ],
                              [ 12.        ,  17.86595043,  43.33623   ],
                              [ 12.        ,  20.32695214,  43.33623   ],
                              [ 12.        ,  22.50142024,  43.50166026],
                              [ 12.        ,  11.99997976,  43.88122974],
                              [ 12.        ,  14.17444786,  44.04666   ],
                              [ 12.        ,  16.63544957,  44.04666   ],
                              [ 12.        ,  19.09645128,  44.04666   ],
                              [ 12.        ,  21.55745299,  44.04666   ],
                              [ 12.        ,  14.17444786,  45.46752   ],
                              [ 12.        ,  16.63544957,  45.46752   ],
                              [ 12.        ,  19.09645128,  45.46752   ],
                              [ 12.        ,  21.55745299,  45.46752   ],
                              [ 12.        ,  11.99997976,  45.63295026],
                              [ 12.        ,  22.50142024,  46.01251974],
                              [ 12.        ,  12.94394701,  46.17795   ],
                              [ 12.        ,  15.40494872,  46.17795   ],
                              [ 12.        ,  17.86595043,  46.17795   ],
                              [ 12.        ,  20.32695214,  46.17795   ],
                              [ 12.        ,  12.94394701,  47.59881   ],
                              [ 12.        ,  15.40494872,  47.59881   ],
                              [ 12.        ,  17.86595043,  47.59881   ],
                              [ 12.        ,  20.32695214,  47.59881   ],
                              [ 12.        ,  22.50142024,  47.76424026],
                              [ 12.        ,  11.99997976,  48.14380974],
                              [ 12.        ,  14.17444786,  48.30924   ],
                              [ 12.        ,  16.63544957,  48.30924   ],
                              [ 12.        ,  19.09645128,  48.30924   ],
                              [ 12.        ,  21.55745299,  48.30924   ],
                              [ 12.        ,  14.17444786,  49.7301    ],
                              [ 12.        ,  16.63544957,  49.7301    ],
                              [ 12.        ,  19.09645128,  49.7301    ],
                              [ 12.        ,  21.55745299,  49.7301    ],
                              [ 12.        ,  11.99997976,  49.89553026],
                              [ 12.        ,  22.50142024,  50.27509974],
                              [ 12.        ,  12.94394701,  50.44053   ],
                              [ 12.        ,  15.40494872,  50.44053   ],
                              [ 12.        ,  17.86595043,  50.44053   ],
                              [ 12.        ,  20.32695214,  50.44053   ]]*Angstrom

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
        xmin =  1.0 *Angstrom,  xmax =  11.0 *Angstrom,
        ymin =  10.99997976 *Angstrom,  ymax =  23.50142024 *Angstrom,
        zmin =  10.220265 *Angstrom,  zmax =  40.220265 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  23.0 *Angstrom,  xmax =  13.0 *Angstrom,
        ymin =  10.99997976 *Angstrom,  ymax =  23.50142024 *Angstrom,
        zmin =  10.220265 *Angstrom,  zmax =  40.220265 *Angstrom,
)


dielectric_regions = [dielectric_region_0, dielectric_region_1]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  10.99997976 *Angstrom,  ymax =  23.50142024 *Angstrom,
        zmin =  10.220265 *Angstrom,  zmax =  40.220265 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  23.0 *Angstrom,  xmax =  24.0 *Angstrom,
        ymin =  10.99997976 *Angstrom,  ymax =  23.50142024 *Angstrom,
        zmin =  10.220265 *Angstrom,  zmax =  40.220265 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1]
central_region.setMetallicRegions(metallic_regions)

basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]

#charge = (10.5Angstrom * 2Angstrom * 8.53Angstrom) * (5e20 cm^-3)
charge = 0.0896
temp = 300


