# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.65667223,  0.5       ,  0.66666667],
                          [ 0.65133376,  0.54054976,  0.83333333],
                          [ 0.65667223,  0.5       ,  0.33333333],
                          [ 0.63568214,  0.57833612,  0.66666667],
                          [ 0.610784  ,  0.610784  ,  0.83333333],
                          [ 0.65133376,  0.54054976,  0.16666667],
                          [ 0.63568214,  0.57833612,  0.33333333],
                          [ 0.57833612,  0.63568214,  0.66666667],
                          [ 0.54054976,  0.65133376,  0.83333333],
                          [ 0.610784  ,  0.610784  ,  0.16666667],
                          [ 0.57833612,  0.63568214,  0.33333333],
                          [ 0.5       ,  0.65667223,  0.66666667],
                          [ 0.45945024,  0.65133376,  0.83333333],
                          [ 0.54054976,  0.65133376,  0.16666667],
                          [ 0.5       ,  0.65667223,  0.33333333],
                          [ 0.42166388,  0.63568214,  0.66666667],
                          [ 0.389216  ,  0.610784  ,  0.83333333],
                          [ 0.45945024,  0.65133376,  0.16666667],
                          [ 0.42166388,  0.63568214,  0.33333333],
                          [ 0.36431786,  0.57833612,  0.66666667],
                          [ 0.34866624,  0.54054976,  0.83333333],
                          [ 0.389216  ,  0.610784  ,  0.16666667],
                          [ 0.36431786,  0.57833612,  0.33333333],
                          [ 0.34332777,  0.5       ,  0.66666667],
                          [ 0.34866624,  0.45945024,  0.83333333],
                          [ 0.34866624,  0.54054976,  0.16666667],
                          [ 0.34332777,  0.5       ,  0.33333333],
                          [ 0.36431786,  0.42166388,  0.66666667],
                          [ 0.389216  ,  0.389216  ,  0.83333333],
                          [ 0.34866624,  0.45945024,  0.16666667],
                          [ 0.36431786,  0.42166388,  0.33333333],
                          [ 0.42166388,  0.36431786,  0.66666667],
                          [ 0.45945024,  0.34866624,  0.83333333],
                          [ 0.389216  ,  0.389216  ,  0.16666667],
                          [ 0.42166388,  0.36431786,  0.33333333],
                          [ 0.5       ,  0.34332777,  0.66666667],
                          [ 0.54054976,  0.34866624,  0.83333333],
                          [ 0.45945024,  0.34866624,  0.16666667],
                          [ 0.5       ,  0.34332777,  0.33333333],
                          [ 0.57833612,  0.36431786,  0.66666667],
                          [ 0.610784  ,  0.389216  ,  0.83333333],
                          [ 0.54054976,  0.34866624,  0.16666667],
                          [ 0.57833612,  0.36431786,  0.33333333],
                          [ 0.63568214,  0.42166388,  0.66666667],
                          [ 0.65133376,  0.45945024,  0.83333333],
                          [ 0.610784  ,  0.389216  ,  0.16666667],
                          [ 0.63568214,  0.42166388,  0.33333333],
                          [ 0.65133376,  0.45945024,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


