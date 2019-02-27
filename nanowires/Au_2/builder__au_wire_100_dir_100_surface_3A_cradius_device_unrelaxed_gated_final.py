# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 12.46087497,  12.46087497,   1.0195625 ],
                              [ 16.53912503,  12.46087497,   1.0195625 ],
                              [ 14.5       ,  14.5       ,   1.0195625 ],
                              [ 12.46087497,  16.53912503,   1.0195625 ],
                              [ 16.53912503,  16.53912503,   1.0195625 ],
                              [ 14.5       ,  12.46087497,   3.0586875 ],
                              [ 12.46087497,  14.5       ,   3.0586875 ],
                              [ 16.53912503,  14.5       ,   3.0586875 ],
                              [ 14.5       ,  16.53912503,   3.0586875 ],
                              [ 12.46087497,  12.46087497,   5.0978125 ],
                              [ 16.53912503,  12.46087497,   5.0978125 ],
                              [ 14.5       ,  14.5       ,   5.0978125 ],
                              [ 12.46087497,  16.53912503,   5.0978125 ],
                              [ 16.53912503,  16.53912503,   5.0978125 ],
                              [ 14.5       ,  12.46087497,   7.1369375 ],
                              [ 12.46087497,  14.5       ,   7.1369375 ],
                              [ 16.53912503,  14.5       ,   7.1369375 ],
                              [ 14.5       ,  16.53912503,   7.1369375 ]]*Angstrom

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
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 12.46087497,  12.46087497,   1.0195625 ],
                               [ 16.53912503,  12.46087497,   1.0195625 ],
                               [ 14.5       ,  14.5       ,   1.0195625 ],
                               [ 12.46087497,  16.53912503,   1.0195625 ],
                               [ 16.53912503,  16.53912503,   1.0195625 ],
                               [ 14.5       ,  12.46087497,   3.0586875 ],
                               [ 12.46087497,  14.5       ,   3.0586875 ],
                               [ 16.53912503,  14.5       ,   3.0586875 ],
                               [ 14.5       ,  16.53912503,   3.0586875 ],
                               [ 12.46087497,  12.46087497,   5.0978125 ],
                               [ 16.53912503,  12.46087497,   5.0978125 ],
                               [ 14.5       ,  14.5       ,   5.0978125 ],
                               [ 12.46087497,  16.53912503,   5.0978125 ],
                               [ 16.53912503,  16.53912503,   5.0978125 ],
                               [ 14.5       ,  12.46087497,   7.1369375 ],
                               [ 12.46087497,  14.5       ,   7.1369375 ],
                               [ 16.53912503,  14.5       ,   7.1369375 ],
                               [ 14.5       ,  16.53912503,   7.1369375 ]]*Angstrom

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
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 48.939]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 12.46087497,  12.46087497,   1.0195625 ],
                              [ 16.53912503,  12.46087497,   1.0195625 ],
                              [ 14.5       ,  14.5       ,   1.0195625 ],
                              [ 12.46087497,  16.53912503,   1.0195625 ],
                              [ 16.53912503,  16.53912503,   1.0195625 ],
                              [ 14.5       ,  12.46087497,   3.0586875 ],
                              [ 12.46087497,  14.5       ,   3.0586875 ],
                              [ 16.53912503,  14.5       ,   3.0586875 ],
                              [ 14.5       ,  16.53912503,   3.0586875 ],
                              [ 12.46087497,  12.46087497,   5.0978125 ],
                              [ 16.53912503,  12.46087497,   5.0978125 ],
                              [ 14.5       ,  14.5       ,   5.0978125 ],
                              [ 12.46087497,  16.53912503,   5.0978125 ],
                              [ 16.53912503,  16.53912503,   5.0978125 ],
                              [ 14.5       ,  12.46087497,   7.1369375 ],
                              [ 12.46087497,  14.5       ,   7.1369375 ],
                              [ 16.53912503,  14.5       ,   7.1369375 ],
                              [ 14.5       ,  16.53912503,   7.1369375 ],
                              [ 12.46087497,  12.46087497,   9.1760625 ],
                              [ 16.53912503,  12.46087497,   9.1760625 ],
                              [ 14.5       ,  14.5       ,   9.1760625 ],
                              [ 12.46087497,  16.53912503,   9.1760625 ],
                              [ 16.53912503,  16.53912503,   9.1760625 ],
                              [ 14.5       ,  12.46087497,  11.2151875 ],
                              [ 12.46087497,  14.5       ,  11.2151875 ],
                              [ 16.53912503,  14.5       ,  11.2151875 ],
                              [ 14.5       ,  16.53912503,  11.2151875 ],
                              [ 12.46087497,  12.46087497,  13.2543125 ],
                              [ 16.53912503,  12.46087497,  13.2543125 ],
                              [ 14.5       ,  14.5       ,  13.2543125 ],
                              [ 12.46087497,  16.53912503,  13.2543125 ],
                              [ 16.53912503,  16.53912503,  13.2543125 ],
                              [ 14.5       ,  12.46087497,  15.2934375 ],
                              [ 12.46087497,  14.5       ,  15.2934375 ],
                              [ 16.53912503,  14.5       ,  15.2934375 ],
                              [ 14.5       ,  16.53912503,  15.2934375 ],
                              [ 12.46087497,  12.46087497,  17.3325625 ],
                              [ 16.53912503,  12.46087497,  17.3325625 ],
                              [ 14.5       ,  14.5       ,  17.3325625 ],
                              [ 12.46087497,  16.53912503,  17.3325625 ],
                              [ 16.53912503,  16.53912503,  17.3325625 ],
                              [ 14.5       ,  12.46087497,  19.3716875 ],
                              [ 12.46087497,  14.5       ,  19.3716875 ],
                              [ 16.53912503,  14.5       ,  19.3716875 ],
                              [ 14.5       ,  16.53912503,  19.3716875 ],
                              [ 12.46087497,  12.46087497,  21.4108125 ],
                              [ 16.53912503,  12.46087497,  21.4108125 ],
                              [ 14.5       ,  14.5       ,  21.4108125 ],
                              [ 12.46087497,  16.53912503,  21.4108125 ],
                              [ 16.53912503,  16.53912503,  21.4108125 ],
                              [ 14.5       ,  12.46087497,  23.4499375 ],
                              [ 12.46087497,  14.5       ,  23.4499375 ],
                              [ 16.53912503,  14.5       ,  23.4499375 ],
                              [ 14.5       ,  16.53912503,  23.4499375 ],
                              [ 12.46087497,  12.46087497,  25.4890625 ],
                              [ 16.53912503,  12.46087497,  25.4890625 ],
                              [ 14.5       ,  14.5       ,  25.4890625 ],
                              [ 12.46087497,  16.53912503,  25.4890625 ],
                              [ 16.53912503,  16.53912503,  25.4890625 ],
                              [ 14.5       ,  12.46087497,  27.5281875 ],
                              [ 12.46087497,  14.5       ,  27.5281875 ],
                              [ 16.53912503,  14.5       ,  27.5281875 ],
                              [ 14.5       ,  16.53912503,  27.5281875 ],
                              [ 12.46087497,  12.46087497,  29.5673125 ],
                              [ 16.53912503,  12.46087497,  29.5673125 ],
                              [ 14.5       ,  14.5       ,  29.5673125 ],
                              [ 12.46087497,  16.53912503,  29.5673125 ],
                              [ 16.53912503,  16.53912503,  29.5673125 ],
                              [ 14.5       ,  12.46087497,  31.6064375 ],
                              [ 12.46087497,  14.5       ,  31.6064375 ],
                              [ 16.53912503,  14.5       ,  31.6064375 ],
                              [ 14.5       ,  16.53912503,  31.6064375 ],
                              [ 12.46087497,  12.46087497,  33.6455625 ],
                              [ 16.53912503,  12.46087497,  33.6455625 ],
                              [ 14.5       ,  14.5       ,  33.6455625 ],
                              [ 12.46087497,  16.53912503,  33.6455625 ],
                              [ 16.53912503,  16.53912503,  33.6455625 ],
                              [ 14.5       ,  12.46087497,  35.6846875 ],
                              [ 12.46087497,  14.5       ,  35.6846875 ],
                              [ 16.53912503,  14.5       ,  35.6846875 ],
                              [ 14.5       ,  16.53912503,  35.6846875 ],
                              [ 12.46087497,  12.46087497,  37.7238125 ],
                              [ 16.53912503,  12.46087497,  37.7238125 ],
                              [ 14.5       ,  14.5       ,  37.7238125 ],
                              [ 12.46087497,  16.53912503,  37.7238125 ],
                              [ 16.53912503,  16.53912503,  37.7238125 ],
                              [ 14.5       ,  12.46087497,  39.7629375 ],
                              [ 12.46087497,  14.5       ,  39.7629375 ],
                              [ 16.53912503,  14.5       ,  39.7629375 ],
                              [ 14.5       ,  16.53912503,  39.7629375 ],
                              [ 12.46087497,  12.46087497,  41.8020625 ],
                              [ 16.53912503,  12.46087497,  41.8020625 ],
                              [ 14.5       ,  14.5       ,  41.8020625 ],
                              [ 12.46087497,  16.53912503,  41.8020625 ],
                              [ 16.53912503,  16.53912503,  41.8020625 ],
                              [ 14.5       ,  12.46087497,  43.8411875 ],
                              [ 12.46087497,  14.5       ,  43.8411875 ],
                              [ 16.53912503,  14.5       ,  43.8411875 ],
                              [ 14.5       ,  16.53912503,  43.8411875 ],
                              [ 12.46087497,  12.46087497,  45.8803125 ],
                              [ 16.53912503,  12.46087497,  45.8803125 ],
                              [ 14.5       ,  14.5       ,  45.8803125 ],
                              [ 12.46087497,  16.53912503,  45.8803125 ],
                              [ 16.53912503,  16.53912503,  45.8803125 ],
                              [ 14.5       ,  12.46087497,  47.9194375 ],
                              [ 12.46087497,  14.5       ,  47.9194375 ],
                              [ 16.53912503,  14.5       ,  47.9194375 ],
                              [ 14.5       ,  16.53912503,  47.9194375 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 29.0*Angstrom, xmax = 30.0*Angstrom,
    ymin = 0.0*Angstrom, ymax = 30.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 1.0*Angstrom,
    ymin = 0.0*Angstrom, ymax = 30.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_2 = BoxRegion(
    0.0*Volt,
    xmin = 1.0*Angstrom, xmax = 29.0*Angstrom,
    ymin = 0.0*Angstrom, ymax = 1.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_3 = BoxRegion(
    0.0*Volt,
    xmin = 1.0*Angstrom, xmax = 29.0*Angstrom,
    ymin = 29.0*Angstrom, ymax = 30.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    25.0,
    xmin = 1.0*Angstrom, xmax = 11.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_1 = BoxRegion(
    25.0,
    xmin = 18.0*Angstrom, xmax = 29.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_2 = BoxRegion(
    25.0,
    xmin = 11.0*Angstrom, xmax = 18.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 11.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_3 = BoxRegion(
    25.0,
    xmin = 11.0*Angstrom, xmax = 18.0*Angstrom,
    ymin = 18.0*Angstrom, ymax = 29.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


