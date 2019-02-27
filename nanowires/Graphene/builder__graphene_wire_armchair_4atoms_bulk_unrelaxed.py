# Set up lattice
lattice = SimpleTetragonal(13.69*Angstrom, 4.26258*Angstrom)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.36517521,  0.66666667],
                          [ 0.5       ,  0.45505841,  0.83333333],
                          [ 0.5       ,  0.36517521,  0.33333333],
                          [ 0.5       ,  0.54494159,  0.66666667],
                          [ 0.5       ,  0.63482479,  0.83333333],
                          [ 0.5       ,  0.45505841,  0.16666667],
                          [ 0.5       ,  0.54494159,  0.33333333],
                          [ 0.5       ,  0.63482479,  0.16666667],
                          [ 0.5       ,  0.29622217,  0.79452344],
                          [ 0.5       ,  0.29622217,  0.20547656],
                          [ 0.5       ,  0.70377783,  0.70547656],
                          [ 0.5       ,  0.70377783,  0.29452344]]

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

