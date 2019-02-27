# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [35.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5350329215]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 15.460875  ,  16.05812088,   0.72093956],
                              [ 19.539125  ,  16.05812088,   0.72093956],
                              [ 15.460875  ,  18.94187912,   0.72093956],
                              [ 19.539125  ,  18.94187912,   0.72093956],
                              [ 17.5       ,  14.61624177,   2.16281867],
                              [ 17.5       ,  17.5       ,   2.16281867],
                              [ 17.5       ,  20.38375823,   2.16281867],
                              [ 15.460875  ,  16.05812088,   3.60469779],
                              [ 19.539125  ,  16.05812088,   3.60469779],
                              [ 15.460875  ,  18.94187912,   3.60469779],
                              [ 19.539125  ,  18.94187912,   3.60469779],
                              [ 17.5       ,  17.5       ,   5.0465769 ],
                              [ 15.460875  ,  16.05812088,   6.48845602],
                              [ 19.539125  ,  16.05812088,   6.48845602],
                              [ 15.460875  ,  18.94187912,   6.48845602],
                              [ 19.539125  ,  18.94187912,   6.48845602],
                              [ 17.5       ,  14.61624177,   7.93033513],
                              [ 17.5       ,  17.5       ,   7.93033513],
                              [ 17.5       ,  20.38375823,   7.93033513],
                              [ 15.460875  ,  16.05812088,   9.37221425],
                              [ 19.539125  ,  16.05812088,   9.37221425],
                              [ 15.460875  ,  18.94187912,   9.37221425],
                              [ 19.539125  ,  18.94187912,   9.37221425],
                              [ 17.5       ,  17.5       ,  10.81409336]]*Angstrom

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
vector_a = [35.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.5350329215]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 15.460875  ,  16.05812088,   0.72093956],
                               [ 19.539125  ,  16.05812088,   0.72093956],
                               [ 15.460875  ,  18.94187912,   0.72093956],
                               [ 19.539125  ,  18.94187912,   0.72093956],
                               [ 17.5       ,  14.61624177,   2.16281867],
                               [ 17.5       ,  17.5       ,   2.16281867],
                               [ 17.5       ,  20.38375823,   2.16281867],
                               [ 15.460875  ,  16.05812088,   3.60469779],
                               [ 19.539125  ,  16.05812088,   3.60469779],
                               [ 15.460875  ,  18.94187912,   3.60469779],
                               [ 19.539125  ,  18.94187912,   3.60469779],
                               [ 17.5       ,  17.5       ,   5.0465769 ],
                               [ 15.460875  ,  16.05812088,   6.48845602],
                               [ 19.539125  ,  16.05812088,   6.48845602],
                               [ 15.460875  ,  18.94187912,   6.48845602],
                               [ 19.539125  ,  18.94187912,   6.48845602],
                               [ 17.5       ,  14.61624177,   7.93033513],
                               [ 17.5       ,  17.5       ,   7.93033513],
                               [ 17.5       ,  20.38375823,   7.93033513],
                               [ 15.460875  ,  16.05812088,   9.37221425],
                               [ 19.539125  ,  16.05812088,   9.37221425],
                               [ 15.460875  ,  18.94187912,   9.37221425],
                               [ 19.539125  ,  18.94187912,   9.37221425],
                               [ 17.5       ,  17.5       ,  10.81409336]]*Angstrom

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
vector_a = [35.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 35.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 51.9076481467]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 15.460875  ,  16.05812088,   0.72093956],
                              [ 19.539125  ,  16.05812088,   0.72093956],
                              [ 15.460875  ,  18.94187912,   0.72093956],
                              [ 19.539125  ,  18.94187912,   0.72093956],
                              [ 17.5       ,  14.61624177,   2.16281867],
                              [ 17.5       ,  17.5       ,   2.16281867],
                              [ 17.5       ,  20.38375823,   2.16281867],
                              [ 15.460875  ,  16.05812088,   3.60469779],
                              [ 19.539125  ,  16.05812088,   3.60469779],
                              [ 15.460875  ,  18.94187912,   3.60469779],
                              [ 19.539125  ,  18.94187912,   3.60469779],
                              [ 17.5       ,  17.5       ,   5.0465769 ],
                              [ 15.460875  ,  16.05812088,   6.48845602],
                              [ 19.539125  ,  16.05812088,   6.48845602],
                              [ 15.460875  ,  18.94187912,   6.48845602],
                              [ 19.539125  ,  18.94187912,   6.48845602],
                              [ 17.5       ,  14.61624177,   7.93033513],
                              [ 17.5       ,  17.5       ,   7.93033513],
                              [ 17.5       ,  20.38375823,   7.93033513],
                              [ 15.460875  ,  16.05812088,   9.37221425],
                              [ 19.539125  ,  16.05812088,   9.37221425],
                              [ 15.460875  ,  18.94187912,   9.37221425],
                              [ 19.539125  ,  18.94187912,   9.37221425],
                              [ 17.5       ,  17.5       ,  10.81409336],
                              [ 15.460875  ,  16.05812088,  12.25597248],
                              [ 19.539125  ,  16.05812088,  12.25597248],
                              [ 15.460875  ,  18.94187912,  12.25597248],
                              [ 19.539125  ,  18.94187912,  12.25597248],
                              [ 17.5       ,  14.61624177,  13.69785159],
                              [ 17.5       ,  17.5       ,  13.69785159],
                              [ 17.5       ,  20.38375823,  13.69785159],
                              [ 15.460875  ,  16.05812088,  15.13973071],
                              [ 19.539125  ,  16.05812088,  15.13973071],
                              [ 15.460875  ,  18.94187912,  15.13973071],
                              [ 19.539125  ,  18.94187912,  15.13973071],
                              [ 17.5       ,  17.5       ,  16.58160982],
                              [ 15.460875  ,  16.05812088,  18.02348894],
                              [ 19.539125  ,  16.05812088,  18.02348894],
                              [ 15.460875  ,  18.94187912,  18.02348894],
                              [ 19.539125  ,  18.94187912,  18.02348894],
                              [ 17.5       ,  14.61624177,  19.46536806],
                              [ 17.5       ,  17.5       ,  19.46536806],
                              [ 17.5       ,  20.38375823,  19.46536806],
                              [ 15.460875  ,  16.05812088,  20.90724717],
                              [ 19.539125  ,  16.05812088,  20.90724717],
                              [ 15.460875  ,  18.94187912,  20.90724717],
                              [ 19.539125  ,  18.94187912,  20.90724717],
                              [ 17.5       ,  17.5       ,  22.34912629],
                              [ 15.460875  ,  16.05812088,  23.7910054 ],
                              [ 19.539125  ,  16.05812088,  23.7910054 ],
                              [ 15.460875  ,  18.94187912,  23.7910054 ],
                              [ 19.539125  ,  18.94187912,  23.7910054 ],
                              [ 17.5       ,  14.61624177,  25.23288452],
                              [ 17.5       ,  17.5       ,  25.23288452],
                              [ 17.5       ,  20.38375823,  25.23288452],
                              [ 15.460875  ,  16.05812088,  26.67476363],
                              [ 19.539125  ,  16.05812088,  26.67476363],
                              [ 15.460875  ,  18.94187912,  26.67476363],
                              [ 19.539125  ,  18.94187912,  26.67476363],
                              [ 17.5       ,  17.5       ,  28.11664275],
                              [ 15.460875  ,  16.05812088,  29.55852186],
                              [ 19.539125  ,  16.05812088,  29.55852186],
                              [ 15.460875  ,  18.94187912,  29.55852186],
                              [ 19.539125  ,  18.94187912,  29.55852186],
                              [ 17.5       ,  14.61624177,  31.00040098],
                              [ 17.5       ,  17.5       ,  31.00040098],
                              [ 17.5       ,  20.38375823,  31.00040098],
                              [ 15.460875  ,  16.05812088,  32.44228009],
                              [ 19.539125  ,  16.05812088,  32.44228009],
                              [ 15.460875  ,  18.94187912,  32.44228009],
                              [ 19.539125  ,  18.94187912,  32.44228009],
                              [ 17.5       ,  17.5       ,  33.88415921],
                              [ 15.460875  ,  16.05812088,  35.32603832],
                              [ 19.539125  ,  16.05812088,  35.32603832],
                              [ 15.460875  ,  18.94187912,  35.32603832],
                              [ 19.539125  ,  18.94187912,  35.32603832],
                              [ 17.5       ,  14.61624177,  36.76791744],
                              [ 17.5       ,  17.5       ,  36.76791744],
                              [ 17.5       ,  20.38375823,  36.76791744],
                              [ 15.460875  ,  16.05812088,  38.20979655],
                              [ 19.539125  ,  16.05812088,  38.20979655],
                              [ 15.460875  ,  18.94187912,  38.20979655],
                              [ 19.539125  ,  18.94187912,  38.20979655],
                              [ 17.5       ,  17.5       ,  39.65167567],
                              [ 15.460875  ,  16.05812088,  41.09355478],
                              [ 19.539125  ,  16.05812088,  41.09355478],
                              [ 15.460875  ,  18.94187912,  41.09355478],
                              [ 19.539125  ,  18.94187912,  41.09355478],
                              [ 17.5       ,  14.61624177,  42.5354339 ],
                              [ 17.5       ,  17.5       ,  42.5354339 ],
                              [ 17.5       ,  20.38375823,  42.5354339 ],
                              [ 15.460875  ,  16.05812088,  43.97731301],
                              [ 19.539125  ,  16.05812088,  43.97731301],
                              [ 15.460875  ,  18.94187912,  43.97731301],
                              [ 19.539125  ,  18.94187912,  43.97731301],
                              [ 17.5       ,  17.5       ,  45.41919213],
                              [ 15.460875  ,  16.05812088,  46.86107124],
                              [ 19.539125  ,  16.05812088,  46.86107124],
                              [ 15.460875  ,  18.94187912,  46.86107124],
                              [ 19.539125  ,  18.94187912,  46.86107124],
                              [ 17.5       ,  14.61624177,  48.30295036],
                              [ 17.5       ,  17.5       ,  48.30295036],
                              [ 17.5       ,  20.38375823,  48.30295036],
                              [ 15.460875  ,  16.05812088,  49.74482947],
                              [ 19.539125  ,  16.05812088,  49.74482947],
                              [ 15.460875  ,  18.94187912,  49.74482947],
                              [ 19.539125  ,  18.94187912,  49.74482947],
                              [ 17.5       ,  17.5       ,  51.18670859]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region

metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  4.460875 *Angstrom,  xmax =  3.460875 *Angstrom,
        ymin =  3.61624177 *Angstrom,  ymax =  31.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  3.460875 *Angstrom,  xmax =  31.539125 *Angstrom,
        ymin =  31.38375823 *Angstrom,  ymax =  32.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  30.539125 *Angstrom,  xmax =  31.539125 *Angstrom,
        ymin =  3.61624177 *Angstrom,  ymax =  31.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  3.460875 *Angstrom,  xmax =  31.539125 *Angstrom,
        ymin =  3.61624177 *Angstrom,  ymax =  2.61624177 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)


metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  14.460875 *Angstrom,  xmax =  4.460875 *Angstrom,
        ymin =  13.61624177 *Angstrom,  ymax =  21.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  14.460875 *Angstrom,  xmax =  20.539125 *Angstrom,
        ymin =  21.38375823 *Angstrom,  ymax =  31.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  20.539125 *Angstrom,  xmax =  30.539125 *Angstrom,
        ymin =  13.61624177 *Angstrom,  ymax =  21.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  14.460875 *Angstrom,  xmax =  20.539125 *Angstrom,
        ymin =  13.61624177 *Angstrom,  ymax =  3.61624177 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  14.460875 *Angstrom,  xmax =  4.460875 *Angstrom,
        ymin =  13.61624177 *Angstrom,  ymax =  3.61624177 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  14.460875 *Angstrom,  xmax =  4.460875 *Angstrom,
        ymin =  21.38375823 *Angstrom,  ymax =  31.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  20.539125 *Angstrom,  xmax =  30.539125 *Angstrom,
        ymin =  21.38375823 *Angstrom,  ymax =  31.38375823 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  20.539125 *Angstrom,  xmax =  30.539125 *Angstrom,
        ymin =  13.61624177 *Angstrom,  ymax =  3.61624177 *Angstrom,
        zmin =  10.593354295 *Angstrom,  zmax =  40.593354295 *Angstrom,
)


dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


