# Set up lattice
vector_a = [0.0, 4.07825, 4.07825]*Angstrom
vector_b = [4.07825, 0.0, 4.07825]*Angstrom
vector_c = [4.07825, 4.07825, 0.0]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0. ,  0. ,  0. ],
                          [ 0. ,  0. ,  0.5],
                          [ 0. ,  0.5,  0. ],
                          [ 0. ,  0.5,  0.5],
                          [ 0.5,  0. ,  0. ],
                          [ 0.5,  0. ,  0.5],
                          [ 0.5,  0.5,  0. ],
                          [ 0.5,  0.5,  0.5]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

