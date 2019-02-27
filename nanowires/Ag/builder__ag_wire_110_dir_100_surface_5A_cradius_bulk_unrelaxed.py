# Set up lattice
lattice = SimpleTetragonal(21.3192955476*Angstrom, 5.77805235179*Angstrom)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.69164329,  0.63551227,  0.125     ],
                          [ 0.69164329,  0.5       ,  0.125     ],
                          [ 0.69164329,  0.36448773,  0.125     ],
                          [ 0.5       ,  0.63551227,  0.125     ],
                          [ 0.59582165,  0.70326841,  0.375     ],
                          [ 0.69164329,  0.77102454,  0.625     ],
                          [ 0.5       ,  0.5       ,  0.125     ],
                          [ 0.59582165,  0.56775614,  0.375     ],
                          [ 0.69164329,  0.63551227,  0.625     ],
                          [ 0.5       ,  0.36448773,  0.125     ],
                          [ 0.59582165,  0.43224386,  0.375     ],
                          [ 0.69164329,  0.5       ,  0.625     ],
                          [ 0.59582165,  0.29673159,  0.375     ],
                          [ 0.69164329,  0.36448773,  0.625     ],
                          [ 0.69164329,  0.22897546,  0.625     ],
                          [ 0.30835671,  0.63551227,  0.125     ],
                          [ 0.40417835,  0.70326841,  0.375     ],
                          [ 0.5       ,  0.77102454,  0.625     ],
                          [ 0.30835671,  0.5       ,  0.125     ],
                          [ 0.40417835,  0.56775614,  0.375     ],
                          [ 0.5       ,  0.63551227,  0.625     ],
                          [ 0.59582165,  0.70326841,  0.875     ],
                          [ 0.30835671,  0.36448773,  0.125     ],
                          [ 0.40417835,  0.43224386,  0.375     ],
                          [ 0.5       ,  0.5       ,  0.625     ],
                          [ 0.59582165,  0.56775614,  0.875     ],
                          [ 0.40417835,  0.29673159,  0.375     ],
                          [ 0.5       ,  0.36448773,  0.625     ],
                          [ 0.59582165,  0.43224386,  0.875     ],
                          [ 0.5       ,  0.22897546,  0.625     ],
                          [ 0.59582165,  0.29673159,  0.875     ],
                          [ 0.30835671,  0.77102454,  0.625     ],
                          [ 0.30835671,  0.63551227,  0.625     ],
                          [ 0.40417835,  0.70326841,  0.875     ],
                          [ 0.30835671,  0.5       ,  0.625     ],
                          [ 0.40417835,  0.56775614,  0.875     ],
                          [ 0.30835671,  0.36448773,  0.625     ],
                          [ 0.40417835,  0.43224386,  0.875     ],
                          [ 0.30835671,  0.22897546,  0.625     ],
                          [ 0.40417835,  0.29673159,  0.875     ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]

