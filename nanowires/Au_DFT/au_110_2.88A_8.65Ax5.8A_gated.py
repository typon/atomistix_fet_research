# Set up lattice
vector_a = [33.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 31.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88376]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.36892008,  0.46711089,  0.25000015],
                          [ 0.36892008,  0.59866734,  0.25000015],
                          [ 0.45630669,  0.46711089,  0.25000015],
                          [ 0.45630669,  0.59866734,  0.25000015],
                          [ 0.54369331,  0.46711089,  0.25000015],
                          [ 0.54369331,  0.59866734,  0.25000015],
                          [ 0.63107992,  0.46711089,  0.25000015],
                          [ 0.63107992,  0.59866734,  0.25000015],
                          [ 0.41261339,  0.40133266,  0.74999985],
                          [ 0.41261339,  0.53288911,  0.74999985],
                          [ 0.5       ,  0.40133266,  0.74999985],
                          [ 0.5       ,  0.53288911,  0.74999985],
                          [ 0.58738661,  0.40133266,  0.74999985],
                          [ 0.58738661,  0.53288911,  0.74999985]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )



dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.17436264 *Angstrom,  xmax =  1.17436264 *Angstrom,
        ymin =  11.44131246 *Angstrom,  ymax =  19.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.17436264 *Angstrom,  xmax =  21.82563736 *Angstrom,
        ymin =  19.55868754 *Angstrom,  ymax =  29.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.82563736 *Angstrom,  xmax =  31.82563736 *Angstrom,
        ymin =  11.44131246 *Angstrom,  ymax =  19.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.17436264 *Angstrom,  xmax =  21.82563736 *Angstrom,
        ymin =  11.44131246 *Angstrom,  ymax =  1.44131246 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.17436264 *Angstrom,  xmax =  1.17436264 *Angstrom,
        ymin =  11.44131246 *Angstrom,  ymax =  1.44131246 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.17436264 *Angstrom,  xmax =  1.17436264 *Angstrom,
        ymin =  19.55868754 *Angstrom,  ymax =  29.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.82563736 *Angstrom,  xmax =  31.82563736 *Angstrom,
        ymin =  19.55868754 *Angstrom,  ymax =  29.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.82563736 *Angstrom,  xmax =  31.82563736 *Angstrom,
        ymin =  11.44131246 *Angstrom,  ymax =  1.44131246 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.17436264 *Angstrom,  xmax =  0.17436264 *Angstrom,
        ymin =  1.44131246 *Angstrom,  ymax =  29.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  0.17436264 *Angstrom,  xmax =  32.82563736 *Angstrom,
        ymin =  29.55868754 *Angstrom,  ymax =  30.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.82563736 *Angstrom,  xmax =  32.82563736 *Angstrom,
        ymin =  1.44131246 *Angstrom,  ymax =  29.55868754 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  0.17436264 *Angstrom,  xmax =  32.82563736 *Angstrom,
        ymin =  1.44131246 *Angstrom,  ymax =  0.44131246 *Angstrom,
        zmin =  -0.918590216282 *Angstrom,  zmax =  3.08140978372 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

