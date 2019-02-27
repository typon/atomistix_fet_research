# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.0744, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0744, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.09916]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium]

# Define coordinates
left_electrode_coordinates = [[ 14.024805,  12.000015,   1.012395],
                              [ 18.074385,  12.000015,   1.012395],
                              [ 12.000015,  14.024805,   1.012395],
                              [ 16.049595,  14.024805,   1.012395],
                              [ 14.024805,  16.049595,   1.012395],
                              [ 18.074385,  16.049595,   1.012395],
                              [ 12.000015,  18.074385,   1.012395],
                              [ 16.049595,  18.074385,   1.012395],
                              [ 12.000015,  12.000015,   3.037185],
                              [ 16.049595,  12.000015,   3.037185],
                              [ 14.024805,  14.024805,   3.037185],
                              [ 18.074385,  14.024805,   3.037185],
                              [ 12.000015,  16.049595,   3.037185],
                              [ 16.049595,  16.049595,   3.037185],
                              [ 14.024805,  18.074385,   3.037185],
                              [ 18.074385,  18.074385,   3.037185],
                              [ 14.024805,  12.000015,   5.061975],
                              [ 18.074385,  12.000015,   5.061975],
                              [ 12.000015,  14.024805,   5.061975],
                              [ 16.049595,  14.024805,   5.061975],
                              [ 14.024805,  16.049595,   5.061975],
                              [ 18.074385,  16.049595,   5.061975],
                              [ 12.000015,  18.074385,   5.061975],
                              [ 16.049595,  18.074385,   5.061975],
                              [ 12.000015,  12.000015,   7.086765],
                              [ 16.049595,  12.000015,   7.086765],
                              [ 14.024805,  14.024805,   7.086765],
                              [ 18.074385,  14.024805,   7.086765],
                              [ 12.000015,  16.049595,   7.086765],
                              [ 16.049595,  16.049595,   7.086765],
                              [ 14.024805,  18.074385,   7.086765],
                              [ 18.074385,  18.074385,   7.086765]]*Angstrom

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
vector_a = [30.0744, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0744, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.09916]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                            Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                            Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                            Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                            Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                            Aluminium, Aluminium]

# Define coordinates
right_electrode_coordinates = [[ 14.024805,  12.000015,   1.012395],
                               [ 18.074385,  12.000015,   1.012395],
                               [ 12.000015,  14.024805,   1.012395],
                               [ 16.049595,  14.024805,   1.012395],
                               [ 14.024805,  16.049595,   1.012395],
                               [ 18.074385,  16.049595,   1.012395],
                               [ 12.000015,  18.074385,   1.012395],
                               [ 16.049595,  18.074385,   1.012395],
                               [ 12.000015,  12.000015,   3.037185],
                               [ 16.049595,  12.000015,   3.037185],
                               [ 14.024805,  14.024805,   3.037185],
                               [ 18.074385,  14.024805,   3.037185],
                               [ 12.000015,  16.049595,   3.037185],
                               [ 16.049595,  16.049595,   3.037185],
                               [ 14.024805,  18.074385,   3.037185],
                               [ 18.074385,  18.074385,   3.037185],
                               [ 14.024805,  12.000015,   5.061975],
                               [ 18.074385,  12.000015,   5.061975],
                               [ 12.000015,  14.024805,   5.061975],
                               [ 16.049595,  14.024805,   5.061975],
                               [ 14.024805,  16.049595,   5.061975],
                               [ 18.074385,  16.049595,   5.061975],
                               [ 12.000015,  18.074385,   5.061975],
                               [ 16.049595,  18.074385,   5.061975],
                               [ 12.000015,  12.000015,   7.086765],
                               [ 16.049595,  12.000015,   7.086765],
                               [ 14.024805,  14.024805,   7.086765],
                               [ 18.074385,  14.024805,   7.086765],
                               [ 12.000015,  16.049595,   7.086765],
                               [ 16.049595,  16.049595,   7.086765],
                               [ 14.024805,  18.074385,   7.086765],
                               [ 18.074385,  18.074385,   7.086765]]*Angstrom

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
vector_a = [30.0744, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0744, 0.0]*Angstrom
vector_c = [0.0, 0.0, 48.59496]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium,
                           Aluminium, Aluminium, Aluminium, Aluminium, Aluminium, Aluminium]

