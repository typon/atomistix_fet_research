# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 34.15462, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.46100171044]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.14639308,  0.        ],
                          [ 0.5       ,  0.16719349,  0.5       ],
                          [ 0.5       ,  0.2087943 ,  0.5       ],
                          [ 0.5       ,  0.22959471,  0.        ],
                          [ 0.5       ,  0.27119552,  0.        ],
                          [ 0.5       ,  0.29199593,  0.5       ],
                          [ 0.5       ,  0.33359674,  0.5       ],
                          [ 0.5       ,  0.35439715,  0.        ],
                          [ 0.5       ,  0.39599796,  0.        ],
                          [ 0.5       ,  0.41679837,  0.5       ],
                          [ 0.5       ,  0.45839919,  0.5       ],
                          [ 0.5       ,  0.47919959,  0.        ],
                          [ 0.5       ,  0.52080041,  0.        ],
                          [ 0.5       ,  0.54160081,  0.5       ],
                          [ 0.5       ,  0.58320163,  0.5       ],
                          [ 0.5       ,  0.60400204,  0.        ],
                          [ 0.5       ,  0.64560285,  0.        ],
                          [ 0.5       ,  0.66640326,  0.5       ],
                          [ 0.5       ,  0.70800407,  0.5       ],
                          [ 0.5       ,  0.72880448,  0.        ],
                          [ 0.5       ,  0.77040529,  0.        ],
                          [ 0.5       ,  0.7912057 ,  0.5       ],
                          [ 0.5       ,  0.1144794 ,  0.        ],
                          [ 0.5       ,  0.82311938,  0.5       ]]

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

