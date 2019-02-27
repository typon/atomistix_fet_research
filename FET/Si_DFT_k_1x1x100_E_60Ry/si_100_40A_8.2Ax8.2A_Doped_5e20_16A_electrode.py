# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [32.176, 0.0, 0.0]*Angstrom
vector_b = [0.0, 32.176, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.8612]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen]

# Define coordinates
left_electrode_coordinates = [[ 11.99957506,  13.20798944,   0.175653  ],
                              [ 11.99957506,  17.04800352,   0.175653  ],
                              [ 15.12799648,  13.20798944,   0.678825  ],
                              [ 18.96801056,  13.20798944,   0.678825  ],
                              [ 15.12799648,  17.04800352,   0.678825  ],
                              [ 18.96801056,  17.04800352,   0.678825  ],
                              [ 15.12799648,  20.17642494,   1.181997  ],
                              [ 18.96801056,  20.17642494,   1.181997  ],
                              [ 15.12799648,  11.99957506,   1.533303  ],
                              [ 18.96801056,  11.99957506,   1.533303  ],
                              [ 15.12799648,  15.12799648,   2.036475  ],
                              [ 18.96801056,  15.12799648,   2.036475  ],
                              [ 15.12799648,  18.96801056,   2.036475  ],
                              [ 18.96801056,  18.96801056,   2.036475  ],
                              [ 11.99957506,  15.12799648,   2.539647  ],
                              [ 11.99957506,  18.96801056,   2.539647  ],
                              [ 20.17642494,  15.12799648,   2.890953  ],
                              [ 20.17642494,  18.96801056,   2.890953  ],
                              [ 13.20798944,  15.12799648,   3.394125  ],
                              [ 17.04800352,  15.12799648,   3.394125  ],
                              [ 13.20798944,  18.96801056,   3.394125  ],
                              [ 17.04800352,  18.96801056,   3.394125  ],
                              [ 13.20798944,  11.99957506,   3.897297  ],
                              [ 17.04800352,  11.99957506,   3.897297  ],
                              [ 13.20798944,  20.17642494,   4.248603  ],
                              [ 17.04800352,  20.17642494,   4.248603  ],
                              [ 13.20798944,  13.20798944,   4.751775  ],
                              [ 17.04800352,  13.20798944,   4.751775  ],
                              [ 13.20798944,  17.04800352,   4.751775  ],
                              [ 17.04800352,  17.04800352,   4.751775  ],
                              [ 20.17642494,  13.20798944,   5.254947  ],
                              [ 20.17642494,  17.04800352,   5.254947  ],
                              [ 11.99957506,  13.20798944,   5.606253  ],
                              [ 11.99957506,  17.04800352,   5.606253  ],
                              [ 15.12799648,  13.20798944,   6.109425  ],
                              [ 18.96801056,  13.20798944,   6.109425  ],
                              [ 15.12799648,  17.04800352,   6.109425  ],
                              [ 18.96801056,  17.04800352,   6.109425  ],
                              [ 15.12799648,  20.17642494,   6.612597  ],
                              [ 18.96801056,  20.17642494,   6.612597  ],
                              [ 15.12799648,  11.99957506,   6.963903  ],
                              [ 18.96801056,  11.99957506,   6.963903  ],
                              [ 15.12799648,  15.12799648,   7.467075  ],
                              [ 18.96801056,  15.12799648,   7.467075  ],
                              [ 15.12799648,  18.96801056,   7.467075  ],
                              [ 18.96801056,  18.96801056,   7.467075  ],
                              [ 11.99957506,  15.12799648,   7.970247  ],
                              [ 11.99957506,  18.96801056,   7.970247  ],
                              [ 20.17642494,  15.12799648,   8.321553  ],
                              [ 20.17642494,  18.96801056,   8.321553  ],
                              [ 13.20798944,  15.12799648,   8.824725  ],
                              [ 17.04800352,  15.12799648,   8.824725  ],
                              [ 13.20798944,  18.96801056,   8.824725  ],
                              [ 17.04800352,  18.96801056,   8.824725  ],
                              [ 13.20798944,  11.99957506,   9.327897  ],
                              [ 17.04800352,  11.99957506,   9.327897  ],
                              [ 13.20798944,  20.17642494,   9.679203  ],
                              [ 17.04800352,  20.17642494,   9.679203  ],
                              [ 13.20798944,  13.20798944,  10.182375  ],
                              [ 17.04800352,  13.20798944,  10.182375  ],
                              [ 13.20798944,  17.04800352,  10.182375  ],
                              [ 17.04800352,  17.04800352,  10.182375  ],
                              [ 20.17642494,  13.20798944,  10.685547  ],
                              [ 20.17642494,  17.04800352,  10.685547  ]]*Angstrom

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
vector_a = [32.176, 0.0, 0.0]*Angstrom
vector_b = [0.0, 32.176, 0.0]*Angstrom
vector_c = [0.0, 0.0, 16.2918]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                            Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                            Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                            Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                            Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                            Silicon, Silicon, Silicon, Hydrogen, Hydrogen]

