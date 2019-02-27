# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.46799988,  0.40399965,  0.125     ],
                          [ 0.46799988,  0.53200012,  0.125     ],
                          [ 0.59600035,  0.40399965,  0.125     ],
                          [ 0.59600035,  0.53200012,  0.125     ],
                          [ 0.46799988,  0.46799988,  0.375     ],
                          [ 0.46799988,  0.59600035,  0.375     ],
                          [ 0.59600035,  0.46799988,  0.375     ],
                          [ 0.59600035,  0.59600035,  0.375     ],
                          [ 0.40399965,  0.46799988,  0.625     ],
                          [ 0.40399965,  0.59600035,  0.625     ],
                          [ 0.53200012,  0.46799988,  0.625     ],
                          [ 0.53200012,  0.59600035,  0.625     ],
                          [ 0.40399965,  0.40399965,  0.875     ],
                          [ 0.40399965,  0.53200012,  0.875     ],
                          [ 0.53200012,  0.40399965,  0.875     ],
                          [ 0.53200012,  0.53200012,  0.875     ],
                          [ 0.46799988,  0.36371917,  0.28234504],
                          [ 0.59600035,  0.36371917,  0.28234504],
                          [ 0.63628083,  0.40399965, -0.03234504],
                          [ 0.63628083,  0.53200012, -0.03234504],
                          [ 0.46799988,  0.63628083,  0.21765496],
                          [ 0.63628083,  0.46799988,  0.53234504],
                          [ 0.63628083,  0.59600035,  0.53234504],
                          [ 0.59600035,  0.63628083,  0.21765496],
                          [ 0.36371917,  0.46799988,  0.46765496],
                          [ 0.36371917,  0.59600035,  0.46765496],
                          [ 0.40399965,  0.63628083,  0.78234504],
                          [ 0.53200012,  0.63628083,  0.78234504],
                          [ 0.36371917,  0.40399965,  1.03234504],
                          [ 0.40399965,  0.36371917,  0.71765496],
                          [ 0.36371917,  0.53200012,  1.03234504],
                          [ 0.53200012,  0.36371917,  0.71765496]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


