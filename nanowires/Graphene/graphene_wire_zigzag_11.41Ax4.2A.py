# Set up lattice
vector_a = [20.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.461]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.3460735 ,  0.24999983],
                          [ 0.5       ,  0.3697545 ,  0.75000017],
                          [ 0.5       ,  0.4171165 ,  0.75000017],
                          [ 0.5       ,  0.4407975 ,  0.24999983],
                          [ 0.5       ,  0.4881595 ,  0.24999983],
                          [ 0.5       ,  0.5118405 ,  0.75000017],
                          [ 0.5       ,  0.5592025 ,  0.75000017],
                          [ 0.5       ,  0.5828835 ,  0.24999983],
                          [ 0.5       ,  0.6302455 ,  0.24999983],
                          [ 0.5       ,  0.6539265 ,  0.75000017],
                          [ 0.5       ,  0.30974018,  0.24999983],
                          [ 0.5       ,  0.69025982,  0.75000017]]

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

