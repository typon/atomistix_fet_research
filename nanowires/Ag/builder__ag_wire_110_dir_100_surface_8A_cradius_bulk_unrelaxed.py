# Set up lattice
lattice = SimpleTetragonal(29.0191329621*Angstrom, 5.77805235179*Angstrom)

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
            Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.71118998,  0.74888977,  0.125     ],
                          [ 0.71118998,  0.64933386,  0.125     ],
                          [ 0.71118998,  0.54977795,  0.125     ],
                          [ 0.71118998,  0.45022205,  0.125     ],
                          [ 0.71118998,  0.35066614,  0.125     ],
                          [ 0.71118998,  0.25111023,  0.125     ],
                          [ 0.57039666,  0.74888977,  0.125     ],
                          [ 0.64079332,  0.79866773,  0.375     ],
                          [ 0.57039666,  0.64933386,  0.125     ],
                          [ 0.64079332,  0.69911182,  0.375     ],
                          [ 0.71118998,  0.74888977,  0.625     ],
                          [ 0.57039666,  0.54977795,  0.125     ],
                          [ 0.64079332,  0.59955591,  0.375     ],
                          [ 0.71118998,  0.64933386,  0.625     ],
                          [ 0.57039666,  0.45022205,  0.125     ],
                          [ 0.64079332,  0.5       ,  0.375     ],
                          [ 0.71118998,  0.54977795,  0.625     ],
                          [ 0.57039666,  0.35066614,  0.125     ],
                          [ 0.64079332,  0.40044409,  0.375     ],
                          [ 0.71118998,  0.45022205,  0.625     ],
                          [ 0.57039666,  0.25111023,  0.125     ],
                          [ 0.64079332,  0.30088818,  0.375     ],
                          [ 0.71118998,  0.35066614,  0.625     ],
                          [ 0.64079332,  0.20133227,  0.375     ],
                          [ 0.71118998,  0.25111023,  0.625     ],
                          [ 0.42960334,  0.74888977,  0.125     ],
                          [ 0.5       ,  0.79866773,  0.375     ],
                          [ 0.42960334,  0.64933386,  0.125     ],
                          [ 0.5       ,  0.69911182,  0.375     ],
                          [ 0.57039666,  0.74888977,  0.625     ],
                          [ 0.42960334,  0.54977795,  0.125     ],
                          [ 0.5       ,  0.59955591,  0.375     ],
                          [ 0.57039666,  0.64933386,  0.625     ],
                          [ 0.64079332,  0.69911182,  0.875     ],
                          [ 0.42960334,  0.45022205,  0.125     ],
                          [ 0.5       ,  0.5       ,  0.375     ],
                          [ 0.57039666,  0.54977795,  0.625     ],
                          [ 0.64079332,  0.59955591,  0.875     ],
                          [ 0.42960334,  0.35066614,  0.125     ],
                          [ 0.5       ,  0.40044409,  0.375     ],
                          [ 0.57039666,  0.45022205,  0.625     ],
                          [ 0.64079332,  0.5       ,  0.875     ],
                          [ 0.42960334,  0.25111023,  0.125     ],
                          [ 0.5       ,  0.30088818,  0.375     ],
                          [ 0.57039666,  0.35066614,  0.625     ],
                          [ 0.64079332,  0.40044409,  0.875     ],
                          [ 0.5       ,  0.20133227,  0.375     ],
                          [ 0.57039666,  0.25111023,  0.625     ],
                          [ 0.64079332,  0.30088818,  0.875     ],
                          [ 0.28881002,  0.74888977,  0.125     ],
                          [ 0.35920668,  0.79866773,  0.375     ],
                          [ 0.28881002,  0.64933386,  0.125     ],
                          [ 0.35920668,  0.69911182,  0.375     ],
                          [ 0.42960334,  0.74888977,  0.625     ],
                          [ 0.28881002,  0.54977795,  0.125     ],
                          [ 0.35920668,  0.59955591,  0.375     ],
                          [ 0.42960334,  0.64933386,  0.625     ],
                          [ 0.5       ,  0.69911182,  0.875     ],
                          [ 0.28881002,  0.45022205,  0.125     ],
                          [ 0.35920668,  0.5       ,  0.375     ],
                          [ 0.42960334,  0.54977795,  0.625     ],
                          [ 0.5       ,  0.59955591,  0.875     ],
                          [ 0.28881002,  0.35066614,  0.125     ],
                          [ 0.35920668,  0.40044409,  0.375     ],
                          [ 0.42960334,  0.45022205,  0.625     ],
                          [ 0.5       ,  0.5       ,  0.875     ],
                          [ 0.28881002,  0.25111023,  0.125     ],
                          [ 0.35920668,  0.30088818,  0.375     ],
                          [ 0.42960334,  0.35066614,  0.625     ],
                          [ 0.5       ,  0.40044409,  0.875     ],
                          [ 0.35920668,  0.20133227,  0.375     ],
                          [ 0.42960334,  0.25111023,  0.625     ],
                          [ 0.5       ,  0.30088818,  0.875     ],
                          [ 0.28881002,  0.74888977,  0.625     ],
                          [ 0.28881002,  0.64933386,  0.625     ],
                          [ 0.35920668,  0.69911182,  0.875     ],
                          [ 0.28881002,  0.54977795,  0.625     ],
                          [ 0.35920668,  0.59955591,  0.875     ],
                          [ 0.28881002,  0.45022205,  0.625     ],
                          [ 0.35920668,  0.5       ,  0.875     ],
                          [ 0.28881002,  0.35066614,  0.625     ],
                          [ 0.35920668,  0.40044409,  0.875     ],
                          [ 0.28881002,  0.25111023,  0.625     ],
                          [ 0.35920668,  0.30088818,  0.875     ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]

