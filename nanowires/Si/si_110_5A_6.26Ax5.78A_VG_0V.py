# Set up lattice
vector_a = [15.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 15.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.89683]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.37199953,  0.545255  ,  0.25364501],
                          [ 0.62800047,  0.545255  ,  0.25364501],
                          [ 0.5       ,  0.635765  ,  0.25364501],
                          [ 0.37199953,  0.454745  ,  0.74635499],
                          [ 0.62800047,  0.454745  ,  0.74635499],
                          [ 0.5       ,  0.364235  ,  0.74635499],
                          [ 0.29143857,  0.6022202 ,  0.25364501],
                          [ 0.70856143,  0.6022202 ,  0.25364501],
                          [ 0.5       ,  0.6927302 , -0.05645689],
                          [ 0.5       ,  0.6927302 ,  0.5637469 ],
                          [ 0.29143857,  0.3977798 ,  0.74635499],
                          [ 0.70856143,  0.3977798 ,  0.74635499],
                          [ 0.5       ,  0.3072698 ,  1.05645689],
                          [ 0.5       ,  0.3072698 ,  0.4362531 ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

