# Set up lattice
lattice = SimpleTetragonal(8.66707852768*Angstrom, 7.07663998448*Angstrom)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.68589251,  0.45019025,  0.16666667],
                          [ 0.82197528,  0.58627302,  0.5       ],
                          [ 0.73570226,  0.26429774,  0.5       ],
                          [ 0.45019025,  0.68589251,  0.16666667],
                          [ 0.58627302,  0.82197528,  0.5       ],
                          [ 0.36391724,  0.36391724,  0.16666667],
                          [ 0.5       ,  0.5       ,  0.5       ],
                          [ 0.63608276,  0.63608276,  0.83333333],
                          [ 0.41372698,  0.17802472,  0.5       ],
                          [ 0.54980975,  0.31410749,  0.83333333],
                          [ 0.26429774,  0.73570226,  0.5       ],
                          [ 0.17802472,  0.41372698,  0.5       ],
                          [ 0.31410749,  0.54980975,  0.83333333]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]

