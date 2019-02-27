# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.461]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.618405  ,  0.24999983],
                          [ 0.5       ,  0.381595  ,  0.24999983],
                          [ 0.5       ,  0.405276  ,  0.75000017],
                          [ 0.5       ,  0.452638  ,  0.75000017],
                          [ 0.5       ,  0.476319  ,  0.24999983],
                          [ 0.5       ,  0.523681  ,  0.24999983],
                          [ 0.5       ,  0.547362  ,  0.75000017],
                          [ 0.5       ,  0.594724  ,  0.75000017],
                          [ 0.5       ,  0.65473832,  0.24999983],
                          [ 0.5       ,  0.34526168,  0.24999983]]

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

