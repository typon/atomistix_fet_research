# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                              [ 16.0782625,  12.0000125,   1.0195625],
                              [ 14.0391375,  14.0391375,   1.0195625],
                              [ 18.1173875,  14.0391375,   1.0195625],
                              [ 12.0000125,  16.0782625,   1.0195625],
                              [ 16.0782625,  16.0782625,   1.0195625],
                              [ 14.0391375,  18.1173875,   1.0195625],
                              [ 18.1173875,  18.1173875,   1.0195625],
                              [ 14.0391375,  12.0000125,   3.0586875],
                              [ 18.1173875,  12.0000125,   3.0586875],
                              [ 12.0000125,  14.0391375,   3.0586875],
                              [ 16.0782625,  14.0391375,   3.0586875],
                              [ 14.0391375,  16.0782625,   3.0586875],
                              [ 18.1173875,  16.0782625,   3.0586875],
                              [ 12.0000125,  18.1173875,   3.0586875],
                              [ 16.0782625,  18.1173875,   3.0586875],
                              [ 12.0000125,  12.0000125,   5.0978125],
                              [ 16.0782625,  12.0000125,   5.0978125],
                              [ 14.0391375,  14.0391375,   5.0978125],
                              [ 18.1173875,  14.0391375,   5.0978125],
                              [ 12.0000125,  16.0782625,   5.0978125],
                              [ 16.0782625,  16.0782625,   5.0978125],
                              [ 14.0391375,  18.1173875,   5.0978125],
                              [ 18.1173875,  18.1173875,   5.0978125],
                              [ 14.0391375,  12.0000125,   7.1369375],
                              [ 18.1173875,  12.0000125,   7.1369375],
                              [ 12.0000125,  14.0391375,   7.1369375],
                              [ 16.0782625,  14.0391375,   7.1369375],
                              [ 14.0391375,  16.0782625,   7.1369375],
                              [ 18.1173875,  16.0782625,   7.1369375],
                              [ 12.0000125,  18.1173875,   7.1369375],
                              [ 16.0782625,  18.1173875,   7.1369375]]*Angstrom

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
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                               [ 16.0782625,  12.0000125,   1.0195625],
                               [ 14.0391375,  14.0391375,   1.0195625],
                               [ 18.1173875,  14.0391375,   1.0195625],
                               [ 12.0000125,  16.0782625,   1.0195625],
                               [ 16.0782625,  16.0782625,   1.0195625],
                               [ 14.0391375,  18.1173875,   1.0195625],
                               [ 18.1173875,  18.1173875,   1.0195625],
                               [ 14.0391375,  12.0000125,   3.0586875],
                               [ 18.1173875,  12.0000125,   3.0586875],
                               [ 12.0000125,  14.0391375,   3.0586875],
                               [ 16.0782625,  14.0391375,   3.0586875],
                               [ 14.0391375,  16.0782625,   3.0586875],
                               [ 18.1173875,  16.0782625,   3.0586875],
                               [ 12.0000125,  18.1173875,   3.0586875],
                               [ 16.0782625,  18.1173875,   3.0586875],
                               [ 12.0000125,  12.0000125,   5.0978125],
                               [ 16.0782625,  12.0000125,   5.0978125],
                               [ 14.0391375,  14.0391375,   5.0978125],
                               [ 18.1173875,  14.0391375,   5.0978125],
                               [ 12.0000125,  16.0782625,   5.0978125],
                               [ 16.0782625,  16.0782625,   5.0978125],
                               [ 14.0391375,  18.1173875,   5.0978125],
                               [ 18.1173875,  18.1173875,   5.0978125],
                               [ 14.0391375,  12.0000125,   7.1369375],
                               [ 18.1173875,  12.0000125,   7.1369375],
                               [ 12.0000125,  14.0391375,   7.1369375],
                               [ 16.0782625,  14.0391375,   7.1369375],
                               [ 14.0391375,  16.0782625,   7.1369375],
                               [ 18.1173875,  16.0782625,   7.1369375],
                               [ 12.0000125,  18.1173875,   7.1369375],
                               [ 16.0782625,  18.1173875,   7.1369375]]*Angstrom

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
vector_a = [30.1174, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.1174, 0.0]*Angstrom
vector_c = [0.0, 0.0, 89.7215]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 12.0000125,  12.0000125,   1.0195625],
                              [ 16.0782625,  12.0000125,   1.0195625],
                              [ 14.0391375,  14.0391375,   1.0195625],
                              [ 18.1173875,  14.0391375,   1.0195625],
                              [ 12.0000125,  16.0782625,   1.0195625],
                              [ 16.0782625,  16.0782625,   1.0195625],
                              [ 14.0391375,  18.1173875,   1.0195625],
                              [ 18.1173875,  18.1173875,   1.0195625],
                              [ 14.0391375,  12.0000125,   3.0586875],
                              [ 18.1173875,  12.0000125,   3.0586875],
                              [ 12.0000125,  14.0391375,   3.0586875],
                              [ 16.0782625,  14.0391375,   3.0586875],
                              [ 14.0391375,  16.0782625,   3.0586875],
                              [ 18.1173875,  16.0782625,   3.0586875],
                              [ 12.0000125,  18.1173875,   3.0586875],
                              [ 16.0782625,  18.1173875,   3.0586875],
                              [ 12.0000125,  12.0000125,   5.0978125],
                              [ 16.0782625,  12.0000125,   5.0978125],
                              [ 14.0391375,  14.0391375,   5.0978125],
                              [ 18.1173875,  14.0391375,   5.0978125],
                              [ 12.0000125,  16.0782625,   5.0978125],
                              [ 16.0782625,  16.0782625,   5.0978125],
                              [ 14.0391375,  18.1173875,   5.0978125],
                              [ 18.1173875,  18.1173875,   5.0978125],
                              [ 14.0391375,  12.0000125,   7.1369375],
                              [ 18.1173875,  12.0000125,   7.1369375],
                              [ 12.0000125,  14.0391375,   7.1369375],
                              [ 16.0782625,  14.0391375,   7.1369375],
                              [ 14.0391375,  16.0782625,   7.1369375],
                              [ 18.1173875,  16.0782625,   7.1369375],
                              [ 12.0000125,  18.1173875,   7.1369375],
                              [ 16.0782625,  18.1173875,   7.1369375],
                              [ 12.0000125,  12.0000125,   9.1760625],
                              [ 16.0782625,  12.0000125,   9.1760625],
                              [ 14.0391375,  14.0391375,   9.1760625],
                              [ 18.1173875,  14.0391375,   9.1760625],
                              [ 12.0000125,  16.0782625,   9.1760625],
                              [ 16.0782625,  16.0782625,   9.1760625],
                              [ 14.0391375,  18.1173875,   9.1760625],
                              [ 18.1173875,  18.1173875,   9.1760625],
                              [ 14.0391375,  12.0000125,  11.2151875],
                              [ 18.1173875,  12.0000125,  11.2151875],
                              [ 12.0000125,  14.0391375,  11.2151875],
                              [ 16.0782625,  14.0391375,  11.2151875],
                              [ 14.0391375,  16.0782625,  11.2151875],
                              [ 18.1173875,  16.0782625,  11.2151875],
                              [ 12.0000125,  18.1173875,  11.2151875],
                              [ 16.0782625,  18.1173875,  11.2151875],
                              [ 12.0000125,  12.0000125,  13.2543125],
                              [ 16.0782625,  12.0000125,  13.2543125],
                              [ 14.0391375,  14.0391375,  13.2543125],
                              [ 18.1173875,  14.0391375,  13.2543125],
                              [ 12.0000125,  16.0782625,  13.2543125],
                              [ 16.0782625,  16.0782625,  13.2543125],
                              [ 14.0391375,  18.1173875,  13.2543125],
                              [ 18.1173875,  18.1173875,  13.2543125],
                              [ 14.0391375,  12.0000125,  15.2934375],
                              [ 18.1173875,  12.0000125,  15.2934375],
                              [ 12.0000125,  14.0391375,  15.2934375],
                              [ 16.0782625,  14.0391375,  15.2934375],
                              [ 14.0391375,  16.0782625,  15.2934375],
                              [ 18.1173875,  16.0782625,  15.2934375],
                              [ 12.0000125,  18.1173875,  15.2934375],
                              [ 16.0782625,  18.1173875,  15.2934375],
                              [ 12.0000125,  12.0000125,  17.3325625],
                              [ 16.0782625,  12.0000125,  17.3325625],
                              [ 14.0391375,  14.0391375,  17.3325625],
                              [ 18.1173875,  14.0391375,  17.3325625],
                              [ 12.0000125,  16.0782625,  17.3325625],
                              [ 16.0782625,  16.0782625,  17.3325625],
                              [ 14.0391375,  18.1173875,  17.3325625],
                              [ 18.1173875,  18.1173875,  17.3325625],
                              [ 14.0391375,  12.0000125,  19.3716875],
                              [ 18.1173875,  12.0000125,  19.3716875],
                              [ 12.0000125,  14.0391375,  19.3716875],
                              [ 16.0782625,  14.0391375,  19.3716875],
                              [ 14.0391375,  16.0782625,  19.3716875],
                              [ 18.1173875,  16.0782625,  19.3716875],
                              [ 12.0000125,  18.1173875,  19.3716875],
                              [ 16.0782625,  18.1173875,  19.3716875],
                              [ 12.0000125,  12.0000125,  21.4108125],
                              [ 16.0782625,  12.0000125,  21.4108125],
                              [ 14.0391375,  14.0391375,  21.4108125],
                              [ 18.1173875,  14.0391375,  21.4108125],
                              [ 12.0000125,  16.0782625,  21.4108125],
                              [ 16.0782625,  16.0782625,  21.4108125],
                              [ 14.0391375,  18.1173875,  21.4108125],
                              [ 18.1173875,  18.1173875,  21.4108125],
                              [ 14.0391375,  12.0000125,  23.4499375],
                              [ 18.1173875,  12.0000125,  23.4499375],
                              [ 12.0000125,  14.0391375,  23.4499375],
                              [ 16.0782625,  14.0391375,  23.4499375],
                              [ 14.0391375,  16.0782625,  23.4499375],
                              [ 18.1173875,  16.0782625,  23.4499375],
                              [ 12.0000125,  18.1173875,  23.4499375],
                              [ 16.0782625,  18.1173875,  23.4499375],
                              [ 12.0000125,  12.0000125,  25.4890625],
                              [ 16.0782625,  12.0000125,  25.4890625],
                              [ 14.0391375,  14.0391375,  25.4890625],
                              [ 18.1173875,  14.0391375,  25.4890625],
                              [ 12.0000125,  16.0782625,  25.4890625],
                              [ 16.0782625,  16.0782625,  25.4890625],
                              [ 14.0391375,  18.1173875,  25.4890625],
                              [ 18.1173875,  18.1173875,  25.4890625],
                              [ 14.0391375,  12.0000125,  27.5281875],
                              [ 18.1173875,  12.0000125,  27.5281875],
                              [ 12.0000125,  14.0391375,  27.5281875],
                              [ 16.0782625,  14.0391375,  27.5281875],
                              [ 14.0391375,  16.0782625,  27.5281875],
                              [ 18.1173875,  16.0782625,  27.5281875],
                              [ 12.0000125,  18.1173875,  27.5281875],
                              [ 16.0782625,  18.1173875,  27.5281875],
                              [ 12.0000125,  12.0000125,  29.5673125],
                              [ 16.0782625,  12.0000125,  29.5673125],
                              [ 14.0391375,  14.0391375,  29.5673125],
                              [ 18.1173875,  14.0391375,  29.5673125],
                              [ 12.0000125,  16.0782625,  29.5673125],
                              [ 16.0782625,  16.0782625,  29.5673125],
                              [ 14.0391375,  18.1173875,  29.5673125],
                              [ 18.1173875,  18.1173875,  29.5673125],
                              [ 14.0391375,  12.0000125,  31.6064375],
                              [ 18.1173875,  12.0000125,  31.6064375],
                              [ 12.0000125,  14.0391375,  31.6064375],
                              [ 16.0782625,  14.0391375,  31.6064375],
                              [ 14.0391375,  16.0782625,  31.6064375],
                              [ 18.1173875,  16.0782625,  31.6064375],
                              [ 12.0000125,  18.1173875,  31.6064375],
                              [ 16.0782625,  18.1173875,  31.6064375],
                              [ 12.0000125,  12.0000125,  33.6455625],
                              [ 16.0782625,  12.0000125,  33.6455625],
                              [ 14.0391375,  14.0391375,  33.6455625],
                              [ 18.1173875,  14.0391375,  33.6455625],
                              [ 12.0000125,  16.0782625,  33.6455625],
                              [ 16.0782625,  16.0782625,  33.6455625],
                              [ 14.0391375,  18.1173875,  33.6455625],
                              [ 18.1173875,  18.1173875,  33.6455625],
                              [ 14.0391375,  12.0000125,  35.6846875],
                              [ 18.1173875,  12.0000125,  35.6846875],
                              [ 12.0000125,  14.0391375,  35.6846875],
                              [ 16.0782625,  14.0391375,  35.6846875],
                              [ 14.0391375,  16.0782625,  35.6846875],
                              [ 18.1173875,  16.0782625,  35.6846875],
                              [ 12.0000125,  18.1173875,  35.6846875],
                              [ 16.0782625,  18.1173875,  35.6846875],
                              [ 12.0000125,  12.0000125,  37.7238125],
                              [ 16.0782625,  12.0000125,  37.7238125],
                              [ 14.0391375,  14.0391375,  37.7238125],
                              [ 18.1173875,  14.0391375,  37.7238125],
                              [ 12.0000125,  16.0782625,  37.7238125],
                              [ 16.0782625,  16.0782625,  37.7238125],
                              [ 14.0391375,  18.1173875,  37.7238125],
                              [ 18.1173875,  18.1173875,  37.7238125],
                              [ 14.0391375,  12.0000125,  39.7629375],
                              [ 18.1173875,  12.0000125,  39.7629375],
                              [ 12.0000125,  14.0391375,  39.7629375],
                              [ 16.0782625,  14.0391375,  39.7629375],
                              [ 14.0391375,  16.0782625,  39.7629375],
                              [ 18.1173875,  16.0782625,  39.7629375],
                              [ 12.0000125,  18.1173875,  39.7629375],
                              [ 16.0782625,  18.1173875,  39.7629375],
                              [ 12.0000125,  12.0000125,  41.8020625],
                              [ 16.0782625,  12.0000125,  41.8020625],
                              [ 14.0391375,  14.0391375,  41.8020625],
                              [ 18.1173875,  14.0391375,  41.8020625],
                              [ 12.0000125,  16.0782625,  41.8020625],
                              [ 16.0782625,  16.0782625,  41.8020625],
                              [ 14.0391375,  18.1173875,  41.8020625],
                              [ 18.1173875,  18.1173875,  41.8020625],
                              [ 14.0391375,  12.0000125,  43.8411875],
                              [ 18.1173875,  12.0000125,  43.8411875],
                              [ 12.0000125,  14.0391375,  43.8411875],
                              [ 16.0782625,  14.0391375,  43.8411875],
                              [ 14.0391375,  16.0782625,  43.8411875],
                              [ 18.1173875,  16.0782625,  43.8411875],
                              [ 12.0000125,  18.1173875,  43.8411875],
                              [ 16.0782625,  18.1173875,  43.8411875],
                              [ 12.0000125,  12.0000125,  45.8803125],
                              [ 16.0782625,  12.0000125,  45.8803125],
                              [ 14.0391375,  14.0391375,  45.8803125],
                              [ 18.1173875,  14.0391375,  45.8803125],
                              [ 12.0000125,  16.0782625,  45.8803125],
                              [ 16.0782625,  16.0782625,  45.8803125],
                              [ 14.0391375,  18.1173875,  45.8803125],
                              [ 18.1173875,  18.1173875,  45.8803125],
                              [ 14.0391375,  12.0000125,  47.9194375],
                              [ 18.1173875,  12.0000125,  47.9194375],
                              [ 12.0000125,  14.0391375,  47.9194375],
                              [ 16.0782625,  14.0391375,  47.9194375],
                              [ 14.0391375,  16.0782625,  47.9194375],
                              [ 18.1173875,  16.0782625,  47.9194375],
                              [ 12.0000125,  18.1173875,  47.9194375],
                              [ 16.0782625,  18.1173875,  47.9194375],
                              [ 12.0000125,  12.0000125,  49.9585625],
                              [ 16.0782625,  12.0000125,  49.9585625],
                              [ 14.0391375,  14.0391375,  49.9585625],
                              [ 18.1173875,  14.0391375,  49.9585625],
                              [ 12.0000125,  16.0782625,  49.9585625],
                              [ 16.0782625,  16.0782625,  49.9585625],
                              [ 14.0391375,  18.1173875,  49.9585625],
                              [ 18.1173875,  18.1173875,  49.9585625],
                              [ 14.0391375,  12.0000125,  51.9976875],
                              [ 18.1173875,  12.0000125,  51.9976875],
                              [ 12.0000125,  14.0391375,  51.9976875],
                              [ 16.0782625,  14.0391375,  51.9976875],
                              [ 14.0391375,  16.0782625,  51.9976875],
                              [ 18.1173875,  16.0782625,  51.9976875],
                              [ 12.0000125,  18.1173875,  51.9976875],
                              [ 16.0782625,  18.1173875,  51.9976875],
                              [ 12.0000125,  12.0000125,  54.0368125],
                              [ 16.0782625,  12.0000125,  54.0368125],
                              [ 14.0391375,  14.0391375,  54.0368125],
                              [ 18.1173875,  14.0391375,  54.0368125],
                              [ 12.0000125,  16.0782625,  54.0368125],
                              [ 16.0782625,  16.0782625,  54.0368125],
                              [ 14.0391375,  18.1173875,  54.0368125],
                              [ 18.1173875,  18.1173875,  54.0368125],
                              [ 14.0391375,  12.0000125,  56.0759375],
                              [ 18.1173875,  12.0000125,  56.0759375],
                              [ 12.0000125,  14.0391375,  56.0759375],
                              [ 16.0782625,  14.0391375,  56.0759375],
                              [ 14.0391375,  16.0782625,  56.0759375],
                              [ 18.1173875,  16.0782625,  56.0759375],
                              [ 12.0000125,  18.1173875,  56.0759375],
                              [ 16.0782625,  18.1173875,  56.0759375],
                              [ 12.0000125,  12.0000125,  58.1150625],
                              [ 16.0782625,  12.0000125,  58.1150625],
                              [ 14.0391375,  14.0391375,  58.1150625],
                              [ 18.1173875,  14.0391375,  58.1150625],
                              [ 12.0000125,  16.0782625,  58.1150625],
                              [ 16.0782625,  16.0782625,  58.1150625],
                              [ 14.0391375,  18.1173875,  58.1150625],
                              [ 18.1173875,  18.1173875,  58.1150625],
                              [ 14.0391375,  12.0000125,  60.1541875],
                              [ 18.1173875,  12.0000125,  60.1541875],
                              [ 12.0000125,  14.0391375,  60.1541875],
                              [ 16.0782625,  14.0391375,  60.1541875],
                              [ 14.0391375,  16.0782625,  60.1541875],
                              [ 18.1173875,  16.0782625,  60.1541875],
                              [ 12.0000125,  18.1173875,  60.1541875],
                              [ 16.0782625,  18.1173875,  60.1541875],
                              [ 12.0000125,  12.0000125,  62.1933125],
                              [ 16.0782625,  12.0000125,  62.1933125],
                              [ 14.0391375,  14.0391375,  62.1933125],
                              [ 18.1173875,  14.0391375,  62.1933125],
                              [ 12.0000125,  16.0782625,  62.1933125],
                              [ 16.0782625,  16.0782625,  62.1933125],
                              [ 14.0391375,  18.1173875,  62.1933125],
                              [ 18.1173875,  18.1173875,  62.1933125],
                              [ 14.0391375,  12.0000125,  64.2324375],
                              [ 18.1173875,  12.0000125,  64.2324375],
                              [ 12.0000125,  14.0391375,  64.2324375],
                              [ 16.0782625,  14.0391375,  64.2324375],
                              [ 14.0391375,  16.0782625,  64.2324375],
                              [ 18.1173875,  16.0782625,  64.2324375],
                              [ 12.0000125,  18.1173875,  64.2324375],
                              [ 16.0782625,  18.1173875,  64.2324375],
                              [ 12.0000125,  12.0000125,  66.2715625],
                              [ 16.0782625,  12.0000125,  66.2715625],
                              [ 14.0391375,  14.0391375,  66.2715625],
                              [ 18.1173875,  14.0391375,  66.2715625],
                              [ 12.0000125,  16.0782625,  66.2715625],
                              [ 16.0782625,  16.0782625,  66.2715625],
                              [ 14.0391375,  18.1173875,  66.2715625],
                              [ 18.1173875,  18.1173875,  66.2715625],
                              [ 14.0391375,  12.0000125,  68.3106875],
                              [ 18.1173875,  12.0000125,  68.3106875],
                              [ 12.0000125,  14.0391375,  68.3106875],
                              [ 16.0782625,  14.0391375,  68.3106875],
                              [ 14.0391375,  16.0782625,  68.3106875],
                              [ 18.1173875,  16.0782625,  68.3106875],
                              [ 12.0000125,  18.1173875,  68.3106875],
                              [ 16.0782625,  18.1173875,  68.3106875],
                              [ 12.0000125,  12.0000125,  70.3498125],
                              [ 16.0782625,  12.0000125,  70.3498125],
                              [ 14.0391375,  14.0391375,  70.3498125],
                              [ 18.1173875,  14.0391375,  70.3498125],
                              [ 12.0000125,  16.0782625,  70.3498125],
                              [ 16.0782625,  16.0782625,  70.3498125],
                              [ 14.0391375,  18.1173875,  70.3498125],
                              [ 18.1173875,  18.1173875,  70.3498125],
                              [ 14.0391375,  12.0000125,  72.3889375],
                              [ 18.1173875,  12.0000125,  72.3889375],
                              [ 12.0000125,  14.0391375,  72.3889375],
                              [ 16.0782625,  14.0391375,  72.3889375],
                              [ 14.0391375,  16.0782625,  72.3889375],
                              [ 18.1173875,  16.0782625,  72.3889375],
                              [ 12.0000125,  18.1173875,  72.3889375],
                              [ 16.0782625,  18.1173875,  72.3889375],
                              [ 12.0000125,  12.0000125,  74.4280625],
                              [ 16.0782625,  12.0000125,  74.4280625],
                              [ 14.0391375,  14.0391375,  74.4280625],
                              [ 18.1173875,  14.0391375,  74.4280625],
                              [ 12.0000125,  16.0782625,  74.4280625],
                              [ 16.0782625,  16.0782625,  74.4280625],
                              [ 14.0391375,  18.1173875,  74.4280625],
                              [ 18.1173875,  18.1173875,  74.4280625],
                              [ 14.0391375,  12.0000125,  76.4671875],
                              [ 18.1173875,  12.0000125,  76.4671875],
                              [ 12.0000125,  14.0391375,  76.4671875],
                              [ 16.0782625,  14.0391375,  76.4671875],
                              [ 14.0391375,  16.0782625,  76.4671875],
                              [ 18.1173875,  16.0782625,  76.4671875],
                              [ 12.0000125,  18.1173875,  76.4671875],
                              [ 16.0782625,  18.1173875,  76.4671875],
                              [ 12.0000125,  12.0000125,  78.5063125],
                              [ 16.0782625,  12.0000125,  78.5063125],
                              [ 14.0391375,  14.0391375,  78.5063125],
                              [ 18.1173875,  14.0391375,  78.5063125],
                              [ 12.0000125,  16.0782625,  78.5063125],
                              [ 16.0782625,  16.0782625,  78.5063125],
                              [ 14.0391375,  18.1173875,  78.5063125],
                              [ 18.1173875,  18.1173875,  78.5063125],
                              [ 14.0391375,  12.0000125,  80.5454375],
                              [ 18.1173875,  12.0000125,  80.5454375],
                              [ 12.0000125,  14.0391375,  80.5454375],
                              [ 16.0782625,  14.0391375,  80.5454375],
                              [ 14.0391375,  16.0782625,  80.5454375],
                              [ 18.1173875,  16.0782625,  80.5454375],
                              [ 12.0000125,  18.1173875,  80.5454375],
                              [ 16.0782625,  18.1173875,  80.5454375],
                              [ 12.0000125,  12.0000125,  82.5845625],
                              [ 16.0782625,  12.0000125,  82.5845625],
                              [ 14.0391375,  14.0391375,  82.5845625],
                              [ 18.1173875,  14.0391375,  82.5845625],
                              [ 12.0000125,  16.0782625,  82.5845625],
                              [ 16.0782625,  16.0782625,  82.5845625],
                              [ 14.0391375,  18.1173875,  82.5845625],
                              [ 18.1173875,  18.1173875,  82.5845625],
                              [ 14.0391375,  12.0000125,  84.6236875],
                              [ 18.1173875,  12.0000125,  84.6236875],
                              [ 12.0000125,  14.0391375,  84.6236875],
                              [ 16.0782625,  14.0391375,  84.6236875],
                              [ 14.0391375,  16.0782625,  84.6236875],
                              [ 18.1173875,  16.0782625,  84.6236875],
                              [ 12.0000125,  18.1173875,  84.6236875],
                              [ 16.0782625,  18.1173875,  84.6236875],
                              [ 12.0000125,  12.0000125,  86.6628125],
                              [ 16.0782625,  12.0000125,  86.6628125],
                              [ 14.0391375,  14.0391375,  86.6628125],
                              [ 18.1173875,  14.0391375,  86.6628125],
                              [ 12.0000125,  16.0782625,  86.6628125],
                              [ 16.0782625,  16.0782625,  86.6628125],
                              [ 14.0391375,  18.1173875,  86.6628125],
                              [ 18.1173875,  18.1173875,  86.6628125],
                              [ 14.0391375,  12.0000125,  88.7019375],
                              [ 18.1173875,  12.0000125,  88.7019375],
                              [ 12.0000125,  14.0391375,  88.7019375],
                              [ 16.0782625,  14.0391375,  88.7019375],
                              [ 14.0391375,  16.0782625,  88.7019375],
                              [ 18.1173875,  16.0782625,  88.7019375],
                              [ 12.0000125,  18.1173875,  88.7019375],
                              [ 16.0782625,  18.1173875,  88.7019375]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  19.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  19.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.0000125 *Angstrom,  xmax =  1.0000125 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  19.1173875 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  19.1173875 *Angstrom,  xmax =  29.1173875 *Angstrom,
        ymin =  11.0000125 *Angstrom,  ymax =  1.0000125 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.0000125 *Angstrom,  xmax =  1.25000000004e-05 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  29.1173875 *Angstrom,  ymax =  30.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  29.1173875 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  29.1173875 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.25000000004e-05 *Angstrom,  xmax =  30.1173875 *Angstrom,
        ymin =  1.0000125 *Angstrom,  ymax =  1.25000000004e-05 *Angstrom,
        zmin =  9.35096875 *Angstrom,  zmax =  79.35096875 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)


device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )


