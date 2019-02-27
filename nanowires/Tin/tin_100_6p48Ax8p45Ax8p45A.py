# Set up lattice
lattice = SimpleTetragonal(30.0*Angstrom, 6.4892*Angstrom)

# Define elements
elements = [Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin, Tin,
            Tin, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.39184667,  0.20062527],
                          [ 0.60815333,  0.5       ,  0.20062527],
                          [ 0.60815333,  0.39184667,  0.70062527],
                          [ 0.39184667,  0.5       ,  0.20062527],
                          [ 0.5       ,  0.60815333,  0.20062527],
                          [ 0.39184667,  0.39184667,  0.70062527],
                          [ 0.44592333,  0.44592333,  0.45062527],
                          [ 0.5       ,  0.5       ,  0.70062527],
                          [ 0.55407667,  0.55407667,  0.45062527],
                          [ 0.60815333,  0.60815333,  0.70062527],
                          [ 0.55407667,  0.44592333,  0.95062527],
                          [ 0.39184667,  0.60815333,  0.70062527],
                          [ 0.44592333,  0.55407667,  0.95062527],
                          [ 0.5327165 ,  0.35913017,  0.35187581],
                          [ 0.4672835 ,  0.35913017,  0.04937473],
                          [ 0.64086983,  0.4672835 ,  0.35187581],
                          [ 0.64086983,  0.5327165 ,  0.04937473],
                          [ 0.64086983,  0.42456317,  0.54937473],
                          [ 0.64086983,  0.35913017,  0.85187581],
                          [ 0.57543683,  0.35913017,  0.54937473],
                          [ 0.35913017,  0.4672835 ,  0.04937473],
                          [ 0.35913017,  0.5327165 ,  0.35187581],
                          [ 0.5327165 ,  0.64086983,  0.04937473],
                          [ 0.4672835 ,  0.64086983,  0.35187581],
                          [ 0.42456317,  0.35913017,  0.85187581],
                          [ 0.35913017,  0.42456317,  0.85187581],
                          [ 0.35913017,  0.35913017,  0.54937473],
                          [ 0.64086983,  0.64086983,  0.54937473],
                          [ 0.57543683,  0.64086983,  0.85187581],
                          [ 0.64086983,  0.57543683,  0.85187581],
                          [ 0.42456317,  0.64086983,  0.54937473],
                          [ 0.35913017,  0.57543683,  0.54937473],
                          [ 0.35913017,  0.64086983,  0.85187581]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Tin_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


