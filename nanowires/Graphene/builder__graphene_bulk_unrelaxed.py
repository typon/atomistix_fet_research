# Set up lattice
vector_a = [4.9224, -8.52584689518, 0.0]*Angstrom
vector_b = [4.9224, 8.52584689518, 0.0]*Angstrom
vector_c = [0.0, 0.0, 6.709]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.        ,  0.        ,  0.        ],
                          [ 0.        ,  0.5       ,  0.        ],
                          [ 0.5       ,  0.        ,  0.        ],
                          [ 0.5       ,  0.5       ,  0.        ],
                          [ 0.        ,  0.25      ,  0.        ],
                          [ 0.        ,  0.75      ,  0.        ],
                          [ 0.5       ,  0.25      ,  0.        ],
                          [ 0.5       ,  0.75      ,  0.        ],
                          [ 0.25      ,  0.        ,  0.        ],
                          [ 0.25      ,  0.5       ,  0.        ],
                          [ 0.75      ,  0.        ,  0.        ],
                          [ 0.75      ,  0.5       ,  0.        ],
                          [ 0.25      ,  0.25      ,  0.        ],
                          [ 0.25      ,  0.75      ,  0.        ],
                          [ 0.75      ,  0.25      ,  0.        ],
                          [ 0.75      ,  0.75      ,  0.        ],
                          [ 0.08333333,  0.16666667,  0.        ],
                          [ 0.08333333,  0.66666667,  0.        ],
                          [ 0.58333333,  0.16666667,  0.        ],
                          [ 0.58333333,  0.66666667,  0.        ],
                          [ 0.08333333,  0.41666667,  0.        ],
                          [ 0.08333333,  0.91666667,  0.        ],
                          [ 0.58333333,  0.41666667,  0.        ],
                          [ 0.58333333,  0.91666667,  0.        ],
                          [ 0.33333333,  0.16666667,  0.        ],
                          [ 0.33333333,  0.66666667,  0.        ],
                          [ 0.83333333,  0.16666667,  0.        ],
                          [ 0.83333333,  0.66666667,  0.        ],
                          [ 0.33333333,  0.41666667,  0.        ],
                          [ 0.33333333,  0.91666667,  0.        ],
                          [ 0.83333333,  0.41666667,  0.        ],
                          [ 0.83333333,  0.91666667,  0.        ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]

