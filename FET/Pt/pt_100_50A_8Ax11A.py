# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [32.3232, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.5488, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.8472]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum]

# Define coordinates
left_electrode_coordinates = [[ 11.99999375,  11.99999583,   0.9809    ],
                              [ 14.77439792,  11.99999583,   0.9809    ],
                              [ 17.54880208,  11.99999583,   0.9809    ],
                              [ 20.32320625,  11.99999583,   0.9809    ],
                              [ 11.99999375,  14.7744    ,   0.9809    ],
                              [ 14.77439792,  14.7744    ,   0.9809    ],
                              [ 17.54880208,  14.7744    ,   0.9809    ],
                              [ 20.32320625,  14.7744    ,   0.9809    ],
                              [ 11.99999375,  17.54880417,   0.9809    ],
                              [ 14.77439792,  17.54880417,   0.9809    ],
                              [ 17.54880208,  17.54880417,   0.9809    ],
                              [ 20.32320625,  17.54880417,   0.9809    ],
                              [ 13.38719583,  13.38719792,   2.9427    ],
                              [ 16.1616    ,  13.38719792,   2.9427    ],
                              [ 18.93600417,  13.38719792,   2.9427    ],
                              [ 13.38719583,  16.16160208,   2.9427    ],
                              [ 16.1616    ,  16.16160208,   2.9427    ],
                              [ 18.93600417,  16.16160208,   2.9427    ],
                              [ 11.99999375,  11.99999583,   4.9045    ],
                              [ 14.77439792,  11.99999583,   4.9045    ],
                              [ 17.54880208,  11.99999583,   4.9045    ],
                              [ 20.32320625,  11.99999583,   4.9045    ],
                              [ 11.99999375,  14.7744    ,   4.9045    ],
                              [ 14.77439792,  14.7744    ,   4.9045    ],
                              [ 17.54880208,  14.7744    ,   4.9045    ],
                              [ 20.32320625,  14.7744    ,   4.9045    ],
                              [ 11.99999375,  17.54880417,   4.9045    ],
                              [ 14.77439792,  17.54880417,   4.9045    ],
                              [ 17.54880208,  17.54880417,   4.9045    ],
                              [ 20.32320625,  17.54880417,   4.9045    ],
                              [ 13.38719583,  13.38719792,   6.8663    ],
                              [ 16.1616    ,  13.38719792,   6.8663    ],
                              [ 18.93600417,  13.38719792,   6.8663    ],
                              [ 13.38719583,  16.16160208,   6.8663    ],
                              [ 16.1616    ,  16.16160208,   6.8663    ],
                              [ 18.93600417,  16.16160208,   6.8663    ]]*Angstrom

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
vector_a = [32.3232, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.5488, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.8472]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                            Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                            Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                            Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                            Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                            Platinum, Platinum, Platinum, Platinum, Platinum, Platinum]

