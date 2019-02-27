# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.55616]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper, Copper, Copper]

# Define coordinates
fractional_coordinates = [[ 0.41479458,  0.409626  ,  0.75000027],
                          [ 0.41479458,  0.53012467,  0.75000027],
                          [ 0.5       ,  0.409626  ,  0.75000027],
                          [ 0.5       ,  0.53012467,  0.75000027],
                          [ 0.58520542,  0.409626  ,  0.75000027],
                          [ 0.58520542,  0.53012467,  0.75000027],
                          [ 0.37219186,  0.46987533,  0.24999973],
                          [ 0.37219186,  0.590374  ,  0.24999973],
                          [ 0.45739729,  0.46987533,  0.24999973],
                          [ 0.45739729,  0.590374  ,  0.24999973],
                          [ 0.54260271,  0.46987533,  0.24999973],
                          [ 0.54260271,  0.590374  ,  0.24999973],
                          [ 0.62780814,  0.46987533,  0.24999973],
                          [ 0.62780814,  0.590374  ,  0.24999973]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

