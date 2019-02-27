# Set up lattice
vector_a = [10.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 33.3795162492, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.14979246,  0.66666667],
                          [ 0.5       ,  0.18665642,  0.83333333],
                          [ 0.5       ,  0.14979246,  0.33333333],
                          [ 0.5       ,  0.22352037,  0.66666667],
                          [ 0.5       ,  0.26038432,  0.83333333],
                          [ 0.5       ,  0.18665642,  0.16666667],
                          [ 0.5       ,  0.22352037,  0.33333333],
                          [ 0.5       ,  0.29724827,  0.66666667],
                          [ 0.5       ,  0.33411222,  0.83333333],
                          [ 0.5       ,  0.26038432,  0.16666667],
                          [ 0.5       ,  0.29724827,  0.33333333],
                          [ 0.5       ,  0.37097617,  0.66666667],
                          [ 0.5       ,  0.40784012,  0.83333333],
                          [ 0.5       ,  0.33411222,  0.16666667],
                          [ 0.5       ,  0.37097617,  0.33333333],
                          [ 0.5       ,  0.44470407,  0.66666667],
                          [ 0.5       ,  0.48156802,  0.83333333],
                          [ 0.5       ,  0.40784012,  0.16666667],
                          [ 0.5       ,  0.44470407,  0.33333333],
                          [ 0.5       ,  0.51843198,  0.66666667],
                          [ 0.5       ,  0.55529593,  0.83333333],
                          [ 0.5       ,  0.48156802,  0.16666667],
                          [ 0.5       ,  0.51843198,  0.33333333],
                          [ 0.5       ,  0.59215988,  0.66666667],
                          [ 0.5       ,  0.62902383,  0.83333333],
                          [ 0.5       ,  0.55529593,  0.16666667],
                          [ 0.5       ,  0.59215988,  0.33333333],
                          [ 0.5       ,  0.66588778,  0.66666667],
                          [ 0.5       ,  0.70275173,  0.83333333],
                          [ 0.5       ,  0.62902383,  0.16666667],
                          [ 0.5       ,  0.66588778,  0.33333333],
                          [ 0.5       ,  0.73961568,  0.66666667],
                          [ 0.5       ,  0.77647963,  0.83333333],
                          [ 0.5       ,  0.70275173,  0.16666667],
                          [ 0.5       ,  0.73961568,  0.33333333],
                          [ 0.5       ,  0.81334358,  0.66666667],
                          [ 0.5       ,  0.85020754,  0.83333333],
                          [ 0.5       ,  0.77647963,  0.16666667],
                          [ 0.5       ,  0.81334358,  0.33333333],
                          [ 0.5       ,  0.85020754,  0.16666667],
                          [ 0.5       ,  0.12151263,  0.79452344],
                          [ 0.5       ,  0.12151263,  0.20547656],
                          [ 0.5       ,  0.87848737,  0.70547656],
                          [ 0.5       ,  0.87848737,  0.29452344]]

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

