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
            Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.41771398,  0.36285664,  0.125     ],
                          [ 0.41771398,  0.47257133,  0.125     ],
                          [ 0.41771398,  0.58228602,  0.125     ],
                          [ 0.52742867,  0.36285664,  0.125     ],
                          [ 0.52742867,  0.47257133,  0.125     ],
                          [ 0.52742867,  0.58228602,  0.125     ],
                          [ 0.63714336,  0.36285664,  0.125     ],
                          [ 0.63714336,  0.47257133,  0.125     ],
                          [ 0.63714336,  0.58228602,  0.125     ],
                          [ 0.41771398,  0.41771398,  0.375     ],
                          [ 0.41771398,  0.52742867,  0.375     ],
                          [ 0.41771398,  0.63714336,  0.375     ],
                          [ 0.52742867,  0.41771398,  0.375     ],
                          [ 0.52742867,  0.52742867,  0.375     ],
                          [ 0.52742867,  0.63714336,  0.375     ],
                          [ 0.63714336,  0.41771398,  0.375     ],
                          [ 0.63714336,  0.52742867,  0.375     ],
                          [ 0.63714336,  0.63714336,  0.375     ],
                          [ 0.36285664,  0.41771398,  0.625     ],
                          [ 0.36285664,  0.52742867,  0.625     ],
                          [ 0.36285664,  0.63714336,  0.625     ],
                          [ 0.47257133,  0.41771398,  0.625     ],
                          [ 0.47257133,  0.52742867,  0.625     ],
                          [ 0.47257133,  0.63714336,  0.625     ],
                          [ 0.58228602,  0.41771398,  0.625     ],
                          [ 0.58228602,  0.52742867,  0.625     ],
                          [ 0.58228602,  0.63714336,  0.625     ],
                          [ 0.36285664,  0.36285664,  0.875     ],
                          [ 0.36285664,  0.47257133,  0.875     ],
                          [ 0.36285664,  0.58228602,  0.875     ],
                          [ 0.47257133,  0.36285664,  0.875     ],
                          [ 0.47257133,  0.47257133,  0.875     ],
                          [ 0.47257133,  0.58228602,  0.875     ],
                          [ 0.58228602,  0.36285664,  0.875     ],
                          [ 0.58228602,  0.47257133,  0.875     ],
                          [ 0.58228602,  0.58228602,  0.875     ],
                          [ 0.41771398,  0.32833051,  0.28234504],
                          [ 0.52742867,  0.32833051,  0.28234504],
                          [ 0.63714336,  0.32833051,  0.28234504],
                          [ 0.67166949,  0.36285664, -0.03234504],
                          [ 0.67166949,  0.47257133, -0.03234504],
                          [ 0.67166949,  0.58228602, -0.03234504],
                          [ 0.41771398,  0.67166949,  0.21765496],
                          [ 0.52742867,  0.67166949,  0.21765496],
                          [ 0.67166949,  0.41771398,  0.53234504],
                          [ 0.67166949,  0.52742867,  0.53234504],
                          [ 0.63714336,  0.67166949,  0.21765496],
                          [ 0.67166949,  0.63714336,  0.53234504],
                          [ 0.32833051,  0.41771398,  0.46765496],
                          [ 0.32833051,  0.52742867,  0.46765496],
                          [ 0.32833051,  0.63714336,  0.46765496],
                          [ 0.36285664,  0.67166949,  0.78234504],
                          [ 0.47257133,  0.67166949,  0.78234504],
                          [ 0.58228602,  0.67166949,  0.78234504],
                          [ 0.32833051,  0.36285664,  1.03234504],
                          [ 0.36285664,  0.32833051,  0.71765496],
                          [ 0.32833051,  0.47257133,  1.03234504],
                          [ 0.32833051,  0.58228602,  1.03234504],
                          [ 0.47257133,  0.32833051,  0.71765496],
                          [ 0.58228602,  0.32833051,  0.71765496]]

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


