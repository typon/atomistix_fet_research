# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [29.571, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.571, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 13.60821063,  13.60821063,   1.17728937],
                              [ 16.39370718,  14.35458218,   1.17728937],
                              [ 14.35458218,  16.39370718,   1.17728937],
                              [ 14.03912845,  12.00000345,   3.5318681 ],
                              [ 16.824625  ,  12.746375  ,   3.5318681 ],
                              [ 12.00000345,  14.03912845,   3.5318681 ],
                              [ 14.7855    ,  14.7855    ,   3.5318681 ],
                              [ 17.57099655,  15.53187155,   3.5318681 ],
                              [ 12.746375  ,  16.824625  ,   3.5318681 ],
                              [ 15.53187155,  17.57099655,   3.5318681 ],
                              [ 15.21641782,  13.17729282,   5.88644684],
                              [ 13.17729282,  15.21641782,   5.88644684],
                              [ 15.96278937,  15.96278937,   5.88644684]]*Angstrom

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
vector_a = [29.571, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.571, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 13.60821063,  13.60821063,   1.17728937],
                               [ 16.39370718,  14.35458218,   1.17728937],
                               [ 14.35458218,  16.39370718,   1.17728937],
                               [ 14.03912845,  12.00000345,   3.5318681 ],
                               [ 16.824625  ,  12.746375  ,   3.5318681 ],
                               [ 12.00000345,  14.03912845,   3.5318681 ],
                               [ 14.7855    ,  14.7855    ,   3.5318681 ],
                               [ 17.57099655,  15.53187155,   3.5318681 ],
                               [ 12.746375  ,  16.824625  ,   3.5318681 ],
                               [ 15.53187155,  17.57099655,   3.5318681 ],
                               [ 15.21641782,  13.17729282,   5.88644684],
                               [ 13.17729282,  15.21641782,   5.88644684],
                               [ 15.96278937,  15.96278937,   5.88644684]]*Angstrom

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
vector_a = [29.571, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.571, 0.0]*Angstrom
vector_c = [0.0, 0.0, 49.4461534418]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold]

