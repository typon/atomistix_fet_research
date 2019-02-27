# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.7819, 0.0]*Angstrom
vector_c = [0.0, 0.0, 49.9202168831]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen,
            Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen, Silicon, Hydrogen,
            Hydrogen, Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.4029292 ,  0.00497616],
                          [ 0.43654296,  0.52279321,  0.0192311 ],
                          [ 0.56345704,  0.52279321,  0.0192311 ],
                          [ 0.39660435,  0.55148439,  0.0192311 ],
                          [ 0.60339565,  0.55148439,  0.0192311 ],
                          [ 0.5       ,  0.56837962,  0.0192311 ],
                          [ 0.5       ,  0.4029292 ,  0.0334857 ],
                          [ 0.5       ,  0.5970708 ,  0.04343801],
                          [ 0.5       ,  0.43162038,  0.05769261],
                          [ 0.39660435,  0.44851561,  0.05769261],
                          [ 0.60339565,  0.44851561,  0.05769261],
                          [ 0.43654296,  0.47720679,  0.05769261],
                          [ 0.56345704,  0.47720679,  0.05769261],
                          [ 0.5       ,  0.5970708 ,  0.07194721],
                          [ 0.5       ,  0.4029292 ,  0.08189952],
                          [ 0.43654296,  0.52279321,  0.09615412],
                          [ 0.56345704,  0.52279321,  0.09615412],
                          [ 0.39660435,  0.55148439,  0.09615412],
                          [ 0.60339565,  0.55148439,  0.09615412],
                          [ 0.5       ,  0.56837962,  0.09615412],
                          [ 0.5       ,  0.4029292 ,  0.11040871],
                          [ 0.5       ,  0.5970708 ,  0.12036104],
                          [ 0.5       ,  0.43162038,  0.13461563],
                          [ 0.39660435,  0.44851561,  0.13461563],
                          [ 0.60339565,  0.44851561,  0.13461563],
                          [ 0.43654296,  0.47720679,  0.13461563],
                          [ 0.56345704,  0.47720679,  0.13461563],
                          [ 0.5       ,  0.5970708 ,  0.14887023],
                          [ 0.5       ,  0.4029292 ,  0.15882254],
                          [ 0.43654296,  0.52279321,  0.17307714],
                          [ 0.56345704,  0.52279321,  0.17307714],
                          [ 0.39660435,  0.55148439,  0.17307714],
                          [ 0.60339565,  0.55148439,  0.17307714],
                          [ 0.5       ,  0.56837962,  0.17307714],
                          [ 0.5       ,  0.4029292 ,  0.18733174],
                          [ 0.5       ,  0.5970708 ,  0.19728405],
                          [ 0.5       ,  0.43162038,  0.21153866],
                          [ 0.39660435,  0.44851561,  0.21153866],
                          [ 0.60339565,  0.44851561,  0.21153866],
                          [ 0.43654296,  0.47720679,  0.21153866],
                          [ 0.56345704,  0.47720679,  0.21153866],
                          [ 0.5       ,  0.5970708 ,  0.22579326],
                          [ 0.5       ,  0.4029292 ,  0.23574557],
                          [ 0.43654296,  0.52279321,  0.25000017],
                          [ 0.56345704,  0.52279321,  0.25000017],
                          [ 0.39660435,  0.55148439,  0.25000017],
                          [ 0.60339565,  0.55148439,  0.25000017],
                          [ 0.5       ,  0.56837962,  0.25000017],
                          [ 0.5       ,  0.4029292 ,  0.26425477],
                          [ 0.5       ,  0.5970708 ,  0.27420708],
                          [ 0.5       ,  0.43162038,  0.28846168],
                          [ 0.39660435,  0.44851561,  0.28846168],
                          [ 0.60339565,  0.44851561,  0.28846168],
                          [ 0.43654296,  0.47720679,  0.28846168],
                          [ 0.56345704,  0.47720679,  0.28846168],
                          [ 0.5       ,  0.5970708 ,  0.30271628],
                          [ 0.5       ,  0.4029292 ,  0.3126686 ],
                          [ 0.43654296,  0.52279321,  0.3269232 ],
                          [ 0.56345704,  0.52279321,  0.3269232 ],
                          [ 0.39660435,  0.55148439,  0.3269232 ],
                          [ 0.60339565,  0.55148439,  0.3269232 ],
                          [ 0.5       ,  0.56837962,  0.3269232 ],
                          [ 0.5       ,  0.4029292 ,  0.3411778 ],
                          [ 0.5       ,  0.5970708 ,  0.35113011],
                          [ 0.5       ,  0.43162038,  0.36538471],
                          [ 0.39660435,  0.44851561,  0.36538471],
                          [ 0.60339565,  0.44851561,  0.36538471],
                          [ 0.43654296,  0.47720679,  0.36538471],
                          [ 0.56345704,  0.47720679,  0.36538471],
                          [ 0.5       ,  0.5970708 ,  0.3796393 ],
                          [ 0.5       ,  0.4029292 ,  0.38959162],
                          [ 0.43654296,  0.52279321,  0.40384621],
                          [ 0.56345704,  0.52279321,  0.40384621],
                          [ 0.39660435,  0.55148439,  0.40384621],
                          [ 0.60339565,  0.55148439,  0.40384621],
                          [ 0.5       ,  0.56837962,  0.40384621],
                          [ 0.5       ,  0.4029292 ,  0.41810082],
                          [ 0.5       ,  0.5970708 ,  0.42805313],
                          [ 0.5       ,  0.43162038,  0.44230773],
                          [ 0.39660435,  0.44851561,  0.44230773],
                          [ 0.60339565,  0.44851561,  0.44230773],
                          [ 0.43654296,  0.47720679,  0.44230773],
                          [ 0.56345704,  0.47720679,  0.44230773],
                          [ 0.5       ,  0.5970708 ,  0.45656233],
                          [ 0.5       ,  0.4029292 ,  0.46651464],
                          [ 0.43654296,  0.52279321,  0.48076924],
                          [ 0.56345704,  0.52279321,  0.48076924],
                          [ 0.39660435,  0.55148439,  0.48076924],
                          [ 0.60339565,  0.55148439,  0.48076924],
                          [ 0.5       ,  0.56837962,  0.48076924],
                          [ 0.5       ,  0.4029292 ,  0.49502384],
                          [ 0.5       ,  0.5970708 ,  0.50497616],
                          [ 0.5       ,  0.43162038,  0.51923076],
                          [ 0.39660435,  0.44851561,  0.51923076],
                          [ 0.60339565,  0.44851561,  0.51923076],
                          [ 0.43654296,  0.47720679,  0.51923076],
                          [ 0.56345704,  0.47720679,  0.51923076],
                          [ 0.5       ,  0.5970708 ,  0.53348536],
                          [ 0.5       ,  0.4029292 ,  0.54343767],
                          [ 0.43654296,  0.52279321,  0.55769227],
                          [ 0.56345704,  0.52279321,  0.55769227],
                          [ 0.39660435,  0.55148439,  0.55769227],
                          [ 0.60339565,  0.55148439,  0.55769227],
                          [ 0.5       ,  0.56837962,  0.55769227],
                          [ 0.5       ,  0.4029292 ,  0.57194687],
                          [ 0.5       ,  0.5970708 ,  0.58189918],
                          [ 0.5       ,  0.43162038,  0.59615378],
                          [ 0.39660435,  0.44851561,  0.59615378],
                          [ 0.60339565,  0.44851561,  0.59615378],
                          [ 0.43654296,  0.47720679,  0.59615378],
                          [ 0.56345704,  0.47720679,  0.59615378],
                          [ 0.5       ,  0.5970708 ,  0.61040838],
                          [ 0.5       ,  0.4029292 ,  0.6203607 ],
                          [ 0.43654296,  0.52279321,  0.63461529],
                          [ 0.56345704,  0.52279321,  0.63461529],
                          [ 0.39660435,  0.55148439,  0.63461529],
                          [ 0.60339565,  0.55148439,  0.63461529],
                          [ 0.5       ,  0.56837962,  0.63461529],
                          [ 0.5       ,  0.4029292 ,  0.64886989],
                          [ 0.5       ,  0.5970708 ,  0.6588222 ],
                          [ 0.5       ,  0.43162038,  0.6730768 ],
                          [ 0.39660435,  0.44851561,  0.6730768 ],
                          [ 0.60339565,  0.44851561,  0.6730768 ],
                          [ 0.43654296,  0.47720679,  0.6730768 ],
                          [ 0.56345704,  0.47720679,  0.6730768 ],
                          [ 0.5       ,  0.5970708 ,  0.6873314 ],
                          [ 0.5       ,  0.4029292 ,  0.69728372],
                          [ 0.43654296,  0.52279321,  0.71153832],
                          [ 0.56345704,  0.52279321,  0.71153832],
                          [ 0.39660435,  0.55148439,  0.71153832],
                          [ 0.60339565,  0.55148439,  0.71153832],
                          [ 0.5       ,  0.56837962,  0.71153832],
                          [ 0.5       ,  0.4029292 ,  0.72579292],
                          [ 0.5       ,  0.5970708 ,  0.73574523],
                          [ 0.5       ,  0.43162038,  0.74999983],
                          [ 0.39660435,  0.44851561,  0.74999983],
                          [ 0.60339565,  0.44851561,  0.74999983],
                          [ 0.43654296,  0.47720679,  0.74999983],
                          [ 0.56345704,  0.47720679,  0.74999983],
                          [ 0.5       ,  0.5970708 ,  0.76425443],
                          [ 0.5       ,  0.4029292 ,  0.77420674],
                          [ 0.43654296,  0.52279321,  0.78846134],
                          [ 0.56345704,  0.52279321,  0.78846134],
                          [ 0.39660435,  0.55148439,  0.78846134],
                          [ 0.60339565,  0.55148439,  0.78846134],
                          [ 0.5       ,  0.56837962,  0.78846134],
                          [ 0.5       ,  0.4029292 ,  0.80271595],
                          [ 0.5       ,  0.5970708 ,  0.81266826],
                          [ 0.5       ,  0.43162038,  0.82692286],
                          [ 0.39660435,  0.44851561,  0.82692286],
                          [ 0.60339565,  0.44851561,  0.82692286],
                          [ 0.43654296,  0.47720679,  0.82692286],
                          [ 0.56345704,  0.47720679,  0.82692286],
                          [ 0.5       ,  0.5970708 ,  0.84117746],
                          [ 0.5       ,  0.4029292 ,  0.85112977],
                          [ 0.43654296,  0.52279321,  0.86538437],
                          [ 0.56345704,  0.52279321,  0.86538437],
                          [ 0.39660435,  0.55148439,  0.86538437],
                          [ 0.60339565,  0.55148439,  0.86538437],
                          [ 0.5       ,  0.56837962,  0.86538437],
                          [ 0.5       ,  0.4029292 ,  0.87963896],
                          [ 0.5       ,  0.5970708 ,  0.88959129],
                          [ 0.5       ,  0.43162038,  0.90384588],
                          [ 0.39660435,  0.44851561,  0.90384588],
                          [ 0.60339565,  0.44851561,  0.90384588],
                          [ 0.43654296,  0.47720679,  0.90384588],
                          [ 0.56345704,  0.47720679,  0.90384588],
                          [ 0.5       ,  0.5970708 ,  0.91810048],
                          [ 0.5       ,  0.4029292 ,  0.92805279],
                          [ 0.43654296,  0.52279321,  0.94230739],
                          [ 0.56345704,  0.52279321,  0.94230739],
                          [ 0.39660435,  0.55148439,  0.94230739],
                          [ 0.60339565,  0.55148439,  0.94230739],
                          [ 0.5       ,  0.56837962,  0.94230739],
                          [ 0.5       ,  0.4029292 ,  0.95656199],
                          [ 0.5       ,  0.5970708 ,  0.9665143 ],
                          [ 0.5       ,  0.43162038,  0.9807689 ],
                          [ 0.39660435,  0.44851561,  0.9807689 ],
                          [ 0.60339565,  0.44851561,  0.9807689 ],
                          [ 0.43654296,  0.47720679,  0.9807689 ],
                          [ 0.56345704,  0.47720679,  0.9807689 ],
                          [ 0.5       ,  0.5970708 ,  0.99502384]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 0.99997862*Angstrom, xmax = -2.13799999997e-05*Angstrom,
    ymin = 0.99999703*Angstrom, ymax = 28.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = -2.13799999997e-05*Angstrom, xmax = 30.25682138*Angstrom,
    ymin = 28.78190297*Angstrom, ymax = 29.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

