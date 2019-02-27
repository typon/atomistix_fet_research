# Set up lattice
lattice = SimpleTetragonal(9.08500614447*Angstrom, 4.0857*Angstrom)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.27514049,  0.25      ],
                          [ 0.72485951,  0.5       ,  0.25      ],
                          [ 0.72485951,  0.27514049,  0.75      ],
                          [ 0.27514049,  0.5       ,  0.25      ],
                          [ 0.5       ,  0.72485951,  0.25      ],
                          [ 0.27514049,  0.27514049,  0.75      ],
                          [ 0.5       ,  0.5       ,  0.75      ],
                          [ 0.72485951,  0.72485951,  0.75      ],
                          [ 0.27514049,  0.72485951,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]