# Define coordinates
right_electrode_coordinates = [[ 11.99957506,  13.20798944,   0.175653  ],
                               [ 11.99957506,  17.04800352,   0.175653  ],
                               [ 15.12799648,  13.20798944,   0.678825  ],
                               [ 18.96801056,  13.20798944,   0.678825  ],
                               [ 15.12799648,  17.04800352,   0.678825  ],
                               [ 18.96801056,  17.04800352,   0.678825  ],
                               [ 15.12799648,  20.17642494,   1.181997  ],
                               [ 18.96801056,  20.17642494,   1.181997  ],
                               [ 15.12799648,  11.99957506,   1.533303  ],
                               [ 18.96801056,  11.99957506,   1.533303  ],
                               [ 15.12799648,  15.12799648,   2.036475  ],
                               [ 18.96801056,  15.12799648,   2.036475  ],
                               [ 15.12799648,  18.96801056,   2.036475  ],
                               [ 18.96801056,  18.96801056,   2.036475  ],
                               [ 11.99957506,  15.12799648,   2.539647  ],
                               [ 11.99957506,  18.96801056,   2.539647  ],
                               [ 20.17642494,  15.12799648,   2.890953  ],
                               [ 20.17642494,  18.96801056,   2.890953  ],
                               [ 13.20798944,  15.12799648,   3.394125  ],
                               [ 17.04800352,  15.12799648,   3.394125  ],
                               [ 13.20798944,  18.96801056,   3.394125  ],
                               [ 17.04800352,  18.96801056,   3.394125  ],
                               [ 13.20798944,  11.99957506,   3.897297  ],
                               [ 17.04800352,  11.99957506,   3.897297  ],
                               [ 13.20798944,  20.17642494,   4.248603  ],
                               [ 17.04800352,  20.17642494,   4.248603  ],
                               [ 13.20798944,  13.20798944,   4.751775  ],
                               [ 17.04800352,  13.20798944,   4.751775  ],
                               [ 13.20798944,  17.04800352,   4.751775  ],
                               [ 17.04800352,  17.04800352,   4.751775  ],
                               [ 20.17642494,  13.20798944,   5.254947  ],
                               [ 20.17642494,  17.04800352,   5.254947  ],
                               [ 11.99957506,  13.20798944,   5.606253  ],
                               [ 11.99957506,  17.04800352,   5.606253  ],
                               [ 15.12799648,  13.20798944,   6.109425  ],
                               [ 18.96801056,  13.20798944,   6.109425  ],
                               [ 15.12799648,  17.04800352,   6.109425  ],
                               [ 18.96801056,  17.04800352,   6.109425  ],
                               [ 15.12799648,  20.17642494,   6.612597  ],
                               [ 18.96801056,  20.17642494,   6.612597  ],
                               [ 15.12799648,  11.99957506,   6.963903  ],
                               [ 18.96801056,  11.99957506,   6.963903  ],
                               [ 15.12799648,  15.12799648,   7.467075  ],
                               [ 18.96801056,  15.12799648,   7.467075  ],
                               [ 15.12799648,  18.96801056,   7.467075  ],
                               [ 18.96801056,  18.96801056,   7.467075  ],
                               [ 11.99957506,  15.12799648,   7.970247  ],
                               [ 11.99957506,  18.96801056,   7.970247  ],
                               [ 20.17642494,  15.12799648,   8.321553  ],
                               [ 20.17642494,  18.96801056,   8.321553  ],
                               [ 13.20798944,  15.12799648,   8.824725  ],
                               [ 17.04800352,  15.12799648,   8.824725  ],
                               [ 13.20798944,  18.96801056,   8.824725  ],
                               [ 17.04800352,  18.96801056,   8.824725  ],
                               [ 13.20798944,  11.99957506,   9.327897  ],
                               [ 17.04800352,  11.99957506,   9.327897  ],
                               [ 13.20798944,  20.17642494,   9.679203  ],
                               [ 17.04800352,  20.17642494,   9.679203  ],
                               [ 13.20798944,  13.20798944,  10.182375  ],
                               [ 17.04800352,  13.20798944,  10.182375  ],
                               [ 13.20798944,  17.04800352,  10.182375  ],
                               [ 17.04800352,  17.04800352,  10.182375  ],
                               [ 20.17642494,  13.20798944,  10.685547  ],
                               [ 20.17642494,  17.04800352,  10.685547  ],
                               [ 11.99957506,  13.20798944,  11.036853  ],
                               [ 11.99957506,  17.04800352,  11.036853  ],
                               [ 15.12799648,  13.20798944,  11.540025  ],
                               [ 18.96801056,  13.20798944,  11.540025  ],
                               [ 15.12799648,  17.04800352,  11.540025  ],
                               [ 18.96801056,  17.04800352,  11.540025  ],
                               [ 15.12799648,  20.17642494,  12.043197  ],
                               [ 18.96801056,  20.17642494,  12.043197  ],
                               [ 15.12799648,  11.99957506,  12.394503  ],
                               [ 18.96801056,  11.99957506,  12.394503  ],
                               [ 15.12799648,  15.12799648,  12.897675  ],
                               [ 18.96801056,  15.12799648,  12.897675  ],
                               [ 15.12799648,  18.96801056,  12.897675  ],
                               [ 18.96801056,  18.96801056,  12.897675  ],
                               [ 11.99957506,  18.96801056,  13.400847  ],
                               [ 11.99957506,  15.12799648,  13.400847  ],
                               [ 20.17642494,  15.12799648,  13.752153  ],
                               [ 20.17642494,  18.96801056,  13.752153  ],
                               [ 13.20798944,  15.12799648,  14.255325  ],
                               [ 17.04800352,  15.12799648,  14.255325  ],
                               [ 13.20798944,  18.96801056,  14.255325  ],
                               [ 17.04800352,  18.96801056,  14.255325  ],
                               [ 13.20798944,  11.99957506,  14.758497  ],
                               [ 17.04800352,  11.99957506,  14.758497  ],
                               [ 13.20798944,  20.17642494,  15.109803  ],
                               [ 17.04800352,  20.17642494,  15.109803  ],
                               [ 13.20798944,  13.20798944,  15.612975  ],
                               [ 17.04800352,  13.20798944,  15.612975  ],
                               [ 13.20798944,  17.04800352,  15.612975  ],
                               [ 17.04800352,  17.04800352,  15.612975  ],
                               [ 20.17642494,  13.20798944,  16.116147  ],
                               [ 20.17642494,  17.04800352,  16.116147  ]]*Angstrom

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
vector_a = [32.176, 0.0, 0.0]*Angstrom
vector_b = [0.0, 32.176, 0.0]*Angstrom
vector_c = [0.0, 0.0, 38.0142]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen]

