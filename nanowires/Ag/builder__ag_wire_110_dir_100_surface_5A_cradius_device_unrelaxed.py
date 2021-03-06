# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [21.3192955476, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.3192955476, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88902617589]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver]

# Define coordinates
left_electrode_coordinates = [[  6.57394777,   7.7706216 ,   0.72225654],
                              [ 10.65964777,   7.7706216 ,   0.72225654],
                              [ 14.74534777,   7.7706216 ,   0.72225654],
                              [  6.57394777,  10.65964777,   0.72225654],
                              [ 10.65964777,  10.65964777,   0.72225654],
                              [ 14.74534777,  10.65964777,   0.72225654],
                              [  6.57394777,  13.54867395,   0.72225654],
                              [ 10.65964777,  13.54867395,   0.72225654],
                              [ 14.74534777,  13.54867395,   0.72225654],
                              [  8.61679777,   6.32610851,   2.16676963],
                              [ 12.70249777,   6.32610851,   2.16676963],
                              [  8.61679777,   9.21513469,   2.16676963],
                              [ 12.70249777,   9.21513469,   2.16676963],
                              [  8.61679777,  12.10416086,   2.16676963],
                              [ 12.70249777,  12.10416086,   2.16676963],
                              [  8.61679777,  14.99318704,   2.16676963],
                              [ 12.70249777,  14.99318704,   2.16676963]]*Angstrom

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
vector_a = [21.3192955476, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.3192955476, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88902617589]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                            Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
right_electrode_coordinates = [[  6.57394777,   4.88159542,   0.72225654],
                               [ 10.65964777,   4.88159542,   0.72225654],
                               [ 14.74534777,   4.88159542,   0.72225654],
                               [  6.57394777,   7.7706216 ,   0.72225654],
                               [ 10.65964777,   7.7706216 ,   0.72225654],
                               [ 14.74534777,   7.7706216 ,   0.72225654],
                               [  6.57394777,  10.65964777,   0.72225654],
                               [ 10.65964777,  10.65964777,   0.72225654],
                               [ 14.74534777,  10.65964777,   0.72225654],
                               [  6.57394777,  13.54867395,   0.72225654],
                               [ 10.65964777,  13.54867395,   0.72225654],
                               [ 14.74534777,  13.54867395,   0.72225654],
                               [  6.57394777,  16.43770013,   0.72225654],
                               [ 10.65964777,  16.43770013,   0.72225654],
                               [ 14.74534777,  16.43770013,   0.72225654],
                               [  8.61679777,   6.32610851,   2.16676963],
                               [ 12.70249777,   6.32610851,   2.16676963],
                               [  8.61679777,   9.21513469,   2.16676963],
                               [ 12.70249777,   9.21513469,   2.16676963],
                               [  8.61679777,  12.10416086,   2.16676963],
                               [ 12.70249777,  12.10416086,   2.16676963],
                               [  8.61679777,  14.99318704,   2.16676963],
                               [ 12.70249777,  14.99318704,   2.16676963]]*Angstrom

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
vector_a = [21.3192955476, 0.0, 0.0]*Angstrom
vector_b = [0.0, 21.3192955476, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5561047036]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
                           Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
