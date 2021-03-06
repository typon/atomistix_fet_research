# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.69584029,  0.5       ,  0.66666667],
                          [ 0.69156071,  0.54071749,  0.83333333],
                          [ 0.69584029,  0.5       ,  0.33333333],
                          [ 0.67890901,  0.57965542,  0.66666667],
                          [ 0.65843813,  0.61511204,  0.83333333],
                          [ 0.69156071,  0.54071749,  0.16666667],
                          [ 0.67890901,  0.57965542,  0.33333333],
                          [ 0.63104273,  0.6455377 ,  0.66666667],
                          [ 0.59792015,  0.66960267,  0.83333333],
                          [ 0.65843813,  0.61511204,  0.16666667],
                          [ 0.63104273,  0.6455377 ,  0.33333333],
                          [ 0.56051798,  0.68625519,  0.66666667],
                          [ 0.52047088,  0.69476746,  0.83333333],
                          [ 0.59792015,  0.66960267,  0.16666667],
                          [ 0.56051798,  0.68625519,  0.33333333],
                          [ 0.47952912,  0.69476746,  0.66666667],
                          [ 0.43948202,  0.68625519,  0.83333333],
                          [ 0.52047088,  0.69476746,  0.16666667],
                          [ 0.47952912,  0.69476746,  0.33333333],
                          [ 0.40207985,  0.66960267,  0.66666667],
                          [ 0.36895727,  0.6455377 ,  0.83333333],
                          [ 0.43948202,  0.68625519,  0.16666667],
                          [ 0.40207985,  0.66960267,  0.33333333],
                          [ 0.34156187,  0.61511204,  0.66666667],
                          [ 0.32109099,  0.57965542,  0.83333333],
                          [ 0.36895727,  0.6455377 ,  0.16666667],
                          [ 0.34156187,  0.61511204,  0.33333333],
                          [ 0.30843929,  0.54071749,  0.66666667],
                          [ 0.30415971,  0.5       ,  0.83333333],
                          [ 0.32109099,  0.57965542,  0.16666667],
                          [ 0.30843929,  0.54071749,  0.33333333],
                          [ 0.30843929,  0.45928251,  0.66666667],
                          [ 0.32109099,  0.42034458,  0.83333333],
                          [ 0.30415971,  0.5       ,  0.16666667],
                          [ 0.30843929,  0.45928251,  0.33333333],
                          [ 0.34156187,  0.38488796,  0.66666667],
                          [ 0.36895727,  0.3544623 ,  0.83333333],
                          [ 0.32109099,  0.42034458,  0.16666667],
                          [ 0.34156187,  0.38488796,  0.33333333],
                          [ 0.40207985,  0.33039733,  0.66666667],
                          [ 0.43948202,  0.31374481,  0.83333333],
                          [ 0.36895727,  0.3544623 ,  0.16666667],
                          [ 0.40207985,  0.33039733,  0.33333333],
                          [ 0.47952912,  0.30523254,  0.66666667],
                          [ 0.52047088,  0.30523254,  0.83333333],
                          [ 0.43948202,  0.31374481,  0.16666667],
                          [ 0.47952912,  0.30523254,  0.33333333],
                          [ 0.56051798,  0.31374481,  0.66666667],
                          [ 0.59792015,  0.33039733,  0.83333333],
                          [ 0.52047088,  0.30523254,  0.16666667],
                          [ 0.56051798,  0.31374481,  0.33333333],
                          [ 0.63104273,  0.3544623 ,  0.66666667],
                          [ 0.65843813,  0.38488796,  0.83333333],
                          [ 0.59792015,  0.33039733,  0.16666667],
                          [ 0.63104273,  0.3544623 ,  0.33333333],
                          [ 0.67890901,  0.42034458,  0.66666667],
                          [ 0.69156071,  0.45928251,  0.83333333],
                          [ 0.65843813,  0.38488796,  0.16666667],
                          [ 0.67890901,  0.42034458,  0.33333333],
                          [ 0.69156071,  0.45928251,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


