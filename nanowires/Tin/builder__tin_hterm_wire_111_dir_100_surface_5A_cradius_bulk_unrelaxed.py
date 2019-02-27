# Set up lattice
lattice = SimpleTetragonal(17.3783090094*Angstrom, 11.2396241005*Angstrom)

# Define elements
elements = [Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin,
            Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin,
            Tin, Tin, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.64724881,  0.4605448 ,  0.04166667],
                          [ 0.64724881,  0.4605448 ,  0.29166667],
                          [ 0.75504242,  0.56833841,  0.375     ],
                          [ 0.75504242,  0.56833841,  0.625     ],
                          [ 0.68670401,  0.31329599,  0.375     ],
                          [ 0.68670401,  0.31329599,  0.625     ],
                          [ 0.4605448 ,  0.64724881,  0.04166667],
                          [ 0.4605448 ,  0.64724881,  0.29166667],
                          [ 0.56833841,  0.75504242,  0.375     ],
                          [ 0.56833841,  0.75504242,  0.625     ],
                          [ 0.39220639,  0.39220639,  0.04166667],
                          [ 0.39220639,  0.39220639,  0.29166667],
                          [ 0.5       ,  0.5       ,  0.375     ],
                          [ 0.5       ,  0.5       ,  0.625     ],
                          [ 0.60779361,  0.60779361,  0.70833333],
                          [ 0.60779361,  0.60779361,  0.95833333],
                          [ 0.43166159,  0.24495758,  0.375     ],
                          [ 0.43166159,  0.24495758,  0.625     ],
                          [ 0.5394552 ,  0.35275119,  0.70833333],
                          [ 0.5394552 ,  0.35275119,  0.95833333],
                          [ 0.31329599,  0.68670401,  0.375     ],
                          [ 0.31329599,  0.68670401,  0.625     ],
                          [ 0.24495758,  0.43166159,  0.375     ],
                          [ 0.24495758,  0.43166159,  0.625     ],
                          [ 0.35275119,  0.5394552 ,  0.70833333],
                          [ 0.35275119,  0.5394552 ,  0.95833333],
                          [ 0.73633466,  0.43667432, -0.00875018],
                          [ 0.84412827,  0.54446793,  0.32458315],
                          [ 0.73117194,  0.65742426,  0.32458315],
                          [ 0.82025779,  0.63355378,  0.67541685],
                          [ 0.7789129 ,  0.47925256,  0.67541685],
                          [ 0.62148864,  0.24808062,  0.32458315],
                          [ 0.77578986,  0.28942551,  0.32458315],
                          [ 0.75191938,  0.37851136,  0.67541685],
                          [ 0.71057449,  0.22421014,  0.67541685],
                          [ 0.43667432,  0.73633466, -0.00875018],
                          [ 0.65742426,  0.73117194,  0.32458315],
                          [ 0.54446793,  0.84412827,  0.32458315],
                          [ 0.47925256,  0.7789129 ,  0.67541685],
                          [ 0.63355378,  0.82025779,  0.67541685],
                          [ 0.32699102,  0.32699102, -0.00875018],
                          [ 0.67300898,  0.67300898,  1.00875018],
                          [ 0.52074744,  0.2210871 ,  0.32458315],
                          [ 0.36644622,  0.17974221,  0.32458315],
                          [ 0.34257574,  0.26882806,  0.67541685],
                          [ 0.45553207,  0.15587173,  0.67541685],
                          [ 0.56332568,  0.26366534,  1.00875018],
                          [ 0.24808062,  0.62148864,  0.32458315],
                          [ 0.28942551,  0.77578986,  0.32458315],
                          [ 0.37851136,  0.75191938,  0.67541685],
                          [ 0.22421014,  0.71057449,  0.67541685],
                          [ 0.17974221,  0.36644622,  0.32458315],
                          [ 0.2210871 ,  0.52074744,  0.32458315],
                          [ 0.15587173,  0.45553207,  0.67541685],
                          [ 0.26882806,  0.34257574,  0.67541685],
                          [ 0.26366534,  0.56332568,  1.00875018]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Tin_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]