central_region_coordinates = [[  6.57394777,   7.7706216 ,   0.72225654],
                              [ 10.65964777,   7.7706216 ,   0.72225654],
                              [ 14.74534777,   7.7706216 ,   0.72225654],
                              [  6.57394777,  10.65964777,   0.72225654],
                              [ 10.65964777,  10.65964777,   0.72225654],
                              [ 14.74534777,  10.65964777,   0.72225654],
                              [  6.57394777,  13.54867395,   0.72225654],
                              [ 10.65964777,  13.54867395,   0.72225654],
                              [ 14.74534777,  13.54867395,   0.72225654],
                              [  8.61679777,   6.32610851,   2.16676963],
                              [ 12.70249777,   6.32610851,   2.16676963],
                              [  8.61679777,   9.21513469,   2.16676963],
                              [ 12.70249777,   9.21513469,   2.16676963],
                              [  8.61679777,  12.10416086,   2.16676963],
                              [ 12.70249777,  12.10416086,   2.16676963],
                              [  8.61679777,  14.99318704,   2.16676963],
                              [ 12.70249777,  14.99318704,   2.16676963],
                              [  6.57394777,   4.88159542,   3.61128272],
                              [ 10.65964777,   4.88159542,   3.61128272],
                              [ 14.74534777,   4.88159542,   3.61128272],
                              [  6.57394777,   7.7706216 ,   3.61128272],
                              [ 10.65964777,   7.7706216 ,   3.61128272],
                              [ 14.74534777,   7.7706216 ,   3.61128272],
                              [  6.57394777,  10.65964777,   3.61128272],
                              [ 10.65964777,  10.65964777,   3.61128272],
                              [ 14.74534777,  10.65964777,   3.61128272],
                              [  6.57394777,  13.54867395,   3.61128272],
                              [ 10.65964777,  13.54867395,   3.61128272],
                              [ 14.74534777,  13.54867395,   3.61128272],
                              [  6.57394777,  16.43770013,   3.61128272],
                              [ 10.65964777,  16.43770013,   3.61128272],
                              [ 14.74534777,  16.43770013,   3.61128272],
                              [  8.61679777,   6.32610851,   5.05579581],
                              [ 12.70249777,   6.32610851,   5.05579581],
                              [  8.61679777,   9.21513469,   5.05579581],
                              [ 12.70249777,   9.21513469,   5.05579581],
                              [  8.61679777,  12.10416086,   5.05579581],
                              [ 12.70249777,  12.10416086,   5.05579581],
                              [  8.61679777,  14.99318704,   5.05579581],
                              [ 12.70249777,  14.99318704,   5.05579581],
                              [  6.57394777,   7.7706216 ,   6.5003089 ],
                              [ 10.65964777,   7.7706216 ,   6.5003089 ],
                              [ 14.74534777,   7.7706216 ,   6.5003089 ],
                              [  6.57394777,  10.65964777,   6.5003089 ],
                              [ 10.65964777,  10.65964777,   6.5003089 ],
                              [ 14.74534777,  10.65964777,   6.5003089 ],
                              [  6.57394777,  13.54867395,   6.5003089 ],
                              [ 10.65964777,  13.54867395,   6.5003089 ],
                              [ 14.74534777,  13.54867395,   6.5003089 ],
                              [  8.61679777,   6.32610851,   7.94482198],
                              [ 12.70249777,   6.32610851,   7.94482198],
                              [  8.61679777,   9.21513469,   7.94482198],
                              [ 12.70249777,   9.21513469,   7.94482198],
                              [  8.61679777,  12.10416086,   7.94482198],
                              [ 12.70249777,  12.10416086,   7.94482198],
                              [  8.61679777,  14.99318704,   7.94482198],
                              [ 12.70249777,  14.99318704,   7.94482198],
                              [  6.57394777,   4.88159542,   9.38933507],
                              [ 10.65964777,   4.88159542,   9.38933507],
                              [ 14.74534777,   4.88159542,   9.38933507],
                              [  6.57394777,   7.7706216 ,   9.38933507],
                              [ 10.65964777,   7.7706216 ,   9.38933507],
                              [ 14.74534777,   7.7706216 ,   9.38933507],
                              [  6.57394777,  10.65964777,   9.38933507],
                              [ 10.65964777,  10.65964777,   9.38933507],
                              [ 14.74534777,  10.65964777,   9.38933507],
                              [  6.57394777,  13.54867395,   9.38933507],
                              [ 10.65964777,  13.54867395,   9.38933507],
                              [ 14.74534777,  13.54867395,   9.38933507],
                              [  6.57394777,  16.43770013,   9.38933507],
                              [ 10.65964777,  16.43770013,   9.38933507],
                              [ 14.74534777,  16.43770013,   9.38933507],
                              [  8.61679777,   6.32610851,  10.83384816],
                              [ 12.70249777,   6.32610851,  10.83384816],
                              [  8.61679777,   9.21513469,  10.83384816],
                              [ 12.70249777,   9.21513469,  10.83384816],
                              [  8.61679777,  12.10416086,  10.83384816],
                              [ 12.70249777,  12.10416086,  10.83384816],
                              [  8.61679777,  14.99318704,  10.83384816],
                              [ 12.70249777,  14.99318704,  10.83384816]]*Angstrom

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

