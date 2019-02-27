# Set up lattice
lattice = SimpleTetragonal(18.4247277601*Angstrom, 2.8848*Angstrom)

# Define elements
elements = [Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
            Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
            Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
            Chromium, Chromium, Chromium, Chromium, Chromium, Chromium,
            Chromium]

# Define coordinates
fractional_coordinates = [[ 0.26514171,  0.26514171,  0.25      ],
                          [ 0.4217139 ,  0.26514171,  0.25      ],
                          [ 0.5782861 ,  0.26514171,  0.25      ],
                          [ 0.73485829,  0.26514171,  0.25      ],
                          [ 0.26514171,  0.4217139 ,  0.25      ],
                          [ 0.34342781,  0.34342781,  0.75      ],
                          [ 0.4217139 ,  0.4217139 ,  0.25      ],
                          [ 0.5       ,  0.34342781,  0.75      ],
                          [ 0.5782861 ,  0.4217139 ,  0.25      ],
                          [ 0.65657219,  0.34342781,  0.75      ],
                          [ 0.73485829,  0.4217139 ,  0.25      ],
                          [ 0.26514171,  0.5782861 ,  0.25      ],
                          [ 0.34342781,  0.5       ,  0.75      ],
                          [ 0.4217139 ,  0.5782861 ,  0.25      ],
                          [ 0.5       ,  0.5       ,  0.75      ],
                          [ 0.5782861 ,  0.5782861 ,  0.25      ],
                          [ 0.65657219,  0.5       ,  0.75      ],
                          [ 0.73485829,  0.5782861 ,  0.25      ],
                          [ 0.26514171,  0.73485829,  0.25      ],
                          [ 0.34342781,  0.65657219,  0.75      ],
                          [ 0.4217139 ,  0.73485829,  0.25      ],
                          [ 0.5       ,  0.65657219,  0.75      ],
                          [ 0.5782861 ,  0.73485829,  0.25      ],
                          [ 0.65657219,  0.65657219,  0.75      ],
                          [ 0.73485829,  0.73485829,  0.25      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Chromium_DoubleZetaPolarized,
    ]


