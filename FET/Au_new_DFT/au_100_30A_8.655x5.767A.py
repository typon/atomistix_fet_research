# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                              [ 16.32565   ,  13.44312088,   1.0195625 ],
                              [ 19.20940823,  13.44312088,   1.0195625 ],
                              [ 13.44189177,  16.32687912,   1.0195625 ],
                              [ 16.32565   ,  16.32687912,   1.0195625 ],
                              [ 19.20940823,  16.32687912,   1.0195625 ],
                              [ 12.00001265,  12.00124177,   3.0586875 ],
                              [ 14.88377088,  12.00124177,   3.0586875 ],
                              [ 17.76752912,  12.00124177,   3.0586875 ],
                              [ 20.65128735,  12.00124177,   3.0586875 ],
                              [ 12.00001265,  14.885     ,   3.0586875 ],
                              [ 14.88377088,  14.885     ,   3.0586875 ],
                              [ 17.76752912,  14.885     ,   3.0586875 ],
                              [ 20.65128735,  14.885     ,   3.0586875 ],
                              [ 12.00001265,  17.76875823,   3.0586875 ],
                              [ 14.88377088,  17.76875823,   3.0586875 ],
                              [ 17.76752912,  17.76875823,   3.0586875 ],
                              [ 20.65128735,  17.76875823,   3.0586875 ],
                              [ 13.44189177,  13.44312088,   5.0978125 ],
                              [ 16.32565   ,  13.44312088,   5.0978125 ],
                              [ 19.20940823,  13.44312088,   5.0978125 ],
                              [ 13.44189177,  16.32687912,   5.0978125 ],
                              [ 16.32565   ,  16.32687912,   5.0978125 ],
                              [ 19.20940823,  16.32687912,   5.0978125 ],
                              [ 12.00001265,  12.00124177,   7.1369375 ],
                              [ 14.88377088,  12.00124177,   7.1369375 ],
                              [ 17.76752912,  12.00124177,   7.1369375 ],
                              [ 20.65128735,  12.00124177,   7.1369375 ],
                              [ 12.00001265,  14.885     ,   7.1369375 ],
                              [ 14.88377088,  14.885     ,   7.1369375 ],
                              [ 17.76752912,  14.885     ,   7.1369375 ],
                              [ 20.65128735,  14.885     ,   7.1369375 ],
                              [ 12.00001265,  17.76875823,   7.1369375 ],
                              [ 14.88377088,  17.76875823,   7.1369375 ],
                              [ 17.76752912,  17.76875823,   7.1369375 ],
                              [ 20.65128735,  17.76875823,   7.1369375 ]]*Angstrom

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
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                               [ 16.32565   ,  13.44312088,   1.0195625 ],
                               [ 19.20940823,  13.44312088,   1.0195625 ],
                               [ 13.44189177,  16.32687912,   1.0195625 ],
                               [ 16.32565   ,  16.32687912,   1.0195625 ],
                               [ 19.20940823,  16.32687912,   1.0195625 ],
                               [ 12.00001265,  12.00124177,   3.0586875 ],
                               [ 14.88377088,  12.00124177,   3.0586875 ],
                               [ 17.76752912,  12.00124177,   3.0586875 ],
                               [ 20.65128735,  12.00124177,   3.0586875 ],
                               [ 12.00001265,  14.885     ,   3.0586875 ],
                               [ 14.88377088,  14.885     ,   3.0586875 ],
                               [ 17.76752912,  14.885     ,   3.0586875 ],
                               [ 20.65128735,  14.885     ,   3.0586875 ],
                               [ 12.00001265,  17.76875823,   3.0586875 ],
                               [ 14.88377088,  17.76875823,   3.0586875 ],
                               [ 17.76752912,  17.76875823,   3.0586875 ],
                               [ 20.65128735,  17.76875823,   3.0586875 ],
                               [ 13.44189177,  13.44312088,   5.0978125 ],
                               [ 16.32565   ,  13.44312088,   5.0978125 ],
                               [ 19.20940823,  13.44312088,   5.0978125 ],
                               [ 13.44189177,  16.32687912,   5.0978125 ],
                               [ 16.32565   ,  16.32687912,   5.0978125 ],
                               [ 19.20940823,  16.32687912,   5.0978125 ],
                               [ 12.00001265,  12.00124177,   7.1369375 ],
                               [ 14.88377088,  12.00124177,   7.1369375 ],
                               [ 17.76752912,  12.00124177,   7.1369375 ],
                               [ 20.65128735,  12.00124177,   7.1369375 ],
                               [ 12.00001265,  14.885     ,   7.1369375 ],
                               [ 14.88377088,  14.885     ,   7.1369375 ],
                               [ 17.76752912,  14.885     ,   7.1369375 ],
                               [ 20.65128735,  14.885     ,   7.1369375 ],
                               [ 12.00001265,  17.76875823,   7.1369375 ],
                               [ 14.88377088,  17.76875823,   7.1369375 ],
                               [ 17.76752912,  17.76875823,   7.1369375 ],
                               [ 20.65128735,  17.76875823,   7.1369375 ]]*Angstrom

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
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 20.39125]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                              [ 16.32565   ,  13.44312088,   1.0195625 ],
                              [ 19.20940823,  13.44312088,   1.0195625 ],
                              [ 13.44189177,  16.32687912,   1.0195625 ],
                              [ 16.32565   ,  16.32687912,   1.0195625 ],
                              [ 19.20940823,  16.32687912,   1.0195625 ],
                              [ 12.00001265,  12.00124177,   3.0586875 ],
                              [ 14.88377088,  12.00124177,   3.0586875 ],
                              [ 17.76752912,  12.00124177,   3.0586875 ],
                              [ 20.65128735,  12.00124177,   3.0586875 ],
                              [ 12.00001265,  14.885     ,   3.0586875 ],
                              [ 14.88377088,  14.885     ,   3.0586875 ],
                              [ 17.76752912,  14.885     ,   3.0586875 ],
                              [ 20.65128735,  14.885     ,   3.0586875 ],
                              [ 12.00001265,  17.76875823,   3.0586875 ],
                              [ 14.88377088,  17.76875823,   3.0586875 ],
                              [ 17.76752912,  17.76875823,   3.0586875 ],
                              [ 20.65128735,  17.76875823,   3.0586875 ],
                              [ 13.44189177,  13.44312088,   5.0978125 ],
                              [ 16.32565   ,  13.44312088,   5.0978125 ],
                              [ 19.20940823,  13.44312088,   5.0978125 ],
                              [ 13.44189177,  16.32687912,   5.0978125 ],
                              [ 16.32565   ,  16.32687912,   5.0978125 ],
                              [ 19.20940823,  16.32687912,   5.0978125 ],
                              [ 12.00001265,  12.00124177,   7.1369375 ],
                              [ 14.88377088,  12.00124177,   7.1369375 ],
                              [ 17.76752912,  12.00124177,   7.1369375 ],
                              [ 20.65128735,  12.00124177,   7.1369375 ],
                              [ 12.00001265,  14.885     ,   7.1369375 ],
                              [ 14.88377088,  14.885     ,   7.1369375 ],
                              [ 17.76752912,  14.885     ,   7.1369375 ],
                              [ 20.65128735,  14.885     ,   7.1369375 ],
                              [ 12.00001265,  17.76875823,   7.1369375 ],
                              [ 14.88377088,  17.76875823,   7.1369375 ],
                              [ 17.76752912,  17.76875823,   7.1369375 ],
                              [ 20.65128735,  17.76875823,   7.1369375 ],
                              [ 13.44189177,  13.44312088,   9.1760625 ],
                              [ 16.32565   ,  13.44312088,   9.1760625 ],
                              [ 19.20940823,  13.44312088,   9.1760625 ],
                              [ 13.44189177,  16.32687912,   9.1760625 ],
                              [ 16.32565   ,  16.32687912,   9.1760625 ],
                              [ 19.20940823,  16.32687912,   9.1760625 ],
                              [ 12.00001265,  12.00124177,  11.2151875 ],
                              [ 14.88377088,  12.00124177,  11.2151875 ],
                              [ 17.76752912,  12.00124177,  11.2151875 ],
                              [ 20.65128735,  12.00124177,  11.2151875 ],
                              [ 12.00001265,  14.885     ,  11.2151875 ],
                              [ 14.88377088,  14.885     ,  11.2151875 ],
                              [ 17.76752912,  14.885     ,  11.2151875 ],
                              [ 20.65128735,  14.885     ,  11.2151875 ],
                              [ 12.00001265,  17.76875823,  11.2151875 ],
                              [ 14.88377088,  17.76875823,  11.2151875 ],
                              [ 17.76752912,  17.76875823,  11.2151875 ],
                              [ 20.65128735,  17.76875823,  11.2151875 ],
                              [ 13.44189177,  13.44312088,  13.2543125 ],
                              [ 16.32565   ,  13.44312088,  13.2543125 ],
                              [ 19.20940823,  13.44312088,  13.2543125 ],
                              [ 13.44189177,  16.32687912,  13.2543125 ],
                              [ 16.32565   ,  16.32687912,  13.2543125 ],
                              [ 19.20940823,  16.32687912,  13.2543125 ],
                              [ 12.00001265,  12.00124177,  15.2934375 ],
                              [ 14.88377088,  12.00124177,  15.2934375 ],
                              [ 17.76752912,  12.00124177,  15.2934375 ],
                              [ 20.65128735,  12.00124177,  15.2934375 ],
                              [ 12.00001265,  14.885     ,  15.2934375 ],
                              [ 14.88377088,  14.885     ,  15.2934375 ],
                              [ 17.76752912,  14.885     ,  15.2934375 ],
                              [ 20.65128735,  14.885     ,  15.2934375 ],
                              [ 12.00001265,  17.76875823,  15.2934375 ],
                              [ 14.88377088,  17.76875823,  15.2934375 ],
                              [ 17.76752912,  17.76875823,  15.2934375 ],
                              [ 20.65128735,  17.76875823,  15.2934375 ],
                              [ 13.44189177,  13.44312088,  17.3325625 ],
                              [ 16.32565   ,  13.44312088,  17.3325625 ],
                              [ 19.20940823,  13.44312088,  17.3325625 ],
                              [ 13.44189177,  16.32687912,  17.3325625 ],
                              [ 16.32565   ,  16.32687912,  17.3325625 ],
                              [ 19.20940823,  16.32687912,  17.3325625 ],
                              [ 12.00001265,  12.00124177,  19.3716875 ],
                              [ 14.88377088,  12.00124177,  19.3716875 ],
                              [ 17.76752912,  12.00124177,  19.3716875 ],
                              [ 20.65128735,  12.00124177,  19.3716875 ],
                              [ 12.00001265,  14.885     ,  19.3716875 ],
                              [ 14.88377088,  14.885     ,  19.3716875 ],
                              [ 17.76752912,  14.885     ,  19.3716875 ],
                              [ 20.65128735,  14.885     ,  19.3716875 ],
                              [ 12.00001265,  17.76875823,  19.3716875 ],
                              [ 14.88377088,  17.76875823,  19.3716875 ],
                              [ 17.76752912,  17.76875823,  19.3716875 ],
                              [ 20.65128735,  17.76875823,  19.3716875 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  18.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  18.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.00001265 *Angstrom,  xmax =  1.26500000004e-05 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  28.76875823 *Angstrom,  ymax =  29.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.65128735 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  0.00124177 *Angstrom,
        zmin =  4.68584375 *Angstrom,  zmax =  14.68584375 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


