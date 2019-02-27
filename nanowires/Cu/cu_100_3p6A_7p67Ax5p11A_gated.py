# Set up lattice
vector_a = [31.6684, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.1123, 0.0]*Angstrom
vector_c = [0.0, 0.0, 3.61496]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper, Copper, Copper, Copper, Copper, Copper, Copper,
            Copper, Copper]

# Define coordinates
fractional_coordinates = [[ 0.37892524,  0.41219647,  0.25      ],
                          [ 0.37892524,  0.5       ,  0.25      ],
                          [ 0.37892524,  0.58780353,  0.25      ],
                          [ 0.45964175,  0.41219647,  0.25      ],
                          [ 0.45964175,  0.5       ,  0.25      ],
                          [ 0.45964175,  0.58780353,  0.25      ],
                          [ 0.54035825,  0.41219647,  0.25      ],
                          [ 0.54035825,  0.5       ,  0.25      ],
                          [ 0.54035825,  0.58780353,  0.25      ],
                          [ 0.62107476,  0.41219647,  0.25      ],
                          [ 0.62107476,  0.5       ,  0.25      ],
                          [ 0.62107476,  0.58780353,  0.25      ],
                          [ 0.41928349,  0.45609824,  0.75      ],
                          [ 0.41928349,  0.54390176,  0.75      ],
                          [ 0.5       ,  0.45609824,  0.75      ],
                          [ 0.5       ,  0.54390176,  0.75      ],
                          [ 0.58071651,  0.45609824,  0.75      ],
                          [ 0.58071651,  0.54390176,  0.75      ]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  10.9999560704 *Angstrom,  xmax =  0.999956070416 *Angstrom,
        ymin =  10.9999872936 *Angstrom,  ymax =  18.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.9999560704 *Angstrom,  xmax =  20.6684439296 *Angstrom,
        ymin =  18.1123127064 *Angstrom,  ymax =  28.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  20.6684439296 *Angstrom,  xmax =  30.6684439296 *Angstrom,
        ymin =  10.9999872936 *Angstrom,  ymax =  18.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.9999560704 *Angstrom,  xmax =  20.6684439296 *Angstrom,
        ymin =  10.9999872936 *Angstrom,  ymax =  0.999987293581 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.9999560704 *Angstrom,  xmax =  0.999956070416 *Angstrom,
        ymin =  10.9999872936 *Angstrom,  ymax =  0.999987293581 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.9999560704 *Angstrom,  xmax =  0.999956070416 *Angstrom,
        ymin =  18.1123127064 *Angstrom,  ymax =  28.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  20.6684439296 *Angstrom,  xmax =  30.6684439296 *Angstrom,
        ymin =  18.1123127064 *Angstrom,  ymax =  28.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  20.6684439296 *Angstrom,  xmax =  30.6684439296 *Angstrom,
        ymin =  10.9999872936 *Angstrom,  ymax =  0.999987293581 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.999956070416 *Angstrom,  xmax =  -4.39295840007e-05 *Angstrom,
        ymin =  0.999987293581 *Angstrom,  ymax =  28.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -4.39295840007e-05 *Angstrom,  xmax =  31.6684439296 *Angstrom,
        ymin =  28.1123127064 *Angstrom,  ymax =  29.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  30.6684439296 *Angstrom,  xmax =  31.6684439296 *Angstrom,
        ymin =  0.999987293581 *Angstrom,  ymax =  28.1123127064 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -4.39295840007e-05 *Angstrom,  xmax =  31.6684439296 *Angstrom,
        ymin =  0.999987293581 *Angstrom,  ymax =  -1.27064189996e-05 *Angstrom,
        zmin =  -1.14439 *Angstrom,  zmax =  3.85561 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)

basis_set = [
    GGABasis.Copper_DoubleZetaPolarized,
    ]