# Define coordinates
central_region_coordinates = [[ 13.60821063,  13.60821063,   1.17728937],
                              [ 16.39370718,  14.35458218,   1.17728937],
                              [ 14.35458218,  16.39370718,   1.17728937],
                              [ 14.03912845,  12.00000345,   3.5318681 ],
                              [ 16.824625  ,  12.746375  ,   3.5318681 ],
                              [ 12.00000345,  14.03912845,   3.5318681 ],
                              [ 14.7855    ,  14.7855    ,   3.5318681 ],
                              [ 17.57099655,  15.53187155,   3.5318681 ],
                              [ 12.746375  ,  16.824625  ,   3.5318681 ],
                              [ 15.53187155,  17.57099655,   3.5318681 ],
                              [ 15.21641782,  13.17729282,   5.88644684],
                              [ 13.17729282,  15.21641782,   5.88644684],
                              [ 15.96278937,  15.96278937,   5.88644684],
                              [ 13.60821063,  13.60821063,   8.24102557],
                              [ 16.39370718,  14.35458218,   8.24102557],
                              [ 14.35458218,  16.39370718,   8.24102557],
                              [ 14.03912845,  12.00000345,  10.59560431],
                              [ 16.824625  ,  12.746375  ,  10.59560431],
                              [ 12.00000345,  14.03912845,  10.59560431],
                              [ 14.7855    ,  14.7855    ,  10.59560431],
                              [ 17.57099655,  15.53187155,  10.59560431],
                              [ 12.746375  ,  16.824625  ,  10.59560431],
                              [ 15.53187155,  17.57099655,  10.59560431],
                              [ 15.21641782,  13.17729282,  12.95018304],
                              [ 13.17729282,  15.21641782,  12.95018304],
                              [ 15.96278937,  15.96278937,  12.95018304],
                              [ 13.60821063,  13.60821063,  15.30476178],
                              [ 16.39370718,  14.35458218,  15.30476178],
                              [ 14.35458218,  16.39370718,  15.30476178],
                              [ 14.03912845,  12.00000345,  17.65934051],
                              [ 16.824625  ,  12.746375  ,  17.65934051],
                              [ 12.00000345,  14.03912845,  17.65934051],
                              [ 14.7855    ,  14.7855    ,  17.65934051],
                              [ 17.57099655,  15.53187155,  17.65934051],
                              [ 12.746375  ,  16.824625  ,  17.65934051],
                              [ 15.53187155,  17.57099655,  17.65934051],
                              [ 15.21641782,  13.17729282,  20.01391925],
                              [ 13.17729282,  15.21641782,  20.01391925],
                              [ 15.96278937,  15.96278937,  20.01391925],
                              [ 13.60821063,  13.60821063,  22.36849799],
                              [ 16.39370718,  14.35458218,  22.36849799],
                              [ 14.35458218,  16.39370718,  22.36849799],
                              [ 14.03912845,  12.00000345,  24.72307672],
                              [ 16.824625  ,  12.746375  ,  24.72307672],
                              [ 12.00000345,  14.03912845,  24.72307672],
                              [ 14.7855    ,  14.7855    ,  24.72307672],
                              [ 17.57099655,  15.53187155,  24.72307672],
                              [ 12.746375  ,  16.824625  ,  24.72307672],
                              [ 15.53187155,  17.57099655,  24.72307672],
                              [ 15.21641782,  13.17729282,  27.07765546],
                              [ 13.17729282,  15.21641782,  27.07765546],
                              [ 15.96278937,  15.96278937,  27.07765546],
                              [ 13.60821063,  13.60821063,  29.43223419],
                              [ 16.39370718,  14.35458218,  29.43223419],
                              [ 14.35458218,  16.39370718,  29.43223419],
                              [ 14.03912845,  12.00000345,  31.78681293],
                              [ 16.824625  ,  12.746375  ,  31.78681293],
                              [ 12.00000345,  14.03912845,  31.78681293],
                              [ 14.7855    ,  14.7855    ,  31.78681293],
                              [ 17.57099655,  15.53187155,  31.78681293],
                              [ 12.746375  ,  16.824625  ,  31.78681293],
                              [ 15.53187155,  17.57099655,  31.78681293],
                              [ 15.21641782,  13.17729282,  34.14139166],
                              [ 13.17729282,  15.21641782,  34.14139166],
                              [ 15.96278937,  15.96278937,  34.14139166],
                              [ 13.60821063,  13.60821063,  36.4959704 ],
                              [ 16.39370718,  14.35458218,  36.4959704 ],
                              [ 14.35458218,  16.39370718,  36.4959704 ],
                              [ 14.03912845,  12.00000345,  38.85054913],
                              [ 16.824625  ,  12.746375  ,  38.85054913],
                              [ 12.00000345,  14.03912845,  38.85054913],
                              [ 14.7855    ,  14.7855    ,  38.85054913],
                              [ 17.57099655,  15.53187155,  38.85054913],
                              [ 12.746375  ,  16.824625  ,  38.85054913],
                              [ 15.53187155,  17.57099655,  38.85054913],
                              [ 15.21641782,  13.17729282,  41.20512787],
                              [ 13.17729282,  15.21641782,  41.20512787],
                              [ 15.96278937,  15.96278937,  41.20512787],
                              [ 13.60821063,  13.60821063,  43.5597066 ],
                              [ 16.39370718,  14.35458218,  43.5597066 ],
                              [ 14.35458218,  16.39370718,  43.5597066 ],
                              [ 14.03912845,  12.00000345,  45.91428534],
                              [ 16.824625  ,  12.746375  ,  45.91428534],
                              [ 12.00000345,  14.03912845,  45.91428534],
                              [ 14.7855    ,  14.7855    ,  45.91428534],
                              [ 17.57099655,  15.53187155,  45.91428534],
                              [ 12.746375  ,  16.824625  ,  45.91428534],
                              [ 15.53187155,  17.57099655,  45.91428534],
                              [ 15.21641782,  13.17729282,  48.26886407],
                              [ 13.17729282,  15.21641782,  48.26886407],
                              [ 15.96278937,  15.96278937,  48.26886407]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 1.00000345*Angstrom, xmax = 3.44999999946e-06*Angstrom,
    ymin = 1.00000345*Angstrom, ymax = 28.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = 3.44999999946e-06*Angstrom, xmax = 29.57099655*Angstrom,
    ymin = 28.57099655*Angstrom, ymax = 29.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

metallic_region_2 = BoxRegion(
    0.0*Volt,
    xmin = 28.57099655*Angstrom, xmax = 29.57099655*Angstrom,
    ymin = 1.00000345*Angstrom, ymax = 28.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

metallic_region_3 = BoxRegion(
    0.0*Volt,
    xmin = 3.44999999946e-06*Angstrom, xmax = 29.57099655*Angstrom,
    ymin = 1.00000345*Angstrom, ymax = 3.44999999946e-06*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    25.0,
    xmin = 11.00000345*Angstrom, xmax = 1.00000345*Angstrom,
    ymin = 11.00000345*Angstrom, ymax = 18.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_1 = BoxRegion(
    25.0,
    xmin = 11.00000345*Angstrom, xmax = 18.57099655*Angstrom,
    ymin = 18.57099655*Angstrom, ymax = 28.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_2 = BoxRegion(
    25.0,
    xmin = 18.57099655*Angstrom, xmax = 28.57099655*Angstrom,
    ymin = 11.00000345*Angstrom, ymax = 18.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_3 = BoxRegion(
    25.0,
    xmin = 11.00000345*Angstrom, xmax = 18.57099655*Angstrom,
    ymin = 11.00000345*Angstrom, ymax = 1.00000345*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_4 = BoxRegion(
    25.0,
    xmin = 11.00000345*Angstrom, xmax = 1.00000345*Angstrom,
    ymin = 11.00000345*Angstrom, ymax = 1.00000345*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_5 = BoxRegion(
    25.0,
    xmin = 11.00000345*Angstrom, xmax = 1.00000345*Angstrom,
    ymin = 18.57099655*Angstrom, ymax = 28.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_6 = BoxRegion(
    25.0,
    xmin = 18.57099655*Angstrom, xmax = 28.57099655*Angstrom,
    ymin = 18.57099655*Angstrom, ymax = 28.57099655*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_region_7 = BoxRegion(
    25.0,
    xmin = 18.57099655*Angstrom, xmax = 28.57099655*Angstrom,
    ymin = 11.00000345*Angstrom, ymax = 1.00000345*Angstrom,
    zmin = 9.134432035*Angstrom, zmax = 39.134432035*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


