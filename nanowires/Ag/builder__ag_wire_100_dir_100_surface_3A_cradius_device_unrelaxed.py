# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [9.08500614447, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.08500614447, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver]

# Define coordinates
left_electrode_coordinates = [[ 4.54250307,  2.49965307,  1.021425  ],
                              [ 2.49965307,  4.54250307,  1.021425  ],
                              [ 6.58535307,  4.54250307,  1.021425  ],
                              [ 4.54250307,  6.58535307,  1.021425  ],
                              [ 2.49965307,  2.49965307,  3.064275  ],
                              [ 6.58535307,  2.49965307,  3.064275  ],
                              [ 4.54250307,  4.54250307,  3.064275  ],
                              [ 2.49965307,  6.58535307,  3.064275  ],
                              [ 6.58535307,  6.58535307,  3.064275  ]]*Angstrom

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
vector_a = [9.08500614447, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.08500614447, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver]

# Define coordinates
right_electrode_coordinates = [[ 4.54250307,  2.49965307,  1.021425  ],
                               [ 2.49965307,  4.54250307,  1.021425  ],
                               [ 6.58535307,  4.54250307,  1.021425  ],
                               [ 4.54250307,  6.58535307,  1.021425  ],
                               [ 2.49965307,  2.49965307,  3.064275  ],
                               [ 6.58535307,  2.49965307,  3.064275  ],
                               [ 4.54250307,  4.54250307,  3.064275  ],
                               [ 2.49965307,  6.58535307,  3.064275  ],
                               [ 6.58535307,  6.58535307,  3.064275  ]]*Angstrom

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
vector_a = [9.08500614447, 0.0, 0.0]*Angstrom
vector_b = [0.0, 9.08500614447, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1714]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver]

# Define coordinates
central_region_coordinates = [[ 4.54250307,  2.49965307,  1.021425  ],
                              [ 2.49965307,  4.54250307,  1.021425  ],
                              [ 6.58535307,  4.54250307,  1.021425  ],
                              [ 4.54250307,  6.58535307,  1.021425  ],
                              [ 2.49965307,  2.49965307,  3.064275  ],
                              [ 6.58535307,  2.49965307,  3.064275  ],
                              [ 4.54250307,  4.54250307,  3.064275  ],
                              [ 2.49965307,  6.58535307,  3.064275  ],
                              [ 6.58535307,  6.58535307,  3.064275  ],
                              [ 4.54250307,  2.49965307,  5.107125  ],
                              [ 2.49965307,  4.54250307,  5.107125  ],
                              [ 6.58535307,  4.54250307,  5.107125  ],
                              [ 4.54250307,  6.58535307,  5.107125  ],
                              [ 2.49965307,  2.49965307,  7.149975  ],
                              [ 6.58535307,  2.49965307,  7.149975  ],
                              [ 4.54250307,  4.54250307,  7.149975  ],
                              [ 2.49965307,  6.58535307,  7.149975  ],
                              [ 6.58535307,  6.58535307,  7.149975  ]]*Angstrom

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

