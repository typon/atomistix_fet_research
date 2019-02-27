# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.9236]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Platinum, Platinum, Platinum, Platinum, Platinum, Platinum,
            Platinum, Platinum, Platinum]

# Define coordinates
fractional_coordinates = [[ 0.5     ,  0.450955,  0.25    ],
                          [ 0.549045,  0.5     ,  0.25    ],
                          [ 0.549045,  0.450955,  0.75    ],
                          [ 0.450955,  0.5     ,  0.25    ],
                          [ 0.5     ,  0.549045,  0.25    ],
                          [ 0.450955,  0.450955,  0.75    ],
                          [ 0.5     ,  0.5     ,  0.75    ],
                          [ 0.549045,  0.549045,  0.75    ],
                          [ 0.450955,  0.549045,  0.75    ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Platinum_DoubleZetaPolarized,
    ]

