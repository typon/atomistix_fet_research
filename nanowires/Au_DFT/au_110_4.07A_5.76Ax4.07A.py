# Set up lattice
vector_a = [40.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.76752]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.55097812,  0.53604698,  0.12500023],
                          [ 0.55097812,  0.46395302,  0.12500023],
                          [ 0.44902188,  0.53604698,  0.12500023],
                          [ 0.5       ,  0.57209396,  0.37500008],
                          [ 0.44902188,  0.46395302,  0.12500023],
                          [ 0.5       ,  0.5       ,  0.37500008],
                          [ 0.55097812,  0.53604698,  0.62499992],
                          [ 0.5       ,  0.42790604,  0.37500008],
                          [ 0.55097812,  0.46395302,  0.62499992],
                          [ 0.44902188,  0.53604698,  0.62499992],
                          [ 0.44902188,  0.46395302,  0.62499992],
                          [ 0.5       ,  0.5       ,  0.87499977]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

