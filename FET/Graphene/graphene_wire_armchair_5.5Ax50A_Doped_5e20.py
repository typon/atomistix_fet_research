# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.59233, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.5251601705]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon]

# Define coordinates
left_electrode_coordinates = [[ 12.        ,  14.18091461,   0.71043006],
                              [ 12.        ,  16.64191633,   0.71043006],
                              [ 12.        ,  12.00644646,   0.87586045],
                              [ 12.        ,  17.58588354,   1.25542972],
                              [ 12.        ,  12.95041368,   1.42086011],
                              [ 12.        ,  15.4114154 ,   1.42086011],
                              [ 12.        ,  12.95041368,   2.84172023],
                              [ 12.        ,  15.4114154 ,   2.84172023],
                              [ 12.        ,  17.58588354,   3.0071501 ],
                              [ 12.        ,  12.00644646,   3.3867199 ],
                              [ 12.        ,  14.18091461,   3.55214977],
                              [ 12.        ,  16.64191633,   3.55214977],
                              [ 12.        ,  14.18091461,   4.97300989],
                              [ 12.        ,  16.64191633,   4.97300989],
                              [ 12.        ,  12.00644646,   5.13844028],
                              [ 12.        ,  17.58588354,   5.51800955],
                              [ 12.        ,  12.95041368,   5.68343994],
                              [ 12.        ,  15.4114154 ,   5.68343994],
                              [ 12.        ,  12.95041368,   7.10430006],
                              [ 12.        ,  15.4114154 ,   7.10430006],
                              [ 12.        ,  17.58588354,   7.26973045],
                              [ 12.        ,  12.00644646,   7.64929972],
                              [ 12.        ,  14.18091461,   7.81473011],
                              [ 12.        ,  16.64191633,   7.81473011]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.59233, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.5251601705]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                            Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                            Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                            Hydrogen, Carbon, Carbon]

# Define coordinates
right_electrode_coordinates = [[ 12.        ,  14.18091461,   0.71043006],
                               [ 12.        ,  16.64191633,   0.71043006],
                               [ 12.        ,  12.00644646,   0.87586045],
                               [ 12.        ,  17.58588354,   1.25542972],
                               [ 12.        ,  12.95041368,   1.42086011],
                               [ 12.        ,  15.4114154 ,   1.42086011],
                               [ 12.        ,  12.95041368,   2.84172023],
                               [ 12.        ,  15.4114154 ,   2.84172023],
                               [ 12.        ,  17.58588354,   3.00715062],
                               [ 12.        ,  12.00644646,   3.38671989],
                               [ 12.        ,  14.18091461,   3.55215028],
                               [ 12.        ,  16.64191633,   3.55215028],
                               [ 12.        ,  14.18091461,   4.9730104 ],
                               [ 12.        ,  16.64191633,   4.9730104 ],
                               [ 12.        ,  12.00644646,   5.13844027],
                               [ 12.        ,  17.58588354,   5.51801007],
                               [ 12.        ,  12.95041368,   5.68343994],
                               [ 12.        ,  15.4114154 ,   5.68343994],
                               [ 12.        ,  12.95041368,   7.10430006],
                               [ 12.        ,  15.4114154 ,   7.10430006],
                               [ 12.        ,  17.58588354,   7.26973045],
                               [ 12.        ,  12.00644646,   7.64929972],
                               [ 12.        ,  14.18091461,   7.81473011],
                               [ 12.        ,  16.64191633,   7.81473011]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Central region
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.59233, 0.0]*Angstrom
vector_c = [0.0, 0.0, 51.15096]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon,
                           Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon,
                           Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen,
                           Hydrogen, Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen,
                           Carbon, Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon,
                           Carbon, Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon,
                           Carbon, Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon,
                           Carbon, Hydrogen, Hydrogen, Carbon, Carbon, Carbon, Carbon,
                           Hydrogen, Hydrogen, Carbon, Carbon]