# Define coordinates
right_electrode_coordinates = [[ 11.99999375,  11.99999583,   0.9809    ],
                               [ 14.77439792,  11.99999583,   0.9809    ],
                               [ 17.54880208,  11.99999583,   0.9809    ],
                               [ 20.32320625,  11.99999583,   0.9809    ],
                               [ 11.99999375,  14.7744    ,   0.9809    ],
                               [ 14.77439792,  14.7744    ,   0.9809    ],
                               [ 17.54880208,  14.7744    ,   0.9809    ],
                               [ 20.32320625,  14.7744    ,   0.9809    ],
                               [ 11.99999375,  17.54880417,   0.9809    ],
                               [ 14.77439792,  17.54880417,   0.9809    ],
                               [ 17.54880208,  17.54880417,   0.9809    ],
                               [ 20.32320625,  17.54880417,   0.9809    ],
                               [ 13.38719583,  13.38719792,   2.9427    ],
                               [ 16.1616    ,  13.38719792,   2.9427    ],
                               [ 18.93600417,  13.38719792,   2.9427    ],
                               [ 13.38719583,  16.16160208,   2.9427    ],
                               [ 16.1616    ,  16.16160208,   2.9427    ],
                               [ 18.93600417,  16.16160208,   2.9427    ],
                               [ 11.99999375,  11.99999583,   4.9045    ],
                               [ 14.77439792,  11.99999583,   4.9045    ],
                               [ 17.54880208,  11.99999583,   4.9045    ],
                               [ 20.32320625,  11.99999583,   4.9045    ],
                               [ 11.99999375,  14.7744    ,   4.9045    ],
                               [ 14.77439792,  14.7744    ,   4.9045    ],
                               [ 17.54880208,  14.7744    ,   4.9045    ],
                               [ 20.32320625,  14.7744    ,   4.9045    ],
                               [ 11.99999375,  17.54880417,   4.9045    ],
                               [ 14.77439792,  17.54880417,   4.9045    ],
                               [ 17.54880208,  17.54880417,   4.9045    ],
                               [ 20.32320625,  17.54880417,   4.9045    ],
                               [ 13.38719583,  13.38719792,   6.8663    ],
                               [ 16.1616    ,  13.38719792,   6.8663    ],
                               [ 18.93600417,  13.38719792,   6.8663    ],
                               [ 13.38719583,  16.16160208,   6.8663    ],
                               [ 16.1616    ,  16.16160208,   6.8663    ],
                               [ 18.93600417,  16.16160208,   6.8663    ]]*Angstrom

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
vector_a = [32.3232, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.5488, 0.0]*Angstrom
vector_c = [0.0, 0.0, 51.0068]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
                           Platinum, Platinum, Platinum, Platinum, Platinum, Platinum]

