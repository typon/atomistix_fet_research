# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [20.2626704098, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.2626704098, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon]

# Define coordinates
left_electrode_coordinates = [[  7.24038221,   4.52508221,   0.251586  ],
                              [ 12.67098221,   4.52508221,   0.251586  ],
                              [  4.52508221,   7.24038221,   0.251586  ],
                              [  4.52508221,  12.67098221,   0.251586  ],
                              [ 15.7375882 ,   7.5916882 ,   0.60289199],
                              [ 15.7375882 ,  13.0222882 ,   0.60289199],
                              [  7.5916882 ,  15.7375882 ,   0.60289199],
                              [ 13.0222882 ,  15.7375882 ,   0.60289199],
                              [  8.0948602 ,   5.3795602 ,   1.106064  ],
                              [ 13.5254602 ,   5.3795602 ,   1.106064  ],
                              [  5.3795602 ,   8.0948602 ,   1.106064  ],
                              [ 10.8101602 ,   8.0948602 ,   1.106064  ],
                              [  8.0948602 ,  10.8101602 ,   1.106064  ],
                              [ 13.5254602 ,  10.8101602 ,   1.106064  ],
                              [  5.3795602 ,  13.5254602 ,   1.106064  ],
                              [ 10.8101602 ,  13.5254602 ,   1.106064  ],
                              [ 15.7375882 ,   8.59803221,   1.609236  ],
                              [ 15.7375882 ,  14.02863221,   1.609236  ],
                              [  8.59803221,  15.7375882 ,   1.609236  ],
                              [ 14.02863221,  15.7375882 ,   1.609236  ],
                              [  8.9493382 ,   4.52508221,   1.96054199],
                              [ 14.3799382 ,   4.52508221,   1.96054199],
                              [  4.52508221,   8.9493382 ,   1.96054199],
                              [  4.52508221,  14.3799382 ,   1.96054199],
                              [  6.7372102 ,   6.7372102 ,   2.463714  ],
                              [ 12.1678102 ,   6.7372102 ,   2.463714  ],
                              [  9.4525102 ,   9.4525102 ,   2.463714  ],
                              [ 14.8831102 ,   9.4525102 ,   2.463714  ],
                              [  6.7372102 ,  12.1678102 ,   2.463714  ],
                              [ 12.1678102 ,  12.1678102 ,   2.463714  ],
                              [  9.4525102 ,  14.8831102 ,   2.463714  ],
                              [ 14.8831102 ,  14.8831102 ,   2.463714  ],
                              [  4.52508221,   4.52508221,   2.966886  ],
                              [  9.95568221,   4.52508221,   2.966886  ],
                              [  4.52508221,   9.95568221,   2.966886  ],
                              [ 15.7375882 ,  10.3069882 ,   3.31819199],
                              [ 10.3069882 ,  15.7375882 ,   3.31819199],
                              [ 15.7375882 ,  15.7375882 ,   3.31819199],
                              [  5.3795602 ,   5.3795602 ,   3.821364  ],
                              [ 10.8101602 ,   5.3795602 ,   3.821364  ],
                              [  8.0948602 ,   8.0948602 ,   3.821364  ],
                              [ 13.5254602 ,   8.0948602 ,   3.821364  ],
                              [  5.3795602 ,  10.8101602 ,   3.821364  ],
                              [ 10.8101602 ,  10.8101602 ,   3.821364  ],
                              [  8.0948602 ,  13.5254602 ,   3.821364  ],
                              [ 13.5254602 ,  13.5254602 ,   3.821364  ],
                              [ 15.7375882 ,   5.88273221,   4.324536  ],
                              [ 15.7375882 ,  11.31333221,   4.324536  ],
                              [  5.88273221,  15.7375882 ,   4.324536  ],
                              [ 11.31333221,  15.7375882 ,   4.324536  ],
                              [  6.2340382 ,   4.52508221,   4.67584199],
                              [ 11.6646382 ,   4.52508221,   4.67584199],
                              [  4.52508221,   6.2340382 ,   4.67584199],
                              [  4.52508221,  11.6646382 ,   4.67584199],
                              [  9.4525102 ,   6.7372102 ,   5.179014  ],
                              [ 14.8831102 ,   6.7372102 ,   5.179014  ],
                              [  6.7372102 ,   9.4525102 ,   5.179014  ],
                              [ 12.1678102 ,   9.4525102 ,   5.179014  ],
                              [  9.4525102 ,  12.1678102 ,   5.179014  ],
                              [ 14.8831102 ,  12.1678102 ,   5.179014  ],
                              [  6.7372102 ,  14.8831102 ,   5.179014  ],
                              [ 12.1678102 ,  14.8831102 ,   5.179014  ]]*Angstrom

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
vector_a = [20.2626704098, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.2626704098, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                            Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                            Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                            Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                            Hydrogen]

