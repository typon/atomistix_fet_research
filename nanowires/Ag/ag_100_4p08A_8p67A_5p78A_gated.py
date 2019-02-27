# Set up lattice
vector_a = [33.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.0857]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.36868063,  0.40369913,  0.25      ],
                          [ 0.36868063,  0.5       ,  0.25      ],
                          [ 0.36868063,  0.59630087,  0.25      ],
                          [ 0.45622688,  0.40369913,  0.25      ],
                          [ 0.45622688,  0.5       ,  0.25      ],
                          [ 0.45622688,  0.59630087,  0.25      ],
                          [ 0.54377312,  0.40369913,  0.25      ],
                          [ 0.54377312,  0.5       ,  0.25      ],
                          [ 0.54377312,  0.59630087,  0.25      ],
                          [ 0.63131937,  0.40369913,  0.25      ],
                          [ 0.63131937,  0.5       ,  0.25      ],
                          [ 0.63131937,  0.59630087,  0.25      ],
                          [ 0.41245375,  0.45184956,  0.75      ],
                          [ 0.41245375,  0.54815044,  0.75      ],
                          [ 0.5       ,  0.45184956,  0.75      ],
                          [ 0.5       ,  0.54815044,  0.75      ],
                          [ 0.58754625,  0.45184956,  0.75      ],
                          [ 0.58754625,  0.54815044,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.16646079 *Angstrom,  xmax =  1.16646079 *Angstrom,
        ymin =  11.1109739 *Angstrom,  ymax =  18.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.16646079 *Angstrom,  xmax =  21.83353921 *Angstrom,
        ymin =  18.8890261 *Angstrom,  ymax =  28.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.83353921 *Angstrom,  xmax =  31.83353921 *Angstrom,
        ymin =  11.1109739 *Angstrom,  ymax =  18.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.16646079 *Angstrom,  xmax =  21.83353921 *Angstrom,
        ymin =  11.1109739 *Angstrom,  ymax =  1.1109739 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.16646079 *Angstrom,  xmax =  1.16646079 *Angstrom,
        ymin =  11.1109739 *Angstrom,  ymax =  1.1109739 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.16646079 *Angstrom,  xmax =  1.16646079 *Angstrom,
        ymin =  18.8890261 *Angstrom,  ymax =  28.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.83353921 *Angstrom,  xmax =  31.83353921 *Angstrom,
        ymin =  18.8890261 *Angstrom,  ymax =  28.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.83353921 *Angstrom,  xmax =  31.83353921 *Angstrom,
        ymin =  11.1109739 *Angstrom,  ymax =  1.1109739 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.16646079 *Angstrom,  xmax =  0.16646079 *Angstrom,
        ymin =  1.1109739 *Angstrom,  ymax =  28.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  0.16646079 *Angstrom,  xmax =  32.83353921 *Angstrom,
        ymin =  28.8890261 *Angstrom,  ymax =  29.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.83353921 *Angstrom,  xmax =  32.83353921 *Angstrom,
        ymin =  1.1109739 *Angstrom,  ymax =  28.8890261 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  0.16646079 *Angstrom,  xmax =  32.83353921 *Angstrom,
        ymin =  1.1109739 *Angstrom,  ymax =  0.1109739 *Angstrom,
        zmin =  -1.1178625 *Angstrom,  zmax =  4.1821375 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)

basis_set = [
    GGABasis.Silver_DoubleZetaPolarized,
    ]


