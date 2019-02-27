# Set up lattice
vector_a = [11.53503293, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.65127468519, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.25      ,  0.33333333,  0.125     ],
                          [ 0.5       ,  0.33333333,  0.125     ],
                          [ 0.75      ,  0.33333333,  0.125     ],
                          [ 0.25      ,  0.66666667,  0.125     ],
                          [ 0.5       ,  0.66666667,  0.125     ],
                          [ 0.75      ,  0.66666667,  0.125     ],
                          [ 0.125     ,  0.16666667,  0.375     ],
                          [ 0.375     ,  0.16666667,  0.375     ],
                          [ 0.625     ,  0.16666667,  0.375     ],
                          [ 0.875     ,  0.16666667,  0.375     ],
                          [ 0.125     ,  0.5       ,  0.375     ],
                          [ 0.375     ,  0.5       ,  0.375     ],
                          [ 0.625     ,  0.5       ,  0.375     ],
                          [ 0.875     ,  0.5       ,  0.375     ],
                          [ 0.125     ,  0.83333333,  0.375     ],
                          [ 0.375     ,  0.83333333,  0.375     ],
                          [ 0.625     ,  0.83333333,  0.375     ],
                          [ 0.875     ,  0.83333333,  0.375     ],
                          [ 0.25      ,  0.33333333,  0.625     ],
                          [ 0.5       ,  0.33333333,  0.625     ],
                          [ 0.75      ,  0.33333333,  0.625     ],
                          [ 0.25      ,  0.66666667,  0.625     ],
                          [ 0.5       ,  0.66666667,  0.625     ],
                          [ 0.75      ,  0.66666667,  0.625     ],
                          [ 0.125     ,  0.16666667,  0.875     ],
                          [ 0.375     ,  0.16666667,  0.875     ],
                          [ 0.625     ,  0.16666667,  0.875     ],
                          [ 0.875     ,  0.16666667,  0.875     ],
                          [ 0.125     ,  0.5       ,  0.875     ],
                          [ 0.375     ,  0.5       ,  0.875     ],
                          [ 0.625     ,  0.5       ,  0.875     ],
                          [ 0.875     ,  0.5       ,  0.875     ],
                          [ 0.125     ,  0.83333333,  0.875     ],
                          [ 0.375     ,  0.83333333,  0.875     ],
                          [ 0.625     ,  0.83333333,  0.875     ],
                          [ 0.875     ,  0.83333333,  0.875     ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


