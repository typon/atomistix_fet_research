# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 6.4892]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.42352404,  0.04937473],
                          [ 0.5       ,  0.57647596,  0.04937473],
                          [ 0.5       ,  0.5       ,  0.29937473],
                          [ 0.42352404,  0.5       ,  0.54937473],
                          [ 0.57647596,  0.5       ,  0.54937473],
                          [ 0.42352404,  0.42352404,  0.79937473],
                          [ 0.42352404,  0.57647596,  0.79937473],
                          [ 0.57647596,  0.42352404,  0.79937473],
                          [ 0.57647596,  0.57647596,  0.79937473],
                          [ 0.5       ,  0.37725593,  0.20062527],
                          [ 0.5       ,  0.62274407,  0.20062527],
                          [ 0.37725593,  0.5       ,  0.39812419],
                          [ 0.62274407,  0.5       ,  0.39812419],
                          [ 0.37725593,  0.42352404,  0.95062527],
                          [ 0.42352404,  0.37725593,  0.64812419],
                          [ 0.42352404,  0.62274407,  0.64812419],
                          [ 0.37725593,  0.57647596,  0.95062527],
                          [ 0.62274407,  0.42352404,  0.95062527],
                          [ 0.57647596,  0.37725593,  0.64812419],
                          [ 0.57647596,  0.62274407,  0.64812419],
                          [ 0.62274407,  0.57647596,  0.95062527]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Tin_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


