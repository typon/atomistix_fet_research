# Set up lattice
lattice = SimpleTetragonal(14.7002*Angstrom, 4.26258*Angstrom)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.65986745,  0.5       ,  0.66666667],
                          [ 0.63844928,  0.57993373,  0.83333333],
                          [ 0.65986745,  0.5       ,  0.33333333],
                          [ 0.57993373,  0.63844928,  0.66666667],
                          [ 0.5       ,  0.65986745,  0.83333333],
                          [ 0.63844928,  0.57993373,  0.16666667],
                          [ 0.57993373,  0.63844928,  0.33333333],
                          [ 0.42006627,  0.63844928,  0.66666667],
                          [ 0.36155072,  0.57993373,  0.83333333],
                          [ 0.5       ,  0.65986745,  0.16666667],
                          [ 0.42006627,  0.63844928,  0.33333333],
                          [ 0.34013255,  0.5       ,  0.66666667],
                          [ 0.36155072,  0.42006627,  0.83333333],
                          [ 0.36155072,  0.57993373,  0.16666667],
                          [ 0.34013255,  0.5       ,  0.33333333],
                          [ 0.42006627,  0.36155072,  0.66666667],
                          [ 0.5       ,  0.34013255,  0.83333333],
                          [ 0.36155072,  0.42006627,  0.16666667],
                          [ 0.42006627,  0.36155072,  0.33333333],
                          [ 0.57993373,  0.36155072,  0.66666667],
                          [ 0.63844928,  0.42006627,  0.83333333],
                          [ 0.5       ,  0.34013255,  0.16666667],
                          [ 0.57993373,  0.36155072,  0.33333333],
                          [ 0.63844928,  0.42006627,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


