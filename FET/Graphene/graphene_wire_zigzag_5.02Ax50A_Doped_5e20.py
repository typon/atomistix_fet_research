# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.0217, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.38300513133]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon]

# Define coordinates
left_electrode_coordinates = [[ 12.        ,  11.99999051,   0.61525043],
                              [ 12.        ,  13.08999   ,   0.61525043],
                              [ 12.        ,  15.93171   ,   0.61525043],
                              [ 12.        ,  17.02170949,   0.61525043],
                              [ 12.        ,  13.80042   ,   1.84575128],
                              [ 12.        ,  15.22128   ,   1.84575128],
                              [ 12.        ,  11.99999051,   3.07625214],
                              [ 12.        ,  13.08999   ,   3.07625214],
                              [ 12.        ,  15.93171   ,   3.07625214],
                              [ 12.        ,  17.02170949,   3.07625214],
                              [ 12.        ,  13.80042   ,   4.30675299],
                              [ 12.        ,  15.22128   ,   4.30675299],
                              [ 12.        ,  11.99999051,   5.53725385],
                              [ 12.        ,  13.08999   ,   5.53725385],
                              [ 12.        ,  15.93171   ,   5.53725385],
                              [ 12.        ,  17.02170949,   5.53725385],
                              [ 12.        ,  13.80042   ,   6.7677547 ],
                              [ 12.        ,  15.22128   ,   6.7677547 ]]*Angstrom

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
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.0217, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.38300513133]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                            Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                            Carbon, Hydrogen, Carbon, Carbon]

# Define coordinates
right_electrode_coordinates = [[ 12.        ,  11.99999051,   0.61525043],
                               [ 12.        ,  13.08999   ,   0.61525043],
                               [ 12.        ,  15.93171   ,   0.61525043],
                               [ 12.        ,  17.02170949,   0.61525043],
                               [ 12.        ,  13.80042   ,   1.84575128],
                               [ 12.        ,  15.22128   ,   1.84575128],
                               [ 12.        ,  11.99999051,   3.07625214],
                               [ 12.        ,  13.08999   ,   3.07625214],
                               [ 12.        ,  15.93171   ,   3.07625214],
                               [ 12.        ,  17.02170949,   3.07625214],
                               [ 12.        ,  13.80042   ,   4.30675299],
                               [ 12.        ,  15.22128   ,   4.30675299],
                               [ 12.        ,  11.99999051,   5.53725385],
                               [ 12.        ,  13.08999   ,   5.53725385],
                               [ 12.        ,  15.93171   ,   5.53725385],
                               [ 12.        ,  17.02170949,   5.53725385],
                               [ 12.        ,  13.80042   ,   6.7677547 ],
                               [ 12.        ,  15.22128   ,   6.7677547 ]]*Angstrom

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
vector_a = [24.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.0217, 0.0]*Angstrom
vector_c = [0.0, 0.0, 49.2200342088]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon,
                           Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon,
                           Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon,
                           Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon,
                           Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon,
                           Hydrogen, Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen,
                           Carbon, Carbon, Hydrogen, Carbon, Carbon, Hydrogen, Carbon,
                           Carbon]

