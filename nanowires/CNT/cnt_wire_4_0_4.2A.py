# Set up lattice
vector_a = [20.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.57833612,  0.5       ,  0.66666667],
                          [ 0.555392  ,  0.555392  ,  0.83333333],
                          [ 0.57833612,  0.5       ,  0.33333333],
                          [ 0.5       ,  0.57833612,  0.66666667],
                          [ 0.444608  ,  0.555392  ,  0.83333333],
                          [ 0.555392  ,  0.555392  ,  0.16666667],
                          [ 0.5       ,  0.57833612,  0.33333333],
                          [ 0.42166388,  0.5       ,  0.66666667],
                          [ 0.444608  ,  0.444608  ,  0.83333333],
                          [ 0.444608  ,  0.555392  ,  0.16666667],
                          [ 0.42166388,  0.5       ,  0.33333333],
                          [ 0.5       ,  0.42166388,  0.66666667],
                          [ 0.555392  ,  0.444608  ,  0.83333333],
                          [ 0.444608  ,  0.444608  ,  0.16666667],
                          [ 0.5       ,  0.42166388,  0.33333333],
                          [ 0.555392  ,  0.444608  ,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


