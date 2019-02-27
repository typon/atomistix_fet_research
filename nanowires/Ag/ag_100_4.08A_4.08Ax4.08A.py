# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.44892875,  0.25      ],
                          [ 0.55107125,  0.5       ,  0.25      ],
                          [ 0.55107125,  0.44892875,  0.75      ],
                          [ 0.44892875,  0.5       ,  0.25      ],
                          [ 0.5       ,  0.55107125,  0.25      ],
                          [ 0.44892875,  0.44892875,  0.75      ],
                          [ 0.5       ,  0.5       ,  0.75      ],
                          [ 0.55107125,  0.55107125,  0.75      ],
                          [ 0.44892875,  0.55107125,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]


