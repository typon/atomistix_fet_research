# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.59400334,  0.5       ,  0.66666667],
                          [ 0.58140928,  0.54700167,  0.83333333],
                          [ 0.59400334,  0.5       ,  0.33333333],
                          [ 0.54700167,  0.58140928,  0.66666667],
                          [ 0.5       ,  0.59400334,  0.83333333],
                          [ 0.58140928,  0.54700167,  0.16666667],
                          [ 0.54700167,  0.58140928,  0.33333333],
                          [ 0.45299833,  0.58140928,  0.66666667],
                          [ 0.41859072,  0.54700167,  0.83333333],
                          [ 0.5       ,  0.59400334,  0.16666667],
                          [ 0.45299833,  0.58140928,  0.33333333],
                          [ 0.40599666,  0.5       ,  0.66666667],
                          [ 0.41859072,  0.45299833,  0.83333333],
                          [ 0.41859072,  0.54700167,  0.16666667],
                          [ 0.40599666,  0.5       ,  0.33333333],
                          [ 0.45299833,  0.41859072,  0.66666667],
                          [ 0.5       ,  0.40599666,  0.83333333],
                          [ 0.41859072,  0.45299833,  0.16666667],
                          [ 0.45299833,  0.41859072,  0.33333333],
                          [ 0.54700167,  0.41859072,  0.66666667],
                          [ 0.58140928,  0.45299833,  0.83333333],
                          [ 0.5       ,  0.40599666,  0.16666667],
                          [ 0.54700167,  0.41859072,  0.33333333],
                          [ 0.58140928,  0.45299833,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