# Define coordinates
central_region_coordinates = [[ 11.99957506,  13.20798944,   0.175653  ],
                              [ 11.99957506,  17.04800352,   0.175653  ],
                              [ 15.12799648,  13.20798944,   0.678825  ],
                              [ 18.96801056,  13.20798944,   0.678825  ],
                              [ 15.12799648,  17.04800352,   0.678825  ],
                              [ 18.96801056,  17.04800352,   0.678825  ],
                              [ 15.12799648,  20.17642494,   1.181997  ],
                              [ 18.96801056,  20.17642494,   1.181997  ],
                              [ 15.12799648,  11.99957506,   1.533303  ],
                              [ 18.96801056,  11.99957506,   1.533303  ],
                              [ 15.12799648,  15.12799648,   2.036475  ],
                              [ 18.96801056,  15.12799648,   2.036475  ],
                              [ 15.12799648,  18.96801056,   2.036475  ],
                              [ 18.96801056,  18.96801056,   2.036475  ],
                              [ 11.99957506,  15.12799648,   2.539647  ],
                              [ 11.99957506,  18.96801056,   2.539647  ],
                              [ 20.17642494,  15.12799648,   2.890953  ],
                              [ 20.17642494,  18.96801056,   2.890953  ],
                              [ 13.20798944,  15.12799648,   3.394125  ],
                              [ 17.04800352,  15.12799648,   3.394125  ],
                              [ 13.20798944,  18.96801056,   3.394125  ],
                              [ 17.04800352,  18.96801056,   3.394125  ],
                              [ 13.20798944,  11.99957506,   3.897297  ],
                              [ 17.04800352,  11.99957506,   3.897297  ],
                              [ 13.20798944,  20.17642494,   4.248603  ],
                              [ 17.04800352,  20.17642494,   4.248603  ],
                              [ 13.20798944,  13.20798944,   4.751775  ],
                              [ 17.04800352,  13.20798944,   4.751775  ],
                              [ 13.20798944,  17.04800352,   4.751775  ],
                              [ 17.04800352,  17.04800352,   4.751775  ],
                              [ 20.17642494,  13.20798944,   5.254947  ],
                              [ 20.17642494,  17.04800352,   5.254947  ],
                              [ 11.99957506,  13.20798944,   5.606253  ],
                              [ 11.99957506,  17.04800352,   5.606253  ],
                              [ 15.12799648,  13.20798944,   6.109425  ],
                              [ 18.96801056,  13.20798944,   6.109425  ],
                              [ 15.12799648,  17.04800352,   6.109425  ],
                              [ 18.96801056,  17.04800352,   6.109425  ],
                              [ 15.12799648,  20.17642494,   6.612597  ],
                              [ 18.96801056,  20.17642494,   6.612597  ],
                              [ 15.12799648,  11.99957506,   6.963903  ],
                              [ 18.96801056,  11.99957506,   6.963903  ],
                              [ 15.12799648,  15.12799648,   7.467075  ],
                              [ 18.96801056,  15.12799648,   7.467075  ],
                              [ 15.12799648,  18.96801056,   7.467075  ],
                              [ 18.96801056,  18.96801056,   7.467075  ],
                              [ 11.99957506,  15.12799648,   7.970247  ],
                              [ 11.99957506,  18.96801056,   7.970247  ],
                              [ 20.17642494,  15.12799648,   8.321553  ],
                              [ 20.17642494,  18.96801056,   8.321553  ],
                              [ 13.20798944,  15.12799648,   8.824725  ],
                              [ 17.04800352,  15.12799648,   8.824725  ],
                              [ 13.20798944,  18.96801056,   8.824725  ],
                              [ 17.04800352,  18.96801056,   8.824725  ],
                              [ 13.20798944,  11.99957506,   9.327897  ],
                              [ 17.04800352,  11.99957506,   9.327897  ],
                              [ 13.20798944,  20.17642494,   9.679203  ],
                              [ 17.04800352,  20.17642494,   9.679203  ],
                              [ 13.20798944,  13.20798944,  10.182375  ],
                              [ 17.04800352,  13.20798944,  10.182375  ],
                              [ 13.20798944,  17.04800352,  10.182375  ],
                              [ 17.04800352,  17.04800352,  10.182375  ],
                              [ 20.17642494,  13.20798944,  10.685547  ],
                              [ 20.17642494,  17.04800352,  10.685547  ],
                              [ 11.99957506,  13.20798944,  11.036853  ],
                              [ 11.99957506,  17.04800352,  11.036853  ],
                              [ 15.12799648,  13.20798944,  11.540025  ],
                              [ 18.96801056,  13.20798944,  11.540025  ],
                              [ 15.12799648,  17.04800352,  11.540025  ],
                              [ 18.96801056,  17.04800352,  11.540025  ],
                              [ 15.12799648,  20.17642494,  12.043197  ],
                              [ 18.96801056,  20.17642494,  12.043197  ],
                              [ 15.12799648,  11.99957506,  12.394503  ],
                              [ 18.96801056,  11.99957506,  12.394503  ],
                              [ 15.12799648,  15.12799648,  12.897675  ],
                              [ 18.96801056,  15.12799648,  12.897675  ],
                              [ 15.12799648,  18.96801056,  12.897675  ],
                              [ 18.96801056,  18.96801056,  12.897675  ],
                              [ 11.99957506,  15.12799648,  13.400847  ],
                              [ 11.99957506,  18.96801056,  13.400847  ],
                              [ 20.17642494,  15.12799648,  13.752153  ],
                              [ 20.17642494,  18.96801056,  13.752153  ],
                              [ 13.20798944,  15.12799648,  14.255325  ],
                              [ 17.04800352,  15.12799648,  14.255325  ],
                              [ 13.20798944,  18.96801056,  14.255325  ],
                              [ 17.04800352,  18.96801056,  14.255325  ],
                              [ 13.20798944,  11.99957506,  14.758497  ],
                              [ 17.04800352,  11.99957506,  14.758497  ],
                              [ 13.20798944,  20.17642494,  15.109803  ],
                              [ 17.04800352,  20.17642494,  15.109803  ],
                              [ 13.20798944,  13.20798944,  15.612975  ],
                              [ 17.04800352,  13.20798944,  15.612975  ],
                              [ 13.20798944,  17.04800352,  15.612975  ],
                              [ 17.04800352,  17.04800352,  15.612975  ],
                              [ 20.17642494,  13.20798944,  16.116147  ],
                              [ 20.17642494,  17.04800352,  16.116147  ],
                              [ 11.99957506,  13.20798944,  16.467453  ],
                              [ 11.99957506,  17.04800352,  16.467453  ],
                              [ 15.12799648,  13.20798944,  16.970625  ],
                              [ 18.96801056,  13.20798944,  16.970625  ],
                              [ 15.12799648,  17.04800352,  16.970625  ],
                              [ 18.96801056,  17.04800352,  16.970625  ],
                              [ 15.12799648,  20.17642494,  17.473797  ],
                              [ 18.96801056,  20.17642494,  17.473797  ],
                              [ 15.12799648,  11.99957506,  17.825103  ],
                              [ 18.96801056,  11.99957506,  17.825103  ],
                              [ 15.12799648,  15.12799648,  18.328275  ],
                              [ 18.96801056,  15.12799648,  18.328275  ],
                              [ 15.12799648,  18.96801056,  18.328275  ],
                              [ 18.96801056,  18.96801056,  18.328275  ],
                              [ 11.99957506,  15.12799648,  18.831447  ],
                              [ 11.99957506,  18.96801056,  18.831447  ],
                              [ 20.17642494,  15.12799648,  19.182753  ],
                              [ 20.17642494,  18.96801056,  19.182753  ],
                              [ 13.20798944,  15.12799648,  19.685925  ],
                              [ 17.04800352,  15.12799648,  19.685925  ],
                              [ 13.20798944,  18.96801056,  19.685925  ],
                              [ 17.04800352,  18.96801056,  19.685925  ],
                              [ 13.20798944,  11.99957506,  20.189097  ],
                              [ 17.04800352,  11.99957506,  20.189097  ],
                              [ 13.20798944,  20.17642494,  20.540403  ],
                              [ 17.04800352,  20.17642494,  20.540403  ],
                              [ 13.20798944,  13.20798944,  21.043575  ],
                              [ 17.04800352,  13.20798944,  21.043575  ],
                              [ 13.20798944,  17.04800352,  21.043575  ],
                              [ 17.04800352,  17.04800352,  21.043575  ],
                              [ 20.17642494,  13.20798944,  21.546747  ],
                              [ 20.17642494,  17.04800352,  21.546747  ],
                              [ 11.99957506,  13.20798944,  21.898053  ],
                              [ 11.99957506,  17.04800352,  21.898053  ],
                              [ 15.12799648,  13.20798944,  22.401225  ],
                              [ 18.96801056,  13.20798944,  22.401225  ],
                              [ 15.12799648,  17.04800352,  22.401225  ],
                              [ 18.96801056,  17.04800352,  22.401225  ],
                              [ 15.12799648,  20.17642494,  22.904397  ],
                              [ 18.96801056,  20.17642494,  22.904397  ],
                              [ 15.12799648,  11.99957506,  23.255703  ],
                              [ 18.96801056,  11.99957506,  23.255703  ],
                              [ 15.12799648,  15.12799648,  23.758875  ],
                              [ 18.96801056,  15.12799648,  23.758875  ],
                              [ 15.12799648,  18.96801056,  23.758875  ],
                              [ 18.96801056,  18.96801056,  23.758875  ],
                              [ 11.99957506,  15.12799648,  24.262047  ],
                              [ 11.99957506,  18.96801056,  24.262047  ],
                              [ 20.17642494,  15.12799648,  24.613353  ],
                              [ 20.17642494,  18.96801056,  24.613353  ],
                              [ 13.20798944,  15.12799648,  25.116525  ],
                              [ 17.04800352,  15.12799648,  25.116525  ],
                              [ 13.20798944,  18.96801056,  25.116525  ],
                              [ 17.04800352,  18.96801056,  25.116525  ],
                              [ 13.20798944,  11.99957506,  25.619697  ],
                              [ 17.04800352,  11.99957506,  25.619697  ],
                              [ 13.20798944,  20.17642494,  25.971003  ],
                              [ 17.04800352,  20.17642494,  25.971003  ],
                              [ 13.20798944,  13.20798944,  26.474175  ],
                              [ 17.04800352,  13.20798944,  26.474175  ],
                              [ 13.20798944,  17.04800352,  26.474175  ],
                              [ 17.04800352,  17.04800352,  26.474175  ],
                              [ 20.17642494,  13.20798944,  26.977347  ],
                              [ 20.17642494,  17.04800352,  26.977347  ],
                              [ 11.99957506,  13.20798944,  27.328653  ],
                              [ 11.99957506,  17.04800352,  27.328653  ],
                              [ 15.12799648,  13.20798944,  27.831825  ],
                              [ 18.96801056,  13.20798944,  27.831825  ],
                              [ 15.12799648,  17.04800352,  27.831825  ],
                              [ 18.96801056,  17.04800352,  27.831825  ],
                              [ 15.12799648,  20.17642494,  28.334997  ],
                              [ 18.96801056,  20.17642494,  28.334997  ],
                              [ 15.12799648,  11.99957506,  28.686303  ],
                              [ 18.96801056,  11.99957506,  28.686303  ],
                              [ 15.12799648,  15.12799648,  29.189475  ],
                              [ 18.96801056,  15.12799648,  29.189475  ],
                              [ 15.12799648,  18.96801056,  29.189475  ],
                              [ 18.96801056,  18.96801056,  29.189475  ],
                              [ 11.99957506,  15.12799648,  29.692647  ],
                              [ 11.99957506,  18.96801056,  29.692647  ],
                              [ 20.17642494,  15.12799648,  30.043953  ],
                              [ 20.17642494,  18.96801056,  30.043953  ],
                              [ 13.20798944,  15.12799648,  30.547125  ],
                              [ 17.04800352,  15.12799648,  30.547125  ],
                              [ 13.20798944,  18.96801056,  30.547125  ],
                              [ 17.04800352,  18.96801056,  30.547125  ],
                              [ 13.20798944,  11.99957506,  31.050297  ],
                              [ 17.04800352,  11.99957506,  31.050297  ],
                              [ 13.20798944,  20.17642494,  31.401603  ],
                              [ 17.04800352,  20.17642494,  31.401603  ],
                              [ 13.20798944,  13.20798944,  31.904775  ],
                              [ 17.04800352,  13.20798944,  31.904775  ],
                              [ 13.20798944,  17.04800352,  31.904775  ],
                              [ 17.04800352,  17.04800352,  31.904775  ],
                              [ 20.17642494,  13.20798944,  32.407947  ],
                              [ 20.17642494,  17.04800352,  32.407947  ],
                              [ 11.99957506,  13.20798944,  32.759253  ],
                              [ 11.99957506,  17.04800352,  32.759253  ],
                              [ 15.12799648,  13.20798944,  33.262425  ],
                              [ 18.96801056,  13.20798944,  33.262425  ],
                              [ 15.12799648,  17.04800352,  33.262425  ],
                              [ 18.96801056,  17.04800352,  33.262425  ],
                              [ 15.12799648,  20.17642494,  33.765597  ],
                              [ 18.96801056,  20.17642494,  33.765597  ],
                              [ 15.12799648,  11.99957506,  34.116903  ],
                              [ 18.96801056,  11.99957506,  34.116903  ],
                              [ 15.12799648,  15.12799648,  34.620075  ],
                              [ 18.96801056,  15.12799648,  34.620075  ],
                              [ 15.12799648,  18.96801056,  34.620075  ],
                              [ 18.96801056,  18.96801056,  34.620075  ],
                              [ 11.99957506,  18.96801056,  35.123247  ],
                              [ 11.99957506,  15.12799648,  35.123247  ],
                              [ 20.17642494,  15.12799648,  35.474553  ],
                              [ 20.17642494,  18.96801056,  35.474553  ],
                              [ 13.20798944,  15.12799648,  35.977725  ],
                              [ 17.04800352,  15.12799648,  35.977725  ],
                              [ 13.20798944,  18.96801056,  35.977725  ],
                              [ 17.04800352,  18.96801056,  35.977725  ],
                              [ 13.20798944,  11.99957506,  36.480897  ],
                              [ 17.04800352,  11.99957506,  36.480897  ],
                              [ 13.20798944,  20.17642494,  36.832203  ],
                              [ 17.04800352,  20.17642494,  36.832203  ],
                              [ 13.20798944,  13.20798944,  37.335375  ],
                              [ 17.04800352,  13.20798944,  37.335375  ],
                              [ 13.20798944,  17.04800352,  37.335375  ],
                              [ 17.04800352,  17.04800352,  37.335375  ],
                              [ 20.17642494,  13.20798944,  37.838547  ],
                              [ 20.17642494,  17.04800352,  37.838547  ]]*Angstrom

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
        xmin =  10.99957506 *Angstrom,  xmax =  0.99957506 *Angstrom,
        ymin =  10.99957506 *Angstrom,  ymax =  21.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.99957506 *Angstrom,  xmax =  21.17642494 *Angstrom,
        ymin =  21.17642494 *Angstrom,  ymax =  31.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.17642494 *Angstrom,  xmax =  31.17642494 *Angstrom,
        ymin =  10.99957506 *Angstrom,  ymax =  21.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.99957506 *Angstrom,  xmax =  21.17642494 *Angstrom,
        ymin =  10.99957506 *Angstrom,  ymax =  0.99957506 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.99957506 *Angstrom,  xmax =  0.99957506 *Angstrom,
        ymin =  10.99957506 *Angstrom,  ymax =  0.99957506 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.99957506 *Angstrom,  xmax =  0.99957506 *Angstrom,
        ymin =  21.17642494 *Angstrom,  ymax =  31.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.17642494 *Angstrom,  xmax =  31.17642494 *Angstrom,
        ymin =  21.17642494 *Angstrom,  ymax =  31.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.17642494 *Angstrom,  xmax =  31.17642494 *Angstrom,
        ymin =  10.99957506 *Angstrom,  ymax =  0.99957506 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.99957506 *Angstrom,  xmax =  -0.00042494 *Angstrom,
        ymin =  0.99957506 *Angstrom,  ymax =  31.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -0.00042494 *Angstrom,  xmax =  32.17642494 *Angstrom,
        ymin =  31.17642494 *Angstrom,  ymax =  32.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.17642494 *Angstrom,  xmax =  32.17642494 *Angstrom,
        ymin =  0.99957506 *Angstrom,  ymax =  31.17642494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -0.00042494 *Angstrom,  xmax =  32.17642494 *Angstrom,
        ymin =  0.99957506 *Angstrom,  ymax =  -0.00042494 *Angstrom,
        zmin =  8.9192735 *Angstrom,  zmax =  28.9192735 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)


basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


#x = (5e20 cm^-3) * (8.18Angstrom * 8.18Angstrom * 16.29Angstrom)
charge = 0.545
temp = 300
