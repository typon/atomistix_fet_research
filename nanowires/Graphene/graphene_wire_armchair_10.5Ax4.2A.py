# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.32772988,  0.66666667],
                          [ 0.5       ,  0.37694991,  0.83333333],
                          [ 0.5       ,  0.32772988,  0.33333333],
                          [ 0.5       ,  0.42616995,  0.66666667],
                          [ 0.5       ,  0.47538998,  0.83333333],
                          [ 0.5       ,  0.37694991,  0.16666667],
                          [ 0.5       ,  0.42616995,  0.33333333],
                          [ 0.5       ,  0.52461002,  0.66666667],
                          [ 0.5       ,  0.57383005,  0.83333333],
                          [ 0.5       ,  0.47538998,  0.16666667],
                          [ 0.5       ,  0.52461002,  0.33333333],
                          [ 0.5       ,  0.62305009,  0.66666667],
                          [ 0.5       ,  0.67227012,  0.83333333],
                          [ 0.5       ,  0.57383005,  0.16666667],
                          [ 0.5       ,  0.62305009,  0.33333333],
                          [ 0.5       ,  0.67227012,  0.16666667],
                          [ 0.5       ,  0.28997119,  0.79452344],
                          [ 0.5       ,  0.28997119,  0.20547656],
                          [ 0.5       ,  0.71002881,  0.70547656],
                          [ 0.5       ,  0.71002881,  0.29452344]]

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

