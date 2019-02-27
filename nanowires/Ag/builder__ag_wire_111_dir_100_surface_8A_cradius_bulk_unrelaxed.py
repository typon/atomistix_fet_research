# Set up lattice
lattice = SimpleTetragonal(28.7454475049*Angstrom, 7.07663998448*Angstrom)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.821274  ,  0.46593948,  0.16666667],
                          [ 0.79526171,  0.36886028,  0.16666667],
                          [ 0.7502071 ,  0.53700638,  0.16666667],
                          [ 0.79123759,  0.57803688,  0.5       ],
                          [ 0.7241948 ,  0.43992718,  0.16666667],
                          [ 0.7652253 ,  0.48095768,  0.5       ],
                          [ 0.69818251,  0.34284798,  0.16666667],
                          [ 0.73921301,  0.38387848,  0.5       ],
                          [ 0.71320072,  0.28679928,  0.5       ],
                          [ 0.67914019,  0.60807329,  0.16666667],
                          [ 0.72017069,  0.64910378,  0.5       ],
                          [ 0.76120119,  0.69013428,  0.83333333],
                          [ 0.6531279 ,  0.51099409,  0.16666667],
                          [ 0.6941584 ,  0.55202459,  0.5       ],
                          [ 0.73518889,  0.59305508,  0.83333333],
                          [ 0.62711561,  0.41391489,  0.16666667],
                          [ 0.6681461 ,  0.45494539,  0.5       ],
                          [ 0.7091766 ,  0.49597588,  0.83333333],
                          [ 0.60110331,  0.31683569,  0.16666667],
                          [ 0.64213381,  0.35786619,  0.5       ],
                          [ 0.68316431,  0.39889669,  0.83333333],
                          [ 0.61612152,  0.26078699,  0.5       ],
                          [ 0.65715202,  0.30181749,  0.83333333],
                          [ 0.63113972,  0.20473829,  0.83333333],
                          [ 0.60807329,  0.67914019,  0.16666667],
                          [ 0.64910378,  0.72017069,  0.5       ],
                          [ 0.69013428,  0.76120119,  0.83333333],
                          [ 0.58206099,  0.58206099,  0.16666667],
                          [ 0.62309149,  0.62309149,  0.5       ],
                          [ 0.66412199,  0.66412199,  0.83333333],
                          [ 0.5560487 ,  0.4849818 ,  0.16666667],
                          [ 0.5970792 ,  0.52601229,  0.5       ],
                          [ 0.6381097 ,  0.56704279,  0.83333333],
                          [ 0.53003641,  0.3879026 ,  0.16666667],
                          [ 0.57106691,  0.42893309,  0.5       ],
                          [ 0.6120974 ,  0.46996359,  0.83333333],
                          [ 0.50402412,  0.2908234 ,  0.16666667],
                          [ 0.54505461,  0.3318539 ,  0.5       ],
                          [ 0.58608511,  0.37288439,  0.83333333],
                          [ 0.51904232,  0.2347747 ,  0.5       ],
                          [ 0.56007282,  0.2758052 ,  0.83333333],
                          [ 0.53406052,  0.178726  ,  0.83333333],
                          [ 0.53700638,  0.7502071 ,  0.16666667],
                          [ 0.57803688,  0.79123759,  0.5       ],
                          [ 0.51099409,  0.6531279 ,  0.16666667],
                          [ 0.55202459,  0.6941584 ,  0.5       ],
                          [ 0.59305508,  0.73518889,  0.83333333],
                          [ 0.4849818 ,  0.5560487 ,  0.16666667],
                          [ 0.52601229,  0.5970792 ,  0.5       ],
                          [ 0.56704279,  0.6381097 ,  0.83333333],
                          [ 0.4589695 ,  0.4589695 ,  0.16666667],
                          [ 0.5       ,  0.5       ,  0.5       ],
                          [ 0.5410305 ,  0.5410305 ,  0.83333333],
                          [ 0.43295721,  0.3618903 ,  0.16666667],
                          [ 0.47398771,  0.4029208 ,  0.5       ],
                          [ 0.5150182 ,  0.4439513 ,  0.83333333],
                          [ 0.40694492,  0.26481111,  0.16666667],
                          [ 0.44797541,  0.3058416 ,  0.5       ],
                          [ 0.48900591,  0.3468721 ,  0.83333333],
                          [ 0.42196312,  0.20876241,  0.5       ],
                          [ 0.46299362,  0.2497929 ,  0.83333333],
                          [ 0.46593948,  0.821274  ,  0.16666667],
                          [ 0.43992718,  0.7241948 ,  0.16666667],
                          [ 0.48095768,  0.7652253 ,  0.5       ],
                          [ 0.41391489,  0.62711561,  0.16666667],
                          [ 0.45494539,  0.6681461 ,  0.5       ],
                          [ 0.49597588,  0.7091766 ,  0.83333333],
                          [ 0.3879026 ,  0.53003641,  0.16666667],
                          [ 0.42893309,  0.57106691,  0.5       ],
                          [ 0.46996359,  0.6120974 ,  0.83333333],
                          [ 0.3618903 ,  0.43295721,  0.16666667],
                          [ 0.4029208 ,  0.47398771,  0.5       ],
                          [ 0.4439513 ,  0.5150182 ,  0.83333333],
                          [ 0.33587801,  0.33587801,  0.16666667],
                          [ 0.37690851,  0.37690851,  0.5       ],
                          [ 0.41793901,  0.41793901,  0.83333333],
                          [ 0.30986572,  0.23879881,  0.16666667],
                          [ 0.35089622,  0.27982931,  0.5       ],
                          [ 0.39192671,  0.32085981,  0.83333333],
                          [ 0.36886028,  0.79526171,  0.16666667],
                          [ 0.34284798,  0.69818251,  0.16666667],
                          [ 0.38387848,  0.73921301,  0.5       ],
                          [ 0.31683569,  0.60110331,  0.16666667],
                          [ 0.35786619,  0.64213381,  0.5       ],
                          [ 0.39889669,  0.68316431,  0.83333333],
                          [ 0.2908234 ,  0.50402412,  0.16666667],
                          [ 0.3318539 ,  0.54505461,  0.5       ],
                          [ 0.37288439,  0.58608511,  0.83333333],
                          [ 0.26481111,  0.40694492,  0.16666667],
                          [ 0.3058416 ,  0.44797541,  0.5       ],
                          [ 0.3468721 ,  0.48900591,  0.83333333],
                          [ 0.23879881,  0.30986572,  0.16666667],
                          [ 0.27982931,  0.35089622,  0.5       ],
                          [ 0.32085981,  0.39192671,  0.83333333],
                          [ 0.28679928,  0.71320072,  0.5       ],
                          [ 0.26078699,  0.61612152,  0.5       ],
                          [ 0.30181749,  0.65715202,  0.83333333],
                          [ 0.2347747 ,  0.51904232,  0.5       ],
                          [ 0.2758052 ,  0.56007282,  0.83333333],
                          [ 0.20876241,  0.42196312,  0.5       ],
                          [ 0.2497929 ,  0.46299362,  0.83333333],
                          [ 0.20473829,  0.63113972,  0.83333333],
                          [ 0.178726  ,  0.53406052,  0.83333333]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]
