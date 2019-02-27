# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [10.6385395934, 0.0, 0.0]*Angstrom
vector_b = [-0.409174599746, -10.6306679389, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.6835]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium]

# Define coordinates
left_electrode_coordinates = [[  1.6366984 ,  -0.47247413,   1.170875  ],
                              [  9.41101579,  -1.18118533,   1.170875  ],
                              [  6.5467936 ,  -1.88989652,   1.170875  ],
                              [  3.6825714 ,  -2.59860772,   1.170875  ],
                              [  0.8183492 ,  -3.30731891,   1.170875  ],
                              [  8.59266659,  -4.01603011,   1.170875  ],
                              [  5.7284444 ,  -4.72474131,   1.170875  ],
                              [  2.8642222 ,  -5.4334525 ,   1.170875  ],
                              [  0.        ,  -6.1421637 ,   1.170875  ],
                              [  7.7743174 ,  -6.85087489,   1.170875  ],
                              [  4.9100952 ,  -7.55958609,   1.170875  ],
                              [  2.045873  ,  -8.26829729,   1.170875  ],
                              [  9.82019039,  -8.97700848,   1.170875  ],
                              [  6.9559682 ,  -9.68571968,   1.170875  ],
                              [  4.091746  , -10.39443087,   1.170875  ],
                              [  6.137619  ,  -0.23623707,   3.512625  ],
                              [  3.2733968 ,  -0.94494826,   3.512625  ],
                              [  0.4091746 ,  -1.65365946,   3.512625  ],
                              [  8.18349199,  -2.36237065,   3.512625  ],
                              [  5.3192698 ,  -3.07108185,   3.512625  ],
                              [  2.4550476 ,  -3.77979304,   3.512625  ],
                              [ 10.22936499,  -4.48850424,   3.512625  ],
                              [  7.3651428 ,  -5.19721544,   3.512625  ],
                              [  4.5009206 ,  -5.90592663,   3.512625  ],
                              [  1.6366984 ,  -6.61463783,   3.512625  ],
                              [  9.41101579,  -7.32334902,   3.512625  ],
                              [  6.5467936 ,  -8.03206022,   3.512625  ],
                              [  3.6825714 ,  -8.74077142,   3.512625  ],
                              [  0.8183492 ,  -9.44948261,   3.512625  ],
                              [  8.59266659, -10.15819381,   3.512625  ]]*Angstrom

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
vector_a = [10.6385395934, 0.0, 0.0]*Angstrom
vector_b = [-0.409174599746, -10.6306679389, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.959]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen,
                            Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium,
                            Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen,
                            Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium,
                            Oxygen, Oxygen]

