# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                              [ 16.32565   ,  13.44312088,   1.0195625 ],
                              [ 19.20940823,  13.44312088,   1.0195625 ],
                              [ 13.44189177,  16.32687912,   1.0195625 ],
                              [ 16.32565   ,  16.32687912,   1.0195625 ],
                              [ 19.20940823,  16.32687912,   1.0195625 ],
                              [ 12.00001265,  12.00124177,   3.0586875 ],
                              [ 14.88377088,  12.00124177,   3.0586875 ],
                              [ 17.76752912,  12.00124177,   3.0586875 ],
                              [ 20.65128735,  12.00124177,   3.0586875 ],
                              [ 12.00001265,  14.885     ,   3.0586875 ],
                              [ 14.88377088,  14.885     ,   3.0586875 ],
                              [ 17.76752912,  14.885     ,   3.0586875 ],
                              [ 20.65128735,  14.885     ,   3.0586875 ],
                              [ 12.00001265,  17.76875823,   3.0586875 ],
                              [ 14.88377088,  17.76875823,   3.0586875 ],
                              [ 17.76752912,  17.76875823,   3.0586875 ],
                              [ 20.65128735,  17.76875823,   3.0586875 ],
                              [ 13.44189177,  13.44312088,   5.0978125 ],
                              [ 16.32565   ,  13.44312088,   5.0978125 ],
                              [ 19.20940823,  13.44312088,   5.0978125 ],
                              [ 13.44189177,  16.32687912,   5.0978125 ],
                              [ 16.32565   ,  16.32687912,   5.0978125 ],
                              [ 19.20940823,  16.32687912,   5.0978125 ],
                              [ 12.00001265,  12.00124177,   7.1369375 ],
                              [ 14.88377088,  12.00124177,   7.1369375 ],
                              [ 17.76752912,  12.00124177,   7.1369375 ],
                              [ 20.65128735,  12.00124177,   7.1369375 ],
                              [ 12.00001265,  14.885     ,   7.1369375 ],
                              [ 14.88377088,  14.885     ,   7.1369375 ],
                              [ 17.76752912,  14.885     ,   7.1369375 ],
                              [ 20.65128735,  14.885     ,   7.1369375 ],
                              [ 12.00001265,  17.76875823,   7.1369375 ],
                              [ 14.88377088,  17.76875823,   7.1369375 ],
                              [ 17.76752912,  17.76875823,   7.1369375 ],
                              [ 20.65128735,  17.76875823,   7.1369375 ]]*Angstrom

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
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                               [ 16.32565   ,  13.44312088,   1.0195625 ],
                               [ 19.20940823,  13.44312088,   1.0195625 ],
                               [ 13.44189177,  16.32687912,   1.0195625 ],
                               [ 16.32565   ,  16.32687912,   1.0195625 ],
                               [ 19.20940823,  16.32687912,   1.0195625 ],
                               [ 12.00001265,  12.00124177,   3.0586875 ],
                               [ 14.88377088,  12.00124177,   3.0586875 ],
                               [ 17.76752912,  12.00124177,   3.0586875 ],
                               [ 20.65128735,  12.00124177,   3.0586875 ],
                               [ 12.00001265,  14.885     ,   3.0586875 ],
                               [ 14.88377088,  14.885     ,   3.0586875 ],
                               [ 17.76752912,  14.885     ,   3.0586875 ],
                               [ 20.65128735,  14.885     ,   3.0586875 ],
                               [ 12.00001265,  17.76875823,   3.0586875 ],
                               [ 14.88377088,  17.76875823,   3.0586875 ],
                               [ 17.76752912,  17.76875823,   3.0586875 ],
                               [ 20.65128735,  17.76875823,   3.0586875 ],
                               [ 13.44189177,  13.44312088,   5.0978125 ],
                               [ 16.32565   ,  13.44312088,   5.0978125 ],
                               [ 19.20940823,  13.44312088,   5.0978125 ],
                               [ 13.44189177,  16.32687912,   5.0978125 ],
                               [ 16.32565   ,  16.32687912,   5.0978125 ],
                               [ 19.20940823,  16.32687912,   5.0978125 ],
                               [ 12.00001265,  12.00124177,   7.1369375 ],
                               [ 14.88377088,  12.00124177,   7.1369375 ],
                               [ 17.76752912,  12.00124177,   7.1369375 ],
                               [ 20.65128735,  12.00124177,   7.1369375 ],
                               [ 12.00001265,  14.885     ,   7.1369375 ],
                               [ 14.88377088,  14.885     ,   7.1369375 ],
                               [ 17.76752912,  14.885     ,   7.1369375 ],
                               [ 20.65128735,  14.885     ,   7.1369375 ],
                               [ 12.00001265,  17.76875823,   7.1369375 ],
                               [ 14.88377088,  17.76875823,   7.1369375 ],
                               [ 17.76752912,  17.76875823,   7.1369375 ],
                               [ 20.65128735,  17.76875823,   7.1369375 ]]*Angstrom

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
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.77, 0.0]*Angstrom
vector_c = [0.0, 0.0, 48.939]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 13.44189177,  13.44312088,   1.0195625 ],
                              [ 16.32565   ,  13.44312088,   1.0195625 ],
                              [ 19.20940823,  13.44312088,   1.0195625 ],
                              [ 13.44189177,  16.32687912,   1.0195625 ],
                              [ 16.32565   ,  16.32687912,   1.0195625 ],
                              [ 19.20940823,  16.32687912,   1.0195625 ],
                              [ 12.00001265,  12.00124177,   3.0586875 ],
                              [ 14.88377088,  12.00124177,   3.0586875 ],
                              [ 17.76752912,  12.00124177,   3.0586875 ],
                              [ 20.65128735,  12.00124177,   3.0586875 ],
                              [ 12.00001265,  14.885     ,   3.0586875 ],
                              [ 14.88377088,  14.885     ,   3.0586875 ],
                              [ 17.76752912,  14.885     ,   3.0586875 ],
                              [ 20.65128735,  14.885     ,   3.0586875 ],
                              [ 12.00001265,  17.76875823,   3.0586875 ],
                              [ 14.88377088,  17.76875823,   3.0586875 ],
                              [ 17.76752912,  17.76875823,   3.0586875 ],
                              [ 20.65128735,  17.76875823,   3.0586875 ],
                              [ 13.44189177,  13.44312088,   5.0978125 ],
                              [ 16.32565   ,  13.44312088,   5.0978125 ],
                              [ 19.20940823,  13.44312088,   5.0978125 ],
                              [ 13.44189177,  16.32687912,   5.0978125 ],
                              [ 16.32565   ,  16.32687912,   5.0978125 ],
                              [ 19.20940823,  16.32687912,   5.0978125 ],
                              [ 12.00001265,  12.00124177,   7.1369375 ],
                              [ 14.88377088,  12.00124177,   7.1369375 ],
                              [ 17.76752912,  12.00124177,   7.1369375 ],
                              [ 20.65128735,  12.00124177,   7.1369375 ],
                              [ 12.00001265,  14.885     ,   7.1369375 ],
                              [ 14.88377088,  14.885     ,   7.1369375 ],
                              [ 17.76752912,  14.885     ,   7.1369375 ],
                              [ 20.65128735,  14.885     ,   7.1369375 ],
                              [ 12.00001265,  17.76875823,   7.1369375 ],
                              [ 14.88377088,  17.76875823,   7.1369375 ],
                              [ 17.76752912,  17.76875823,   7.1369375 ],
                              [ 20.65128735,  17.76875823,   7.1369375 ],
                              [ 13.44189177,  13.44312088,   9.1760625 ],
                              [ 16.32565   ,  13.44312088,   9.1760625 ],
                              [ 19.20940823,  13.44312088,   9.1760625 ],
                              [ 13.44189177,  16.32687912,   9.1760625 ],
                              [ 16.32565   ,  16.32687912,   9.1760625 ],
                              [ 19.20940823,  16.32687912,   9.1760625 ],
                              [ 12.00001265,  12.00124177,  11.2151875 ],
                              [ 14.88377088,  12.00124177,  11.2151875 ],
                              [ 17.76752912,  12.00124177,  11.2151875 ],
                              [ 20.65128735,  12.00124177,  11.2151875 ],
                              [ 12.00001265,  14.885     ,  11.2151875 ],
                              [ 14.88377088,  14.885     ,  11.2151875 ],
                              [ 17.76752912,  14.885     ,  11.2151875 ],
                              [ 20.65128735,  14.885     ,  11.2151875 ],
                              [ 12.00001265,  17.76875823,  11.2151875 ],
                              [ 14.88377088,  17.76875823,  11.2151875 ],
                              [ 17.76752912,  17.76875823,  11.2151875 ],
                              [ 20.65128735,  17.76875823,  11.2151875 ],
                              [ 13.44189177,  13.44312088,  13.2543125 ],
                              [ 16.32565   ,  13.44312088,  13.2543125 ],
                              [ 19.20940823,  13.44312088,  13.2543125 ],
                              [ 13.44189177,  16.32687912,  13.2543125 ],
                              [ 16.32565   ,  16.32687912,  13.2543125 ],
                              [ 19.20940823,  16.32687912,  13.2543125 ],
                              [ 12.00001265,  12.00124177,  15.2934375 ],
                              [ 14.88377088,  12.00124177,  15.2934375 ],
                              [ 17.76752912,  12.00124177,  15.2934375 ],
                              [ 20.65128735,  12.00124177,  15.2934375 ],
                              [ 12.00001265,  14.885     ,  15.2934375 ],
                              [ 14.88377088,  14.885     ,  15.2934375 ],
                              [ 17.76752912,  14.885     ,  15.2934375 ],
                              [ 20.65128735,  14.885     ,  15.2934375 ],
                              [ 12.00001265,  17.76875823,  15.2934375 ],
                              [ 14.88377088,  17.76875823,  15.2934375 ],
                              [ 17.76752912,  17.76875823,  15.2934375 ],
                              [ 20.65128735,  17.76875823,  15.2934375 ],
                              [ 13.44189177,  13.44312088,  17.3325625 ],
                              [ 16.32565   ,  13.44312088,  17.3325625 ],
                              [ 19.20940823,  13.44312088,  17.3325625 ],
                              [ 13.44189177,  16.32687912,  17.3325625 ],
                              [ 16.32565   ,  16.32687912,  17.3325625 ],
                              [ 19.20940823,  16.32687912,  17.3325625 ],
                              [ 12.00001265,  12.00124177,  19.3716875 ],
                              [ 14.88377088,  12.00124177,  19.3716875 ],
                              [ 17.76752912,  12.00124177,  19.3716875 ],
                              [ 20.65128735,  12.00124177,  19.3716875 ],
                              [ 12.00001265,  14.885     ,  19.3716875 ],
                              [ 14.88377088,  14.885     ,  19.3716875 ],
                              [ 17.76752912,  14.885     ,  19.3716875 ],
                              [ 20.65128735,  14.885     ,  19.3716875 ],
                              [ 12.00001265,  17.76875823,  19.3716875 ],
                              [ 14.88377088,  17.76875823,  19.3716875 ],
                              [ 17.76752912,  17.76875823,  19.3716875 ],
                              [ 20.65128735,  17.76875823,  19.3716875 ],
                              [ 13.44189177,  13.44312088,  21.4108125 ],
                              [ 16.32565   ,  13.44312088,  21.4108125 ],
                              [ 19.20940823,  13.44312088,  21.4108125 ],
                              [ 13.44189177,  16.32687912,  21.4108125 ],
                              [ 16.32565   ,  16.32687912,  21.4108125 ],
                              [ 19.20940823,  16.32687912,  21.4108125 ],
                              [ 12.00001265,  12.00124177,  23.4499375 ],
                              [ 14.88377088,  12.00124177,  23.4499375 ],
                              [ 17.76752912,  12.00124177,  23.4499375 ],
                              [ 20.65128735,  12.00124177,  23.4499375 ],
                              [ 12.00001265,  14.885     ,  23.4499375 ],
                              [ 14.88377088,  14.885     ,  23.4499375 ],
                              [ 17.76752912,  14.885     ,  23.4499375 ],
                              [ 20.65128735,  14.885     ,  23.4499375 ],
                              [ 12.00001265,  17.76875823,  23.4499375 ],
                              [ 14.88377088,  17.76875823,  23.4499375 ],
                              [ 17.76752912,  17.76875823,  23.4499375 ],
                              [ 20.65128735,  17.76875823,  23.4499375 ],
                              [ 13.44189177,  13.44312088,  25.4890625 ],
                              [ 16.32565   ,  13.44312088,  25.4890625 ],
                              [ 19.20940823,  13.44312088,  25.4890625 ],
                              [ 13.44189177,  16.32687912,  25.4890625 ],
                              [ 16.32565   ,  16.32687912,  25.4890625 ],
                              [ 19.20940823,  16.32687912,  25.4890625 ],
                              [ 12.00001265,  12.00124177,  27.5281875 ],
                              [ 14.88377088,  12.00124177,  27.5281875 ],
                              [ 17.76752912,  12.00124177,  27.5281875 ],
                              [ 20.65128735,  12.00124177,  27.5281875 ],
                              [ 12.00001265,  14.885     ,  27.5281875 ],
                              [ 14.88377088,  14.885     ,  27.5281875 ],
                              [ 17.76752912,  14.885     ,  27.5281875 ],
                              [ 20.65128735,  14.885     ,  27.5281875 ],
                              [ 12.00001265,  17.76875823,  27.5281875 ],
                              [ 14.88377088,  17.76875823,  27.5281875 ],
                              [ 17.76752912,  17.76875823,  27.5281875 ],
                              [ 20.65128735,  17.76875823,  27.5281875 ],
                              [ 13.44189177,  13.44312088,  29.5673125 ],
                              [ 16.32565   ,  13.44312088,  29.5673125 ],
                              [ 19.20940823,  13.44312088,  29.5673125 ],
                              [ 13.44189177,  16.32687912,  29.5673125 ],
                              [ 16.32565   ,  16.32687912,  29.5673125 ],
                              [ 19.20940823,  16.32687912,  29.5673125 ],
                              [ 12.00001265,  12.00124177,  31.6064375 ],
                              [ 14.88377088,  12.00124177,  31.6064375 ],
                              [ 17.76752912,  12.00124177,  31.6064375 ],
                              [ 20.65128735,  12.00124177,  31.6064375 ],
                              [ 12.00001265,  14.885     ,  31.6064375 ],
                              [ 14.88377088,  14.885     ,  31.6064375 ],
                              [ 17.76752912,  14.885     ,  31.6064375 ],
                              [ 20.65128735,  14.885     ,  31.6064375 ],
                              [ 12.00001265,  17.76875823,  31.6064375 ],
                              [ 14.88377088,  17.76875823,  31.6064375 ],
                              [ 17.76752912,  17.76875823,  31.6064375 ],
                              [ 20.65128735,  17.76875823,  31.6064375 ],
                              [ 13.44189177,  13.44312088,  33.6455625 ],
                              [ 16.32565   ,  13.44312088,  33.6455625 ],
                              [ 19.20940823,  13.44312088,  33.6455625 ],
                              [ 13.44189177,  16.32687912,  33.6455625 ],
                              [ 16.32565   ,  16.32687912,  33.6455625 ],
                              [ 19.20940823,  16.32687912,  33.6455625 ],
                              [ 12.00001265,  12.00124177,  35.6846875 ],
                              [ 14.88377088,  12.00124177,  35.6846875 ],
                              [ 17.76752912,  12.00124177,  35.6846875 ],
                              [ 20.65128735,  12.00124177,  35.6846875 ],
                              [ 12.00001265,  14.885     ,  35.6846875 ],
                              [ 14.88377088,  14.885     ,  35.6846875 ],
                              [ 17.76752912,  14.885     ,  35.6846875 ],
                              [ 20.65128735,  14.885     ,  35.6846875 ],
                              [ 12.00001265,  17.76875823,  35.6846875 ],
                              [ 14.88377088,  17.76875823,  35.6846875 ],
                              [ 17.76752912,  17.76875823,  35.6846875 ],
                              [ 20.65128735,  17.76875823,  35.6846875 ],
                              [ 13.44189177,  13.44312088,  37.7238125 ],
                              [ 16.32565   ,  13.44312088,  37.7238125 ],
                              [ 19.20940823,  13.44312088,  37.7238125 ],
                              [ 13.44189177,  16.32687912,  37.7238125 ],
                              [ 16.32565   ,  16.32687912,  37.7238125 ],
                              [ 19.20940823,  16.32687912,  37.7238125 ],
                              [ 12.00001265,  12.00124177,  39.7629375 ],
                              [ 14.88377088,  12.00124177,  39.7629375 ],
                              [ 17.76752912,  12.00124177,  39.7629375 ],
                              [ 20.65128735,  12.00124177,  39.7629375 ],
                              [ 12.00001265,  14.885     ,  39.7629375 ],
                              [ 14.88377088,  14.885     ,  39.7629375 ],
                              [ 17.76752912,  14.885     ,  39.7629375 ],
                              [ 20.65128735,  14.885     ,  39.7629375 ],
                              [ 12.00001265,  17.76875823,  39.7629375 ],
                              [ 14.88377088,  17.76875823,  39.7629375 ],
                              [ 17.76752912,  17.76875823,  39.7629375 ],
                              [ 20.65128735,  17.76875823,  39.7629375 ],
                              [ 13.44189177,  13.44312088,  41.8020625 ],
                              [ 16.32565   ,  13.44312088,  41.8020625 ],
                              [ 19.20940823,  13.44312088,  41.8020625 ],
                              [ 13.44189177,  16.32687912,  41.8020625 ],
                              [ 16.32565   ,  16.32687912,  41.8020625 ],
                              [ 19.20940823,  16.32687912,  41.8020625 ],
                              [ 12.00001265,  12.00124177,  43.8411875 ],
                              [ 14.88377088,  12.00124177,  43.8411875 ],
                              [ 17.76752912,  12.00124177,  43.8411875 ],
                              [ 20.65128735,  12.00124177,  43.8411875 ],
                              [ 12.00001265,  14.885     ,  43.8411875 ],
                              [ 14.88377088,  14.885     ,  43.8411875 ],
                              [ 17.76752912,  14.885     ,  43.8411875 ],
                              [ 20.65128735,  14.885     ,  43.8411875 ],
                              [ 12.00001265,  17.76875823,  43.8411875 ],
                              [ 14.88377088,  17.76875823,  43.8411875 ],
                              [ 17.76752912,  17.76875823,  43.8411875 ],
                              [ 20.65128735,  17.76875823,  43.8411875 ],
                              [ 13.44189177,  13.44312088,  45.8803125 ],
                              [ 16.32565   ,  13.44312088,  45.8803125 ],
                              [ 19.20940823,  13.44312088,  45.8803125 ],
                              [ 13.44189177,  16.32687912,  45.8803125 ],
                              [ 16.32565   ,  16.32687912,  45.8803125 ],
                              [ 19.20940823,  16.32687912,  45.8803125 ],
                              [ 12.00001265,  12.00124177,  47.9194375 ],
                              [ 14.88377088,  12.00124177,  47.9194375 ],
                              [ 17.76752912,  12.00124177,  47.9194375 ],
                              [ 20.65128735,  12.00124177,  47.9194375 ],
                              [ 12.00001265,  14.885     ,  47.9194375 ],
                              [ 14.88377088,  14.885     ,  47.9194375 ],
                              [ 17.76752912,  14.885     ,  47.9194375 ],
                              [ 20.65128735,  14.885     ,  47.9194375 ],
                              [ 12.00001265,  17.76875823,  47.9194375 ],
                              [ 14.88377088,  17.76875823,  47.9194375 ],
                              [ 17.76752912,  17.76875823,  47.9194375 ],
                              [ 20.65128735,  17.76875823,  47.9194375 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  18.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  18.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  18.76875823 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00124177 *Angstrom,  ymax =  1.00124177 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.00001265 *Angstrom,  xmax =  1.26500000004e-05 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  28.76875823 *Angstrom,  ymax =  29.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.65128735 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  28.76875823 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00124177 *Angstrom,  ymax =  0.00124177 *Angstrom,
        zmin =  8.95971875 *Angstrom,  zmax =  38.95971875 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]


