# Set up lattice
vector_a = [20.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.461]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.571043  ,  0.24999983],
                          [ 0.5       ,  0.428957  ,  0.24999983],
                          [ 0.5       ,  0.4644785 ,  0.75000017],
                          [ 0.5       ,  0.5355215 ,  0.75000017],
                          [ 0.5       ,  0.62554297,  0.24999983],
                          [ 0.5       ,  0.37445703,  0.24999983]]

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

