# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.43654296,  0.5       ,  0.20367252],
                          [ 0.56345704,  0.5       ,  0.20367252],
                          [ 0.43654296,  0.43654296,  0.45367252],
                          [ 0.43654296,  0.56345704,  0.45367252],
                          [ 0.56345704,  0.43654296,  0.45367252],
                          [ 0.56345704,  0.56345704,  0.45367252],
                          [ 0.5       ,  0.43654296,  0.70367252],
                          [ 0.5       ,  0.56345704,  0.70367252],
                          [ 0.5       ,  0.5       ,  0.95367252],
                          [ 0.60339565,  0.5       ,  0.04632748],
                          [ 0.43654296,  0.60339565,  0.29632748],
                          [ 0.60339565,  0.43654296,  0.61101757],
                          [ 0.60339565,  0.56345704,  0.61101757],
                          [ 0.56345704,  0.60339565,  0.29632748],
                          [ 0.5       ,  0.60339565,  0.86101757],
                          [ 0.39660435,  0.5       ,  0.04632748],
                          [ 0.39660435,  0.43654296,  0.61101757],
                          [ 0.43654296,  0.39660435,  0.29632748],
                          [ 0.39660435,  0.56345704,  0.61101757],
                          [ 0.56345704,  0.39660435,  0.29632748],
                          [ 0.5       ,  0.39660435,  0.86101757]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