# Define coordinates
right_electrode_coordinates = [[  8.0948602 ,   5.3795602 ,   0.251586  ],
                               [ 13.5254602 ,   5.3795602 ,   0.251586  ],
                               [  5.3795602 ,   8.0948602 ,   0.251586  ],
                               [ 10.8101602 ,   8.0948602 ,   0.251586  ],
                               [  8.0948602 ,  10.8101602 ,   0.251586  ],
                               [ 13.5254602 ,  10.8101602 ,   0.251586  ],
                               [  5.3795602 ,  13.5254602 ,   0.251586  ],
                               [ 10.8101602 ,  13.5254602 ,   0.251586  ],
                               [ 15.7375882 ,   8.59803221,   0.75475801],
                               [ 15.7375882 ,  14.02863221,   0.75475801],
                               [  8.59803221,  15.7375882 ,   0.75475801],
                               [ 14.02863221,  15.7375882 ,   0.75475801],
                               [  8.9493382 ,   4.52508221,   1.106064  ],
                               [ 14.3799382 ,   4.52508221,   1.106064  ],
                               [  4.52508221,   8.9493382 ,   1.106064  ],
                               [  4.52508221,  14.3799382 ,   1.106064  ],
                               [  6.7372102 ,   6.7372102 ,   1.609236  ],
                               [ 12.1678102 ,   6.7372102 ,   1.609236  ],
                               [  9.4525102 ,   9.4525102 ,   1.609236  ],
                               [ 14.8831102 ,   9.4525102 ,   1.609236  ],
                               [  6.7372102 ,  12.1678102 ,   1.609236  ],
                               [ 12.1678102 ,  12.1678102 ,   1.609236  ],
                               [  9.4525102 ,  14.8831102 ,   1.609236  ],
                               [ 14.8831102 ,  14.8831102 ,   1.609236  ],
                               [  4.52508221,   4.52508221,   2.11240801],
                               [  9.95568221,   4.52508221,   2.11240801],
                               [  4.52508221,   9.95568221,   2.11240801],
                               [ 15.7375882 ,  10.3069882 ,   2.463714  ],
                               [ 10.3069882 ,  15.7375882 ,   2.463714  ],
                               [ 15.7375882 ,  15.7375882 ,   2.463714  ],
                               [  5.3795602 ,   5.3795602 ,   2.966886  ],
                               [ 10.8101602 ,   5.3795602 ,   2.966886  ],
                               [  8.0948602 ,   8.0948602 ,   2.966886  ],
                               [ 13.5254602 ,   8.0948602 ,   2.966886  ],
                               [  5.3795602 ,  10.8101602 ,   2.966886  ],
                               [ 10.8101602 ,  10.8101602 ,   2.966886  ],
                               [  8.0948602 ,  13.5254602 ,   2.966886  ],
                               [ 13.5254602 ,  13.5254602 ,   2.966886  ],
                               [ 15.7375882 ,   5.88273221,   3.47005801],
                               [ 15.7375882 ,  11.31333221,   3.47005801],
                               [  5.88273221,  15.7375882 ,   3.47005801],
                               [ 11.31333221,  15.7375882 ,   3.47005801],
                               [  6.2340382 ,   4.52508221,   3.821364  ],
                               [ 11.6646382 ,   4.52508221,   3.821364  ],
                               [  4.52508221,   6.2340382 ,   3.821364  ],
                               [  4.52508221,  11.6646382 ,   3.821364  ],
                               [  9.4525102 ,   6.7372102 ,   4.324536  ],
                               [ 14.8831102 ,   6.7372102 ,   4.324536  ],
                               [  6.7372102 ,   9.4525102 ,   4.324536  ],
                               [ 12.1678102 ,   9.4525102 ,   4.324536  ],
                               [  9.4525102 ,  12.1678102 ,   4.324536  ],
                               [ 14.8831102 ,  12.1678102 ,   4.324536  ],
                               [  6.7372102 ,  14.8831102 ,   4.324536  ],
                               [ 12.1678102 ,  14.8831102 ,   4.324536  ],
                               [  7.24038221,   4.52508221,   4.82770801],
                               [ 12.67098221,   4.52508221,   4.82770801],
                               [  4.52508221,   7.24038221,   4.82770801],
                               [  4.52508221,  12.67098221,   4.82770801],
                               [ 15.7375882 ,   7.5916882 ,   5.179014  ],
                               [ 15.7375882 ,  13.0222882 ,   5.179014  ],
                               [  7.5916882 ,  15.7375882 ,   5.179014  ],
                               [ 13.0222882 ,  15.7375882 ,   5.179014  ]]*Angstrom

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
vector_a = [20.2626704098, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.2626704098, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.7156779965]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
                           Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
