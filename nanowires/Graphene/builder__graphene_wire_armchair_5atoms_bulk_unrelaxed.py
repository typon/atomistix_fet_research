# Set up lattice
lattice = SimpleTetragonal(16.15*Angstrom, 4.26258*Angstrom)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.34761599,  0.66666667],
                          [ 0.5       ,  0.42380799,  0.83333333],
                          [ 0.5       ,  0.34761599,  0.33333333],
                          [ 0.5       ,  0.49999999,  0.66666667],
                          [ 0.5       ,  0.57619201,  0.83333333],
                          [ 0.5       ,  0.42380799,  0.16666667],
                          [ 0.5       ,  0.49999999,  0.33333333],
                          [ 0.5       ,  0.65238401,  0.66666667],
                          [ 0.5       ,  0.57619201,  0.16666667],
                          [ 0.5       ,  0.65238401,  0.33333333],
                          [ 0.5       ,  0.28916601,  0.79452344],
                          [ 0.5       ,  0.28916601,  0.20547656],
                          [ 0.5       ,  0.71083399,  0.79452344],
                          [ 0.5       ,  0.71083399,  0.20547656]]

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

