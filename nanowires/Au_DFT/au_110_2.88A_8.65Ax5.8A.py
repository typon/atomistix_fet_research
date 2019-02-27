# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88376]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.35581209,  0.46601458,  0.25000015],
                          [ 0.35581209,  0.60195625,  0.25000015],
                          [ 0.45193736,  0.46601458,  0.25000015],
                          [ 0.45193736,  0.60195625,  0.25000015],
                          [ 0.54806264,  0.46601458,  0.25000015],
                          [ 0.54806264,  0.60195625,  0.25000015],
                          [ 0.64418791,  0.46601458,  0.25000015],
                          [ 0.64418791,  0.60195625,  0.25000015],
                          [ 0.40387473,  0.39804375,  0.74999985],
                          [ 0.40387473,  0.53398542,  0.74999985],
                          [ 0.5       ,  0.39804375,  0.74999985],
                          [ 0.5       ,  0.53398542,  0.74999985],
                          [ 0.59612527,  0.39804375,  0.74999985],
                          [ 0.59612527,  0.53398542,  0.74999985]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

