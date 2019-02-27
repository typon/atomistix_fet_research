# Set up lattice
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.7675, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.07825]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.36752021,  0.40312394,  0.25      ],
                          [ 0.36752021,  0.5       ,  0.25      ],
                          [ 0.36752021,  0.59687606,  0.25      ],
                          [ 0.45584007,  0.40312394,  0.25      ],
                          [ 0.45584007,  0.5       ,  0.25      ],
                          [ 0.45584007,  0.59687606,  0.25      ],
                          [ 0.54415993,  0.40312394,  0.25      ],
                          [ 0.54415993,  0.5       ,  0.25      ],
                          [ 0.54415993,  0.59687606,  0.25      ],
                          [ 0.63247979,  0.40312394,  0.25      ],
                          [ 0.63247979,  0.5       ,  0.25      ],
                          [ 0.63247979,  0.59687606,  0.25      ],
                          [ 0.41168014,  0.45156197,  0.75      ],
                          [ 0.41168014,  0.54843803,  0.75      ],
                          [ 0.5       ,  0.45156197,  0.75      ],
                          [ 0.5       ,  0.54843803,  0.75      ],
                          [ 0.58831986,  0.45156197,  0.75      ],
                          [ 0.58831986,  0.54843803,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.0000126328 *Angstrom,  xmax =  1.00001263277 *Angstrom,
        ymin =  10.9999918839 *Angstrom,  ymax =  18.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.0000126328 *Angstrom,  xmax =  21.6512873672 *Angstrom,
        ymin =  18.767508116 *Angstrom,  ymax =  28.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.6512873672 *Angstrom,  xmax =  31.6512873672 *Angstrom,
        ymin =  10.9999918839 *Angstrom,  ymax =  18.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.0000126328 *Angstrom,  xmax =  21.6512873672 *Angstrom,
        ymin =  10.9999918839 *Angstrom,  ymax =  0.99999188395 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.0000126328 *Angstrom,  xmax =  1.00001263277 *Angstrom,
        ymin =  10.9999918839 *Angstrom,  ymax =  0.99999188395 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.0000126328 *Angstrom,  xmax =  1.00001263277 *Angstrom,
        ymin =  18.767508116 *Angstrom,  ymax =  28.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.6512873672 *Angstrom,  xmax =  31.6512873672 *Angstrom,
        ymin =  18.767508116 *Angstrom,  ymax =  28.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.6512873672 *Angstrom,  xmax =  31.6512873672 *Angstrom,
        ymin =  10.9999918839 *Angstrom,  ymax =  0.99999188395 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.00001263277 *Angstrom,  xmax =  1.26327730001e-05 *Angstrom,
        ymin =  0.99999188395 *Angstrom,  ymax =  28.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26327730001e-05 *Angstrom,  xmax =  32.6512873672 *Angstrom,
        ymin =  28.767508116 *Angstrom,  ymax =  29.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.6512873672 *Angstrom,  xmax =  32.6512873672 *Angstrom,
        ymin =  0.99999188395 *Angstrom,  ymax =  28.767508116 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26327730001e-05 *Angstrom,  xmax =  32.6512873672 *Angstrom,
        ymin =  0.99999188395 *Angstrom,  ymax =  -8.11605000095e-06 *Angstrom,
        zmin =  -1.47065625 *Angstrom,  zmax =  4.52934375 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

