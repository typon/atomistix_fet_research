# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.62533779,  0.5       ,  0.66666667],
                          [ 0.61579702,  0.54796469,  0.83333333],
                          [ 0.62533779,  0.5       ,  0.33333333],
                          [ 0.5886272 ,  0.5886272 ,  0.66666667],
                          [ 0.54796469,  0.61579702,  0.83333333],
                          [ 0.61579702,  0.54796469,  0.16666667],
                          [ 0.5886272 ,  0.5886272 ,  0.33333333],
                          [ 0.5       ,  0.62533779,  0.66666667],
                          [ 0.45203531,  0.61579702,  0.83333333],
                          [ 0.54796469,  0.61579702,  0.16666667],
                          [ 0.5       ,  0.62533779,  0.33333333],
                          [ 0.4113728 ,  0.5886272 ,  0.66666667],
                          [ 0.38420298,  0.54796469,  0.83333333],
                          [ 0.45203531,  0.61579702,  0.16666667],
                          [ 0.4113728 ,  0.5886272 ,  0.33333333],
                          [ 0.37466221,  0.5       ,  0.66666667],
                          [ 0.38420298,  0.45203531,  0.83333333],
                          [ 0.38420298,  0.54796469,  0.16666667],
                          [ 0.37466221,  0.5       ,  0.33333333],
                          [ 0.4113728 ,  0.4113728 ,  0.66666667],
                          [ 0.45203531,  0.38420298,  0.83333333],
                          [ 0.38420298,  0.45203531,  0.16666667],
                          [ 0.4113728 ,  0.4113728 ,  0.33333333],
                          [ 0.5       ,  0.37466221,  0.66666667],
                          [ 0.54796469,  0.38420298,  0.83333333],
                          [ 0.45203531,  0.38420298,  0.16666667],
                          [ 0.5       ,  0.37466221,  0.33333333],
                          [ 0.5886272 ,  0.4113728 ,  0.66666667],
                          [ 0.61579702,  0.45203531,  0.83333333],
                          [ 0.54796469,  0.38420298,  0.16666667],
                          [ 0.5886272 ,  0.4113728 ,  0.33333333],
                          [ 0.61579702,  0.45203531,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


