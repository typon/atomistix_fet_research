# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 54.306]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Silicon, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Silicon, Silicon, Silicon, Silicon, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Silicon, Silicon, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.5       ,  0.5       ,  0.00463275],
                          [ 0.5       ,  0.39660435,  0.01389824],
                          [ 0.5       ,  0.60339565,  0.01389824],
                          [ 0.5       ,  0.43654296,  0.02963275],
                          [ 0.5       ,  0.56345704,  0.02963275],
                          [ 0.39660435,  0.43654296,  0.03889824],
                          [ 0.60339565,  0.43654296,  0.03889824],
                          [ 0.39660435,  0.56345704,  0.03889824],
                          [ 0.60339565,  0.56345704,  0.03889824],
                          [ 0.43654296,  0.43654296,  0.05463275],
                          [ 0.56345704,  0.43654296,  0.05463275],
                          [ 0.43654296,  0.56345704,  0.05463275],
                          [ 0.56345704,  0.56345704,  0.05463275],
                          [ 0.43654296,  0.39660435,  0.07036725],
                          [ 0.56345704,  0.39660435,  0.07036725],
                          [ 0.43654296,  0.60339565,  0.07036725],
                          [ 0.56345704,  0.60339565,  0.07036725],
                          [ 0.43654296,  0.5       ,  0.07963275],
                          [ 0.56345704,  0.5       ,  0.07963275],
                          [ 0.39660435,  0.5       ,  0.09536725],
                          [ 0.60339565,  0.5       ,  0.09536725],
                          [ 0.5       ,  0.5       ,  0.10463275],
                          [ 0.5       ,  0.39660435,  0.11389824],
                          [ 0.5       ,  0.60339565,  0.11389824],
                          [ 0.5       ,  0.43654296,  0.12963275],
                          [ 0.5       ,  0.56345704,  0.12963275],
                          [ 0.39660435,  0.43654296,  0.13889824],
                          [ 0.60339565,  0.43654296,  0.13889824],
                          [ 0.39660435,  0.56345704,  0.13889824],
                          [ 0.60339565,  0.56345704,  0.13889824],
                          [ 0.43654296,  0.43654296,  0.15463275],
                          [ 0.56345704,  0.43654296,  0.15463275],
                          [ 0.43654296,  0.56345704,  0.15463275],
                          [ 0.56345704,  0.56345704,  0.15463275],
                          [ 0.43654296,  0.39660435,  0.17036725],
                          [ 0.56345704,  0.39660435,  0.17036725],
                          [ 0.43654296,  0.60339565,  0.17036725],
                          [ 0.56345704,  0.60339565,  0.17036725],
                          [ 0.43654296,  0.5       ,  0.17963275],
                          [ 0.56345704,  0.5       ,  0.17963275],
                          [ 0.39660435,  0.5       ,  0.19536725],
                          [ 0.60339565,  0.5       ,  0.19536725],
                          [ 0.5       ,  0.5       ,  0.20463275],
                          [ 0.5       ,  0.39660435,  0.21389824],
                          [ 0.5       ,  0.60339565,  0.21389824],
                          [ 0.5       ,  0.43654296,  0.22963275],
                          [ 0.5       ,  0.56345704,  0.22963275],
                          [ 0.39660435,  0.43654296,  0.23889824],
                          [ 0.60339565,  0.43654296,  0.23889824],
                          [ 0.39660435,  0.56345704,  0.23889824],
                          [ 0.60339565,  0.56345704,  0.23889824],
                          [ 0.43654296,  0.43654296,  0.25463275],
                          [ 0.56345704,  0.43654296,  0.25463275],
                          [ 0.43654296,  0.56345704,  0.25463275],
                          [ 0.56345704,  0.56345704,  0.25463275],
                          [ 0.43654296,  0.39660435,  0.27036725],
                          [ 0.56345704,  0.39660435,  0.27036725],
                          [ 0.43654296,  0.60339565,  0.27036725],
                          [ 0.56345704,  0.60339565,  0.27036725],
                          [ 0.43654296,  0.5       ,  0.27963275],
                          [ 0.56345704,  0.5       ,  0.27963275],
                          [ 0.39660435,  0.5       ,  0.29536725],
                          [ 0.60339565,  0.5       ,  0.29536725],
                          [ 0.5       ,  0.5       ,  0.30463275],
                          [ 0.5       ,  0.39660435,  0.31389824],
                          [ 0.5       ,  0.60339565,  0.31389824],
                          [ 0.5       ,  0.43654296,  0.32963275],
                          [ 0.5       ,  0.56345704,  0.32963275],
                          [ 0.39660435,  0.43654296,  0.33889824],
                          [ 0.60339565,  0.43654296,  0.33889824],
                          [ 0.39660435,  0.56345704,  0.33889824],
                          [ 0.60339565,  0.56345704,  0.33889824],
                          [ 0.43654296,  0.43654296,  0.35463275],
                          [ 0.56345704,  0.43654296,  0.35463275],
                          [ 0.43654296,  0.56345704,  0.35463275],
                          [ 0.56345704,  0.56345704,  0.35463275],
                          [ 0.43654296,  0.39660435,  0.37036725],
                          [ 0.56345704,  0.39660435,  0.37036725],
                          [ 0.43654296,  0.60339565,  0.37036725],
                          [ 0.56345704,  0.60339565,  0.37036725],
                          [ 0.43654296,  0.5       ,  0.37963275],
                          [ 0.56345704,  0.5       ,  0.37963275],
                          [ 0.39660435,  0.5       ,  0.39536725],
                          [ 0.60339565,  0.5       ,  0.39536725],
                          [ 0.5       ,  0.5       ,  0.40463275],
                          [ 0.5       ,  0.39660435,  0.41389824],
                          [ 0.5       ,  0.60339565,  0.41389824],
                          [ 0.5       ,  0.43654296,  0.42963275],
                          [ 0.5       ,  0.56345704,  0.42963275],
                          [ 0.39660435,  0.43654296,  0.43889824],
                          [ 0.60339565,  0.43654296,  0.43889824],
                          [ 0.39660435,  0.56345704,  0.43889824],
                          [ 0.60339565,  0.56345704,  0.43889824],
                          [ 0.43654296,  0.43654296,  0.45463275],
                          [ 0.56345704,  0.43654296,  0.45463275],
                          [ 0.43654296,  0.56345704,  0.45463275],
                          [ 0.56345704,  0.56345704,  0.45463275],
                          [ 0.43654296,  0.39660435,  0.47036725],
                          [ 0.56345704,  0.39660435,  0.47036725],
                          [ 0.43654296,  0.60339565,  0.47036725],
                          [ 0.56345704,  0.60339565,  0.47036725],
                          [ 0.43654296,  0.5       ,  0.47963275],
                          [ 0.56345704,  0.5       ,  0.47963275],
                          [ 0.39660435,  0.5       ,  0.49536725],
                          [ 0.60339565,  0.5       ,  0.49536725],
                          [ 0.5       ,  0.5       ,  0.50463275],
                          [ 0.5       ,  0.39660435,  0.51389824],
                          [ 0.5       ,  0.60339565,  0.51389824],
                          [ 0.5       ,  0.43654296,  0.52963275],
                          [ 0.5       ,  0.56345704,  0.52963275],
                          [ 0.39660435,  0.43654296,  0.53889824],
                          [ 0.60339565,  0.43654296,  0.53889824],
                          [ 0.39660435,  0.56345704,  0.53889824],
                          [ 0.60339565,  0.56345704,  0.53889824],
                          [ 0.43654296,  0.43654296,  0.55463275],
                          [ 0.56345704,  0.43654296,  0.55463275],
                          [ 0.43654296,  0.56345704,  0.55463275],
                          [ 0.56345704,  0.56345704,  0.55463275],
                          [ 0.43654296,  0.39660435,  0.57036725],
                          [ 0.56345704,  0.39660435,  0.57036725],
                          [ 0.43654296,  0.60339565,  0.57036725],
                          [ 0.56345704,  0.60339565,  0.57036725],
                          [ 0.43654296,  0.5       ,  0.57963275],
                          [ 0.56345704,  0.5       ,  0.57963275],
                          [ 0.39660435,  0.5       ,  0.59536725],
                          [ 0.60339565,  0.5       ,  0.59536725],
                          [ 0.5       ,  0.5       ,  0.60463275],
                          [ 0.5       ,  0.39660435,  0.61389824],
                          [ 0.5       ,  0.60339565,  0.61389824],
                          [ 0.5       ,  0.43654296,  0.62963275],
                          [ 0.5       ,  0.56345704,  0.62963275],
                          [ 0.39660435,  0.43654296,  0.63889824],
                          [ 0.60339565,  0.43654296,  0.63889824],
                          [ 0.39660435,  0.56345704,  0.63889824],
                          [ 0.60339565,  0.56345704,  0.63889824],
                          [ 0.43654296,  0.43654296,  0.65463275],
                          [ 0.56345704,  0.43654296,  0.65463275],
                          [ 0.43654296,  0.56345704,  0.65463275],
                          [ 0.56345704,  0.56345704,  0.65463275],
                          [ 0.43654296,  0.39660435,  0.67036725],
                          [ 0.56345704,  0.39660435,  0.67036725],
                          [ 0.43654296,  0.60339565,  0.67036725],
                          [ 0.56345704,  0.60339565,  0.67036725],
                          [ 0.43654296,  0.5       ,  0.67963275],
                          [ 0.56345704,  0.5       ,  0.67963275],
                          [ 0.39660435,  0.5       ,  0.69536725],
                          [ 0.60339565,  0.5       ,  0.69536725],
                          [ 0.5       ,  0.5       ,  0.70463275],
                          [ 0.5       ,  0.39660435,  0.71389824],
                          [ 0.5       ,  0.60339565,  0.71389824],
                          [ 0.5       ,  0.43654296,  0.72963275],
                          [ 0.5       ,  0.56345704,  0.72963275],
                          [ 0.39660435,  0.43654296,  0.73889824],
                          [ 0.60339565,  0.43654296,  0.73889824],
                          [ 0.39660435,  0.56345704,  0.73889824],
                          [ 0.60339565,  0.56345704,  0.73889824],
                          [ 0.43654296,  0.43654296,  0.75463275],
                          [ 0.56345704,  0.43654296,  0.75463275],
                          [ 0.43654296,  0.56345704,  0.75463275],
                          [ 0.56345704,  0.56345704,  0.75463275],
                          [ 0.43654296,  0.39660435,  0.77036725],
                          [ 0.56345704,  0.39660435,  0.77036725],
                          [ 0.43654296,  0.60339565,  0.77036725],
                          [ 0.56345704,  0.60339565,  0.77036725],
                          [ 0.43654296,  0.5       ,  0.77963275],
                          [ 0.56345704,  0.5       ,  0.77963275],
                          [ 0.39660435,  0.5       ,  0.79536725],
                          [ 0.60339565,  0.5       ,  0.79536725],
                          [ 0.5       ,  0.5       ,  0.80463275],
                          [ 0.5       ,  0.39660435,  0.81389824],
                          [ 0.5       ,  0.60339565,  0.81389824],
                          [ 0.5       ,  0.43654296,  0.82963275],
                          [ 0.5       ,  0.56345704,  0.82963275],
                          [ 0.39660435,  0.43654296,  0.83889824],
                          [ 0.60339565,  0.43654296,  0.83889824],
                          [ 0.39660435,  0.56345704,  0.83889824],
                          [ 0.60339565,  0.56345704,  0.83889824],
                          [ 0.43654296,  0.43654296,  0.85463275],
                          [ 0.56345704,  0.43654296,  0.85463275],
                          [ 0.43654296,  0.56345704,  0.85463275],
                          [ 0.56345704,  0.56345704,  0.85463275],
                          [ 0.43654296,  0.39660435,  0.87036725],
                          [ 0.56345704,  0.39660435,  0.87036725],
                          [ 0.43654296,  0.60339565,  0.87036725],
                          [ 0.56345704,  0.60339565,  0.87036725],
                          [ 0.43654296,  0.5       ,  0.87963275],
                          [ 0.56345704,  0.5       ,  0.87963275],
                          [ 0.39660435,  0.5       ,  0.89536725],
                          [ 0.60339565,  0.5       ,  0.89536725],
                          [ 0.5       ,  0.5       ,  0.90463275],
                          [ 0.5       ,  0.39660435,  0.91389824],
                          [ 0.5       ,  0.60339565,  0.91389824],
                          [ 0.5       ,  0.43654296,  0.92963275],
                          [ 0.5       ,  0.56345704,  0.92963275],
                          [ 0.39660435,  0.43654296,  0.93889824],
                          [ 0.60339565,  0.43654296,  0.93889824],
                          [ 0.39660435,  0.56345704,  0.93889824],
                          [ 0.60339565,  0.56345704,  0.93889824],
                          [ 0.43654296,  0.43654296,  0.95463275],
                          [ 0.56345704,  0.43654296,  0.95463275],
                          [ 0.43654296,  0.56345704,  0.95463275],
                          [ 0.56345704,  0.56345704,  0.95463275],
                          [ 0.43654296,  0.39660435,  0.97036725],
                          [ 0.56345704,  0.39660435,  0.97036725],
                          [ 0.43654296,  0.60339565,  0.97036725],
                          [ 0.56345704,  0.60339565,  0.97036725],
                          [ 0.43654296,  0.5       ,  0.97963275],
                          [ 0.56345704,  0.5       ,  0.97963275],
                          [ 0.39660435,  0.5       ,  0.99536725],
                          [ 0.60339565,  0.5       ,  0.99536725]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 0.99997859*Angstrom, xmax = -2.14100000004e-05*Angstrom,
    ymin = 0.99997859*Angstrom, ymax = 29.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = -2.14100000004e-05*Angstrom, xmax = 30.25682141*Angstrom,
    ymin = 29.25682141*Angstrom, ymax = 30.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

