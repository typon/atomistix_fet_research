# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.32697451,  0.38464967,  0.25      ],
                          [ 0.32697451,  0.5       ,  0.25      ],
                          [ 0.32697451,  0.61535033,  0.25      ],
                          [ 0.44232484,  0.38464967,  0.25      ],
                          [ 0.44232484,  0.5       ,  0.25      ],
                          [ 0.44232484,  0.61535033,  0.25      ],
                          [ 0.55767516,  0.38464967,  0.25      ],
                          [ 0.55767516,  0.5       ,  0.25      ],
                          [ 0.55767516,  0.61535033,  0.25      ],
                          [ 0.67302549,  0.38464967,  0.25      ],
                          [ 0.67302549,  0.5       ,  0.25      ],
                          [ 0.67302549,  0.61535033,  0.25      ],
                          [ 0.38464967,  0.44232484,  0.75      ],
                          [ 0.38464967,  0.55767516,  0.75      ],
                          [ 0.5       ,  0.44232484,  0.75      ],
                          [ 0.5       ,  0.55767516,  0.75      ],
                          [ 0.61535033,  0.44232484,  0.75      ],
                          [ 0.61535033,  0.55767516,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

