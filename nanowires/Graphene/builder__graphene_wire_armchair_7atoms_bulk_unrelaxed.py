# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 18.6135059865, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.26862215,  0.66666667],
                          [ 0.5       ,  0.33473011,  0.83333333],
                          [ 0.5       ,  0.26862215,  0.33333333],
                          [ 0.5       ,  0.40083806,  0.66666667],
                          [ 0.5       ,  0.46694602,  0.83333333],
                          [ 0.5       ,  0.33473011,  0.16666667],
                          [ 0.5       ,  0.40083806,  0.33333333],
                          [ 0.5       ,  0.53305398,  0.66666667],
                          [ 0.5       ,  0.59916194,  0.83333333],
                          [ 0.5       ,  0.46694602,  0.16666667],
                          [ 0.5       ,  0.53305398,  0.33333333],
                          [ 0.5       ,  0.66526989,  0.66666667],
                          [ 0.5       ,  0.59916194,  0.16666667],
                          [ 0.5       ,  0.66526989,  0.33333333],
                          [ 0.5       ,  0.21790805,  0.79452344],
                          [ 0.5       ,  0.21790805,  0.20547656],
                          [ 0.5       ,  0.715984  ,  0.79452344],
                          [ 0.5       ,  0.715984  ,  0.20547656]]

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

