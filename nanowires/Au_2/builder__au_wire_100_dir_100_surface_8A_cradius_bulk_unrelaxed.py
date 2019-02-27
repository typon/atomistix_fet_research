# Set up lattice
lattice = SimpleTetragonal(26.1262050405*Angstrom, 4.07825*Angstrom)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.65609806,  0.26585291,  0.25      ],
                          [ 0.73414709,  0.34390194,  0.25      ],
                          [ 0.73414709,  0.26585291,  0.75      ],
                          [ 0.5       ,  0.26585291,  0.25      ],
                          [ 0.57804903,  0.34390194,  0.25      ],
                          [ 0.65609806,  0.42195097,  0.25      ],
                          [ 0.73414709,  0.5       ,  0.25      ],
                          [ 0.57804903,  0.26585291,  0.75      ],
                          [ 0.65609806,  0.34390194,  0.75      ],
                          [ 0.73414709,  0.42195097,  0.75      ],
                          [ 0.34390194,  0.26585291,  0.25      ],
                          [ 0.42195097,  0.34390194,  0.25      ],
                          [ 0.5       ,  0.42195097,  0.25      ],
                          [ 0.57804903,  0.5       ,  0.25      ],
                          [ 0.65609806,  0.57804903,  0.25      ],
                          [ 0.73414709,  0.65609806,  0.25      ],
                          [ 0.42195097,  0.26585291,  0.75      ],
                          [ 0.5       ,  0.34390194,  0.75      ],
                          [ 0.57804903,  0.42195097,  0.75      ],
                          [ 0.65609806,  0.5       ,  0.75      ],
                          [ 0.73414709,  0.57804903,  0.75      ],
                          [ 0.26585291,  0.34390194,  0.25      ],
                          [ 0.34390194,  0.42195097,  0.25      ],
                          [ 0.42195097,  0.5       ,  0.25      ],
                          [ 0.5       ,  0.57804903,  0.25      ],
                          [ 0.57804903,  0.65609806,  0.25      ],
                          [ 0.65609806,  0.73414709,  0.25      ],
                          [ 0.26585291,  0.26585291,  0.75      ],
                          [ 0.34390194,  0.34390194,  0.75      ],
                          [ 0.42195097,  0.42195097,  0.75      ],
                          [ 0.5       ,  0.5       ,  0.75      ],
                          [ 0.57804903,  0.57804903,  0.75      ],
                          [ 0.65609806,  0.65609806,  0.75      ],
                          [ 0.73414709,  0.73414709,  0.75      ],
                          [ 0.26585291,  0.5       ,  0.25      ],
                          [ 0.34390194,  0.57804903,  0.25      ],
                          [ 0.42195097,  0.65609806,  0.25      ],
                          [ 0.5       ,  0.73414709,  0.25      ],
                          [ 0.26585291,  0.42195097,  0.75      ],
                          [ 0.34390194,  0.5       ,  0.75      ],
                          [ 0.42195097,  0.57804903,  0.75      ],
                          [ 0.5       ,  0.65609806,  0.75      ],
                          [ 0.57804903,  0.73414709,  0.75      ],
                          [ 0.26585291,  0.65609806,  0.25      ],
                          [ 0.34390194,  0.73414709,  0.25      ],
                          [ 0.26585291,  0.57804903,  0.75      ],
                          [ 0.34390194,  0.65609806,  0.75      ],
                          [ 0.42195097,  0.73414709,  0.75      ],
                          [ 0.26585291,  0.73414709,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


