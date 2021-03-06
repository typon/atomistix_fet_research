# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                              [ 16.0782625,  12.0000125,   1.0195625],
                              [ 14.0391375,  14.0391375,   1.0195625],
                              [ 18.1173875,  14.0391375,   1.0195625],
                              [ 12.0000125,  16.0782625,   1.0195625],
                              [ 16.0782625,  16.0782625,   1.0195625],
                              [ 14.0391375,  18.1173875,   1.0195625],
                              [ 18.1173875,  18.1173875,   1.0195625],
                              [ 14.0391375,  12.0000125,   3.0586875],
                              [ 18.1173875,  12.0000125,   3.0586875],
                              [ 12.0000125,  14.0391375,   3.0586875],
                              [ 16.0782625,  14.0391375,   3.0586875],
                              [ 14.0391375,  16.0782625,   3.0586875],
                              [ 18.1173875,  16.0782625,   3.0586875],
                              [ 12.0000125,  18.1173875,   3.0586875],
                              [ 16.0782625,  18.1173875,   3.0586875],
                              [ 12.0000125,  12.0000125,   5.0978125],
                              [ 16.0782625,  12.0000125,   5.0978125],
                              [ 14.0391375,  14.0391375,   5.0978125],
                              [ 18.1173875,  14.0391375,   5.0978125],
                              [ 12.0000125,  16.0782625,   5.0978125],
                              [ 16.0782625,  16.0782625,   5.0978125],
                              [ 14.0391375,  18.1173875,   5.0978125],
                              [ 18.1173875,  18.1173875,   5.0978125],
                              [ 14.0391375,  12.0000125,   7.1369375],
                              [ 18.1173875,  12.0000125,   7.1369375],
                              [ 12.0000125,  14.0391375,   7.1369375],
                              [ 16.0782625,  14.0391375,   7.1369375],
                              [ 14.0391375,  16.0782625,   7.1369375],
                              [ 18.1173875,  16.0782625,   7.1369375],
                              [ 12.0000125,  18.1173875,   7.1369375],
                              [ 16.0782625,  18.1173875,   7.1369375]]*Angstrom

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
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                               [ 16.0782625,  12.0000125,   1.0195625],
                               [ 14.0391375,  14.0391375,   1.0195625],
                               [ 18.1173875,  14.0391375,   1.0195625],
                               [ 12.0000125,  16.0782625,   1.0195625],
                               [ 16.0782625,  16.0782625,   1.0195625],
                               [ 14.0391375,  18.1173875,   1.0195625],
                               [ 18.1173875,  18.1173875,   1.0195625],
                               [ 14.0391375,  12.0000125,   3.0586875],
                               [ 18.1173875,  12.0000125,   3.0586875],
                               [ 12.0000125,  14.0391375,   3.0586875],
                               [ 16.0782625,  14.0391375,   3.0586875],
                               [ 14.0391375,  16.0782625,   3.0586875],
                               [ 18.1173875,  16.0782625,   3.0586875],
                               [ 12.0000125,  18.1173875,   3.0586875],
                               [ 16.0782625,  18.1173875,   3.0586875],
                               [ 12.0000125,  12.0000125,   5.0978125],
                               [ 16.0782625,  12.0000125,   5.0978125],
                               [ 14.0391375,  14.0391375,   5.0978125],
                               [ 18.1173875,  14.0391375,   5.0978125],
                               [ 12.0000125,  16.0782625,   5.0978125],
                               [ 16.0782625,  16.0782625,   5.0978125],
                               [ 14.0391375,  18.1173875,   5.0978125],
                               [ 18.1173875,  18.1173875,   5.0978125],
                               [ 14.0391375,  12.0000125,   7.1369375],
                               [ 18.1173875,  12.0000125,   7.1369375],
                               [ 12.0000125,  14.0391375,   7.1369375],
                               [ 16.0782625,  14.0391375,   7.1369375],
                               [ 14.0391375,  16.0782625,   7.1369375],
                               [ 18.1173875,  16.0782625,   7.1369375],
                               [ 12.0000125,  18.1173875,   7.1369375],
                               [ 16.0782625,  18.1173875,   7.1369375]]*Angstrom

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
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 32.626]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                              [ 16.0782625,  12.0000125,   1.0195625],
                              [ 14.0391375,  14.0391375,   1.0195625],
                              [ 18.1173875,  14.0391375,   1.0195625],
                              [ 12.0000125,  16.0782625,   1.0195625],
                              [ 16.0782625,  16.0782625,   1.0195625],
                              [ 14.0391375,  18.1173875,   1.0195625],
                              [ 18.1173875,  18.1173875,   1.0195625],
                              [ 14.0391375,  12.0000125,   3.0586875],
                              [ 18.1173875,  12.0000125,   3.0586875],
                              [ 12.0000125,  14.0391375,   3.0586875],
                              [ 16.0782625,  14.0391375,   3.0586875],
                              [ 14.0391375,  16.0782625,   3.0586875],
                              [ 18.1173875,  16.0782625,   3.0586875],
                              [ 12.0000125,  18.1173875,   3.0586875],
                              [ 16.0782625,  18.1173875,   3.0586875],
                              [ 12.0000125,  12.0000125,   5.0978125],
                              [ 16.0782625,  12.0000125,   5.0978125],
                              [ 14.0391375,  14.0391375,   5.0978125],
                              [ 18.1173875,  14.0391375,   5.0978125],
                              [ 12.0000125,  16.0782625,   5.0978125],
                              [ 16.0782625,  16.0782625,   5.0978125],
                              [ 14.0391375,  18.1173875,   5.0978125],
                              [ 18.1173875,  18.1173875,   5.0978125],
                              [ 14.0391375,  12.0000125,   7.1369375],
                              [ 18.1173875,  12.0000125,   7.1369375],
                              [ 12.0000125,  14.0391375,   7.1369375],
                              [ 16.0782625,  14.0391375,   7.1369375],
                              [ 14.0391375,  16.0782625,   7.1369375],
                              [ 18.1173875,  16.0782625,   7.1369375],
                              [ 12.0000125,  18.1173875,   7.1369375],
                              [ 16.0782625,  18.1173875,   7.1369375],
                              [ 12.0000125,  12.0000125,   9.1760625],
                              [ 16.0782625,  12.0000125,   9.1760625],
                              [ 14.0391375,  14.0391375,   9.1760625],
                              [ 18.1173875,  14.0391375,   9.1760625],
                              [ 12.0000125,  16.0782625,   9.1760625],
                              [ 16.0782625,  16.0782625,   9.1760625],
                              [ 14.0391375,  18.1173875,   9.1760625],
                              [ 18.1173875,  18.1173875,   9.1760625],
                              [ 14.0391375,  12.0000125,  11.2151875],
                              [ 18.1173875,  12.0000125,  11.2151875],
                              [ 12.0000125,  14.0391375,  11.2151875],
                              [ 16.0782625,  14.0391375,  11.2151875],
                              [ 14.0391375,  16.0782625,  11.2151875],
                              [ 18.1173875,  16.0782625,  11.2151875],
                              [ 12.0000125,  18.1173875,  11.2151875],
                              [ 16.0782625,  18.1173875,  11.2151875],
                              [ 12.0000125,  12.0000125,  13.2543125],
                              [ 16.0782625,  12.0000125,  13.2543125],
                              [ 14.0391375,  14.0391375,  13.2543125],
                              [ 18.1173875,  14.0391375,  13.2543125],
                              [ 12.0000125,  16.0782625,  13.2543125],
                              [ 16.0782625,  16.0782625,  13.2543125],
                              [ 14.0391375,  18.1173875,  13.2543125],
                              [ 18.1173875,  18.1173875,  13.2543125],
                              [ 14.0391375,  12.0000125,  15.2934375],
                              [ 18.1173875,  12.0000125,  15.2934375],
                              [ 12.0000125,  14.0391375,  15.2934375],
                              [ 16.0782625,  14.0391375,  15.2934375],
                              [ 14.0391375,  16.0782625,  15.2934375],
                              [ 18.1173875,  16.0782625,  15.2934375],
                              [ 12.0000125,  18.1173875,  15.2934375],
                              [ 16.0782625,  18.1173875,  15.2934375],
                              [ 12.0000125,  12.0000125,  17.3325625],
                              [ 16.0782625,  12.0000125,  17.3325625],
                              [ 14.0391375,  14.0391375,  17.3325625],
                              [ 18.1173875,  14.0391375,  17.3325625],
                              [ 12.0000125,  16.0782625,  17.3325625],
                              [ 16.0782625,  16.0782625,  17.3325625],
                              [ 14.0391375,  18.1173875,  17.3325625],
                              [ 18.1173875,  18.1173875,  17.3325625],
                              [ 14.0391375,  12.0000125,  19.3716875],
                              [ 18.1173875,  12.0000125,  19.3716875],
                              [ 12.0000125,  14.0391375,  19.3716875],
                              [ 16.0782625,  14.0391375,  19.3716875],
                              [ 14.0391375,  16.0782625,  19.3716875],
                              [ 18.1173875,  16.0782625,  19.3716875],
                              [ 12.0000125,  18.1173875,  19.3716875],
                              [ 16.0782625,  18.1173875,  19.3716875],
                              [ 12.0000125,  12.0000125,  21.4108125],
                              [ 16.0782625,  12.0000125,  21.4108125],
                              [ 14.0391375,  14.0391375,  21.4108125],
                              [ 18.1173875,  14.0391375,  21.4108125],
                              [ 12.0000125,  16.0782625,  21.4108125],
                              [ 16.0782625,  16.0782625,  21.4108125],
                              [ 14.0391375,  18.1173875,  21.4108125],
                              [ 18.1173875,  18.1173875,  21.4108125],
                              [ 14.0391375,  12.0000125,  23.4499375],
                              [ 18.1173875,  12.0000125,  23.4499375],
                              [ 12.0000125,  14.0391375,  23.4499375],
                              [ 16.0782625,  14.0391375,  23.4499375],
                              [ 14.0391375,  16.0782625,  23.4499375],
                              [ 18.1173875,  16.0782625,  23.4499375],
                              [ 12.0000125,  18.1173875,  23.4499375],
                              [ 16.0782625,  18.1173875,  23.4499375],
                              [ 12.0000125,  12.0000125,  25.4890625],
                              [ 16.0782625,  12.0000125,  25.4890625],
                              [ 14.0391375,  14.0391375,  25.4890625],
                              [ 18.1173875,  14.0391375,  25.4890625],
                              [ 12.0000125,  16.0782625,  25.4890625],
                              [ 16.0782625,  16.0782625,  25.4890625],
                              [ 14.0391375,  18.1173875,  25.4890625],
                              [ 18.1173875,  18.1173875,  25.4890625],
                              [ 14.0391375,  12.0000125,  27.5281875],
                              [ 18.1173875,  12.0000125,  27.5281875],
                              [ 12.0000125,  14.0391375,  27.5281875],
                              [ 16.0782625,  14.0391375,  27.5281875],
                              [ 14.0391375,  16.0782625,  27.5281875],
                              [ 18.1173875,  16.0782625,  27.5281875],
                              [ 12.0000125,  18.1173875,  27.5281875],
                              [ 16.0782625,  18.1173875,  27.5281875],
                              [ 12.0000125,  12.0000125,  29.5673125],
                              [ 16.0782625,  12.0000125,  29.5673125],
                              [ 14.0391375,  14.0391375,  29.5673125],
                              [ 18.1173875,  14.0391375,  29.5673125],
                              [ 12.0000125,  16.0782625,  29.5673125],
                              [ 16.0782625,  16.0782625,  29.5673125],
                              [ 14.0391375,  18.1173875,  29.5673125],
                              [ 18.1173875,  18.1173875,  29.5673125],
                              [ 14.0391375,  12.0000125,  31.6064375],
                              [ 18.1173875,  12.0000125,  31.6064375],
                              [ 12.0000125,  14.0391375,  31.6064375],
                              [ 16.0782625,  14.0391375,  31.6064375],
                              [ 14.0391375,  16.0782625,  31.6064375],
                              [ 18.1173875,  16.0782625,  31.6064375],
                              [ 12.0000125,  18.1173875,  31.6064375],
                              [ 16.0782625,  18.1173875,  31.6064375]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.0000125 *Angstrom,  xmax =  1.25000000004e-05 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  29.1173875 *Angstrom,  ymax =  30.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.1173875 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  1.25000000004e-05 *Angstrom,
        zmin =  0.80321875 *Angstrom,  zmax =  30.80321875 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.0000125 *Angstrom,  xmax =  1.25000000004e-05 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  29.1173875 *Angstrom,  ymax =  30.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.1173875 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  1.25000000004e-05 *Angstrom,
        zmin =  10.80321875 *Angstrom,  zmax =  20.80321875 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)



device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    CerdaHuckelParameters.Gold_fcc_Basis,
    ]


