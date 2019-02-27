# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06374]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.54020518,  0.48922705,  0.16666685],
                          [ 0.56963741,  0.51865929,  0.5       ],
                          [ 0.55097812,  0.44902188,  0.5       ],
                          [ 0.48922705,  0.54020518,  0.16666685],
                          [ 0.51865929,  0.56963741,  0.5       ],
                          [ 0.47056777,  0.47056777,  0.16666685],
                          [ 0.5       ,  0.5       ,  0.5       ],
                          [ 0.52943223,  0.52943223,  0.83333315],
                          [ 0.48134071,  0.43036259,  0.5       ],
                          [ 0.51077295,  0.45979482,  0.83333315],
                          [ 0.44902188,  0.55097812,  0.5       ],
                          [ 0.43036259,  0.48134071,  0.5       ],
                          [ 0.45979482,  0.51077295,  0.83333315]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

