# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [21.1912086179, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.1912086179, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[  5.88644689,   5.88644689,   1.17728939],
                              [  8.67194331,   6.63281842,   1.17728939],
                              [ 11.45743996,   7.37918995,   1.17728939],
                              [ 14.2429366 ,   8.12556148,   1.17728939],
                              [  6.63281842,   8.67194331,   1.17728939],
                              [ 17.02843303,   8.87193302,   1.17728939],
                              [  9.41831485,   9.41831485,   1.17728939],
                              [ 12.20381149,  10.16468659,   1.17728939],
                              [ 14.98930813,  10.91105812,   1.17728939],
                              [  7.37918995,  11.45743996,   1.17728939],
                              [ 10.16468659,  12.20381149,   1.17728939],
                              [ 12.95018302,  12.95018302,   1.17728939],
                              [  8.12556148,  14.2429366 ,   1.17728939],
                              [ 10.91105812,  14.98930813,   1.17728939],
                              [  8.87193302,  17.02843303,   1.17728939],
                              [  9.10286124,   5.02461124,   3.5318681 ],
                              [ 11.88835767,   5.77098277,   3.5318681 ],
                              [ 14.67385431,   6.5173543 ,   3.5318681 ],
                              [  7.06373614,   7.06373614,   3.5318681 ],
                              [  9.84923278,   7.81010767,   3.5318681 ],
                              [ 12.63472921,   8.55647941,   3.5318681 ],
                              [  5.02461124,   9.10286124,   3.5318681 ],
                              [ 15.42022585,   9.30285094,   3.5318681 ],
                              [  7.81010767,   9.84923278,   3.5318681 ],
                              [ 10.59560431,  10.59560431,   3.5318681 ],
                              [ 13.38110095,  11.34197584,   3.5318681 ],
                              [  5.77098277,  11.88835767,   3.5318681 ],
                              [ 16.16659738,  12.08834737,   3.5318681 ],
                              [  8.55647941,  12.63472921,   3.5318681 ],
                              [ 11.34197584,  13.38110095,   3.5318681 ],
                              [ 14.12747248,  14.12747248,   3.5318681 ],
                              [  6.5173543 ,  14.67385431,   3.5318681 ],
                              [  9.30285094,  15.42022585,   3.5318681 ],
                              [ 12.08834737,  16.16659738,   3.5318681 ],
                              [ 12.3192756 ,   4.16277559,   5.88644681],
                              [ 10.28015049,   6.20190049,   5.88644681],
                              [ 13.06564714,   6.94827202,   5.88644681],
                              [  8.2410256 ,   8.2410256 ,   5.88644681],
                              [ 11.02652203,   8.98739713,   5.88644681],
                              [ 13.81201867,   9.73376866,   5.88644681],
                              [  6.20190049,  10.28015049,   5.88644681],
                              [  8.98739713,  11.02652203,   5.88644681],
                              [ 11.77289377,  11.77289377,   5.88644681],
                              [  4.16277559,  12.3192756 ,   5.88644681],
                              [ 14.5583902 ,  12.5192653 ,   5.88644681],
                              [  6.94827202,  13.06564714,   5.88644681],
                              [  9.73376866,  13.81201867,   5.88644681],
                              [ 12.5192653 ,  14.5583902 ,   5.88644681],
                              [ 15.30476173,  15.30476173,   5.88644681]]*Angstrom

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
vector_a = [21.1912086179, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.1912086179, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[  5.88644689,   5.88644689,   1.17728939],
                               [  8.67194331,   6.63281842,   1.17728939],
                               [ 11.45743996,   7.37918995,   1.17728939],
                               [ 14.2429366 ,   8.12556148,   1.17728939],
                               [  6.63281842,   8.67194331,   1.17728939],
                               [ 17.02843303,   8.87193302,   1.17728939],
                               [  9.41831485,   9.41831485,   1.17728939],
                               [ 12.20381149,  10.16468659,   1.17728939],
                               [ 14.98930813,  10.91105812,   1.17728939],
                               [  7.37918995,  11.45743996,   1.17728939],
                               [ 10.16468659,  12.20381149,   1.17728939],
                               [ 12.95018302,  12.95018302,   1.17728939],
                               [  8.12556148,  14.2429366 ,   1.17728939],
                               [ 10.91105812,  14.98930813,   1.17728939],
                               [  8.87193302,  17.02843303,   1.17728939],
                               [  9.10286124,   5.02461124,   3.5318681 ],
                               [ 11.88835767,   5.77098277,   3.5318681 ],
                               [ 14.67385431,   6.5173543 ,   3.5318681 ],
                               [  7.06373614,   7.06373614,   3.5318681 ],
                               [  9.84923278,   7.81010767,   3.5318681 ],
                               [ 12.63472921,   8.55647941,   3.5318681 ],
                               [  5.02461124,   9.10286124,   3.5318681 ],
                               [ 15.42022585,   9.30285094,   3.5318681 ],
                               [  7.81010767,   9.84923278,   3.5318681 ],
                               [ 10.59560431,  10.59560431,   3.5318681 ],
                               [ 13.38110095,  11.34197584,   3.5318681 ],
                               [  5.77098277,  11.88835767,   3.5318681 ],
                               [ 16.16659738,  12.08834737,   3.5318681 ],
                               [  8.55647941,  12.63472921,   3.5318681 ],
                               [ 11.34197584,  13.38110095,   3.5318681 ],
                               [ 14.12747248,  14.12747248,   3.5318681 ],
                               [  6.5173543 ,  14.67385431,   3.5318681 ],
                               [  9.30285094,  15.42022585,   3.5318681 ],
                               [ 12.08834737,  16.16659738,   3.5318681 ],
                               [ 12.3192756 ,   4.16277559,   5.88644681],
                               [ 10.28015049,   6.20190049,   5.88644681],
                               [ 13.06564714,   6.94827202,   5.88644681],
                               [  8.2410256 ,   8.2410256 ,   5.88644681],
                               [ 11.02652203,   8.98739713,   5.88644681],
                               [ 13.81201867,   9.73376866,   5.88644681],
                               [  6.20190049,  10.28015049,   5.88644681],
                               [  8.98739713,  11.02652203,   5.88644681],
                               [ 11.77289377,  11.77289377,   5.88644681],
                               [  4.16277559,  12.3192756 ,   5.88644681],
                               [ 14.5583902 ,  12.5192653 ,   5.88644681],
                               [  6.94827202,  13.06564714,   5.88644681],
                               [  9.73376866,  13.81201867,   5.88644681],
                               [ 12.5192653 ,  14.5583902 ,   5.88644681],
                               [ 15.30476173,  15.30476173,   5.88644681]]*Angstrom

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
vector_a = [21.1912086179, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.1912086179, 0.0]*Angstrom
vector_c = [0.0, 0.0, 14.1274724119]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[  5.88644689,   5.88644689,   1.17728939],
                              [  8.67194331,   6.63281842,   1.17728939],
                              [ 11.45743996,   7.37918995,   1.17728939],
                              [ 14.2429366 ,   8.12556148,   1.17728939],
                              [  6.63281842,   8.67194331,   1.17728939],
                              [ 17.02843303,   8.87193302,   1.17728939],
                              [  9.41831485,   9.41831485,   1.17728939],
                              [ 12.20381149,  10.16468659,   1.17728939],
                              [ 14.98930813,  10.91105812,   1.17728939],
                              [  7.37918995,  11.45743996,   1.17728939],
                              [ 10.16468659,  12.20381149,   1.17728939],
                              [ 12.95018302,  12.95018302,   1.17728939],
                              [  8.12556148,  14.2429366 ,   1.17728939],
                              [ 10.91105812,  14.98930813,   1.17728939],
                              [  8.87193302,  17.02843303,   1.17728939],
                              [  9.10286124,   5.02461124,   3.5318681 ],
                              [ 11.88835767,   5.77098277,   3.5318681 ],
                              [ 14.67385431,   6.5173543 ,   3.5318681 ],
                              [  7.06373614,   7.06373614,   3.5318681 ],
                              [  9.84923278,   7.81010767,   3.5318681 ],
                              [ 12.63472921,   8.55647941,   3.5318681 ],
                              [  5.02461124,   9.10286124,   3.5318681 ],
                              [ 15.42022585,   9.30285094,   3.5318681 ],
                              [  7.81010767,   9.84923278,   3.5318681 ],
                              [ 10.59560431,  10.59560431,   3.5318681 ],
                              [ 13.38110095,  11.34197584,   3.5318681 ],
                              [  5.77098277,  11.88835767,   3.5318681 ],
                              [ 16.16659738,  12.08834737,   3.5318681 ],
                              [  8.55647941,  12.63472921,   3.5318681 ],
                              [ 11.34197584,  13.38110095,   3.5318681 ],
                              [ 14.12747248,  14.12747248,   3.5318681 ],
                              [  6.5173543 ,  14.67385431,   3.5318681 ],
                              [  9.30285094,  15.42022585,   3.5318681 ],
                              [ 12.08834737,  16.16659738,   3.5318681 ],
                              [ 12.3192756 ,   4.16277559,   5.88644681],
                              [ 10.28015049,   6.20190049,   5.88644681],
                              [ 13.06564714,   6.94827202,   5.88644681],
                              [  8.2410256 ,   8.2410256 ,   5.88644681],
                              [ 11.02652203,   8.98739713,   5.88644681],
                              [ 13.81201867,   9.73376866,   5.88644681],
                              [  6.20190049,  10.28015049,   5.88644681],
                              [  8.98739713,  11.02652203,   5.88644681],
                              [ 11.77289377,  11.77289377,   5.88644681],
                              [  4.16277559,  12.3192756 ,   5.88644681],
                              [ 14.5583902 ,  12.5192653 ,   5.88644681],
                              [  6.94827202,  13.06564714,   5.88644681],
                              [  9.73376866,  13.81201867,   5.88644681],
                              [ 12.5192653 ,  14.5583902 ,   5.88644681],
                              [ 15.30476173,  15.30476173,   5.88644681],
                              [  5.88644689,   5.88644689,   8.2410256 ],
                              [  8.67194331,   6.63281842,   8.2410256 ],
                              [ 11.45743996,   7.37918995,   8.2410256 ],
                              [ 14.2429366 ,   8.12556148,   8.2410256 ],
                              [  6.63281842,   8.67194331,   8.2410256 ],
                              [ 17.02843303,   8.87193302,   8.2410256 ],
                              [  9.41831485,   9.41831485,   8.2410256 ],
                              [ 12.20381149,  10.16468659,   8.2410256 ],
                              [ 14.98930813,  10.91105812,   8.2410256 ],
                              [  7.37918995,  11.45743996,   8.2410256 ],
                              [ 10.16468659,  12.20381149,   8.2410256 ],
                              [ 12.95018302,  12.95018302,   8.2410256 ],
                              [  8.12556148,  14.2429366 ,   8.2410256 ],
                              [ 10.91105812,  14.98930813,   8.2410256 ],
                              [  8.87193302,  17.02843303,   8.2410256 ],
                              [  9.10286124,   5.02461124,  10.59560431],
                              [ 11.88835767,   5.77098277,  10.59560431],
                              [ 14.67385431,   6.5173543 ,  10.59560431],
                              [  7.06373614,   7.06373614,  10.59560431],
                              [  9.84923278,   7.81010767,  10.59560431],
                              [ 12.63472921,   8.55647941,  10.59560431],
                              [  5.02461124,   9.10286124,  10.59560431],
                              [ 15.42022585,   9.30285094,  10.59560431],
                              [  7.81010767,   9.84923278,  10.59560431],
                              [ 10.59560431,  10.59560431,  10.59560431],
                              [ 13.38110095,  11.34197584,  10.59560431],
                              [  5.77098277,  11.88835767,  10.59560431],
                              [ 16.16659738,  12.08834737,  10.59560431],
                              [  8.55647941,  12.63472921,  10.59560431],
                              [ 11.34197584,  13.38110095,  10.59560431],
                              [ 14.12747248,  14.12747248,  10.59560431],
                              [  6.5173543 ,  14.67385431,  10.59560431],
                              [  9.30285094,  15.42022585,  10.59560431],
                              [ 12.08834737,  16.16659738,  10.59560431],
                              [ 12.3192756 ,   4.16277559,  12.95018302],
                              [ 10.28015049,   6.20190049,  12.95018302],
                              [ 13.06564714,   6.94827202,  12.95018302],
                              [  8.2410256 ,   8.2410256 ,  12.95018302],
                              [ 11.02652203,   8.98739713,  12.95018302],
                              [ 13.81201867,   9.73376866,  12.95018302],
                              [  6.20190049,  10.28015049,  12.95018302],
                              [  8.98739713,  11.02652203,  12.95018302],
                              [ 11.77289377,  11.77289377,  12.95018302],
                              [  4.16277559,  12.3192756 ,  12.95018302],
                              [ 14.5583902 ,  12.5192653 ,  12.95018302],
                              [  6.94827202,  13.06564714,  12.95018302],
                              [  9.73376866,  13.81201867,  12.95018302],
                              [ 12.5192653 ,  14.5583902 ,  12.95018302],
                              [ 15.30476173,  15.30476173,  12.95018302]]*Angstrom

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
    GGABasis.Gold_DoubleZetaPolarized,
    ]


