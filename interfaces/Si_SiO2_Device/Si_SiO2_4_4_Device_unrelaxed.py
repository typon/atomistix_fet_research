# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [13.3021989972, 0.0, 0.0]*Angstrom
vector_b = [-6.65109949858, 11.5200422577, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.05455633669]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon]

# Define coordinates
left_electrode_coordinates = [[  2.21703317,  -0.        ,   0.3919198 ],
                              [  8.86813266,  -0.        ,   0.3919198 ],
                              [ -1.10851658,   1.92000704,   0.3919198 ],
                              [  5.54258292,   1.92000704,   0.3919198 ],
                              [  2.21703317,   3.84001409,   0.3919198 ],
                              [  8.86813266,   3.84001409,   0.3919198 ],
                              [ -1.10851658,   5.76002113,   0.3919198 ],
                              [  5.54258292,   5.76002113,   0.3919198 ],
                              [ -4.43406633,   7.68002817,   0.3919198 ],
                              [  2.21703317,   7.68002817,   0.3919198 ],
                              [ -1.10851658,   9.60003521,   0.3919198 ],
                              [  5.54258292,   9.60003521,   0.3919198 ],
                              [  4.43406633,  -0.        ,   1.17575939],
                              [ 11.08516583,   0.        ,   1.17575939],
                              [  1.10851658,   1.92000704,   1.17575939],
                              [  7.75961608,   1.92000704,   1.17575939],
                              [ -2.21703317,   3.84001409,   1.17575939],
                              [  4.43406633,   3.84001409,   1.17575939],
                              [  1.10851658,   5.76002113,   1.17575939],
                              [  7.75961608,   5.76002113,   1.17575939],
                              [ -2.21703317,   7.68002817,   1.17575939],
                              [  4.43406633,   7.68002817,   1.17575939],
                              [ -5.54258292,   9.60003521,   1.17575939],
                              [  1.10851658,   9.60003521,   1.17575939],
                              [  4.43406633,  -0.        ,   3.52727817],
                              [ 11.08516583,  -0.        ,   3.52727817],
                              [  1.10851658,   1.92000704,   3.52727817],
                              [  7.75961608,   1.92000704,   3.52727817],
                              [ -2.21703317,   3.84001409,   3.52727817],
                              [  4.43406633,   3.84001409,   3.52727817],
                              [  1.10851658,   5.76002113,   3.52727817],
                              [  7.75961608,   5.76002113,   3.52727817],
                              [ -2.21703317,   7.68002817,   3.52727817],
                              [  4.43406633,   7.68002817,   3.52727817],
                              [ -5.54258292,   9.60003521,   3.52727817],
                              [  1.10851658,   9.60003521,   3.52727817],
                              [ -0.        ,  -0.        ,   4.31111776],
                              [  6.6510995 ,  -0.        ,   4.31111776],
                              [  3.32554975,   1.92000704,   4.31111776],
                              [  9.97664925,   1.92000704,   4.31111776],
                              [ -0.        ,   3.84001409,   4.31111776],
                              [  6.6510995 ,   3.84001409,   4.31111776],
                              [ -3.32554975,   5.76002113,   4.31111776],
                              [  3.32554975,   5.76002113,   4.31111776],
                              [ -0.        ,   7.68002817,   4.31111776],
                              [  6.6510995 ,   7.68002817,   4.31111776],
                              [ -3.32554975,   9.60003521,   4.31111776],
                              [  3.32554975,   9.60003521,   4.31111776],
                              [ -0.        ,  -0.        ,   6.66263654],
                              [  6.6510995 ,  -0.        ,   6.66263654],
                              [  3.32554975,   1.92000704,   6.66263654],
                              [  9.97664925,   1.92000704,   6.66263654],
                              [ -0.        ,   3.84001409,   6.66263654],
                              [  6.6510995 ,   3.84001409,   6.66263654],
                              [ -3.32554975,   5.76002113,   6.66263654],
                              [  3.32554975,   5.76002113,   6.66263654],
                              [ -0.        ,   7.68002817,   6.66263654],
                              [  6.6510995 ,   7.68002817,   6.66263654],
                              [ -3.32554975,   9.60003521,   6.66263654],
                              [  3.32554975,   9.60003521,   6.66263654]]*Angstrom

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
vector_a = [13.3021989972, 0.0, 0.0]*Angstrom
vector_b = [-6.65109949858, 11.5200422577, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4054]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Silicon,
                            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Silicon, Silicon, Silicon,
                            Silicon, Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen, Oxygen, Silicon, Silicon, Silicon, Silicon,
                            Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen]

