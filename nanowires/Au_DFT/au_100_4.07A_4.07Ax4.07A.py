# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.55097812,  0.44902188,  0.25      ],
                          [ 0.44902188,  0.44902188,  0.25      ],
                          [ 0.5       ,  0.5       ,  0.25      ],
                          [ 0.55097812,  0.55097812,  0.25      ],
                          [ 0.5       ,  0.44902188,  0.75      ],
                          [ 0.55097812,  0.5       ,  0.75      ],
                          [ 0.44902188,  0.55097812,  0.25      ],
                          [ 0.44902188,  0.5       ,  0.75      ],
                          [ 0.5       ,  0.55097812,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

