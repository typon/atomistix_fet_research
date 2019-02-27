# Set up lattice
vector_a = [20.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 20.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.26258]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon, Carbon,
            Carbon, Carbon, Carbon, Carbon]

# Define coordinates
fractional_coordinates = [[ 0.59792015,  0.5       ,  0.66666667],
                          [ 0.57921906,  0.55755602,  0.83333333],
                          [ 0.59792015,  0.5       ,  0.33333333],
                          [ 0.53025899,  0.59312759,  0.66666667],
                          [ 0.46974101,  0.59312759,  0.83333333],
                          [ 0.57921906,  0.55755602,  0.16666667],
                          [ 0.53025899,  0.59312759,  0.33333333],
                          [ 0.42078094,  0.55755602,  0.66666667],
                          [ 0.40207985,  0.5       ,  0.83333333],
                          [ 0.46974101,  0.59312759,  0.16666667],
                          [ 0.42078094,  0.55755602,  0.33333333],
                          [ 0.42078094,  0.44244398,  0.66666667],
                          [ 0.46974101,  0.40687241,  0.83333333],
                          [ 0.40207985,  0.5       ,  0.16666667],
                          [ 0.42078094,  0.44244398,  0.33333333],
                          [ 0.53025899,  0.40687241,  0.66666667],
                          [ 0.57921906,  0.44244398,  0.83333333],
                          [ 0.46974101,  0.40687241,  0.16666667],
                          [ 0.53025899,  0.40687241,  0.33333333],
                          [ 0.57921906,  0.44244398,  0.16666667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    ]


