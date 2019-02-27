# Set up lattice
lattice = SimpleTetragonal(20.0*Angstrom, 4.26258*Angstrom)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.34618739,  0.66666667],
                          [ 0.5       ,  0.40771243,  0.83333333],
                          [ 0.5       ,  0.34618739,  0.33333333],
                          [ 0.5       ,  0.46923747,  0.66666667],
                          [ 0.5       ,  0.53076253,  0.83333333],
                          [ 0.5       ,  0.40771243,  0.16666667],
                          [ 0.5       ,  0.46923747,  0.33333333],
                          [ 0.5       ,  0.59228757,  0.66666667],
                          [ 0.5       ,  0.65381261,  0.83333333],
                          [ 0.5       ,  0.53076253,  0.16666667],
                          [ 0.5       ,  0.59228757,  0.33333333],
                          [ 0.5       ,  0.65381261,  0.16666667],
                          [ 0.5       ,  0.29898903,  0.79452344],
                          [ 0.5       ,  0.29898903,  0.20547656],
                          [ 0.5       ,  0.70101097,  0.70547656],
                          [ 0.5       ,  0.70101097,  0.29452344]]

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