central_region_coordinates = [[  7.24038221,   4.52508221,   0.251586  ],
                              [ 12.67098221,   4.52508221,   0.251586  ],
                              [  4.52508221,   7.24038221,   0.251586  ],
                              [  4.52508221,  12.67098221,   0.251586  ],
                              [ 15.7375882 ,   7.5916882 ,   0.60289199],
                              [ 15.7375882 ,  13.0222882 ,   0.60289199],
                              [  7.5916882 ,  15.7375882 ,   0.60289199],
                              [ 13.0222882 ,  15.7375882 ,   0.60289199],
                              [  8.0948602 ,   5.3795602 ,   1.106064  ],
                              [ 13.5254602 ,   5.3795602 ,   1.106064  ],
                              [  5.3795602 ,   8.0948602 ,   1.106064  ],
                              [ 10.8101602 ,   8.0948602 ,   1.106064  ],
                              [  8.0948602 ,  10.8101602 ,   1.106064  ],
                              [ 13.5254602 ,  10.8101602 ,   1.106064  ],
                              [  5.3795602 ,  13.5254602 ,   1.106064  ],
                              [ 10.8101602 ,  13.5254602 ,   1.106064  ],
                              [ 15.7375882 ,   8.59803221,   1.609236  ],
                              [ 15.7375882 ,  14.02863221,   1.609236  ],
                              [  8.59803221,  15.7375882 ,   1.609236  ],
                              [ 14.02863221,  15.7375882 ,   1.609236  ],
                              [  8.9493382 ,   4.52508221,   1.96054199],
                              [ 14.3799382 ,   4.52508221,   1.96054199],
                              [  4.52508221,   8.9493382 ,   1.96054199],
                              [  4.52508221,  14.3799382 ,   1.96054199],
                              [  6.7372102 ,   6.7372102 ,   2.463714  ],
                              [ 12.1678102 ,   6.7372102 ,   2.463714  ],
                              [  9.4525102 ,   9.4525102 ,   2.463714  ],
                              [ 14.8831102 ,   9.4525102 ,   2.463714  ],
                              [  6.7372102 ,  12.1678102 ,   2.463714  ],
                              [ 12.1678102 ,  12.1678102 ,   2.463714  ],
                              [  9.4525102 ,  14.8831102 ,   2.463714  ],
                              [ 14.8831102 ,  14.8831102 ,   2.463714  ],
                              [  4.52508221,   4.52508221,   2.966886  ],
                              [  9.95568221,   4.52508221,   2.966886  ],
                              [  4.52508221,   9.95568221,   2.966886  ],
                              [ 15.7375882 ,  10.3069882 ,   3.31819199],
                              [ 10.3069882 ,  15.7375882 ,   3.31819199],
                              [ 15.7375882 ,  15.7375882 ,   3.31819199],
                              [  5.3795602 ,   5.3795602 ,   3.821364  ],
                              [ 10.8101602 ,   5.3795602 ,   3.821364  ],
                              [  8.0948602 ,   8.0948602 ,   3.821364  ],
                              [ 13.5254602 ,   8.0948602 ,   3.821364  ],
                              [  5.3795602 ,  10.8101602 ,   3.821364  ],
                              [ 10.8101602 ,  10.8101602 ,   3.821364  ],
                              [  8.0948602 ,  13.5254602 ,   3.821364  ],
                              [ 13.5254602 ,  13.5254602 ,   3.821364  ],
                              [ 15.7375882 ,   5.88273221,   4.324536  ],
                              [ 15.7375882 ,  11.31333221,   4.324536  ],
                              [  5.88273221,  15.7375882 ,   4.324536  ],
                              [ 11.31333221,  15.7375882 ,   4.324536  ],
                              [  6.2340382 ,   4.52508221,   4.67584199],
                              [ 11.6646382 ,   4.52508221,   4.67584199],
                              [  4.52508221,   6.2340382 ,   4.67584199],
                              [  4.52508221,  11.6646382 ,   4.67584199],
                              [  9.4525102 ,   6.7372102 ,   5.179014  ],
                              [ 14.8831102 ,   6.7372102 ,   5.179014  ],
                              [  6.7372102 ,   9.4525102 ,   5.179014  ],
                              [ 12.1678102 ,   9.4525102 ,   5.179014  ],
                              [  9.4525102 ,  12.1678102 ,   5.179014  ],
                              [ 14.8831102 ,  12.1678102 ,   5.179014  ],
                              [  6.7372102 ,  14.8831102 ,   5.179014  ],
                              [ 12.1678102 ,  14.8831102 ,   5.179014  ],
                              [  7.24038221,   4.52508221,   5.682186  ],
                              [ 12.67098221,   4.52508221,   5.682186  ],
                              [  4.52508221,   7.24038221,   5.682186  ],
                              [  4.52508221,  12.67098221,   5.682186  ],
                              [ 15.7375882 ,   7.5916882 ,   6.03349199],
                              [ 15.7375882 ,  13.0222882 ,   6.03349199],
                              [  7.5916882 ,  15.7375882 ,   6.03349199],
                              [ 13.0222882 ,  15.7375882 ,   6.03349199],
                              [  8.0948602 ,   5.3795602 ,   6.536664  ],
                              [ 13.5254602 ,   5.3795602 ,   6.536664  ],
                              [  5.3795602 ,   8.0948602 ,   6.536664  ],
                              [ 10.8101602 ,   8.0948602 ,   6.536664  ],
                              [  8.0948602 ,  10.8101602 ,   6.536664  ],
                              [ 13.5254602 ,  10.8101602 ,   6.536664  ],
                              [  5.3795602 ,  13.5254602 ,   6.536664  ],
                              [ 10.8101602 ,  13.5254602 ,   6.536664  ],
                              [ 15.7375882 ,   8.59803221,   7.039836  ],
                              [ 15.7375882 ,  14.02863221,   7.039836  ],
                              [  8.59803221,  15.7375882 ,   7.039836  ],
                              [ 14.02863221,  15.7375882 ,   7.039836  ],
                              [  8.9493382 ,   4.52508221,   7.39114199],
                              [ 14.3799382 ,   4.52508221,   7.39114199],
                              [  4.52508221,   8.9493382 ,   7.39114199],
                              [  4.52508221,  14.3799382 ,   7.39114199],
                              [  6.7372102 ,   6.7372102 ,   7.894314  ],
                              [ 12.1678102 ,   6.7372102 ,   7.894314  ],
                              [  9.4525102 ,   9.4525102 ,   7.894314  ],
                              [ 14.8831102 ,   9.4525102 ,   7.894314  ],
                              [  6.7372102 ,  12.1678102 ,   7.894314  ],
                              [ 12.1678102 ,  12.1678102 ,   7.894314  ],
                              [  9.4525102 ,  14.8831102 ,   7.894314  ],
                              [ 14.8831102 ,  14.8831102 ,   7.894314  ],
                              [  4.52508221,   4.52508221,   8.397486  ],
                              [  9.95568221,   4.52508221,   8.397486  ],
                              [  4.52508221,   9.95568221,   8.397486  ],
                              [ 15.7375882 ,  10.3069882 ,   8.74879199],
                              [ 10.3069882 ,  15.7375882 ,   8.74879199],
                              [ 15.7375882 ,  15.7375882 ,   8.74879199],
                              [  5.3795602 ,   5.3795602 ,   9.251964  ],
                              [ 10.8101602 ,   5.3795602 ,   9.251964  ],
                              [  8.0948602 ,   8.0948602 ,   9.251964  ],
                              [ 13.5254602 ,   8.0948602 ,   9.251964  ],
                              [  5.3795602 ,  10.8101602 ,   9.251964  ],
                              [ 10.8101602 ,  10.8101602 ,   9.251964  ],
                              [  8.0948602 ,  13.5254602 ,   9.251964  ],
                              [ 13.5254602 ,  13.5254602 ,   9.251964  ],
                              [ 15.7375882 ,   5.88273221,   9.755136  ],
                              [ 15.7375882 ,  11.31333221,   9.755136  ],
                              [  5.88273221,  15.7375882 ,   9.755136  ],
                              [ 11.31333221,  15.7375882 ,   9.755136  ],
                              [  6.2340382 ,   4.52508221,  10.10644199],
                              [ 11.6646382 ,   4.52508221,  10.10644199],
                              [  4.52508221,   6.2340382 ,  10.10644199],
                              [  4.52508221,  11.6646382 ,  10.10644199],
                              [  9.4525102 ,   6.7372102 ,  10.609614  ],
                              [ 14.8831102 ,   6.7372102 ,  10.609614  ],
                              [  6.7372102 ,   9.4525102 ,  10.609614  ],
                              [ 12.1678102 ,   9.4525102 ,  10.609614  ],
                              [  9.4525102 ,  12.1678102 ,  10.609614  ],
                              [ 14.8831102 ,  12.1678102 ,  10.609614  ],
                              [  6.7372102 ,  14.8831102 ,  10.609614  ],
                              [ 12.1678102 ,  14.8831102 ,  10.609614  ],
                              [  7.24038221,   4.52508221,  11.112786  ],
                              [ 12.67098221,   4.52508221,  11.112786  ],
                              [  4.52508221,   7.24038221,  11.112786  ],
                              [  4.52508221,  12.67098221,  11.112786  ],
                              [ 15.7375882 ,   7.5916882 ,  11.46409199],
                              [ 15.7375882 ,  13.0222882 ,  11.46409199],
                              [  7.5916882 ,  15.7375882 ,  11.46409199],
                              [ 13.0222882 ,  15.7375882 ,  11.46409199]]*Angstrom

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
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