# Define coordinates
central_region_coordinates = [[ 12.        ,  11.99999051,   0.61525043],
                              [ 12.        ,  13.08999   ,   0.61525043],
                              [ 12.        ,  15.93171   ,   0.61525043],
                              [ 12.        ,  17.02170949,   0.61525043],
                              [ 12.        ,  13.80042   ,   1.84575128],
                              [ 12.        ,  15.22128   ,   1.84575128],
                              [ 12.        ,  11.99999051,   3.07625214],
                              [ 12.        ,  13.08999   ,   3.07625214],
                              [ 12.        ,  15.93171   ,   3.07625214],
                              [ 12.        ,  17.02170949,   3.07625214],
                              [ 12.        ,  13.80042   ,   4.30675299],
                              [ 12.        ,  15.22128   ,   4.30675299],
                              [ 12.        ,  11.99999051,   5.53725385],
                              [ 12.        ,  13.08999   ,   5.53725385],
                              [ 12.        ,  15.93171   ,   5.53725385],
                              [ 12.        ,  17.02170949,   5.53725385],
                              [ 12.        ,  13.80042   ,   6.7677547 ],
                              [ 12.        ,  15.22128   ,   6.7677547 ],
                              [ 12.        ,  11.99999051,   7.99825556],
                              [ 12.        ,  13.08999   ,   7.99825556],
                              [ 12.        ,  15.93171   ,   7.99825556],
                              [ 12.        ,  17.02170949,   7.99825556],
                              [ 12.        ,  13.80042   ,   9.22875641],
                              [ 12.        ,  15.22128   ,   9.22875641],
                              [ 12.        ,  11.99999051,  10.45925727],
                              [ 12.        ,  13.08999   ,  10.45925727],
                              [ 12.        ,  15.93171   ,  10.45925727],
                              [ 12.        ,  17.02170949,  10.45925727],
                              [ 12.        ,  13.80042   ,  11.68975812],
                              [ 12.        ,  15.22128   ,  11.68975812],
                              [ 12.        ,  11.99999051,  12.92025898],
                              [ 12.        ,  13.08999   ,  12.92025898],
                              [ 12.        ,  15.93171   ,  12.92025898],
                              [ 12.        ,  17.02170949,  12.92025898],
                              [ 12.        ,  13.80042   ,  14.15075984],
                              [ 12.        ,  15.22128   ,  14.15075984],
                              [ 12.        ,  11.99999051,  15.38126069],
                              [ 12.        ,  13.08999   ,  15.38126069],
                              [ 12.        ,  15.93171   ,  15.38126069],
                              [ 12.        ,  17.02170949,  15.38126069],
                              [ 12.        ,  13.80042   ,  16.61176155],
                              [ 12.        ,  15.22128   ,  16.61176155],
                              [ 12.        ,  11.99999051,  17.8422624 ],
                              [ 12.        ,  13.08999   ,  17.8422624 ],
                              [ 12.        ,  15.93171   ,  17.8422624 ],
                              [ 12.        ,  17.02170949,  17.8422624 ],
                              [ 12.        ,  13.80042   ,  19.07276326],
                              [ 12.        ,  15.22128   ,  19.07276326],
                              [ 12.        ,  11.99999051,  20.30326411],
                              [ 12.        ,  13.08999   ,  20.30326411],
                              [ 12.        ,  15.93171   ,  20.30326411],
                              [ 12.        ,  17.02170949,  20.30326411],
                              [ 12.        ,  13.80042   ,  21.53376497],
                              [ 12.        ,  15.22128   ,  21.53376497],
                              [ 12.        ,  11.99999051,  22.76426582],
                              [ 12.        ,  13.08999   ,  22.76426582],
                              [ 12.        ,  15.93171   ,  22.76426582],
                              [ 12.        ,  17.02170949,  22.76426582],
                              [ 12.        ,  13.80042   ,  23.99476668],
                              [ 12.        ,  15.22128   ,  23.99476668],
                              [ 12.        ,  11.99999051,  25.22526753],
                              [ 12.        ,  13.08999   ,  25.22526753],
                              [ 12.        ,  15.93171   ,  25.22526753],
                              [ 12.        ,  17.02170949,  25.22526753],
                              [ 12.        ,  13.80042   ,  26.45576839],
                              [ 12.        ,  15.22128   ,  26.45576839],
                              [ 12.        ,  11.99999051,  27.68626924],
                              [ 12.        ,  13.08999   ,  27.68626924],
                              [ 12.        ,  15.93171   ,  27.68626924],
                              [ 12.        ,  17.02170949,  27.68626924],
                              [ 12.        ,  13.80042   ,  28.9167701 ],
                              [ 12.        ,  15.22128   ,  28.9167701 ],
                              [ 12.        ,  11.99999051,  30.14727095],
                              [ 12.        ,  13.08999   ,  30.14727095],
                              [ 12.        ,  15.93171   ,  30.14727095],
                              [ 12.        ,  17.02170949,  30.14727095],
                              [ 12.        ,  13.80042   ,  31.37777181],
                              [ 12.        ,  15.22128   ,  31.37777181],
                              [ 12.        ,  11.99999051,  32.60827266],
                              [ 12.        ,  13.08999   ,  32.60827266],
                              [ 12.        ,  15.93171   ,  32.60827266],
                              [ 12.        ,  17.02170949,  32.60827266],
                              [ 12.        ,  13.80042   ,  33.83877352],
                              [ 12.        ,  15.22128   ,  33.83877352],
                              [ 12.        ,  11.99999051,  35.06927437],
                              [ 12.        ,  13.08999   ,  35.06927437],
                              [ 12.        ,  15.93171   ,  35.06927437],
                              [ 12.        ,  17.02170949,  35.06927437],
                              [ 12.        ,  13.80042   ,  36.29977523],
                              [ 12.        ,  15.22128   ,  36.29977523],
                              [ 12.        ,  11.99999051,  37.53027608],
                              [ 12.        ,  13.08999   ,  37.53027608],
                              [ 12.        ,  15.93171   ,  37.53027608],
                              [ 12.        ,  17.02170949,  37.53027608],
                              [ 12.        ,  13.80042   ,  38.76077694],
                              [ 12.        ,  15.22128   ,  38.76077694],
                              [ 12.        ,  11.99999051,  39.99127779],
                              [ 12.        ,  13.08999   ,  39.99127779],
                              [ 12.        ,  15.93171   ,  39.99127779],
                              [ 12.        ,  17.02170949,  39.99127779],
                              [ 12.        ,  13.80042   ,  41.22177865],
                              [ 12.        ,  15.22128   ,  41.22177865],
                              [ 12.        ,  11.99999051,  42.45227951],
                              [ 12.        ,  13.08999   ,  42.45227951],
                              [ 12.        ,  15.93171   ,  42.45227951],
                              [ 12.        ,  17.02170949,  42.45227951],
                              [ 12.        ,  13.80042   ,  43.68278036],
                              [ 12.        ,  15.22128   ,  43.68278036],
                              [ 12.        ,  11.99999051,  44.91328122],
                              [ 12.        ,  13.08999   ,  44.91328122],
                              [ 12.        ,  15.93171   ,  44.91328122],
                              [ 12.        ,  17.02170949,  44.91328122],
                              [ 12.        ,  13.80042   ,  46.14378207],
                              [ 12.        ,  15.22128   ,  46.14378207],
                              [ 12.        ,  11.99999051,  47.37428293],
                              [ 12.        ,  13.08999   ,  47.37428293],
                              [ 12.        ,  15.93171   ,  47.37428293],
                              [ 12.        ,  17.02170949,  47.37428293],
                              [ 12.        ,  13.80042   ,  48.60478378],
                              [ 12.        ,  15.22128   ,  48.60478378]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  1.0 *Angstrom,  xmax =  11.0 *Angstrom,
        ymin =  10.99999051 *Angstrom,  ymax =  18.02170949 *Angstrom,
        zmin =  9.30239189 *Angstrom,  zmax =  39.30239189 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  23.0 *Angstrom,  xmax =  13.0 *Angstrom,
        ymin =  10.99999051 *Angstrom,  ymax =  18.02170949 *Angstrom,
        zmin =  9.30239189 *Angstrom,  zmax =  39.30239189 *Angstrom,
)


dielectric_regions = [dielectric_region_0, dielectric_region_1]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  0.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  10.99999051 *Angstrom,  ymax =  18.02170949 *Angstrom,
        zmin =  9.30239189 *Angstrom,  zmax =  39.30239189 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  23.0 *Angstrom,  xmax =  24.0 *Angstrom,
        ymin =  10.99999051 *Angstrom,  ymax =  18.02170949 *Angstrom,
        zmin =  9.30239189 *Angstrom,  zmax =  39.30239189 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1]
central_region.setMetallicRegions(metallic_regions)
basis_set = [
    GGABasis.Carbon_DoubleZetaPolarized,
    GGABasis.Hydrogen_DoubleZetaPolarized,
    ]


#charge = (5.02Angstrom * 2Angstrom * 7.383Angstrom) * (5e20 cm^-3)
charge = 0.03706 
temp = 300
