# Set up lattice
vector_a = [34.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06374]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.41518358,  0.43062756,  0.16666685],
                          [ 0.5       ,  0.43062756,  0.16666685],
                          [ 0.58481642,  0.43062756,  0.16666685],
                          [ 0.37277537,  0.51387449,  0.16666685],
                          [ 0.45759179,  0.51387449,  0.16666685],
                          [ 0.54240821,  0.51387449,  0.16666685],
                          [ 0.62722463,  0.51387449,  0.16666685],
                          [ 0.41518358,  0.59712142,  0.16666685],
                          [ 0.5       ,  0.59712142,  0.16666685],
                          [ 0.58481642,  0.59712142,  0.16666685],
                          [ 0.37277537,  0.45837653,  0.5       ],
                          [ 0.45759179,  0.45837653,  0.5       ],
                          [ 0.54240821,  0.45837653,  0.5       ],
                          [ 0.62722463,  0.45837653,  0.5       ],
                          [ 0.41518358,  0.54162347,  0.5       ],
                          [ 0.5       ,  0.54162347,  0.5       ],
                          [ 0.58481642,  0.54162347,  0.5       ],
                          [ 0.37277537,  0.40287858,  0.83333315],
                          [ 0.45759179,  0.40287858,  0.83333315],
                          [ 0.54240821,  0.40287858,  0.83333315],
                          [ 0.62722463,  0.40287858,  0.83333315],
                          [ 0.41518358,  0.48612551,  0.83333315],
                          [ 0.5       ,  0.48612551,  0.83333315],
                          [ 0.58481642,  0.48612551,  0.83333315],
                          [ 0.37277537,  0.56937244,  0.83333315],
                          [ 0.45759179,  0.56937244,  0.83333315],
                          [ 0.54240821,  0.56937244,  0.83333315],
                          [ 0.62722463,  0.56937244,  0.83333315]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )



dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.67436258 *Angstrom,  xmax =  1.67436258 *Angstrom,
        ymin =  11.0863574 *Angstrom,  ymax =  18.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.67436258 *Angstrom,  xmax =  22.32563742 *Angstrom,
        ymin =  18.9136426 *Angstrom,  ymax =  28.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  22.32563742 *Angstrom,  xmax =  32.32563742 *Angstrom,
        ymin =  11.0863574 *Angstrom,  ymax =  18.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.67436258 *Angstrom,  xmax =  22.32563742 *Angstrom,
        ymin =  11.0863574 *Angstrom,  ymax =  1.0863574 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.67436258 *Angstrom,  xmax =  1.67436258 *Angstrom,
        ymin =  11.0863574 *Angstrom,  ymax =  1.0863574 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.67436258 *Angstrom,  xmax =  1.67436258 *Angstrom,
        ymin =  18.9136426 *Angstrom,  ymax =  28.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  22.32563742 *Angstrom,  xmax =  32.32563742 *Angstrom,
        ymin =  18.9136426 *Angstrom,  ymax =  28.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  22.32563742 *Angstrom,  xmax =  32.32563742 *Angstrom,
        ymin =  11.0863574 *Angstrom,  ymax =  1.0863574 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.67436258 *Angstrom,  xmax =  0.67436258 *Angstrom,
        ymin =  1.0863574 *Angstrom,  ymax =  28.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  0.67436258 *Angstrom,  xmax =  33.32563742 *Angstrom,
        ymin =  28.9136426 *Angstrom,  ymax =  29.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  32.32563742 *Angstrom,  xmax =  33.32563742 *Angstrom,
        ymin =  1.0863574 *Angstrom,  ymax =  28.9136426 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  0.67436258 *Angstrom,  xmax =  33.32563742 *Angstrom,
        ymin =  1.0863574 *Angstrom,  ymax =  0.0863574 *Angstrom,
        zmin =  -1.55677564751 *Angstrom,  zmax =  7.44322435249 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