# Define coordinates
right_electrode_coordinates = [[  6.72625692,   1.60243788,   0.25711596],
                               [  1.97547157,   3.2481582 ,   0.25711596],
                               [ -2.77531379,   4.89387852,   0.25711596],
                               [  5.77609985,   6.53959885,   0.25711596],
                               [  1.0253145 ,   8.18531917,   0.25711596],
                               [ -3.72547086,   9.83103949,   0.25711596],
                               [  4.82594278,  11.47675981,   0.25711596],
                               [  6.76625854,   0.09973065,   0.90090088],
                               [  2.01547318,   1.74545097,   0.90090088],
                               [ 10.56688682,   3.3911713 ,   0.90090088],
                               [  5.81610146,   5.03689162,   0.90090088],
                               [  1.06531611,   6.68261194,   0.90090088],
                               [ -3.68546925,   8.32833226,   0.90090088],
                               [  4.86594439,   9.97405259,   0.90090088],
                               [  3.4970531 ,   1.49118718,   1.54468224],
                               [ -1.25373226,   3.13690751,   1.54468224],
                               [  7.29768139,   4.78262783,   1.54468224],
                               [  2.54689603,   6.42834815,   1.54468224],
                               [ -2.20388933,   8.07406847,   1.54468224],
                               [  6.34752431,   9.7197888 ,   1.54468224],
                               [  1.59673896,  11.36550912,   1.54468224],
                               [  0.87509466,   1.60227331,   2.05891956],
                               [  9.4265083 ,   3.24799363,   2.05891956],
                               [  4.67572295,   4.89371395,   2.05891956],
                               [ -0.07506241,   6.53943427,   2.05891956],
                               [  8.47635123,   8.1851546 ,   2.05891956],
                               [  3.72556588,   9.83087492,   2.05891956],
                               [ -1.02521948,  11.47659524,   2.05891956],
                               [  4.30449658,   0.67326418,   2.70270092],
                               [ -0.44628878,   2.31898451,   2.70270092],
                               [  8.10512486,   3.96470483,   2.70270092],
                               [  3.35433951,   5.61042515,   2.70270092],
                               [ -1.39644585,   7.25614547,   2.70270092],
                               [  7.15496779,   8.9018658 ,   2.70270092],
                               [  2.40418244,  10.54758612,   2.70270092],
                               [ 11.89492136,   1.16303055,   3.34648584],
                               [  7.144136  ,   2.80875087,   3.34648584],
                               [  2.39335065,   4.4544712 ,   3.34648584],
                               [ -2.35743471,   6.10019152,   3.34648584],
                               [  6.19397893,   7.74591184,   3.34648584],
                               [  1.44319358,   9.39163216,   3.34648584],
                               [ -3.30759178,  11.03735249,   3.34648584],
                               [  9.5014757 ,   0.08672946,   3.86071776],
                               [  4.75069034,   1.73244978,   3.86071776],
                               [ -0.00009502,   3.37817011,   3.86071776],
                               [  8.55131863,   5.02389043,   3.86071776],
                               [  3.80053327,   6.66961075,   3.86071776],
                               [ -0.95025209,   8.31533107,   3.86071776],
                               [ -5.70103744,   9.9610514 ,   3.86071776],
                               [ 10.78285752,   0.87272549,   4.5045009 ],
                               [  6.03207217,   2.51844581,   4.5045009 ],
                               [  1.28128681,   4.16416613,   4.5045009 ],
                               [  9.83270045,   5.80988645,   4.5045009 ],
                               [  5.0819151 ,   7.45560678,   4.5045009 ],
                               [  0.33112974,   9.1013271 ,   4.5045009 ],
                               [ -4.41965562,  10.74704742,   4.5045009 ],
                               [  1.71085282,   0.63722291,   5.14828404],
                               [ 10.26226646,   2.28294323,   5.14828404],
                               [  5.51148111,   3.92866355,   5.14828404],
                               [  0.76069575,   5.57438388,   5.14828404],
                               [ -3.9900896 ,   7.2201042 ,   5.14828404],
                               [  4.56132404,   8.86582452,   5.14828404],
                               [ -0.18946132,  10.51154484,   5.14828404]]*Angstrom

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
vector_a = [13.3021989972, 0.0, 0.0]*Angstrom
vector_b = [-6.65109949858, 11.5200422577, 0.0]*Angstrom
vector_c = [0.0, 0.0, 15.3042940112]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Silicon, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Silicon, Silicon, Silicon,
                           Silicon, Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
