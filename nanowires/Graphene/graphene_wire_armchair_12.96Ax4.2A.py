# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.31542487,  0.66666667],
                          [ 0.5       ,  0.35644157,  0.83333333],
                          [ 0.5       ,  0.31542487,  0.33333333],
                          [ 0.5       ,  0.39745826,  0.66666667],
                          [ 0.5       ,  0.43847496,  0.83333333],
                          [ 0.5       ,  0.35644157,  0.16666667],
                          [ 0.5       ,  0.39745826,  0.33333333],
                          [ 0.5       ,  0.47949165,  0.66666667],
                          [ 0.5       ,  0.52050835,  0.83333333],
                          [ 0.5       ,  0.43847496,  0.16666667],
                          [ 0.5       ,  0.47949165,  0.33333333],
                          [ 0.5       ,  0.56152504,  0.66666667],
                          [ 0.5       ,  0.60254174,  0.83333333],
                          [ 0.5       ,  0.52050835,  0.16666667],
                          [ 0.5       ,  0.56152504,  0.33333333],
                          [ 0.5       ,  0.64355843,  0.66666667],
                          [ 0.5       ,  0.68457513,  0.83333333],
                          [ 0.5       ,  0.60254174,  0.16666667],
                          [ 0.5       ,  0.64355843,  0.33333333],
                          [ 0.5       ,  0.68457513,  0.16666667],
                          [ 0.5       ,  0.2839593 ,  0.79452344],
                          [ 0.5       ,  0.2839593 ,  0.20547656],
                          [ 0.5       ,  0.7160407 ,  0.70547656],
                          [ 0.5       ,  0.7160407 ,  0.29452344]]

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