metallic_region_2 = BoxRegion(
    0.0*Volt,
    xmin = 29.25682138*Angstrom, xmax = 30.25682138*Angstrom,
    ymin = 0.99999703*Angstrom, ymax = 28.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

metallic_region_3 = BoxRegion(
    0.0*Volt,
    xmin = -2.13799999997e-05*Angstrom, xmax = 30.25682138*Angstrom,
    ymin = 0.99999703*Angstrom, ymax = -2.9700000006e-06*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    25.0,
    xmin = 10.99997862*Angstrom, xmax = 0.99997862*Angstrom,
    ymin = 10.99999703*Angstrom, ymax = 18.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_1 = BoxRegion(
    25.0,
    xmin = 10.99997862*Angstrom, xmax = 19.25682138*Angstrom,
    ymin = 18.78190297*Angstrom, ymax = 28.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_2 = BoxRegion(
    25.0,
    xmin = 19.25682138*Angstrom, xmax = 29.25682138*Angstrom,
    ymin = 10.99999703*Angstrom, ymax = 18.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_3 = BoxRegion(
    25.0,
    xmin = 10.99997862*Angstrom, xmax = 19.25682138*Angstrom,
    ymin = 10.99999703*Angstrom, ymax = 0.99999703*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_4 = BoxRegion(
    25.0,
    xmin = 10.99997862*Angstrom, xmax = 0.99997862*Angstrom,
    ymin = 10.99999703*Angstrom, ymax = 0.99999703*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_5 = BoxRegion(
    25.0,
    xmin = 10.99997862*Angstrom, xmax = 0.99997862*Angstrom,
    ymin = 18.78190297*Angstrom, ymax = 28.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_6 = BoxRegion(
    25.0,
    xmin = 19.25682138*Angstrom, xmax = 29.25682138*Angstrom,
    ymin = 18.78190297*Angstrom, ymax = 28.78190297*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_region_7 = BoxRegion(
    25.0,
    xmin = 19.25682138*Angstrom, xmax = 29.25682138*Angstrom,
    ymin = 10.99999703*Angstrom, ymax = 0.99999703*Angstrom,
    zmin = 9.83590303*Angstrom, zmax = 39.83590303*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


