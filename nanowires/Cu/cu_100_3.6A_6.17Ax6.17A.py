# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.61496]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper]

# Define coordinates
fractional_coordinates = [[ 0.545187,  0.454813,  0.25    ],
                          [ 0.454813,  0.454813,  0.25    ],
                          [ 0.5     ,  0.5     ,  0.25    ],
                          [ 0.545187,  0.545187,  0.25    ],
                          [ 0.5     ,  0.454813,  0.75    ],
                          [ 0.545187,  0.5     ,  0.75    ],
                          [ 0.454813,  0.545187,  0.25    ],
                          [ 0.454813,  0.5     ,  0.75    ],
                          [ 0.5     ,  0.545187,  0.75    ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Copper_DoubleZetaPolarized,
    ]