central_region_coordinates = [[  2.21703317,  -0.        ,   0.3919198 ],
                              [  8.86813266,  -0.        ,   0.3919198 ],
                              [ -1.10851658,   1.92000704,   0.3919198 ],
                              [  5.54258292,   1.92000704,   0.3919198 ],
                              [  2.21703317,   3.84001409,   0.3919198 ],
                              [  8.86813266,   3.84001409,   0.3919198 ],
                              [ -1.10851658,   5.76002113,   0.3919198 ],
                              [  5.54258292,   5.76002113,   0.3919198 ],
                              [ -4.43406633,   7.68002817,   0.3919198 ],
                              [  2.21703317,   7.68002817,   0.3919198 ],
                              [ -1.10851658,   9.60003521,   0.3919198 ],
                              [  5.54258292,   9.60003521,   0.3919198 ],
                              [  4.43406633,  -0.        ,   1.17575939],
                              [ 11.08516583,   0.        ,   1.17575939],
                              [  1.10851658,   1.92000704,   1.17575939],
                              [  7.75961608,   1.92000704,   1.17575939],
                              [ -2.21703317,   3.84001409,   1.17575939],
                              [  4.43406633,   3.84001409,   1.17575939],
                              [  1.10851658,   5.76002113,   1.17575939],
                              [  7.75961608,   5.76002113,   1.17575939],
                              [ -2.21703317,   7.68002817,   1.17575939],
                              [  4.43406633,   7.68002817,   1.17575939],
                              [ -5.54258292,   9.60003521,   1.17575939],
                              [  1.10851658,   9.60003521,   1.17575939],
                              [  4.43406633,  -0.        ,   3.52727817],
                              [ 11.08516583,  -0.        ,   3.52727817],
                              [  1.10851658,   1.92000704,   3.52727817],
                              [  7.75961608,   1.92000704,   3.52727817],
                              [ -2.21703317,   3.84001409,   3.52727817],
                              [  4.43406633,   3.84001409,   3.52727817],
                              [  1.10851658,   5.76002113,   3.52727817],
                              [  7.75961608,   5.76002113,   3.52727817],
                              [ -2.21703317,   7.68002817,   3.52727817],
                              [  4.43406633,   7.68002817,   3.52727817],
                              [ -5.54258292,   9.60003521,   3.52727817],
                              [  1.10851658,   9.60003521,   3.52727817],
                              [ -0.        ,  -0.        ,   4.31111776],
                              [  6.6510995 ,  -0.        ,   4.31111776],
                              [  3.32554975,   1.92000704,   4.31111776],
                              [  9.97664925,   1.92000704,   4.31111776],
                              [ -0.        ,   3.84001409,   4.31111776],
                              [  6.6510995 ,   3.84001409,   4.31111776],
                              [ -3.32554975,   5.76002113,   4.31111776],
                              [  3.32554975,   5.76002113,   4.31111776],
                              [ -0.        ,   7.68002817,   4.31111776],
                              [  6.6510995 ,   7.68002817,   4.31111776],
                              [ -3.32554975,   9.60003521,   4.31111776],
                              [  3.32554975,   9.60003521,   4.31111776],
                              [ -0.        ,  -0.        ,   6.66263654],
                              [  6.6510995 ,  -0.        ,   6.66263654],
                              [  3.32554975,   1.92000704,   6.66263654],
                              [  9.97664925,   1.92000704,   6.66263654],
                              [ -0.        ,   3.84001409,   6.66263654],
                              [  6.6510995 ,   3.84001409,   6.66263654],
                              [ -3.32554975,   5.76002113,   6.66263654],
                              [  3.32554975,   5.76002113,   6.66263654],
                              [ -0.        ,   7.68002817,   6.66263654],
                              [  6.6510995 ,   7.68002817,   6.66263654],
                              [ -3.32554975,   9.60003521,   6.66263654],
                              [  3.32554975,   9.60003521,   6.66263654],
                              [  2.21703317,  -0.        ,   7.44647613],
                              [  8.86813266,  -0.        ,   7.44647613],
                              [ -1.10851658,   1.92000704,   7.44647613],
                              [  5.54258292,   1.92000704,   7.44647613],
                              [  2.21703317,   3.84001409,   7.44647613],
                              [  8.86813266,   3.84001409,   7.44647613],
                              [ -1.10851658,   5.76002113,   7.44647613],
                              [  5.54258292,   5.76002113,   7.44647613],
                              [ -4.43406633,   7.68002817,   7.44647613],
                              [  2.21703317,   7.68002817,   7.44647613],
                              [ -1.10851658,   9.60003521,   7.44647613],
                              [  5.54258292,   9.60003521,   7.44647613],
                              [ 10.78285752,   0.87272549,   8.99799491],
                              [  6.03207217,   2.51844581,   8.99799491],
                              [  1.28128681,   4.16416613,   8.99799491],
                              [  9.83270045,   5.80988645,   8.99799491],
                              [  5.0819151 ,   7.45560678,   8.99799491],
                              [  0.33112974,   9.1013271 ,   8.99799491],
                              [ -4.41965562,  10.74704742,   8.99799491],
                              [  1.71085282,   0.63722291,   9.64177805],
                              [ 10.26226646,   2.28294323,   9.64177805],
                              [  5.51148111,   3.92866355,   9.64177805],
                              [  0.76069575,   5.57438388,   9.64177805],
                              [ -3.9900896 ,   7.2201042 ,   9.64177805],
                              [  4.56132404,   8.86582452,   9.64177805],
                              [ -0.18946132,  10.51154484,   9.64177805],
                              [  6.72625692,   1.60243788,  10.15600997],
                              [  1.97547157,   3.2481582 ,  10.15600997],
                              [ -2.77531379,   4.89387852,  10.15600997],
                              [  5.77609985,   6.53959885,  10.15600997],
                              [  1.0253145 ,   8.18531917,  10.15600997],
                              [ -3.72547086,   9.83103949,  10.15600997],
                              [  4.82594278,  11.47675981,  10.15600997],
                              [  6.76625854,   0.09973065,  10.79979489],
                              [  2.01547318,   1.74545097,  10.79979489],
                              [ 10.56688682,   3.3911713 ,  10.79979489],
                              [  5.81610146,   5.03689162,  10.79979489],
                              [  1.06531611,   6.68261194,  10.79979489],
                              [ -3.68546925,   8.32833226,  10.79979489],
                              [  4.86594439,   9.97405259,  10.79979489],
                              [  3.4970531 ,   1.49118718,  11.44357625],
                              [ -1.25373226,   3.13690751,  11.44357625],
                              [  7.29768139,   4.78262783,  11.44357625],
                              [  2.54689603,   6.42834815,  11.44357625],
                              [ -2.20388933,   8.07406847,  11.44357625],
                              [  6.34752431,   9.7197888 ,  11.44357625],
                              [  1.59673896,  11.36550912,  11.44357625],
                              [  0.87509466,   1.60227331,  11.95781357],
                              [  9.4265083 ,   3.24799363,  11.95781357],
                              [  4.67572295,   4.89371395,  11.95781357],
                              [ -0.07506241,   6.53943427,  11.95781357],
                              [  8.47635123,   8.1851546 ,  11.95781357],
                              [  3.72556588,   9.83087492,  11.95781357],
                              [ -1.02521948,  11.47659524,  11.95781357],
                              [  4.30449658,   0.67326418,  12.60159493],
                              [ -0.44628878,   2.31898451,  12.60159493],
                              [  8.10512486,   3.96470483,  12.60159493],
                              [  3.35433951,   5.61042515,  12.60159493],
                              [ -1.39644585,   7.25614547,  12.60159493],
                              [  7.15496779,   8.9018658 ,  12.60159493],
                              [  2.40418244,  10.54758612,  12.60159493],
                              [ 11.89492136,   1.16303055,  13.24537985],
                              [  7.144136  ,   2.80875087,  13.24537985],
                              [  2.39335065,   4.4544712 ,  13.24537985],
                              [ -2.35743471,   6.10019152,  13.24537985],
                              [  6.19397893,   7.74591184,  13.24537985],
                              [  1.44319358,   9.39163216,  13.24537985],
                              [ -3.30759178,  11.03735249,  13.24537985],
                              [  9.5014757 ,   0.08672946,  13.75961177],
                              [  4.75069034,   1.73244978,  13.75961177],
                              [ -0.00009502,   3.37817011,  13.75961177],
                              [  8.55131863,   5.02389043,  13.75961177],
                              [  3.80053327,   6.66961075,  13.75961177],
                              [ -0.95025209,   8.31533107,  13.75961177],
                              [ -5.70103744,   9.9610514 ,  13.75961177],
                              [ 10.78285752,   0.87272549,  14.40339491],
                              [  6.03207217,   2.51844581,  14.40339491],
                              [  1.28128681,   4.16416613,  14.40339491],
                              [  9.83270045,   5.80988645,  14.40339491],
                              [  5.0819151 ,   7.45560678,  14.40339491],
                              [  0.33112974,   9.1013271 ,  14.40339491],
                              [ -4.41965562,  10.74704742,  14.40339491],
                              [  1.71085282,   0.63722291,  15.04717805],
                              [ 10.26226646,   2.28294323,  15.04717805],
                              [  5.51148111,   3.92866355,  15.04717805],
                              [  0.76069575,   5.57438388,  15.04717805],
                              [ -3.9900896 ,   7.2201042 ,  15.04717805],
                              [  4.56132404,   8.86582452,  15.04717805],
                              [ -0.18946132,  10.51154484,  15.04717805]]*Angstrom

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
    GGABasis.Oxygen_DoubleZetaPolarized,
    ]

