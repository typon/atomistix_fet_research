# Set up lattice
vector_a = [32.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 6.26129]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper]

# Define coordinates
fractional_coordinates = [[ 0.42011991,  0.43850828,  0.16666643],
                          [ 0.38017987,  0.51229834,  0.16666643],
                          [ 0.5       ,  0.43850828,  0.16666643],
                          [ 0.46005996,  0.51229834,  0.16666643],
                          [ 0.42011991,  0.58608841,  0.16666643],
                          [ 0.57988009,  0.43850828,  0.16666643],
                          [ 0.53994004,  0.51229834,  0.16666643],
                          [ 0.5       ,  0.58608841,  0.16666643],
                          [ 0.61982013,  0.51229834,  0.16666643],
                          [ 0.57988009,  0.58608841,  0.16666643],
                          [ 0.38017987,  0.46310497,  0.5       ],
                          [ 0.46005996,  0.46310497,  0.5       ],
                          [ 0.42011991,  0.53689503,  0.5       ],
                          [ 0.53994004,  0.46310497,  0.5       ],
                          [ 0.5       ,  0.53689503,  0.5       ],
                          [ 0.61982013,  0.46310497,  0.5       ],
                          [ 0.57988009,  0.53689503,  0.5       ],
                          [ 0.38017987,  0.41391159,  0.83333357],
                          [ 0.46005996,  0.41391159,  0.83333357],
                          [ 0.42011991,  0.48770166,  0.83333357],
                          [ 0.38017987,  0.56149172,  0.83333357],
                          [ 0.53994004,  0.41391159,  0.83333357],
                          [ 0.5       ,  0.48770166,  0.83333357],
                          [ 0.46005996,  0.56149172,  0.83333357],
                          [ 0.61982013,  0.41391159,  0.83333357],
                          [ 0.57988009,  0.48770166,  0.83333357],
                          [ 0.53994004,  0.56149172,  0.83333357],
                          [ 0.61982013,  0.56149172,  0.83333357]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

