# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.8405179596, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.13950691,  0.66666667],
                          [ 0.5       ,  0.17383959,  0.83333333],
                          [ 0.5       ,  0.13950691,  0.33333333],
                          [ 0.5       ,  0.20817226,  0.66666667],
                          [ 0.5       ,  0.24250494,  0.83333333],
                          [ 0.5       ,  0.17383959,  0.16666667],
                          [ 0.5       ,  0.20817226,  0.33333333],
                          [ 0.5       ,  0.27683761,  0.66666667],
                          [ 0.5       ,  0.31117029,  0.83333333],
                          [ 0.5       ,  0.24250494,  0.16666667],
                          [ 0.5       ,  0.27683761,  0.33333333],
                          [ 0.5       ,  0.34550296,  0.66666667],
                          [ 0.5       ,  0.37983564,  0.83333333],
                          [ 0.5       ,  0.31117029,  0.16666667],
                          [ 0.5       ,  0.34550296,  0.33333333],
                          [ 0.5       ,  0.41416831,  0.66666667],
                          [ 0.5       ,  0.44850099,  0.83333333],
                          [ 0.5       ,  0.37983564,  0.16666667],
                          [ 0.5       ,  0.41416831,  0.33333333],
                          [ 0.5       ,  0.48283366,  0.66666667],
                          [ 0.5       ,  0.51716634,  0.83333333],
                          [ 0.5       ,  0.44850099,  0.16666667],
                          [ 0.5       ,  0.48283366,  0.33333333],
                          [ 0.5       ,  0.55149901,  0.66666667],
                          [ 0.5       ,  0.58583169,  0.83333333],
                          [ 0.5       ,  0.51716634,  0.16666667],
                          [ 0.5       ,  0.55149901,  0.33333333],
                          [ 0.5       ,  0.62016436,  0.66666667],
                          [ 0.5       ,  0.65449704,  0.83333333],
                          [ 0.5       ,  0.58583169,  0.16666667],
                          [ 0.5       ,  0.62016436,  0.33333333],
                          [ 0.5       ,  0.68882971,  0.66666667],
                          [ 0.5       ,  0.72316239,  0.83333333],
                          [ 0.5       ,  0.65449704,  0.16666667],
                          [ 0.5       ,  0.68882971,  0.33333333],
                          [ 0.5       ,  0.75749506,  0.66666667],
                          [ 0.5       ,  0.79182774,  0.83333333],
                          [ 0.5       ,  0.72316239,  0.16666667],
                          [ 0.5       ,  0.75749506,  0.33333333],
                          [ 0.5       ,  0.82616041,  0.66666667],
                          [ 0.5       ,  0.79182774,  0.16666667],
                          [ 0.5       ,  0.82616041,  0.33333333],
                          [ 0.5       ,  0.11316892,  0.79452344],
                          [ 0.5       ,  0.11316892,  0.20547656],
                          [ 0.5       ,  0.8524984 ,  0.79452344],
                          [ 0.5       ,  0.8524984 ,  0.20547656]]

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

