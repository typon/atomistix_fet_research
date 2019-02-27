# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 48.939]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
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
fractional_coordinates = [[ 0.55130417,  0.4153625 ,  0.02083333],
                          [ 0.55130417,  0.4153625 ,  0.10416667],
                          [ 0.55130417,  0.4153625 ,  0.1875    ],
                          [ 0.55130417,  0.4153625 ,  0.27083333],
                          [ 0.55130417,  0.4153625 ,  0.35416667],
                          [ 0.55130417,  0.4153625 ,  0.4375    ],
                          [ 0.55130417,  0.4153625 ,  0.52083333],
                          [ 0.55130417,  0.4153625 ,  0.60416667],
                          [ 0.55130417,  0.4153625 ,  0.6875    ],
                          [ 0.55130417,  0.4153625 ,  0.77083333],
                          [ 0.55130417,  0.4153625 ,  0.85416667],
                          [ 0.55130417,  0.4153625 ,  0.9375    ],
                          [ 0.4153625 ,  0.4153625 ,  0.02083333],
                          [ 0.4153625 ,  0.4153625 ,  0.10416667],
                          [ 0.4153625 ,  0.4153625 ,  0.1875    ],
                          [ 0.4153625 ,  0.4153625 ,  0.27083333],
                          [ 0.4153625 ,  0.4153625 ,  0.35416667],
                          [ 0.4153625 ,  0.4153625 ,  0.4375    ],
                          [ 0.4153625 ,  0.4153625 ,  0.52083333],
                          [ 0.4153625 ,  0.4153625 ,  0.60416667],
                          [ 0.4153625 ,  0.4153625 ,  0.6875    ],
                          [ 0.4153625 ,  0.4153625 ,  0.77083333],
                          [ 0.4153625 ,  0.4153625 ,  0.85416667],
                          [ 0.4153625 ,  0.4153625 ,  0.9375    ],
                          [ 0.48333333,  0.48333333,  0.02083333],
                          [ 0.48333333,  0.48333333,  0.10416667],
                          [ 0.48333333,  0.48333333,  0.1875    ],
                          [ 0.48333333,  0.48333333,  0.27083333],
                          [ 0.48333333,  0.48333333,  0.35416667],
                          [ 0.48333333,  0.48333333,  0.4375    ],
                          [ 0.48333333,  0.48333333,  0.52083333],
                          [ 0.48333333,  0.48333333,  0.60416667],
                          [ 0.48333333,  0.48333333,  0.6875    ],
                          [ 0.48333333,  0.48333333,  0.77083333],
                          [ 0.48333333,  0.48333333,  0.85416667],
                          [ 0.48333333,  0.48333333,  0.9375    ],
                          [ 0.55130417,  0.55130417,  0.02083333],
                          [ 0.55130417,  0.55130417,  0.10416667],
                          [ 0.55130417,  0.55130417,  0.1875    ],
                          [ 0.55130417,  0.55130417,  0.27083333],
                          [ 0.55130417,  0.55130417,  0.35416667],
                          [ 0.55130417,  0.55130417,  0.4375    ],
                          [ 0.55130417,  0.55130417,  0.52083333],
                          [ 0.55130417,  0.55130417,  0.60416667],
                          [ 0.55130417,  0.55130417,  0.6875    ],
                          [ 0.55130417,  0.55130417,  0.77083333],
                          [ 0.55130417,  0.55130417,  0.85416667],
                          [ 0.55130417,  0.55130417,  0.9375    ],
                          [ 0.48333333,  0.4153625 ,  0.0625    ],
                          [ 0.48333333,  0.4153625 ,  0.14583333],
                          [ 0.48333333,  0.4153625 ,  0.22916667],
                          [ 0.48333333,  0.4153625 ,  0.3125    ],
                          [ 0.48333333,  0.4153625 ,  0.39583333],
                          [ 0.48333333,  0.4153625 ,  0.47916667],
                          [ 0.48333333,  0.4153625 ,  0.5625    ],
                          [ 0.48333333,  0.4153625 ,  0.64583333],
                          [ 0.48333333,  0.4153625 ,  0.72916667],
                          [ 0.48333333,  0.4153625 ,  0.8125    ],
                          [ 0.48333333,  0.4153625 ,  0.89583333],
                          [ 0.48333333,  0.4153625 ,  0.97916667],
                          [ 0.55130417,  0.48333333,  0.0625    ],
                          [ 0.55130417,  0.48333333,  0.14583333],
                          [ 0.55130417,  0.48333333,  0.22916667],
                          [ 0.55130417,  0.48333333,  0.3125    ],
                          [ 0.55130417,  0.48333333,  0.39583333],
                          [ 0.55130417,  0.48333333,  0.47916667],
                          [ 0.55130417,  0.48333333,  0.5625    ],
                          [ 0.55130417,  0.48333333,  0.64583333],
                          [ 0.55130417,  0.48333333,  0.72916667],
                          [ 0.55130417,  0.48333333,  0.8125    ],
                          [ 0.55130417,  0.48333333,  0.89583333],
                          [ 0.55130417,  0.48333333,  0.97916667],
                          [ 0.4153625 ,  0.55130417,  0.02083333],
                          [ 0.4153625 ,  0.55130417,  0.10416667],
                          [ 0.4153625 ,  0.55130417,  0.1875    ],
                          [ 0.4153625 ,  0.55130417,  0.27083333],
                          [ 0.4153625 ,  0.55130417,  0.35416667],
                          [ 0.4153625 ,  0.55130417,  0.4375    ],
                          [ 0.4153625 ,  0.55130417,  0.52083333],
                          [ 0.4153625 ,  0.55130417,  0.60416667],
                          [ 0.4153625 ,  0.55130417,  0.6875    ],
                          [ 0.4153625 ,  0.55130417,  0.77083333],
                          [ 0.4153625 ,  0.55130417,  0.85416667],
                          [ 0.4153625 ,  0.55130417,  0.9375    ],
                          [ 0.4153625 ,  0.48333333,  0.0625    ],
                          [ 0.4153625 ,  0.48333333,  0.14583333],
                          [ 0.4153625 ,  0.48333333,  0.22916667],
                          [ 0.4153625 ,  0.48333333,  0.3125    ],
                          [ 0.4153625 ,  0.48333333,  0.39583333],
                          [ 0.4153625 ,  0.48333333,  0.47916667],
                          [ 0.4153625 ,  0.48333333,  0.5625    ],
                          [ 0.4153625 ,  0.48333333,  0.64583333],
                          [ 0.4153625 ,  0.48333333,  0.72916667],
                          [ 0.4153625 ,  0.48333333,  0.8125    ],
                          [ 0.4153625 ,  0.48333333,  0.89583333],
                          [ 0.4153625 ,  0.48333333,  0.97916667],
                          [ 0.48333333,  0.55130417,  0.0625    ],
                          [ 0.48333333,  0.55130417,  0.14583333],
                          [ 0.48333333,  0.55130417,  0.22916667],
                          [ 0.48333333,  0.55130417,  0.3125    ],
                          [ 0.48333333,  0.55130417,  0.39583333],
                          [ 0.48333333,  0.55130417,  0.47916667],
                          [ 0.48333333,  0.55130417,  0.5625    ],
                          [ 0.48333333,  0.55130417,  0.64583333],
                          [ 0.48333333,  0.55130417,  0.72916667],
                          [ 0.48333333,  0.55130417,  0.8125    ],
                          [ 0.48333333,  0.55130417,  0.89583333],
                          [ 0.48333333,  0.55130417,  0.97916667]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
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
bulk_configuration.setMetallicRegions(metallic_regions)

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
bulk_configuration.setDielectricRegions(dielectric_regions)
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


