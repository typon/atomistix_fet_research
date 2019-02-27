# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 40.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.30004361,  0.66666667],
                          [ 0.5       ,  0.33080613,  0.83333333],
                          [ 0.5       ,  0.30004361,  0.33333333],
                          [ 0.5       ,  0.36156865,  0.66666667],
                          [ 0.5       ,  0.39233118,  0.83333333],
                          [ 0.5       ,  0.33080613,  0.16666667],
                          [ 0.5       ,  0.36156865,  0.33333333],
                          [ 0.5       ,  0.4230937 ,  0.66666667],
                          [ 0.5       ,  0.45385622,  0.83333333],
                          [ 0.5       ,  0.39233118,  0.16666667],
                          [ 0.5       ,  0.4230937 ,  0.33333333],
                          [ 0.5       ,  0.48461874,  0.66666667],
                          [ 0.5       ,  0.51538126,  0.83333333],
                          [ 0.5       ,  0.45385622,  0.16666667],
                          [ 0.5       ,  0.48461874,  0.33333333],
                          [ 0.5       ,  0.54614378,  0.66666667],
                          [ 0.5       ,  0.5769063 ,  0.83333333],
                          [ 0.5       ,  0.51538126,  0.16666667],
                          [ 0.5       ,  0.54614378,  0.33333333],
                          [ 0.5       ,  0.60766882,  0.66666667],
                          [ 0.5       ,  0.63843135,  0.83333333],
                          [ 0.5       ,  0.5769063 ,  0.16666667],
                          [ 0.5       ,  0.60766882,  0.33333333],
                          [ 0.5       ,  0.66919387,  0.66666667],
                          [ 0.5       ,  0.69995639,  0.83333333],
                          [ 0.5       ,  0.63843135,  0.16666667],
                          [ 0.5       ,  0.66919387,  0.33333333],
                          [ 0.5       ,  0.69995639,  0.16666667],
                          [ 0.5       ,  0.27644443,  0.79452344],
                          [ 0.5       ,  0.27644443,  0.20547656],
                          [ 0.5       ,  0.72355557,  0.70547656],
                          [ 0.5       ,  0.72355557,  0.29452344]]

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

