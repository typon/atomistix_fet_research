# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.89204, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.46100171044]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.83273139,  0.        ],
                          [ 0.5       ,  0.16726861,  0.        ],
                          [ 0.5       ,  0.19103514,  0.5       ],
                          [ 0.5       ,  0.23856819,  0.5       ],
                          [ 0.5       ,  0.26233472,  0.        ],
                          [ 0.5       ,  0.30986778,  0.        ],
                          [ 0.5       ,  0.33363431,  0.5       ],
                          [ 0.5       ,  0.38116736,  0.5       ],
                          [ 0.5       ,  0.40493389,  0.        ],
                          [ 0.5       ,  0.45246694,  0.        ],
                          [ 0.5       ,  0.47623347,  0.5       ],
                          [ 0.5       ,  0.52376653,  0.5       ],
                          [ 0.5       ,  0.54753306,  0.        ],
                          [ 0.5       ,  0.59506611,  0.        ],
                          [ 0.5       ,  0.61883264,  0.5       ],
                          [ 0.5       ,  0.66636569,  0.5       ],
                          [ 0.5       ,  0.69013222,  0.        ],
                          [ 0.5       ,  0.73766528,  0.        ],
                          [ 0.5       ,  0.76143181,  0.5       ],
                          [ 0.5       ,  0.80896486,  0.5       ],
                          [ 0.5       ,  0.86919593,  0.        ],
                          [ 0.5       ,  0.13080407,  0.        ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]

