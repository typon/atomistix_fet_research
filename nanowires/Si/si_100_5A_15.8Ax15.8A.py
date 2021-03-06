# Set up lattice
vector_a = [35.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.36285664,  0.3079993 ,  0.125     ],
                          [ 0.36285664,  0.41771398,  0.125     ],
                          [ 0.36285664,  0.52742867,  0.125     ],
                          [ 0.36285664,  0.63714336,  0.125     ],
                          [ 0.47257133,  0.3079993 ,  0.125     ],
                          [ 0.47257133,  0.41771398,  0.125     ],
                          [ 0.47257133,  0.52742867,  0.125     ],
                          [ 0.47257133,  0.63714336,  0.125     ],
                          [ 0.58228602,  0.3079993 ,  0.125     ],
                          [ 0.58228602,  0.41771398,  0.125     ],
                          [ 0.58228602,  0.52742867,  0.125     ],
                          [ 0.58228602,  0.63714336,  0.125     ],
                          [ 0.6920007 ,  0.3079993 ,  0.125     ],
                          [ 0.6920007 ,  0.41771398,  0.125     ],
                          [ 0.6920007 ,  0.52742867,  0.125     ],
                          [ 0.6920007 ,  0.63714336,  0.125     ],
                          [ 0.36285664,  0.36285664,  0.375     ],
                          [ 0.36285664,  0.47257133,  0.375     ],
                          [ 0.36285664,  0.58228602,  0.375     ],
                          [ 0.36285664,  0.6920007 ,  0.375     ],
                          [ 0.47257133,  0.36285664,  0.375     ],
                          [ 0.47257133,  0.47257133,  0.375     ],
                          [ 0.47257133,  0.58228602,  0.375     ],
                          [ 0.47257133,  0.6920007 ,  0.375     ],
                          [ 0.58228602,  0.36285664,  0.375     ],
                          [ 0.58228602,  0.47257133,  0.375     ],
                          [ 0.58228602,  0.58228602,  0.375     ],
                          [ 0.58228602,  0.6920007 ,  0.375     ],
                          [ 0.6920007 ,  0.36285664,  0.375     ],
                          [ 0.6920007 ,  0.47257133,  0.375     ],
                          [ 0.6920007 ,  0.58228602,  0.375     ],
                          [ 0.6920007 ,  0.6920007 ,  0.375     ],
                          [ 0.3079993 ,  0.36285664,  0.625     ],
                          [ 0.3079993 ,  0.47257133,  0.625     ],
                          [ 0.3079993 ,  0.58228602,  0.625     ],
                          [ 0.3079993 ,  0.6920007 ,  0.625     ],
                          [ 0.41771398,  0.36285664,  0.625     ],
                          [ 0.41771398,  0.47257133,  0.625     ],
                          [ 0.41771398,  0.58228602,  0.625     ],
                          [ 0.41771398,  0.6920007 ,  0.625     ],
                          [ 0.52742867,  0.36285664,  0.625     ],
                          [ 0.52742867,  0.47257133,  0.625     ],
                          [ 0.52742867,  0.58228602,  0.625     ],
                          [ 0.52742867,  0.6920007 ,  0.625     ],
                          [ 0.63714336,  0.36285664,  0.625     ],
                          [ 0.63714336,  0.47257133,  0.625     ],
                          [ 0.63714336,  0.58228602,  0.625     ],
                          [ 0.63714336,  0.6920007 ,  0.625     ],
                          [ 0.3079993 ,  0.3079993 ,  0.875     ],
                          [ 0.3079993 ,  0.41771398,  0.875     ],
                          [ 0.3079993 ,  0.52742867,  0.875     ],
                          [ 0.3079993 ,  0.63714336,  0.875     ],
                          [ 0.41771398,  0.3079993 ,  0.875     ],
                          [ 0.41771398,  0.41771398,  0.875     ],
                          [ 0.41771398,  0.52742867,  0.875     ],
                          [ 0.41771398,  0.63714336,  0.875     ],
                          [ 0.52742867,  0.3079993 ,  0.875     ],
                          [ 0.52742867,  0.41771398,  0.875     ],
                          [ 0.52742867,  0.52742867,  0.875     ],
                          [ 0.52742867,  0.63714336,  0.875     ],
                          [ 0.63714336,  0.3079993 ,  0.875     ],
                          [ 0.63714336,  0.41771398,  0.875     ],
                          [ 0.63714336,  0.52742867,  0.875     ],
                          [ 0.63714336,  0.63714336,  0.875     ],
                          [ 0.36285664,  0.27347317,  0.28234504],
                          [ 0.47257133,  0.27347317,  0.28234504],
                          [ 0.58228602,  0.27347317,  0.28234504],
                          [ 0.6920007 ,  0.27347317,  0.28234504],
                          [ 0.72652683,  0.3079993 , -0.03234504],
                          [ 0.72652683,  0.41771398, -0.03234504],
                          [ 0.72652683,  0.52742867, -0.03234504],
                          [ 0.72652683,  0.63714336, -0.03234504],
                          [ 0.36285664,  0.72652683,  0.21765496],
                          [ 0.47257133,  0.72652683,  0.21765496],
                          [ 0.58228602,  0.72652683,  0.21765496],
                          [ 0.72652683,  0.36285664,  0.53234504],
                          [ 0.72652683,  0.47257133,  0.53234504],
                          [ 0.72652683,  0.58228602,  0.53234504],
                          [ 0.6920007 ,  0.72652683,  0.21765496],
                          [ 0.72652683,  0.6920007 ,  0.53234504],
                          [ 0.27347317,  0.36285664,  0.46765496],
                          [ 0.27347317,  0.47257133,  0.46765496],
                          [ 0.27347317,  0.58228602,  0.46765496],
                          [ 0.27347317,  0.6920007 ,  0.46765496],
                          [ 0.3079993 ,  0.72652683,  0.78234504],
                          [ 0.41771398,  0.72652683,  0.78234504],
                          [ 0.52742867,  0.72652683,  0.78234504],
                          [ 0.63714336,  0.72652683,  0.78234504],
                          [ 0.27347317,  0.3079993 ,  1.03234504],
                          [ 0.3079993 ,  0.27347317,  0.71765496],
                          [ 0.27347317,  0.41771398,  1.03234504],
                          [ 0.27347317,  0.52742867,  1.03234504],
                          [ 0.27347317,  0.63714336,  1.03234504],
                          [ 0.41771398,  0.27347317,  0.71765496],
                          [ 0.52742867,  0.27347317,  0.71765496],
                          [ 0.63714336,  0.27347317,  0.71765496]]

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


