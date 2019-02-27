# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.61496]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper]

# Define coordinates
fractional_coordinates = [[ 0.34663024,  0.39775349,  0.25      ],
                          [ 0.34663024,  0.5       ,  0.25      ],
                          [ 0.34663024,  0.60224651,  0.25      ],
                          [ 0.44887675,  0.39775349,  0.25      ],
                          [ 0.44887675,  0.5       ,  0.25      ],
                          [ 0.44887675,  0.60224651,  0.25      ],
                          [ 0.55112325,  0.39775349,  0.25      ],
                          [ 0.55112325,  0.5       ,  0.25      ],
                          [ 0.55112325,  0.60224651,  0.25      ],
                          [ 0.65336976,  0.39775349,  0.25      ],
                          [ 0.65336976,  0.5       ,  0.25      ],
                          [ 0.65336976,  0.60224651,  0.25      ],
                          [ 0.39775349,  0.44887675,  0.75      ],
                          [ 0.39775349,  0.55112325,  0.75      ],
                          [ 0.5       ,  0.44887675,  0.75      ],
                          [ 0.5       ,  0.55112325,  0.75      ],
                          [ 0.60224651,  0.44887675,  0.75      ],
                          [ 0.60224651,  0.55112325,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Copper_DoubleZetaPolarized,
    ]


