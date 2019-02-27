# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.60967056,  0.5       ,  0.66666667],
                          [ 0.59880976,  0.54758427,  0.83333333],
                          [ 0.60967056,  0.5       ,  0.33333333],
                          [ 0.56837848,  0.5857439 ,  0.66666667],
                          [ 0.524404  ,  0.60692089,  0.83333333],
                          [ 0.59880976,  0.54758427,  0.16666667],
                          [ 0.56837848,  0.5857439 ,  0.33333333],
                          [ 0.475596  ,  0.60692089,  0.66666667],
                          [ 0.43162152,  0.5857439 ,  0.83333333],
                          [ 0.524404  ,  0.60692089,  0.16666667],
                          [ 0.475596  ,  0.60692089,  0.33333333],
                          [ 0.40119024,  0.54758427,  0.66666667],
                          [ 0.39032944,  0.5       ,  0.83333333],
                          [ 0.43162152,  0.5857439 ,  0.16666667],
                          [ 0.40119024,  0.54758427,  0.33333333],
                          [ 0.40119024,  0.45241573,  0.66666667],
                          [ 0.43162152,  0.4142561 ,  0.83333333],
                          [ 0.39032944,  0.5       ,  0.16666667],
                          [ 0.40119024,  0.45241573,  0.33333333],
                          [ 0.475596  ,  0.39307911,  0.66666667],
                          [ 0.524404  ,  0.39307911,  0.83333333],
                          [ 0.43162152,  0.4142561 ,  0.16666667],
                          [ 0.475596  ,  0.39307911,  0.33333333],
                          [ 0.56837848,  0.4142561 ,  0.66666667],
                          [ 0.59880976,  0.45241573,  0.83333333],
                          [ 0.524404  ,  0.39307911,  0.16666667],
                          [ 0.56837848,  0.4142561 ,  0.33333333],
                          [ 0.59880976,  0.45241573,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


