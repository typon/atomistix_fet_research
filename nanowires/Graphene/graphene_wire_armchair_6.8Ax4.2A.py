# Set up lattice
vector_a = [20.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.37694991,  0.66666667],
                          [ 0.5       ,  0.43847496,  0.83333333],
                          [ 0.5       ,  0.37694991,  0.33333333],
                          [ 0.5       ,  0.5       ,  0.66666667],
                          [ 0.5       ,  0.56152504,  0.83333333],
                          [ 0.5       ,  0.43847496,  0.16666667],
                          [ 0.5       ,  0.5       ,  0.33333333],
                          [ 0.5       ,  0.62305009,  0.66666667],
                          [ 0.5       ,  0.56152504,  0.16666667],
                          [ 0.5       ,  0.62305009,  0.33333333],
                          [ 0.5       ,  0.32975155,  0.79452344],
                          [ 0.5       ,  0.32975155,  0.20547656],
                          [ 0.5       ,  0.67024845,  0.79452344],
                          [ 0.5       ,  0.67024845,  0.20547656]]

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

