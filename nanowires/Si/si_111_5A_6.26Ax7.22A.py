# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 9.40608]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.5       ,  0.12500019],
                          [ 0.5       ,  0.41131867,  0.20833348],
                          [ 0.42319972,  0.54434066,  0.20833348],
                          [ 0.57680028,  0.54434066,  0.20833348],
                          [ 0.5       ,  0.41131867,  0.45833335],
                          [ 0.42319972,  0.54434066,  0.45833335],
                          [ 0.57680028,  0.54434066,  0.45833335],
                          [ 0.42319972,  0.45565934,  0.54166665],
                          [ 0.57680028,  0.45565934,  0.54166665],
                          [ 0.5       ,  0.58868133,  0.54166665],
                          [ 0.42319972,  0.45565934,  0.79166652],
                          [ 0.57680028,  0.45565934,  0.79166652],
                          [ 0.5       ,  0.58868133,  0.79166652],
                          [ 0.5       ,  0.5       ,  0.87499981],
                          [ 0.54833657,  0.38341154,  0.15588516],
                          [ 0.45166343,  0.38341154,  0.15588516],
                          [ 0.37486314,  0.51643353,  0.15588516],
                          [ 0.42319972,  0.60015493,  0.15588516],
                          [ 0.62513686,  0.51643353,  0.15588516],
                          [ 0.57680028,  0.60015493,  0.15588516],
                          [ 0.5       ,  0.3555044 ,  0.51078168],
                          [ 0.37486314,  0.5722478 ,  0.51078168],
                          [ 0.62513686,  0.5722478 ,  0.51078168],
                          [ 0.37486314,  0.4277522 ,  0.48921832],
                          [ 0.62513686,  0.4277522 ,  0.48921832],
                          [ 0.5       ,  0.6444956 ,  0.48921832],
                          [ 0.37486314,  0.48356647,  0.84411484],
                          [ 0.42319972,  0.39984507,  0.84411484],
                          [ 0.62513686,  0.48356647,  0.84411484],
                          [ 0.57680028,  0.39984507,  0.84411484],
                          [ 0.54833657,  0.61658846,  0.84411484],
                          [ 0.45166343,  0.61658846,  0.84411484]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


