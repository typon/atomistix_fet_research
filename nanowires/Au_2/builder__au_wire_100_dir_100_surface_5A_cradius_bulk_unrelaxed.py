# Set up lattice
lattice = SimpleTetragonal(17.5499375418*Angstrom, 4.07825*Angstrom)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.73237974,  0.26762026,  0.25      ],
                          [ 0.5       ,  0.26762026,  0.25      ],
                          [ 0.61618987,  0.38381013,  0.25      ],
                          [ 0.73237974,  0.5       ,  0.25      ],
                          [ 0.61618987,  0.26762026,  0.75      ],
                          [ 0.73237974,  0.38381013,  0.75      ],
                          [ 0.26762026,  0.26762026,  0.25      ],
                          [ 0.38381013,  0.38381013,  0.25      ],
                          [ 0.5       ,  0.5       ,  0.25      ],
                          [ 0.61618987,  0.61618987,  0.25      ],
                          [ 0.73237974,  0.73237974,  0.25      ],
                          [ 0.38381013,  0.26762026,  0.75      ],
                          [ 0.5       ,  0.38381013,  0.75      ],
                          [ 0.61618987,  0.5       ,  0.75      ],
                          [ 0.73237974,  0.61618987,  0.75      ],
                          [ 0.26762026,  0.5       ,  0.25      ],
                          [ 0.38381013,  0.61618987,  0.25      ],
                          [ 0.5       ,  0.73237974,  0.25      ],
                          [ 0.26762026,  0.38381013,  0.75      ],
                          [ 0.38381013,  0.5       ,  0.75      ],
                          [ 0.5       ,  0.61618987,  0.75      ],
                          [ 0.61618987,  0.73237974,  0.75      ],
                          [ 0.26762026,  0.73237974,  0.25      ],
                          [ 0.26762026,  0.61618987,  0.75      ],
                          [ 0.38381013,  0.73237974,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