# Define coordinates
right_electrode_coordinates = [[  9.37851915,  -0.41438344,   0.73975   ],
                               [  7.40606026,  -1.06306679,   0.73975   ],
                               [  5.43360136,  -1.71175015,   0.73975   ],
                               [  2.91356047,  -2.54051702,   0.73975   ],
                               [  0.94110158,  -3.18920038,   0.73975   ],
                               [  9.60718228,  -3.83788374,   0.73975   ],
                               [  7.08714139,  -4.66665061,   0.73975   ],
                               [  5.1146825 ,  -5.31533397,   0.73975   ],
                               [  3.1422236 ,  -5.96401733,   0.73975   ],
                               [  0.62218271,  -6.7927842 ,   0.73975   ],
                               [  9.28826341,  -7.44146756,   0.73975   ],
                               [  7.31580452,  -8.09015091,   0.73975   ],
                               [  4.79576363,  -8.91891779,   0.73975   ],
                               [  2.82330474,  -9.56760115,   0.73975   ],
                               [  0.85084585, -10.2162845 ,   0.73975   ],
                               [  0.        ,   0.        ,   2.21925   ],
                               [  3.59932073,  -0.18008351,   2.21925   ],
                               [  0.57426018,  -1.94605007,   2.21925   ],
                               [  4.17358092,  -2.12613359,   2.21925   ],
                               [  7.77290165,  -2.3062171 ,   2.21925   ],
                               [  4.7478411 ,  -4.07218366,   2.21925   ],
                               [  8.34716183,  -4.25226718,   2.21925   ],
                               [  1.30794298,  -4.43235069,   2.21925   ],
                               [  8.92142202,  -6.19831725,   2.21925   ],
                               [  1.88220316,  -6.37840076,   2.21925   ],
                               [  5.48152389,  -6.55848428,   2.21925   ],
                               [  2.45646334,  -8.32445084,   2.21925   ],
                               [  6.05578408,  -8.50453435,   2.21925   ],
                               [  9.65510481,  -8.68461787,   2.21925   ],
                               [  6.63004426, -10.45058442,   2.21925   ]]*Angstrom

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
vector_a = [10.6385395934, 0.0, 0.0]*Angstrom
vector_b = [-0.409174599746, -10.6306679389, 0.0]*Angstrom
vector_c = [0.0, 0.0, 18.3665]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Oxygen, Oxygen, Titanium,
                           Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen,
                           Oxygen, Titanium, Oxygen, Oxygen, Oxygen, Titanium, Oxygen,
                           Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen,
                           Titanium, Oxygen, Oxygen, Titanium, Oxygen, Titanium, Oxygen,
                           Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen,
                           Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Oxygen,
                           Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium,
                           Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen,
                           Titanium, Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium,
                           Oxygen, Oxygen, Titanium, Oxygen, Oxygen, Titanium, Oxygen,
                           Oxygen]

