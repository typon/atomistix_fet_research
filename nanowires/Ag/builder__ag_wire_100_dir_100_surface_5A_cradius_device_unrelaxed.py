# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [17.5819971347, 0.0, 0.0]*Angstrom
vector_b = [0.0, 17.5819971347, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver]

# Define coordinates
left_electrode_coordinates = [[  6.74814857,   4.70529857,   1.021425  ],
                              [ 10.83384857,   4.70529857,   1.021425  ],
                              [  4.70529857,   6.74814857,   1.021425  ],
                              [  8.79099857,   6.74814857,   1.021425  ],
                              [ 12.87669857,   6.74814857,   1.021425  ],
                              [  6.74814857,   8.79099857,   1.021425  ],
                              [ 10.83384857,   8.79099857,   1.021425  ],
                              [  4.70529857,  10.83384857,   1.021425  ],
                              [  8.79099857,  10.83384857,   1.021425  ],
                              [ 12.87669857,  10.83384857,   1.021425  ],
                              [  6.74814857,  12.87669857,   1.021425  ],
                              [ 10.83384857,  12.87669857,   1.021425  ],
                              [  4.70529857,   4.70529857,   3.064275  ],
                              [  8.79099857,   4.70529857,   3.064275  ],
                              [ 12.87669857,   4.70529857,   3.064275  ],
                              [  6.74814857,   6.74814857,   3.064275  ],
                              [ 10.83384857,   6.74814857,   3.064275  ],
                              [  4.70529857,   8.79099857,   3.064275  ],
                              [  8.79099857,   8.79099857,   3.064275  ],
                              [ 12.87669857,   8.79099857,   3.064275  ],
                              [  6.74814857,  10.83384857,   3.064275  ],
                              [ 10.83384857,  10.83384857,   3.064275  ],
                              [  4.70529857,  12.87669857,   3.064275  ],
                              [  8.79099857,  12.87669857,   3.064275  ],
                              [ 12.87669857,  12.87669857,   3.064275  ]]*Angstrom

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
vector_a = [17.5819971347, 0.0, 0.0]*Angstrom
vector_b = [0.0, 17.5819971347, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver]

# Define coordinates
right_electrode_coordinates = [[  6.74814857,   4.70529857,   1.021425  ],
                               [ 10.83384857,   4.70529857,   1.021425  ],
                               [  4.70529857,   6.74814857,   1.021425  ],
                               [  8.79099857,   6.74814857,   1.021425  ],
                               [ 12.87669857,   6.74814857,   1.021425  ],
                               [  6.74814857,   8.79099857,   1.021425  ],
                               [ 10.83384857,   8.79099857,   1.021425  ],
                               [  4.70529857,  10.83384857,   1.021425  ],
                               [  8.79099857,  10.83384857,   1.021425  ],
                               [ 12.87669857,  10.83384857,   1.021425  ],
                               [  6.74814857,  12.87669857,   1.021425  ],
                               [ 10.83384857,  12.87669857,   1.021425  ],
                               [  4.70529857,   4.70529857,   3.064275  ],
                               [  8.79099857,   4.70529857,   3.064275  ],
                               [ 12.87669857,   4.70529857,   3.064275  ],
                               [  6.74814857,   6.74814857,   3.064275  ],
                               [ 10.83384857,   6.74814857,   3.064275  ],
                               [  4.70529857,   8.79099857,   3.064275  ],
                               [  8.79099857,   8.79099857,   3.064275  ],
                               [ 12.87669857,   8.79099857,   3.064275  ],
                               [  6.74814857,  10.83384857,   3.064275  ],
                               [ 10.83384857,  10.83384857,   3.064275  ],
                               [  4.70529857,  12.87669857,   3.064275  ],
                               [  8.79099857,  12.87669857,   3.064275  ],
                               [ 12.87669857,  12.87669857,   3.064275  ]]*Angstrom

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
vector_a = [17.5819971347, 0.0, 0.0]*Angstrom
vector_b = [0.0, 17.5819971347, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1714]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver]

# Define coordinates
central_region_coordinates = [[  6.74814857,   4.70529857,   1.021425  ],
                              [ 10.83384857,   4.70529857,   1.021425  ],
                              [  4.70529857,   6.74814857,   1.021425  ],
                              [  8.79099857,   6.74814857,   1.021425  ],
                              [ 12.87669857,   6.74814857,   1.021425  ],
                              [  6.74814857,   8.79099857,   1.021425  ],
                              [ 10.83384857,   8.79099857,   1.021425  ],
                              [  4.70529857,  10.83384857,   1.021425  ],
                              [  8.79099857,  10.83384857,   1.021425  ],
                              [ 12.87669857,  10.83384857,   1.021425  ],
                              [  6.74814857,  12.87669857,   1.021425  ],
                              [ 10.83384857,  12.87669857,   1.021425  ],
                              [  4.70529857,   4.70529857,   3.064275  ],
                              [  8.79099857,   4.70529857,   3.064275  ],
                              [ 12.87669857,   4.70529857,   3.064275  ],
                              [  6.74814857,   6.74814857,   3.064275  ],
                              [ 10.83384857,   6.74814857,   3.064275  ],
                              [  4.70529857,   8.79099857,   3.064275  ],
                              [  8.79099857,   8.79099857,   3.064275  ],
                              [ 12.87669857,   8.79099857,   3.064275  ],
                              [  6.74814857,  10.83384857,   3.064275  ],
                              [ 10.83384857,  10.83384857,   3.064275  ],
                              [  4.70529857,  12.87669857,   3.064275  ],
                              [  8.79099857,  12.87669857,   3.064275  ],
                              [ 12.87669857,  12.87669857,   3.064275  ],
                              [  6.74814857,   4.70529857,   5.107125  ],
                              [ 10.83384857,   4.70529857,   5.107125  ],
                              [  4.70529857,   6.74814857,   5.107125  ],
                              [  8.79099857,   6.74814857,   5.107125  ],
                              [ 12.87669857,   6.74814857,   5.107125  ],
                              [  6.74814857,   8.79099857,   5.107125  ],
                              [ 10.83384857,   8.79099857,   5.107125  ],
                              [  4.70529857,  10.83384857,   5.107125  ],
                              [  8.79099857,  10.83384857,   5.107125  ],
                              [ 12.87669857,  10.83384857,   5.107125  ],
                              [  6.74814857,  12.87669857,   5.107125  ],
                              [ 10.83384857,  12.87669857,   5.107125  ],
                              [  4.70529857,   4.70529857,   7.149975  ],
                              [  8.79099857,   4.70529857,   7.149975  ],
                              [ 12.87669857,   4.70529857,   7.149975  ],
                              [  6.74814857,   6.74814857,   7.149975  ],
                              [ 10.83384857,   6.74814857,   7.149975  ],
                              [  4.70529857,   8.79099857,   7.149975  ],
                              [  8.79099857,   8.79099857,   7.149975  ],
                              [ 12.87669857,   8.79099857,   7.149975  ],
                              [  6.74814857,  10.83384857,   7.149975  ],
                              [ 10.83384857,  10.83384857,   7.149975  ],
                              [  4.70529857,  12.87669857,   7.149975  ],
                              [  8.79099857,  12.87669857,   7.149975  ],
                              [ 12.87669857,  12.87669857,   7.149975  ]]*Angstrom

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

