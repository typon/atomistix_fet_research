# Set up lattice
vector_a = [30.2568, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.2568, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.4306]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen, Hydrogen,
            Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.43654296,  0.5       ,  0.20367252],
                          [ 0.56345704,  0.5       ,  0.20367252],
                          [ 0.43654296,  0.43654296,  0.45367252],
                          [ 0.43654296,  0.56345704,  0.45367252],
                          [ 0.56345704,  0.43654296,  0.45367252],
                          [ 0.56345704,  0.56345704,  0.45367252],
                          [ 0.5       ,  0.43654296,  0.70367252],
                          [ 0.5       ,  0.56345704,  0.70367252],
                          [ 0.5       ,  0.5       ,  0.95367252],
                          [ 0.60339565,  0.5       ,  0.04632748],
                          [ 0.43654296,  0.60339565,  0.29632748],
                          [ 0.60339565,  0.43654296,  0.61101757],
                          [ 0.60339565,  0.56345704,  0.61101757],
                          [ 0.56345704,  0.60339565,  0.29632748],
                          [ 0.5       ,  0.60339565,  0.86101757],
                          [ 0.39660435,  0.5       ,  0.04632748],
                          [ 0.39660435,  0.43654296,  0.61101757],
                          [ 0.43654296,  0.39660435,  0.29632748],
                          [ 0.39660435,  0.56345704,  0.61101757],
                          [ 0.56345704,  0.39660435,  0.29632748],
                          [ 0.5       ,  0.39660435,  0.86101757]]


# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Silicon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  10.9999784971 *Angstrom,  xmax =  0.99997849708 *Angstrom,
        ymin =  10.9999784971 *Angstrom,  ymax =  19.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  10.9999784971 *Angstrom,  xmax =  19.2568215029 *Angstrom,
        ymin =  19.2568215029 *Angstrom,  ymax =  29.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.2568215029 *Angstrom,  xmax =  29.2568215029 *Angstrom,
        ymin =  10.9999784971 *Angstrom,  ymax =  19.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  10.9999784971 *Angstrom,  xmax =  19.2568215029 *Angstrom,
        ymin =  10.9999784971 *Angstrom,  ymax =  0.99997849708 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  10.9999784971 *Angstrom,  xmax =  0.99997849708 *Angstrom,
        ymin =  10.9999784971 *Angstrom,  ymax =  0.99997849708 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  10.9999784971 *Angstrom,  xmax =  0.99997849708 *Angstrom,
        ymin =  19.2568215029 *Angstrom,  ymax =  29.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.2568215029 *Angstrom,  xmax =  29.2568215029 *Angstrom,
        ymin =  19.2568215029 *Angstrom,  ymax =  29.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.2568215029 *Angstrom,  xmax =  29.2568215029 *Angstrom,
        ymin =  10.9999784971 *Angstrom,  ymax =  0.99997849708 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
bulk_configuration.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.99997849708 *Angstrom,  xmax =  -2.1502920001e-05 *Angstrom,
        ymin =  0.99997849708 *Angstrom,  ymax =  29.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.1502920001e-05 *Angstrom,  xmax =  30.2568215029 *Angstrom,
        ymin =  29.2568215029 *Angstrom,  ymax =  30.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.2568215029 *Angstrom,  xmax =  30.2568215029 *Angstrom,
        ymin =  0.99997849708 *Angstrom,  ymax =  29.2568215029 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  -2.1502920001e-05 *Angstrom,  xmax =  30.2568215029 *Angstrom,
        ymin =  0.99997849708 *Angstrom,  ymax =  -2.1502920001e-05 *Angstrom,
        zmin =  -0.135493006444 *Angstrom,  zmax =  5.31450699356 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
bulk_configuration.setMetallicRegions(metallic_regions)


