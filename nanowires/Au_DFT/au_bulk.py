# Set up lattice
lattice = FaceCenteredCubic(4.07825*Angstrom)

# Define elements
elements = [Gold]

# Define coordinates
fractional_coordinates = [[ 0.,  0.,  0.]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

