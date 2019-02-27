# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.30663558,  0.66666667],
                          [ 0.5       ,  0.34179275,  0.83333333],
                          [ 0.5       ,  0.30663558,  0.33333333],
                          [ 0.5       ,  0.37694991,  0.66666667],
                          [ 0.5       ,  0.41210708,  0.83333333],
                          [ 0.5       ,  0.34179275,  0.16666667],
                          [ 0.5       ,  0.37694991,  0.33333333],
                          [ 0.5       ,  0.44726425,  0.66666667],
                          [ 0.5       ,  0.48242142,  0.83333333],
                          [ 0.5       ,  0.41210708,  0.16666667],
                          [ 0.5       ,  0.44726425,  0.33333333],
                          [ 0.5       ,  0.51757858,  0.66666667],
                          [ 0.5       ,  0.55273575,  0.83333333],
                          [ 0.5       ,  0.48242142,  0.16666667],
                          [ 0.5       ,  0.51757858,  0.33333333],
                          [ 0.5       ,  0.58789292,  0.66666667],
                          [ 0.5       ,  0.62305009,  0.83333333],
                          [ 0.5       ,  0.55273575,  0.16666667],
                          [ 0.5       ,  0.58789292,  0.33333333],
                          [ 0.5       ,  0.65820725,  0.66666667],
                          [ 0.5       ,  0.69336442,  0.83333333],
                          [ 0.5       ,  0.62305009,  0.16666667],
                          [ 0.5       ,  0.65820725,  0.33333333],
                          [ 0.5       ,  0.69336442,  0.16666667],
                          [ 0.5       ,  0.27966509,  0.79452344],
                          [ 0.5       ,  0.27966509,  0.20547656],
                          [ 0.5       ,  0.72033491,  0.70547656],
                          [ 0.5       ,  0.72033491,  0.29452344]]

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

