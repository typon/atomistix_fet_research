# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.32421416,  0.66666667],
                          [ 0.5       ,  0.35937133,  0.83333333],
                          [ 0.5       ,  0.32421416,  0.33333333],
                          [ 0.5       ,  0.3945285 ,  0.66666667],
                          [ 0.5       ,  0.42968567,  0.83333333],
                          [ 0.5       ,  0.35937133,  0.16666667],
                          [ 0.5       ,  0.3945285 ,  0.33333333],
                          [ 0.5       ,  0.46484283,  0.66666667],
                          [ 0.5       ,  0.5       ,  0.83333333],
                          [ 0.5       ,  0.42968567,  0.16666667],
                          [ 0.5       ,  0.46484283,  0.33333333],
                          [ 0.5       ,  0.53515717,  0.66666667],
                          [ 0.5       ,  0.57031433,  0.83333333],
                          [ 0.5       ,  0.5       ,  0.16666667],
                          [ 0.5       ,  0.53515717,  0.33333333],
                          [ 0.5       ,  0.6054715 ,  0.66666667],
                          [ 0.5       ,  0.64062867,  0.83333333],
                          [ 0.5       ,  0.57031433,  0.16666667],
                          [ 0.5       ,  0.6054715 ,  0.33333333],
                          [ 0.5       ,  0.67578584,  0.66666667],
                          [ 0.5       ,  0.64062867,  0.16666667],
                          [ 0.5       ,  0.67578584,  0.33333333],
                          [ 0.5       ,  0.29724367,  0.79452344],
                          [ 0.5       ,  0.29724367,  0.20547656],
                          [ 0.5       ,  0.70275633,  0.79452344],
                          [ 0.5       ,  0.70275633,  0.20547656]]

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