# Define coordinates
central_region_coordinates = [[  1.6366984 ,  -0.47247413,   1.170875  ],
                              [  9.41101579,  -1.18118533,   1.170875  ],
                              [  6.5467936 ,  -1.88989652,   1.170875  ],
                              [  3.6825714 ,  -2.59860772,   1.170875  ],
                              [  0.8183492 ,  -3.30731891,   1.170875  ],
                              [  8.59266659,  -4.01603011,   1.170875  ],
                              [  5.7284444 ,  -4.72474131,   1.170875  ],
                              [  2.8642222 ,  -5.4334525 ,   1.170875  ],
                              [  0.        ,  -6.1421637 ,   1.170875  ],
                              [  7.7743174 ,  -6.85087489,   1.170875  ],
                              [  4.9100952 ,  -7.55958609,   1.170875  ],
                              [  2.045873  ,  -8.26829729,   1.170875  ],
                              [  9.82019039,  -8.97700848,   1.170875  ],
                              [  6.9559682 ,  -9.68571968,   1.170875  ],
                              [  4.091746  , -10.39443087,   1.170875  ],
                              [  6.137619  ,  -0.23623707,   3.512625  ],
                              [  3.2733968 ,  -0.94494826,   3.512625  ],
                              [  0.4091746 ,  -1.65365946,   3.512625  ],
                              [  8.18349199,  -2.36237065,   3.512625  ],
                              [  5.3192698 ,  -3.07108185,   3.512625  ],
                              [  2.4550476 ,  -3.77979304,   3.512625  ],
                              [ 10.22936499,  -4.48850424,   3.512625  ],
                              [  7.3651428 ,  -5.19721544,   3.512625  ],
                              [  4.5009206 ,  -5.90592663,   3.512625  ],
                              [  1.6366984 ,  -6.61463783,   3.512625  ],
                              [  9.41101579,  -7.32334902,   3.512625  ],
                              [  6.5467936 ,  -8.03206022,   3.512625  ],
                              [  3.6825714 ,  -8.74077142,   3.512625  ],
                              [  0.8183492 ,  -9.44948261,   3.512625  ],
                              [  8.59266659, -10.15819381,   3.512625  ],
                              [  1.6366984 ,  -0.47247413,   5.854375  ],
                              [  9.41101579,  -1.18118533,   5.854375  ],
                              [  6.5467936 ,  -1.88989652,   5.854375  ],
                              [  3.6825714 ,  -2.59860772,   5.854375  ],
                              [  0.8183492 ,  -3.30731891,   5.854375  ],
                              [  8.59266659,  -4.01603011,   5.854375  ],
                              [  5.7284444 ,  -4.72474131,   5.854375  ],
                              [  2.8642222 ,  -5.4334525 ,   5.854375  ],
                              [  0.        ,  -6.1421637 ,   5.854375  ],
                              [  7.7743174 ,  -6.85087489,   5.854375  ],
                              [  4.9100952 ,  -7.55958609,   5.854375  ],
                              [  2.045873  ,  -8.26829729,   5.854375  ],
                              [  9.82019039,  -8.97700848,   5.854375  ],
                              [  6.9559682 ,  -9.68571968,   5.854375  ],
                              [  4.091746  , -10.39443087,   5.854375  ],
                              [  6.137619  ,  -0.23623707,   8.196125  ],
                              [  3.2733968 ,  -0.94494826,   8.196125  ],
                              [  0.4091746 ,  -1.65365946,   8.196125  ],
                              [  8.18349199,  -2.36237065,   8.196125  ],
                              [  5.3192698 ,  -3.07108185,   8.196125  ],
                              [  2.4550476 ,  -3.77979304,   8.196125  ],
                              [ 10.22936499,  -4.48850424,   8.196125  ],
                              [  7.3651428 ,  -5.19721544,   8.196125  ],
                              [  4.5009206 ,  -5.90592663,   8.196125  ],
                              [  1.6366984 ,  -6.61463783,   8.196125  ],
                              [  9.41101579,  -7.32334902,   8.196125  ],
                              [  6.5467936 ,  -8.03206022,   8.196125  ],
                              [  3.6825714 ,  -8.74077142,   8.196125  ],
                              [  0.8183492 ,  -9.44948261,   8.196125  ],
                              [  8.59266659, -10.15819381,   8.196125  ],
                              [  1.6366984 ,  -0.47247413,  10.537875  ],
                              [  9.41101579,  -1.18118533,  10.537875  ],
                              [  6.5467936 ,  -1.88989652,  10.537875  ],
                              [  3.6825714 ,  -2.59860772,  10.537875  ],
                              [  0.8183492 ,  -3.30731891,  10.537875  ],
                              [  8.59266659,  -4.01603011,  10.537875  ],
                              [  5.7284444 ,  -4.72474131,  10.537875  ],
                              [  2.8642222 ,  -5.4334525 ,  10.537875  ],
                              [  0.        ,  -6.1421637 ,  10.537875  ],
                              [  7.7743174 ,  -6.85087489,  10.537875  ],
                              [  4.9100952 ,  -7.55958609,  10.537875  ],
                              [  2.045873  ,  -8.26829729,  10.537875  ],
                              [  9.82019039,  -8.97700848,  10.537875  ],
                              [  6.9559682 ,  -9.68571968,  10.537875  ],
                              [  4.091746  , -10.39443087,  10.537875  ],
                              [  0.        ,   0.        ,  11.70875   ],
                              [  3.59932073,  -0.18008351,  11.70875   ],
                              [  0.57426018,  -1.94605007,  11.70875   ],
                              [  4.17358092,  -2.12613359,  11.70875   ],
                              [  7.77290165,  -2.3062171 ,  11.70875   ],
                              [  4.7478411 ,  -4.07218366,  11.70875   ],
                              [  8.34716183,  -4.25226718,  11.70875   ],
                              [  1.30794298,  -4.43235069,  11.70875   ],
                              [  8.92142202,  -6.19831725,  11.70875   ],
                              [  1.88220316,  -6.37840076,  11.70875   ],
                              [  5.48152389,  -6.55848428,  11.70875   ],
                              [  2.45646334,  -8.32445084,  11.70875   ],
                              [  6.05578408,  -8.50453435,  11.70875   ],
                              [  9.65510481,  -8.68461787,  11.70875   ],
                              [  6.63004426, -10.45058442,  11.70875   ],
                              [  9.37851915,  -0.41438344,  13.18825   ],
                              [  7.40606026,  -1.06306679,  13.18825   ],
                              [  5.43360136,  -1.71175015,  13.18825   ],
                              [  2.91356047,  -2.54051702,  13.18825   ],
                              [  0.94110158,  -3.18920038,  13.18825   ],
                              [  9.60718228,  -3.83788374,  13.18825   ],
                              [  7.08714139,  -4.66665061,  13.18825   ],
                              [  5.1146825 ,  -5.31533397,  13.18825   ],
                              [  3.1422236 ,  -5.96401733,  13.18825   ],
                              [  0.62218271,  -6.7927842 ,  13.18825   ],
                              [  9.28826341,  -7.44146756,  13.18825   ],
                              [  7.31580452,  -8.09015091,  13.18825   ],
                              [  4.79576363,  -8.91891779,  13.18825   ],
                              [  2.82330474,  -9.56760115,  13.18825   ],
                              [  0.85084585, -10.2162845 ,  13.18825   ],
                              [  0.        ,   0.        ,  14.66775   ],
                              [  3.59932073,  -0.18008351,  14.66775   ],
                              [  0.57426018,  -1.94605007,  14.66775   ],
                              [  4.17358092,  -2.12613359,  14.66775   ],
                              [  7.77290165,  -2.3062171 ,  14.66775   ],
                              [  4.7478411 ,  -4.07218366,  14.66775   ],
                              [  8.34716183,  -4.25226718,  14.66775   ],
                              [  1.30794298,  -4.43235069,  14.66775   ],
                              [  8.92142202,  -6.19831725,  14.66775   ],
                              [  1.88220316,  -6.37840076,  14.66775   ],
                              [  5.48152389,  -6.55848428,  14.66775   ],
                              [  2.45646334,  -8.32445084,  14.66775   ],
                              [  6.05578408,  -8.50453435,  14.66775   ],
                              [  9.65510481,  -8.68461787,  14.66775   ],
                              [  6.63004426, -10.45058442,  14.66775   ],
                              [  9.37851915,  -0.41438344,  16.14725   ],
                              [  7.40606026,  -1.06306679,  16.14725   ],
                              [  5.43360136,  -1.71175015,  16.14725   ],
                              [  2.91356047,  -2.54051702,  16.14725   ],
                              [  0.94110158,  -3.18920038,  16.14725   ],
                              [  9.60718228,  -3.83788374,  16.14725   ],
                              [  7.08714139,  -4.66665061,  16.14725   ],
                              [  5.1146825 ,  -5.31533397,  16.14725   ],
                              [  3.1422236 ,  -5.96401733,  16.14725   ],
                              [  0.62218271,  -6.7927842 ,  16.14725   ],
                              [  9.28826341,  -7.44146756,  16.14725   ],
                              [  7.31580452,  -8.09015091,  16.14725   ],
                              [  4.79576363,  -8.91891779,  16.14725   ],
                              [  2.82330474,  -9.56760115,  16.14725   ],
                              [  0.85084585, -10.2162845 ,  16.14725   ],
                              [  0.        ,   0.        ,  17.62675   ],
                              [  3.59932073,  -0.18008351,  17.62675   ],
                              [  0.57426018,  -1.94605007,  17.62675   ],
                              [  4.17358092,  -2.12613359,  17.62675   ],
                              [  7.77290165,  -2.3062171 ,  17.62675   ],
                              [  4.7478411 ,  -4.07218366,  17.62675   ],
                              [  8.34716183,  -4.25226718,  17.62675   ],
                              [  1.30794298,  -4.43235069,  17.62675   ],
                              [  8.92142202,  -6.19831725,  17.62675   ],
                              [  1.88220316,  -6.37840076,  17.62675   ],
                              [  5.48152389,  -6.55848428,  17.62675   ],
                              [  2.45646334,  -8.32445084,  17.62675   ],
                              [  6.05578408,  -8.50453435,  17.62675   ],
                              [  9.65510481,  -8.68461787,  17.62675   ],
                              [  6.63004426, -10.45058442,  17.62675   ]]*Angstrom

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
    GGABasis.Titanium_DoubleZetaPolarized,
    GGABasis.Oxygen_DoubleZetaPolarized,
    ]