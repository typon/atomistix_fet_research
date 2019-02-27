# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.3523399 ,  0.66666667],
                          [ 0.5       ,  0.40155993,  0.83333333],
                          [ 0.5       ,  0.3523399 ,  0.33333333],
                          [ 0.5       ,  0.45077997,  0.66666667],
                          [ 0.5       ,  0.5       ,  0.83333333],
                          [ 0.5       ,  0.40155993,  0.16666667],
                          [ 0.5       ,  0.45077997,  0.33333333],
                          [ 0.5       ,  0.54922003,  0.66666667],
                          [ 0.5       ,  0.59844007,  0.83333333],
                          [ 0.5       ,  0.5       ,  0.16666667],
                          [ 0.5       ,  0.54922003,  0.33333333],
                          [ 0.5       ,  0.6476601 ,  0.66666667],
                          [ 0.5       ,  0.59844007,  0.16666667],
                          [ 0.5       ,  0.6476601 ,  0.33333333],
                          [ 0.5       ,  0.31458121,  0.79452344],
                          [ 0.5       ,  0.31458121,  0.20547656],
                          [ 0.5       ,  0.68541879,  0.79452344],
                          [ 0.5       ,  0.68541879,  0.20547656]]

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