# Define coordinates
central_region_coordinates = [[ 11.99999375,  11.99999583,   0.9809    ],
                              [ 14.77439792,  11.99999583,   0.9809    ],
                              [ 17.54880208,  11.99999583,   0.9809    ],
                              [ 20.32320625,  11.99999583,   0.9809    ],
                              [ 11.99999375,  14.7744    ,   0.9809    ],
                              [ 14.77439792,  14.7744    ,   0.9809    ],
                              [ 17.54880208,  14.7744    ,   0.9809    ],
                              [ 20.32320625,  14.7744    ,   0.9809    ],
                              [ 11.99999375,  17.54880417,   0.9809    ],
                              [ 14.77439792,  17.54880417,   0.9809    ],
                              [ 17.54880208,  17.54880417,   0.9809    ],
                              [ 20.32320625,  17.54880417,   0.9809    ],
                              [ 13.38719583,  13.38719792,   2.9427    ],
                              [ 16.1616    ,  13.38719792,   2.9427    ],
                              [ 18.93600417,  13.38719792,   2.9427    ],
                              [ 13.38719583,  16.16160208,   2.9427    ],
                              [ 16.1616    ,  16.16160208,   2.9427    ],
                              [ 18.93600417,  16.16160208,   2.9427    ],
                              [ 11.99999375,  11.99999583,   4.9045    ],
                              [ 14.77439792,  11.99999583,   4.9045    ],
                              [ 17.54880208,  11.99999583,   4.9045    ],
                              [ 20.32320625,  11.99999583,   4.9045    ],
                              [ 11.99999375,  14.7744    ,   4.9045    ],
                              [ 14.77439792,  14.7744    ,   4.9045    ],
                              [ 17.54880208,  14.7744    ,   4.9045    ],
                              [ 20.32320625,  14.7744    ,   4.9045    ],
                              [ 11.99999375,  17.54880417,   4.9045    ],
                              [ 14.77439792,  17.54880417,   4.9045    ],
                              [ 17.54880208,  17.54880417,   4.9045    ],
                              [ 20.32320625,  17.54880417,   4.9045    ],
                              [ 13.38719583,  13.38719792,   6.8663    ],
                              [ 16.1616    ,  13.38719792,   6.8663    ],
                              [ 18.93600417,  13.38719792,   6.8663    ],
                              [ 13.38719583,  16.16160208,   6.8663    ],
                              [ 16.1616    ,  16.16160208,   6.8663    ],
                              [ 18.93600417,  16.16160208,   6.8663    ],
                              [ 11.99999375,  11.99999583,   8.8281    ],
                              [ 14.77439792,  11.99999583,   8.8281    ],
                              [ 17.54880208,  11.99999583,   8.8281    ],
                              [ 20.32320625,  11.99999583,   8.8281    ],
                              [ 11.99999375,  14.7744    ,   8.8281    ],
                              [ 14.77439792,  14.7744    ,   8.8281    ],
                              [ 17.54880208,  14.7744    ,   8.8281    ],
                              [ 20.32320625,  14.7744    ,   8.8281    ],
                              [ 11.99999375,  17.54880417,   8.8281    ],
                              [ 14.77439792,  17.54880417,   8.8281    ],
                              [ 17.54880208,  17.54880417,   8.8281    ],
                              [ 20.32320625,  17.54880417,   8.8281    ],
                              [ 13.38719583,  13.38719792,  10.7899    ],
                              [ 16.1616    ,  13.38719792,  10.7899    ],
                              [ 18.93600417,  13.38719792,  10.7899    ],
                              [ 13.38719583,  16.16160208,  10.7899    ],
                              [ 16.1616    ,  16.16160208,  10.7899    ],
                              [ 18.93600417,  16.16160208,  10.7899    ],
                              [ 11.99999375,  11.99999583,  12.7517    ],
                              [ 14.77439792,  11.99999583,  12.7517    ],
                              [ 17.54880208,  11.99999583,  12.7517    ],
                              [ 20.32320625,  11.99999583,  12.7517    ],
                              [ 11.99999375,  14.7744    ,  12.7517    ],
                              [ 14.77439792,  14.7744    ,  12.7517    ],
                              [ 17.54880208,  14.7744    ,  12.7517    ],
                              [ 20.32320625,  14.7744    ,  12.7517    ],
                              [ 11.99999375,  17.54880417,  12.7517    ],
                              [ 14.77439792,  17.54880417,  12.7517    ],
                              [ 17.54880208,  17.54880417,  12.7517    ],
                              [ 20.32320625,  17.54880417,  12.7517    ],
                              [ 13.38719583,  13.38719792,  14.7135    ],
                              [ 16.1616    ,  13.38719792,  14.7135    ],
                              [ 18.93600417,  13.38719792,  14.7135    ],
                              [ 13.38719583,  16.16160208,  14.7135    ],
                              [ 16.1616    ,  16.16160208,  14.7135    ],
                              [ 18.93600417,  16.16160208,  14.7135    ],
                              [ 11.99999375,  11.99999583,  16.6753    ],
                              [ 14.77439792,  11.99999583,  16.6753    ],
                              [ 17.54880208,  11.99999583,  16.6753    ],
                              [ 20.32320625,  11.99999583,  16.6753    ],
                              [ 11.99999375,  14.7744    ,  16.6753    ],
                              [ 14.77439792,  14.7744    ,  16.6753    ],
                              [ 17.54880208,  14.7744    ,  16.6753    ],
                              [ 20.32320625,  14.7744    ,  16.6753    ],
                              [ 11.99999375,  17.54880417,  16.6753    ],
                              [ 14.77439792,  17.54880417,  16.6753    ],
                              [ 17.54880208,  17.54880417,  16.6753    ],
                              [ 20.32320625,  17.54880417,  16.6753    ],
                              [ 13.38719583,  13.38719792,  18.6371    ],
                              [ 16.1616    ,  13.38719792,  18.6371    ],
                              [ 18.93600417,  13.38719792,  18.6371    ],
                              [ 13.38719583,  16.16160208,  18.6371    ],
                              [ 16.1616    ,  16.16160208,  18.6371    ],
                              [ 18.93600417,  16.16160208,  18.6371    ],
                              [ 11.99999375,  11.99999583,  20.5989    ],
                              [ 14.77439792,  11.99999583,  20.5989    ],
                              [ 17.54880208,  11.99999583,  20.5989    ],
                              [ 20.32320625,  11.99999583,  20.5989    ],
                              [ 11.99999375,  14.7744    ,  20.5989    ],
                              [ 14.77439792,  14.7744    ,  20.5989    ],
                              [ 17.54880208,  14.7744    ,  20.5989    ],
                              [ 20.32320625,  14.7744    ,  20.5989    ],
                              [ 11.99999375,  17.54880417,  20.5989    ],
                              [ 14.77439792,  17.54880417,  20.5989    ],
                              [ 17.54880208,  17.54880417,  20.5989    ],
                              [ 20.32320625,  17.54880417,  20.5989    ],
                              [ 13.38719583,  13.38719792,  22.5607    ],
                              [ 16.1616    ,  13.38719792,  22.5607    ],
                              [ 18.93600417,  13.38719792,  22.5607    ],
                              [ 13.38719583,  16.16160208,  22.5607    ],
                              [ 16.1616    ,  16.16160208,  22.5607    ],
                              [ 18.93600417,  16.16160208,  22.5607    ],
                              [ 11.99999375,  11.99999583,  24.5225    ],
                              [ 14.77439792,  11.99999583,  24.5225    ],
                              [ 17.54880208,  11.99999583,  24.5225    ],
                              [ 20.32320625,  11.99999583,  24.5225    ],
                              [ 11.99999375,  14.7744    ,  24.5225    ],
                              [ 14.77439792,  14.7744    ,  24.5225    ],
                              [ 17.54880208,  14.7744    ,  24.5225    ],
                              [ 20.32320625,  14.7744    ,  24.5225    ],
                              [ 11.99999375,  17.54880417,  24.5225    ],
                              [ 14.77439792,  17.54880417,  24.5225    ],
                              [ 17.54880208,  17.54880417,  24.5225    ],
                              [ 20.32320625,  17.54880417,  24.5225    ],
                              [ 13.38719583,  13.38719792,  26.4843    ],
                              [ 16.1616    ,  13.38719792,  26.4843    ],
                              [ 18.93600417,  13.38719792,  26.4843    ],
                              [ 13.38719583,  16.16160208,  26.4843    ],
                              [ 16.1616    ,  16.16160208,  26.4843    ],
                              [ 18.93600417,  16.16160208,  26.4843    ],
                              [ 11.99999375,  11.99999583,  28.4461    ],
                              [ 14.77439792,  11.99999583,  28.4461    ],
                              [ 17.54880208,  11.99999583,  28.4461    ],
                              [ 20.32320625,  11.99999583,  28.4461    ],
                              [ 11.99999375,  14.7744    ,  28.4461    ],
                              [ 14.77439792,  14.7744    ,  28.4461    ],
                              [ 17.54880208,  14.7744    ,  28.4461    ],
                              [ 20.32320625,  14.7744    ,  28.4461    ],
                              [ 11.99999375,  17.54880417,  28.4461    ],
                              [ 14.77439792,  17.54880417,  28.4461    ],
                              [ 17.54880208,  17.54880417,  28.4461    ],
                              [ 20.32320625,  17.54880417,  28.4461    ],
                              [ 13.38719583,  13.38719792,  30.4079    ],
                              [ 16.1616    ,  13.38719792,  30.4079    ],
                              [ 18.93600417,  13.38719792,  30.4079    ],
                              [ 13.38719583,  16.16160208,  30.4079    ],
                              [ 16.1616    ,  16.16160208,  30.4079    ],
                              [ 18.93600417,  16.16160208,  30.4079    ],
                              [ 11.99999375,  11.99999583,  32.3697    ],
                              [ 14.77439792,  11.99999583,  32.3697    ],
                              [ 17.54880208,  11.99999583,  32.3697    ],
                              [ 20.32320625,  11.99999583,  32.3697    ],
                              [ 11.99999375,  14.7744    ,  32.3697    ],
                              [ 14.77439792,  14.7744    ,  32.3697    ],
                              [ 17.54880208,  14.7744    ,  32.3697    ],
                              [ 20.32320625,  14.7744    ,  32.3697    ],
                              [ 11.99999375,  17.54880417,  32.3697    ],
                              [ 14.77439792,  17.54880417,  32.3697    ],
                              [ 17.54880208,  17.54880417,  32.3697    ],
                              [ 20.32320625,  17.54880417,  32.3697    ],
                              [ 13.38719583,  13.38719792,  34.3315    ],
                              [ 16.1616    ,  13.38719792,  34.3315    ],
                              [ 18.93600417,  13.38719792,  34.3315    ],
                              [ 13.38719583,  16.16160208,  34.3315    ],
                              [ 16.1616    ,  16.16160208,  34.3315    ],
                              [ 18.93600417,  16.16160208,  34.3315    ],
                              [ 11.99999375,  11.99999583,  36.2933    ],
                              [ 14.77439792,  11.99999583,  36.2933    ],
                              [ 17.54880208,  11.99999583,  36.2933    ],
                              [ 20.32320625,  11.99999583,  36.2933    ],
                              [ 11.99999375,  14.7744    ,  36.2933    ],
                              [ 14.77439792,  14.7744    ,  36.2933    ],
                              [ 17.54880208,  14.7744    ,  36.2933    ],
                              [ 20.32320625,  14.7744    ,  36.2933    ],
                              [ 11.99999375,  17.54880417,  36.2933    ],
                              [ 14.77439792,  17.54880417,  36.2933    ],
                              [ 17.54880208,  17.54880417,  36.2933    ],
                              [ 20.32320625,  17.54880417,  36.2933    ],
                              [ 13.38719583,  13.38719792,  38.2551    ],
                              [ 16.1616    ,  13.38719792,  38.2551    ],
                              [ 18.93600417,  13.38719792,  38.2551    ],
                              [ 13.38719583,  16.16160208,  38.2551    ],
                              [ 16.1616    ,  16.16160208,  38.2551    ],
                              [ 18.93600417,  16.16160208,  38.2551    ],
                              [ 11.99999375,  11.99999583,  40.2169    ],
                              [ 14.77439792,  11.99999583,  40.2169    ],
                              [ 17.54880208,  11.99999583,  40.2169    ],
                              [ 20.32320625,  11.99999583,  40.2169    ],
                              [ 11.99999375,  14.7744    ,  40.2169    ],
                              [ 14.77439792,  14.7744    ,  40.2169    ],
                              [ 17.54880208,  14.7744    ,  40.2169    ],
                              [ 20.32320625,  14.7744    ,  40.2169    ],
                              [ 11.99999375,  17.54880417,  40.2169    ],
                              [ 14.77439792,  17.54880417,  40.2169    ],
                              [ 17.54880208,  17.54880417,  40.2169    ],
                              [ 20.32320625,  17.54880417,  40.2169    ],
                              [ 13.38719583,  13.38719792,  42.1787    ],
                              [ 16.1616    ,  13.38719792,  42.1787    ],
                              [ 18.93600417,  13.38719792,  42.1787    ],
                              [ 13.38719583,  16.16160208,  42.1787    ],
                              [ 16.1616    ,  16.16160208,  42.1787    ],
                              [ 18.93600417,  16.16160208,  42.1787    ],
                              [ 11.99999375,  11.99999583,  44.1405    ],
                              [ 14.77439792,  11.99999583,  44.1405    ],
                              [ 17.54880208,  11.99999583,  44.1405    ],
                              [ 20.32320625,  11.99999583,  44.1405    ],
                              [ 11.99999375,  14.7744    ,  44.1405    ],
                              [ 14.77439792,  14.7744    ,  44.1405    ],
                              [ 17.54880208,  14.7744    ,  44.1405    ],
                              [ 20.32320625,  14.7744    ,  44.1405    ],
                              [ 11.99999375,  17.54880417,  44.1405    ],
                              [ 14.77439792,  17.54880417,  44.1405    ],
                              [ 17.54880208,  17.54880417,  44.1405    ],
                              [ 20.32320625,  17.54880417,  44.1405    ],
                              [ 13.38719583,  13.38719792,  46.1023    ],
                              [ 16.1616    ,  13.38719792,  46.1023    ],
                              [ 18.93600417,  13.38719792,  46.1023    ],
                              [ 13.38719583,  16.16160208,  46.1023    ],
                              [ 16.1616    ,  16.16160208,  46.1023    ],
                              [ 18.93600417,  16.16160208,  46.1023    ],
                              [ 11.99999375,  11.99999583,  48.0641    ],
                              [ 14.77439792,  11.99999583,  48.0641    ],
                              [ 17.54880208,  11.99999583,  48.0641    ],
                              [ 20.32320625,  11.99999583,  48.0641    ],
                              [ 11.99999375,  14.7744    ,  48.0641    ],
                              [ 14.77439792,  14.7744    ,  48.0641    ],
                              [ 17.54880208,  14.7744    ,  48.0641    ],
                              [ 20.32320625,  14.7744    ,  48.0641    ],
                              [ 11.99999375,  17.54880417,  48.0641    ],
                              [ 14.77439792,  17.54880417,  48.0641    ],
                              [ 17.54880208,  17.54880417,  48.0641    ],
                              [ 20.32320625,  17.54880417,  48.0641    ],
                              [ 13.38719583,  13.38719792,  50.0259    ],
                              [ 16.1616    ,  13.38719792,  50.0259    ],
                              [ 18.93600417,  13.38719792,  50.0259    ],
                              [ 13.38719583,  16.16160208,  50.0259    ],
                              [ 16.1616    ,  16.16160208,  50.0259    ],
                              [ 18.93600417,  16.16160208,  50.0259    ]]*Angstrom

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
        xmin =  10.99999375 *Angstrom,  xmax =  0.99999375 *Angstrom,
        ymin =  10.99999583 *Angstrom,  ymax =  18.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.99999375 *Angstrom,  xmax =  21.32320625 *Angstrom,
        ymin =  18.54880417 *Angstrom,  ymax =  28.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.32320625 *Angstrom,  xmax =  31.32320625 *Angstrom,
        ymin =  10.99999583 *Angstrom,  ymax =  18.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.99999375 *Angstrom,  xmax =  21.32320625 *Angstrom,
        ymin =  10.99999583 *Angstrom,  ymax =  0.99999583 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.99999375 *Angstrom,  xmax =  0.99999375 *Angstrom,
        ymin =  10.99999583 *Angstrom,  ymax =  0.99999583 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.99999375 *Angstrom,  xmax =  0.99999375 *Angstrom,
        ymin =  18.54880417 *Angstrom,  ymax =  28.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.32320625 *Angstrom,  xmax =  31.32320625 *Angstrom,
        ymin =  18.54880417 *Angstrom,  ymax =  28.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.32320625 *Angstrom,  xmax =  31.32320625 *Angstrom,
        ymin =  10.99999583 *Angstrom,  ymax =  0.99999583 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.99999375 *Angstrom,  xmax =  -6.25000000021e-06 *Angstrom,
        ymin =  0.99999583 *Angstrom,  ymax =  28.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -6.25000000021e-06 *Angstrom,  xmax =  32.32320625 *Angstrom,
        ymin =  28.54880417 *Angstrom,  ymax =  29.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.32320625 *Angstrom,  xmax =  32.32320625 *Angstrom,
        ymin =  0.99999583 *Angstrom,  ymax =  28.54880417 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -6.25000000021e-06 *Angstrom,  xmax =  32.32320625 *Angstrom,
        ymin =  0.99999583 *Angstrom,  ymax =  -4.17000000041e-06 *Angstrom,
        zmin =  10.01295 *Angstrom,  zmax =  40.01295 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

basis_set = [
    GGABasis.Platinum_DoubleZetaPolarized,
    ]


