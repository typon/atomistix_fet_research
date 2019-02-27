# Set up lattice
vector_a = [25.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 25.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.32665843,  0.38443895,  0.25      ],
                          [ 0.32665843,  0.5       ,  0.25      ],
                          [ 0.32665843,  0.61556105,  0.25      ],
                          [ 0.44221948,  0.38443895,  0.25      ],
                          [ 0.44221948,  0.5       ,  0.25      ],
                          [ 0.44221948,  0.61556105,  0.25      ],
                          [ 0.55778052,  0.38443895,  0.25      ],
                          [ 0.55778052,  0.5       ,  0.25      ],
                          [ 0.55778052,  0.61556105,  0.25      ],
                          [ 0.67334157,  0.38443895,  0.25      ],
                          [ 0.67334157,  0.5       ,  0.25      ],
                          [ 0.67334157,  0.61556105,  0.25      ],
                          [ 0.38443895,  0.44221948,  0.75      ],
                          [ 0.38443895,  0.55778052,  0.75      ],
                          [ 0.5       ,  0.44221948,  0.75      ],
                          [ 0.5       ,  0.55778052,  0.75      ],
                          [ 0.61556105,  0.44221948,  0.75      ],
                          [ 0.61556105,  0.55778052,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]


