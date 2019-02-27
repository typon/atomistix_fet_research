# Set up lattice
lattice = SimpleTetragonal(9.03334676493*Angstrom, 5.76751646075*Angstrom)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.72573306,  0.65961738,  0.125     ],
                          [ 0.72573306,  0.34038262,  0.125     ],
                          [ 0.27426694,  0.65961738,  0.125     ],
                          [ 0.5       ,  0.81923475,  0.375     ],
                          [ 0.27426694,  0.34038262,  0.125     ],
                          [ 0.5       ,  0.5       ,  0.375     ],
                          [ 0.72573306,  0.65961738,  0.625     ],
                          [ 0.5       ,  0.18076525,  0.375     ],
                          [ 0.72573306,  0.34038262,  0.625     ],
                          [ 0.27426694,  0.65961738,  0.625     ],
                          [ 0.27426694,  0.34038262,  0.625     ],
                          [ 0.5       ,  0.5       ,  0.875     ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