metallic_region_2 = BoxRegion(
    0.0*Volt,
    xmin = 29.25682141*Angstrom, xmax = 30.25682141*Angstrom,
    ymin = 0.99997859*Angstrom, ymax = 29.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

metallic_region_3 = BoxRegion(
    0.0*Volt,
    xmin = -2.14100000004e-05*Angstrom, xmax = 30.25682141*Angstrom,
    ymin = 0.99997859*Angstrom, ymax = -2.14100000004e-05*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    25.0,
    xmin = 10.99997859*Angstrom, xmax = 0.99997859*Angstrom,
    ymin = 10.99997859*Angstrom, ymax = 19.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_1 = BoxRegion(
    25.0,
    xmin = 10.99997859*Angstrom, xmax = 19.25682141*Angstrom,
    ymin = 19.25682141*Angstrom, ymax = 29.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_2 = BoxRegion(
    25.0,
    xmin = 19.25682141*Angstrom, xmax = 29.25682141*Angstrom,
    ymin = 10.99997859*Angstrom, ymax = 19.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_3 = BoxRegion(
    25.0,
    xmin = 10.99997859*Angstrom, xmax = 19.25682141*Angstrom,
    ymin = 10.99997859*Angstrom, ymax = 0.99997859*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_4 = BoxRegion(
    25.0,
    xmin = 10.99997859*Angstrom, xmax = 0.99997859*Angstrom,
    ymin = 10.99997859*Angstrom, ymax = 0.99997859*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_5 = BoxRegion(
    25.0,
    xmin = 10.99997859*Angstrom, xmax = 0.99997859*Angstrom,
    ymin = 19.25682141*Angstrom, ymax = 29.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_6 = BoxRegion(
    25.0,
    xmin = 19.25682141*Angstrom, xmax = 29.25682141*Angstrom,
    ymin = 19.25682141*Angstrom, ymax = 29.25682141*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_region_7 = BoxRegion(
    25.0,
    xmin = 19.25682141*Angstrom, xmax = 29.25682141*Angstrom,
    ymin = 10.99997859*Angstrom, ymax = 0.99997859*Angstrom,
    zmin = 12.027207*Angstrom, zmax = 42.027207*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


