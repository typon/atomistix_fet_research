# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.5923, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.43762731,  0.66666667],
                          [ 0.5       ,  0.4792091 ,  0.83333333],
                          [ 0.5       ,  0.43762731,  0.33333333],
                          [ 0.5       ,  0.5207909 ,  0.66666667],
                          [ 0.5       ,  0.56237269,  0.83333333],
                          [ 0.5       ,  0.4792091 ,  0.16666667],
                          [ 0.5       ,  0.5207909 ,  0.33333333],
                          [ 0.5       ,  0.56237269,  0.16666667],
                          [ 0.5       ,  0.40572823,  0.79452344],
                          [ 0.5       ,  0.40572823,  0.20547656],
                          [ 0.5       ,  0.59427177,  0.70547656],
                          [ 0.5       ,  0.59427177,  0.29452344]]

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

