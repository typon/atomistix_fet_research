# Set up lattice
vector_a = [32.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.07664]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.40971793,  0.43050083,  0.16666667],
                          [ 0.3645769 ,  0.51389983,  0.16666667],
                          [ 0.5       ,  0.43050083,  0.16666667],
                          [ 0.45485897,  0.51389983,  0.16666667],
                          [ 0.40971793,  0.59729884,  0.16666667],
                          [ 0.59028207,  0.43050083,  0.16666667],
                          [ 0.54514103,  0.51389983,  0.16666667],
                          [ 0.5       ,  0.59729884,  0.16666667],
                          [ 0.6354231 ,  0.51389983,  0.16666667],
                          [ 0.59028207,  0.59729884,  0.16666667],
                          [ 0.3645769 ,  0.4583005 ,  0.5       ],
                          [ 0.45485897,  0.4583005 ,  0.5       ],
                          [ 0.40971793,  0.5416995 ,  0.5       ],
                          [ 0.54514103,  0.4583005 ,  0.5       ],
                          [ 0.5       ,  0.5416995 ,  0.5       ],
                          [ 0.6354231 ,  0.4583005 ,  0.5       ],
                          [ 0.59028207,  0.5416995 ,  0.5       ],
                          [ 0.3645769 ,  0.40270116,  0.83333333],
                          [ 0.45485897,  0.40270116,  0.83333333],
                          [ 0.40971793,  0.48610017,  0.83333333],
                          [ 0.3645769 ,  0.56949917,  0.83333333],
                          [ 0.54514103,  0.40270116,  0.83333333],
                          [ 0.5       ,  0.48610017,  0.83333333],
                          [ 0.45485897,  0.56949917,  0.83333333],
                          [ 0.6354231 ,  0.40270116,  0.83333333],
                          [ 0.59028207,  0.48610017,  0.83333333],
                          [ 0.54514103,  0.56949917,  0.83333333],
                          [ 0.6354231 ,  0.56949917,  0.83333333]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