# Define coordinates
central_region_coordinates = [[ 12.        ,  14.18091461,   0.71043006],
                              [ 12.        ,  16.64191633,   0.71043006],
                              [ 12.        ,  12.00644646,   0.87586045],
                              [ 12.        ,  17.58588354,   1.25542972],
                              [ 12.        ,  12.95041368,   1.42086011],
                              [ 12.        ,  15.4114154 ,   1.42086011],
                              [ 12.        ,  12.95041368,   2.84172023],
                              [ 12.        ,  15.4114154 ,   2.84172023],
                              [ 12.        ,  17.58588354,   3.0071501 ],
                              [ 12.        ,  12.00644646,   3.3867199 ],
                              [ 12.        ,  14.18091461,   3.55214977],
                              [ 12.        ,  16.64191633,   3.55214977],
                              [ 12.        ,  14.18091461,   4.97300989],
                              [ 12.        ,  16.64191633,   4.97300989],
                              [ 12.        ,  12.00644646,   5.13844028],
                              [ 12.        ,  17.58588354,   5.51800955],
                              [ 12.        ,  12.95041368,   5.68343994],
                              [ 12.        ,  15.4114154 ,   5.68343994],
                              [ 12.        ,  12.95041368,   7.10430006],
                              [ 12.        ,  15.4114154 ,   7.10430006],
                              [ 12.        ,  17.58588354,   7.26973045],
                              [ 12.        ,  12.00644646,   7.64929972],
                              [ 12.        ,  14.18091461,   7.81473011],
                              [ 12.        ,  16.64191633,   7.81473011],
                              [ 12.        ,  14.18091461,   9.23559023],
                              [ 12.        ,  16.64191633,   9.23559023],
                              [ 12.        ,  12.00644646,   9.4010201 ],
                              [ 12.        ,  17.58588354,   9.7805899 ],
                              [ 12.        ,  12.95041368,   9.94601977],
                              [ 12.        ,  15.4114154 ,   9.94601977],
                              [ 12.        ,  12.95041368,  11.36687989],
                              [ 12.        ,  15.4114154 ,  11.36687989],
                              [ 12.        ,  17.58588354,  11.53231028],
                              [ 12.        ,  12.00644646,  11.91187955],
                              [ 12.        ,  14.18091461,  12.07730994],
                              [ 12.        ,  16.64191633,  12.07730994],
                              [ 12.        ,  14.18091461,  13.49817006],
                              [ 12.        ,  16.64191633,  13.49817006],
                              [ 12.        ,  12.00644646,  13.66360045],
                              [ 12.        ,  17.58588354,  14.04316972],
                              [ 12.        ,  12.95041368,  14.20860011],
                              [ 12.        ,  15.4114154 ,  14.20860011],
                              [ 12.        ,  12.95041368,  15.62946023],
                              [ 12.        ,  15.4114154 ,  15.62946023],
                              [ 12.        ,  17.58588354,  15.7948901 ],
                              [ 12.        ,  12.00644646,  16.1744599 ],
                              [ 12.        ,  14.18091461,  16.33988977],
                              [ 12.        ,  16.64191633,  16.33988977],
                              [ 12.        ,  14.18091461,  17.76074989],
                              [ 12.        ,  16.64191633,  17.76074989],
                              [ 12.        ,  12.00644646,  17.92618028],
                              [ 12.        ,  17.58588354,  18.30574955],
                              [ 12.        ,  12.95041368,  18.47117994],
                              [ 12.        ,  15.4114154 ,  18.47117994],
                              [ 12.        ,  12.95041368,  19.89204006],
                              [ 12.        ,  15.4114154 ,  19.89204006],
                              [ 12.        ,  17.58588354,  20.05747045],
                              [ 12.        ,  12.00644646,  20.43703972],
                              [ 12.        ,  14.18091461,  20.60247011],
                              [ 12.        ,  16.64191633,  20.60247011],
                              [ 12.        ,  14.18091461,  22.02333023],
                              [ 12.        ,  16.64191633,  22.02333023],
                              [ 12.        ,  12.00644646,  22.1887601 ],
                              [ 12.        ,  17.58588354,  22.5683299 ],
                              [ 12.        ,  12.95041368,  22.73375977],
                              [ 12.        ,  15.4114154 ,  22.73375977],
                              [ 12.        ,  12.95041368,  24.15461989],
                              [ 12.        ,  15.4114154 ,  24.15461989],
                              [ 12.        ,  17.58588354,  24.32005028],
                              [ 12.        ,  12.00644646,  24.69961955],
                              [ 12.        ,  14.18091461,  24.86504994],
                              [ 12.        ,  16.64191633,  24.86504994],
                              [ 12.        ,  14.18091461,  26.28591006],
                              [ 12.        ,  16.64191633,  26.28591006],
                              [ 12.        ,  12.00644646,  26.45134045],
                              [ 12.        ,  17.58588354,  26.83090972],
                              [ 12.        ,  12.95041368,  26.99634011],
                              [ 12.        ,  15.4114154 ,  26.99634011],
                              [ 12.        ,  12.95041368,  28.41720023],
                              [ 12.        ,  15.4114154 ,  28.41720023],
                              [ 12.        ,  17.58588354,  28.5826301 ],
                              [ 12.        ,  12.00644646,  28.9621999 ],
                              [ 12.        ,  14.18091461,  29.12762977],
                              [ 12.        ,  16.64191633,  29.12762977],
                              [ 12.        ,  14.18091461,  30.54848989],
                              [ 12.        ,  16.64191633,  30.54848989],
                              [ 12.        ,  12.00644646,  30.71392028],
                              [ 12.        ,  17.58588354,  31.09348955],
                              [ 12.        ,  12.95041368,  31.25891994],
                              [ 12.        ,  15.4114154 ,  31.25891994],
                              [ 12.        ,  12.95041368,  32.67978006],
                              [ 12.        ,  15.4114154 ,  32.67978006],
                              [ 12.        ,  17.58588354,  32.84521045],
                              [ 12.        ,  12.00644646,  33.22477972],
                              [ 12.        ,  14.18091461,  33.39021011],
                              [ 12.        ,  16.64191633,  33.39021011],
                              [ 12.        ,  14.18091461,  34.81107023],
                              [ 12.        ,  16.64191633,  34.81107023],
                              [ 12.        ,  12.00644646,  34.9765001 ],
                              [ 12.        ,  17.58588354,  35.3560699 ],
                              [ 12.        ,  12.95041368,  35.52149977],
                              [ 12.        ,  15.4114154 ,  35.52149977],
                              [ 12.        ,  12.95041368,  36.94235989],
                              [ 12.        ,  15.4114154 ,  36.94235989],
                              [ 12.        ,  17.58588354,  37.10779028],
                              [ 12.        ,  12.00644646,  37.48735955],
                              [ 12.        ,  14.18091461,  37.65278994],
                              [ 12.        ,  16.64191633,  37.65278994],
                              [ 12.        ,  14.18091461,  39.07365006],
                              [ 12.        ,  16.64191633,  39.07365006],
                              [ 12.        ,  12.00644646,  39.23908045],
                              [ 12.        ,  17.58588354,  39.61864972],
                              [ 12.        ,  12.95041368,  39.78408011],
                              [ 12.        ,  15.4114154 ,  39.78408011],
                              [ 12.        ,  12.95041368,  41.20494023],
                              [ 12.        ,  15.4114154 ,  41.20494023],
                              [ 12.        ,  17.58588354,  41.3703701 ],
                              [ 12.        ,  12.00644646,  41.7499399 ],
                              [ 12.        ,  14.18091461,  41.91536977],
                              [ 12.        ,  16.64191633,  41.91536977],
                              [ 12.        ,  14.18091461,  43.33622989],
                              [ 12.        ,  16.64191633,  43.33622989],
                              [ 12.        ,  12.00644646,  43.50166028],
                              [ 12.        ,  17.58588354,  43.88122955],
                              [ 12.        ,  12.95041368,  44.04665994],
                              [ 12.        ,  15.4114154 ,  44.04665994],
                              [ 12.        ,  12.95041368,  45.46752006],
                              [ 12.        ,  15.4114154 ,  45.46752006],
                              [ 12.        ,  17.58588354,  45.63295045],
                              [ 12.        ,  12.00644646,  46.01251972],
                              [ 12.        ,  14.18091461,  46.17795011],
                              [ 12.        ,  16.64191633,  46.17795011],
                              [ 12.        ,  14.18091461,  47.59881023],
                              [ 12.        ,  16.64191633,  47.59881023],
                              [ 12.        ,  12.00644646,  47.7642401 ],
                              [ 12.        ,  17.58588354,  48.1438099 ],
                              [ 12.        ,  12.95041368,  48.30923977],
                              [ 12.        ,  15.4114154 ,  48.30923977],
                              [ 12.        ,  12.95041368,  49.73009989],
                              [ 12.        ,  15.4114154 ,  49.73009989],
                              [ 12.        ,  17.58588354,  49.89553028],
                              [ 12.        ,  12.00644646,  50.27509955],
                              [ 12.        ,  14.18091461,  50.44052994],
                              [ 12.        ,  16.64191633,  50.44052994]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region

metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.0 *Angstrom,  xmax =  0.0 *Angstrom,
        ymin =  11.00644646 *Angstrom,  ymax =  18.58588354 *Angstrom,
        zmin =  10.22026497 *Angstrom,  zmax =  40.22026497 *Angstrom,
)

metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  23.0 *Angstrom,  xmax =  24.0 *Angstrom,
        ymin =  11.00644646 *Angstrom,  ymax =  18.58588354 *Angstrom,
        zmin =  10.22026497 *Angstrom,  zmax =  40.22026497 *Angstrom,
)


metallic_regions = [metallic_region_0, metallic_region_1]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  11.00644646 *Angstrom,  ymax =  18.58588354 *Angstrom,
        zmin =  10.22026497 *Angstrom,  zmax =  40.22026497 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  13.0 *Angstrom,  xmax =  23.0 *Angstrom,
        ymin =  11.00644646 *Angstrom,  ymax =  18.58588354 *Angstrom,
        zmin =  10.22026497 *Angstrom,  zmax =  40.22026497 *Angstrom,
)


dielectric_regions = [dielectric_region_0, dielectric_region_1]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]

#charge = (24Angstrom * 29.59Angstrom * 8.52Angstrom) * (5e20 cm^-3)
charge = 3.025


