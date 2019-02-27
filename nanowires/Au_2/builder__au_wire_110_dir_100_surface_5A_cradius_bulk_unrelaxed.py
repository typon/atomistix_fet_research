# Set up lattice
lattice = SimpleTetragonal(21.2804212417*Angstrom, 5.76751646075*Angstrom)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.59582165,  0.70326841,  0.125     ],
                          [ 0.69164329,  0.77102454,  0.375     ],
                          [ 0.59582165,  0.56775614,  0.125     ],
                          [ 0.69164329,  0.63551227,  0.375     ],
                          [ 0.59582165,  0.43224386,  0.125     ],
                          [ 0.69164329,  0.5       ,  0.375     ],
                          [ 0.59582165,  0.29673159,  0.125     ],
                          [ 0.69164329,  0.36448773,  0.375     ],
                          [ 0.69164329,  0.22897546,  0.375     ],
                          [ 0.40417835,  0.70326841,  0.125     ],
                          [ 0.5       ,  0.77102454,  0.375     ],
                          [ 0.40417835,  0.56775614,  0.125     ],
                          [ 0.5       ,  0.63551227,  0.375     ],
                          [ 0.59582165,  0.70326841,  0.625     ],
                          [ 0.40417835,  0.43224386,  0.125     ],
                          [ 0.5       ,  0.5       ,  0.375     ],
                          [ 0.59582165,  0.56775614,  0.625     ],
                          [ 0.69164329,  0.63551227,  0.875     ],
                          [ 0.40417835,  0.29673159,  0.125     ],
                          [ 0.5       ,  0.36448773,  0.375     ],
                          [ 0.59582165,  0.43224386,  0.625     ],
                          [ 0.69164329,  0.5       ,  0.875     ],
                          [ 0.5       ,  0.22897546,  0.375     ],
                          [ 0.59582165,  0.29673159,  0.625     ],
                          [ 0.69164329,  0.36448773,  0.875     ],
                          [ 0.30835671,  0.77102454,  0.375     ],
                          [ 0.30835671,  0.63551227,  0.375     ],
                          [ 0.40417835,  0.70326841,  0.625     ],
                          [ 0.30835671,  0.5       ,  0.375     ],
                          [ 0.40417835,  0.56775614,  0.625     ],
                          [ 0.5       ,  0.63551227,  0.875     ],
                          [ 0.30835671,  0.36448773,  0.375     ],
                          [ 0.40417835,  0.43224386,  0.625     ],
                          [ 0.5       ,  0.5       ,  0.875     ],
                          [ 0.30835671,  0.22897546,  0.375     ],
                          [ 0.40417835,  0.29673159,  0.625     ],
                          [ 0.5       ,  0.36448773,  0.875     ],
                          [ 0.30835671,  0.63551227,  0.875     ],
                          [ 0.30835671,  0.5       ,  0.875     ],
                          [ 0.30835671,  0.36448773,  0.875     ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