# Define coordinates
central_region_coordinates = [[ 14.024805,  12.000015,   1.012395],
                              [ 18.074385,  12.000015,   1.012395],
                              [ 12.000015,  14.024805,   1.012395],
                              [ 16.049595,  14.024805,   1.012395],
                              [ 14.024805,  16.049595,   1.012395],
                              [ 18.074385,  16.049595,   1.012395],
                              [ 12.000015,  18.074385,   1.012395],
                              [ 16.049595,  18.074385,   1.012395],
                              [ 12.000015,  12.000015,   3.037185],
                              [ 16.049595,  12.000015,   3.037185],
                              [ 14.024805,  14.024805,   3.037185],
                              [ 18.074385,  14.024805,   3.037185],
                              [ 12.000015,  16.049595,   3.037185],
                              [ 16.049595,  16.049595,   3.037185],
                              [ 14.024805,  18.074385,   3.037185],
                              [ 18.074385,  18.074385,   3.037185],
                              [ 14.024805,  12.000015,   5.061975],
                              [ 18.074385,  12.000015,   5.061975],
                              [ 12.000015,  14.024805,   5.061975],
                              [ 16.049595,  14.024805,   5.061975],
                              [ 14.024805,  16.049595,   5.061975],
                              [ 18.074385,  16.049595,   5.061975],
                              [ 12.000015,  18.074385,   5.061975],
                              [ 16.049595,  18.074385,   5.061975],
                              [ 12.000015,  12.000015,   7.086765],
                              [ 16.049595,  12.000015,   7.086765],
                              [ 14.024805,  14.024805,   7.086765],
                              [ 18.074385,  14.024805,   7.086765],
                              [ 12.000015,  16.049595,   7.086765],
                              [ 16.049595,  16.049595,   7.086765],
                              [ 14.024805,  18.074385,   7.086765],
                              [ 18.074385,  18.074385,   7.086765],
                              [ 14.024805,  12.000015,   9.111555],
                              [ 18.074385,  12.000015,   9.111555],
                              [ 12.000015,  14.024805,   9.111555],
                              [ 16.049595,  14.024805,   9.111555],
                              [ 14.024805,  16.049595,   9.111555],
                              [ 18.074385,  16.049595,   9.111555],
                              [ 12.000015,  18.074385,   9.111555],
                              [ 16.049595,  18.074385,   9.111555],
                              [ 12.000015,  12.000015,  11.136345],
                              [ 16.049595,  12.000015,  11.136345],
                              [ 14.024805,  14.024805,  11.136345],
                              [ 18.074385,  14.024805,  11.136345],
                              [ 12.000015,  16.049595,  11.136345],
                              [ 16.049595,  16.049595,  11.136345],
                              [ 14.024805,  18.074385,  11.136345],
                              [ 18.074385,  18.074385,  11.136345],
                              [ 14.024805,  12.000015,  13.161135],
                              [ 18.074385,  12.000015,  13.161135],
                              [ 12.000015,  14.024805,  13.161135],
                              [ 16.049595,  14.024805,  13.161135],
                              [ 14.024805,  16.049595,  13.161135],
                              [ 18.074385,  16.049595,  13.161135],
                              [ 12.000015,  18.074385,  13.161135],
                              [ 16.049595,  18.074385,  13.161135],
                              [ 12.000015,  12.000015,  15.185925],
                              [ 16.049595,  12.000015,  15.185925],
                              [ 14.024805,  14.024805,  15.185925],
                              [ 18.074385,  14.024805,  15.185925],
                              [ 12.000015,  16.049595,  15.185925],
                              [ 16.049595,  16.049595,  15.185925],
                              [ 14.024805,  18.074385,  15.185925],
                              [ 18.074385,  18.074385,  15.185925],
                              [ 14.024805,  12.000015,  17.210715],
                              [ 18.074385,  12.000015,  17.210715],
                              [ 12.000015,  14.024805,  17.210715],
                              [ 16.049595,  14.024805,  17.210715],
                              [ 14.024805,  16.049595,  17.210715],
                              [ 18.074385,  16.049595,  17.210715],
                              [ 12.000015,  18.074385,  17.210715],
                              [ 16.049595,  18.074385,  17.210715],
                              [ 12.000015,  12.000015,  19.235505],
                              [ 16.049595,  12.000015,  19.235505],
                              [ 14.024805,  14.024805,  19.235505],
                              [ 18.074385,  14.024805,  19.235505],
                              [ 12.000015,  16.049595,  19.235505],
                              [ 16.049595,  16.049595,  19.235505],
                              [ 14.024805,  18.074385,  19.235505],
                              [ 18.074385,  18.074385,  19.235505],
                              [ 14.024805,  12.000015,  21.260295],
                              [ 18.074385,  12.000015,  21.260295],
                              [ 12.000015,  14.024805,  21.260295],
                              [ 16.049595,  14.024805,  21.260295],
                              [ 14.024805,  16.049595,  21.260295],
                              [ 18.074385,  16.049595,  21.260295],
                              [ 12.000015,  18.074385,  21.260295],
                              [ 16.049595,  18.074385,  21.260295],
                              [ 12.000015,  12.000015,  23.285085],
                              [ 16.049595,  12.000015,  23.285085],
                              [ 14.024805,  14.024805,  23.285085],
                              [ 18.074385,  14.024805,  23.285085],
                              [ 12.000015,  16.049595,  23.285085],
                              [ 16.049595,  16.049595,  23.285085],
                              [ 14.024805,  18.074385,  23.285085],
                              [ 18.074385,  18.074385,  23.285085],
                              [ 14.024805,  12.000015,  25.309875],
                              [ 18.074385,  12.000015,  25.309875],
                              [ 12.000015,  14.024805,  25.309875],
                              [ 16.049595,  14.024805,  25.309875],
                              [ 14.024805,  16.049595,  25.309875],
                              [ 18.074385,  16.049595,  25.309875],
                              [ 12.000015,  18.074385,  25.309875],
                              [ 16.049595,  18.074385,  25.309875],
                              [ 12.000015,  12.000015,  27.334665],
                              [ 16.049595,  12.000015,  27.334665],
                              [ 14.024805,  14.024805,  27.334665],
                              [ 18.074385,  14.024805,  27.334665],
                              [ 12.000015,  16.049595,  27.334665],
                              [ 16.049595,  16.049595,  27.334665],
                              [ 14.024805,  18.074385,  27.334665],
                              [ 18.074385,  18.074385,  27.334665],
                              [ 14.024805,  12.000015,  29.359455],
                              [ 18.074385,  12.000015,  29.359455],
                              [ 12.000015,  14.024805,  29.359455],
                              [ 16.049595,  14.024805,  29.359455],
                              [ 14.024805,  16.049595,  29.359455],
                              [ 18.074385,  16.049595,  29.359455],
                              [ 12.000015,  18.074385,  29.359455],
                              [ 16.049595,  18.074385,  29.359455],
                              [ 12.000015,  12.000015,  31.384245],
                              [ 16.049595,  12.000015,  31.384245],
                              [ 14.024805,  14.024805,  31.384245],
                              [ 18.074385,  14.024805,  31.384245],
                              [ 12.000015,  16.049595,  31.384245],
                              [ 16.049595,  16.049595,  31.384245],
                              [ 14.024805,  18.074385,  31.384245],
                              [ 18.074385,  18.074385,  31.384245],
                              [ 14.024805,  12.000015,  33.409035],
                              [ 18.074385,  12.000015,  33.409035],
                              [ 12.000015,  14.024805,  33.409035],
                              [ 16.049595,  14.024805,  33.409035],
                              [ 14.024805,  16.049595,  33.409035],
                              [ 18.074385,  16.049595,  33.409035],
                              [ 12.000015,  18.074385,  33.409035],
                              [ 16.049595,  18.074385,  33.409035],
                              [ 12.000015,  12.000015,  35.433825],
                              [ 16.049595,  12.000015,  35.433825],
                              [ 14.024805,  14.024805,  35.433825],
                              [ 18.074385,  14.024805,  35.433825],
                              [ 12.000015,  16.049595,  35.433825],
                              [ 16.049595,  16.049595,  35.433825],
                              [ 14.024805,  18.074385,  35.433825],
                              [ 18.074385,  18.074385,  35.433825],
                              [ 14.024805,  12.000015,  37.458615],
                              [ 18.074385,  12.000015,  37.458615],
                              [ 12.000015,  14.024805,  37.458615],
                              [ 16.049595,  14.024805,  37.458615],
                              [ 14.024805,  16.049595,  37.458615],
                              [ 18.074385,  16.049595,  37.458615],
                              [ 12.000015,  18.074385,  37.458615],
                              [ 16.049595,  18.074385,  37.458615],
                              [ 12.000015,  12.000015,  39.483405],
                              [ 16.049595,  12.000015,  39.483405],
                              [ 14.024805,  14.024805,  39.483405],
                              [ 18.074385,  14.024805,  39.483405],
                              [ 12.000015,  16.049595,  39.483405],
                              [ 16.049595,  16.049595,  39.483405],
                              [ 14.024805,  18.074385,  39.483405],
                              [ 18.074385,  18.074385,  39.483405],
                              [ 14.024805,  12.000015,  41.508195],
                              [ 18.074385,  12.000015,  41.508195],
                              [ 12.000015,  14.024805,  41.508195],
                              [ 16.049595,  14.024805,  41.508195],
                              [ 14.024805,  16.049595,  41.508195],
                              [ 18.074385,  16.049595,  41.508195],
                              [ 12.000015,  18.074385,  41.508195],
                              [ 16.049595,  18.074385,  41.508195],
                              [ 12.000015,  12.000015,  43.532985],
                              [ 16.049595,  12.000015,  43.532985],
                              [ 14.024805,  14.024805,  43.532985],
                              [ 18.074385,  14.024805,  43.532985],
                              [ 12.000015,  16.049595,  43.532985],
                              [ 16.049595,  16.049595,  43.532985],
                              [ 14.024805,  18.074385,  43.532985],
                              [ 18.074385,  18.074385,  43.532985],
                              [ 14.024805,  12.000015,  45.557775],
                              [ 18.074385,  12.000015,  45.557775],
                              [ 12.000015,  14.024805,  45.557775],
                              [ 16.049595,  14.024805,  45.557775],
                              [ 14.024805,  16.049595,  45.557775],
                              [ 18.074385,  16.049595,  45.557775],
                              [ 12.000015,  18.074385,  45.557775],
                              [ 16.049595,  18.074385,  45.557775],
                              [ 12.000015,  12.000015,  47.582565],
                              [ 16.049595,  12.000015,  47.582565],
                              [ 14.024805,  14.024805,  47.582565],
                              [ 18.074385,  14.024805,  47.582565],
                              [ 12.000015,  16.049595,  47.582565],
                              [ 16.049595,  16.049595,  47.582565],
                              [ 14.024805,  18.074385,  47.582565],
                              [ 18.074385,  18.074385,  47.582565]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.000015 *Angstrom,  xmax =  1.000015 *Angstrom,
        ymin =  11.000015 *Angstrom,  ymax =  19.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.000015 *Angstrom,  xmax =  19.074385 *Angstrom,
        ymin =  19.074385 *Angstrom,  ymax =  29.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.074385 *Angstrom,  xmax =  29.074385 *Angstrom,
        ymin =  11.000015 *Angstrom,  ymax =  19.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.000015 *Angstrom,  xmax =  19.074385 *Angstrom,
        ymin =  11.000015 *Angstrom,  ymax =  1.000015 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.000015 *Angstrom,  xmax =  1.000015 *Angstrom,
        ymin =  11.000015 *Angstrom,  ymax =  1.000015 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.000015 *Angstrom,  xmax =  1.000015 *Angstrom,
        ymin =  19.074385 *Angstrom,  ymax =  29.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.074385 *Angstrom,  xmax =  29.074385 *Angstrom,
        ymin =  19.074385 *Angstrom,  ymax =  29.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.074385 *Angstrom,  xmax =  29.074385 *Angstrom,
        ymin =  11.000015 *Angstrom,  ymax =  1.000015 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.000015 *Angstrom,  xmax =  1.49999999994e-05 *Angstrom,
        ymin =  1.000015 *Angstrom,  ymax =  29.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.49999999994e-05 *Angstrom,  xmax =  30.074385 *Angstrom,
        ymin =  29.074385 *Angstrom,  ymax =  30.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.074385 *Angstrom,  xmax =  30.074385 *Angstrom,
        ymin =  1.000015 *Angstrom,  ymax =  29.074385 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.49999999994e-05 *Angstrom,  xmax =  30.074385 *Angstrom,
        ymin =  1.000015 *Angstrom,  ymax =  1.49999999994e-05 *Angstrom,
        zmin =  8.7912825 *Angstrom,  zmax =  38.7912825 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)


device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

