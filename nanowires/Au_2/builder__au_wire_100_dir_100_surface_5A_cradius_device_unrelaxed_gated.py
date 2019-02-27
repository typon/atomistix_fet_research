# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [30.15, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.15, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 10.99675008,  10.99675008,   1.0195625 ],
                              [ 15.075     ,  10.99675008,   1.0195625 ],
                              [ 19.15324992,  10.99675008,   1.0195625 ],
                              [ 13.03587504,  13.03587504,   1.0195625 ],
                              [ 17.11412496,  13.03587504,   1.0195625 ],
                              [ 10.99675008,  15.075     ,   1.0195625 ],
                              [ 15.075     ,  15.075     ,   1.0195625 ],
                              [ 19.15324992,  15.075     ,   1.0195625 ],
                              [ 13.03587504,  17.11412496,   1.0195625 ],
                              [ 17.11412496,  17.11412496,   1.0195625 ],
                              [ 10.99675008,  19.15324992,   1.0195625 ],
                              [ 15.075     ,  19.15324992,   1.0195625 ],
                              [ 19.15324992,  19.15324992,   1.0195625 ],
                              [ 13.03587504,  10.99675008,   3.0586875 ],
                              [ 17.11412496,  10.99675008,   3.0586875 ],
                              [ 10.99675008,  13.03587504,   3.0586875 ],
                              [ 15.075     ,  13.03587504,   3.0586875 ],
                              [ 19.15324992,  13.03587504,   3.0586875 ],
                              [ 13.03587504,  15.075     ,   3.0586875 ],
                              [ 17.11412496,  15.075     ,   3.0586875 ],
                              [ 10.99675008,  17.11412496,   3.0586875 ],
                              [ 15.075     ,  17.11412496,   3.0586875 ],
                              [ 19.15324992,  17.11412496,   3.0586875 ],
                              [ 13.03587504,  19.15324992,   3.0586875 ],
                              [ 17.11412496,  19.15324992,   3.0586875 ],
                              [ 10.99675008,  10.99675008,   5.0978125 ],
                              [ 15.075     ,  10.99675008,   5.0978125 ],
                              [ 19.15324992,  10.99675008,   5.0978125 ],
                              [ 13.03587504,  13.03587504,   5.0978125 ],
                              [ 17.11412496,  13.03587504,   5.0978125 ],
                              [ 10.99675008,  15.075     ,   5.0978125 ],
                              [ 15.075     ,  15.075     ,   5.0978125 ],
                              [ 19.15324992,  15.075     ,   5.0978125 ],
                              [ 13.03587504,  17.11412496,   5.0978125 ],
                              [ 17.11412496,  17.11412496,   5.0978125 ],
                              [ 10.99675008,  19.15324992,   5.0978125 ],
                              [ 15.075     ,  19.15324992,   5.0978125 ],
                              [ 19.15324992,  19.15324992,   5.0978125 ],
                              [ 13.03587504,  10.99675008,   7.1369375 ],
                              [ 17.11412496,  10.99675008,   7.1369375 ],
                              [ 10.99675008,  13.03587504,   7.1369375 ],
                              [ 15.075     ,  13.03587504,   7.1369375 ],
                              [ 19.15324992,  13.03587504,   7.1369375 ],
                              [ 13.03587504,  15.075     ,   7.1369375 ],
                              [ 17.11412496,  15.075     ,   7.1369375 ],
                              [ 10.99675008,  17.11412496,   7.1369375 ],
                              [ 15.075     ,  17.11412496,   7.1369375 ],
                              [ 19.15324992,  17.11412496,   7.1369375 ],
                              [ 13.03587504,  19.15324992,   7.1369375 ],
                              [ 17.11412496,  19.15324992,   7.1369375 ]]*Angstrom

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
vector_a = [30.15, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.15, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.1565]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 10.99675008,  10.99675008,   1.0195625 ],
                               [ 15.075     ,  10.99675008,   1.0195625 ],
                               [ 19.15324992,  10.99675008,   1.0195625 ],
                               [ 13.03587504,  13.03587504,   1.0195625 ],
                               [ 17.11412496,  13.03587504,   1.0195625 ],
                               [ 10.99675008,  15.075     ,   1.0195625 ],
                               [ 15.075     ,  15.075     ,   1.0195625 ],
                               [ 19.15324992,  15.075     ,   1.0195625 ],
                               [ 13.03587504,  17.11412496,   1.0195625 ],
                               [ 17.11412496,  17.11412496,   1.0195625 ],
                               [ 10.99675008,  19.15324992,   1.0195625 ],
                               [ 15.075     ,  19.15324992,   1.0195625 ],
                               [ 19.15324992,  19.15324992,   1.0195625 ],
                               [ 13.03587504,  10.99675008,   3.0586875 ],
                               [ 17.11412496,  10.99675008,   3.0586875 ],
                               [ 10.99675008,  13.03587504,   3.0586875 ],
                               [ 15.075     ,  13.03587504,   3.0586875 ],
                               [ 19.15324992,  13.03587504,   3.0586875 ],
                               [ 13.03587504,  15.075     ,   3.0586875 ],
                               [ 17.11412496,  15.075     ,   3.0586875 ],
                               [ 10.99675008,  17.11412496,   3.0586875 ],
                               [ 15.075     ,  17.11412496,   3.0586875 ],
                               [ 19.15324992,  17.11412496,   3.0586875 ],
                               [ 13.03587504,  19.15324992,   3.0586875 ],
                               [ 17.11412496,  19.15324992,   3.0586875 ],
                               [ 10.99675008,  10.99675008,   5.0978125 ],
                               [ 15.075     ,  10.99675008,   5.0978125 ],
                               [ 19.15324992,  10.99675008,   5.0978125 ],
                               [ 13.03587504,  13.03587504,   5.0978125 ],
                               [ 17.11412496,  13.03587504,   5.0978125 ],
                               [ 10.99675008,  15.075     ,   5.0978125 ],
                               [ 15.075     ,  15.075     ,   5.0978125 ],
                               [ 19.15324992,  15.075     ,   5.0978125 ],
                               [ 13.03587504,  17.11412496,   5.0978125 ],
                               [ 17.11412496,  17.11412496,   5.0978125 ],
                               [ 10.99675008,  19.15324992,   5.0978125 ],
                               [ 15.075     ,  19.15324992,   5.0978125 ],
                               [ 19.15324992,  19.15324992,   5.0978125 ],
                               [ 13.03587504,  10.99675008,   7.1369375 ],
                               [ 17.11412496,  10.99675008,   7.1369375 ],
                               [ 10.99675008,  13.03587504,   7.1369375 ],
                               [ 15.075     ,  13.03587504,   7.1369375 ],
                               [ 19.15324992,  13.03587504,   7.1369375 ],
                               [ 13.03587504,  15.075     ,   7.1369375 ],
                               [ 17.11412496,  15.075     ,   7.1369375 ],
                               [ 10.99675008,  17.11412496,   7.1369375 ],
                               [ 15.075     ,  17.11412496,   7.1369375 ],
                               [ 19.15324992,  17.11412496,   7.1369375 ],
                               [ 13.03587504,  19.15324992,   7.1369375 ],
                               [ 17.11412496,  19.15324992,   7.1369375 ]]*Angstrom

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
vector_a = [30.15, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.15, 0.0]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 10.99675008,  10.99675008,   1.0195625 ],
                              [ 15.075     ,  10.99675008,   1.0195625 ],
                              [ 19.15324992,  10.99675008,   1.0195625 ],
                              [ 13.03587504,  13.03587504,   1.0195625 ],
                              [ 17.11412496,  13.03587504,   1.0195625 ],
                              [ 10.99675008,  15.075     ,   1.0195625 ],
                              [ 15.075     ,  15.075     ,   1.0195625 ],
                              [ 19.15324992,  15.075     ,   1.0195625 ],
                              [ 13.03587504,  17.11412496,   1.0195625 ],
                              [ 17.11412496,  17.11412496,   1.0195625 ],
                              [ 10.99675008,  19.15324992,   1.0195625 ],
                              [ 15.075     ,  19.15324992,   1.0195625 ],
                              [ 19.15324992,  19.15324992,   1.0195625 ],
                              [ 13.03587504,  10.99675008,   3.0586875 ],
                              [ 17.11412496,  10.99675008,   3.0586875 ],
                              [ 10.99675008,  13.03587504,   3.0586875 ],
                              [ 15.075     ,  13.03587504,   3.0586875 ],
                              [ 19.15324992,  13.03587504,   3.0586875 ],
                              [ 13.03587504,  15.075     ,   3.0586875 ],
                              [ 17.11412496,  15.075     ,   3.0586875 ],
                              [ 10.99675008,  17.11412496,   3.0586875 ],
                              [ 15.075     ,  17.11412496,   3.0586875 ],
                              [ 19.15324992,  17.11412496,   3.0586875 ],
                              [ 13.03587504,  19.15324992,   3.0586875 ],
                              [ 17.11412496,  19.15324992,   3.0586875 ],
                              [ 10.99675008,  10.99675008,   5.0978125 ],
                              [ 15.075     ,  10.99675008,   5.0978125 ],
                              [ 19.15324992,  10.99675008,   5.0978125 ],
                              [ 13.03587504,  13.03587504,   5.0978125 ],
                              [ 17.11412496,  13.03587504,   5.0978125 ],
                              [ 10.99675008,  15.075     ,   5.0978125 ],
                              [ 15.075     ,  15.075     ,   5.0978125 ],
                              [ 19.15324992,  15.075     ,   5.0978125 ],
                              [ 13.03587504,  17.11412496,   5.0978125 ],
                              [ 17.11412496,  17.11412496,   5.0978125 ],
                              [ 10.99675008,  19.15324992,   5.0978125 ],
                              [ 15.075     ,  19.15324992,   5.0978125 ],
                              [ 19.15324992,  19.15324992,   5.0978125 ],
                              [ 13.03587504,  10.99675008,   7.1369375 ],
                              [ 17.11412496,  10.99675008,   7.1369375 ],
                              [ 10.99675008,  13.03587504,   7.1369375 ],
                              [ 15.075     ,  13.03587504,   7.1369375 ],
                              [ 19.15324992,  13.03587504,   7.1369375 ],
                              [ 13.03587504,  15.075     ,   7.1369375 ],
                              [ 17.11412496,  15.075     ,   7.1369375 ],
                              [ 10.99675008,  17.11412496,   7.1369375 ],
                              [ 15.075     ,  17.11412496,   7.1369375 ],
                              [ 19.15324992,  17.11412496,   7.1369375 ],
                              [ 13.03587504,  19.15324992,   7.1369375 ],
                              [ 17.11412496,  19.15324992,   7.1369375 ],
                              [ 10.99675008,  10.99675008,   9.1760625 ],
                              [ 15.075     ,  10.99675008,   9.1760625 ],
                              [ 19.15324992,  10.99675008,   9.1760625 ],
                              [ 13.03587504,  13.03587504,   9.1760625 ],
                              [ 17.11412496,  13.03587504,   9.1760625 ],
                              [ 10.99675008,  15.075     ,   9.1760625 ],
                              [ 15.075     ,  15.075     ,   9.1760625 ],
                              [ 19.15324992,  15.075     ,   9.1760625 ],
                              [ 13.03587504,  17.11412496,   9.1760625 ],
                              [ 17.11412496,  17.11412496,   9.1760625 ],
                              [ 10.99675008,  19.15324992,   9.1760625 ],
                              [ 15.075     ,  19.15324992,   9.1760625 ],
                              [ 19.15324992,  19.15324992,   9.1760625 ],
                              [ 13.03587504,  10.99675008,  11.2151875 ],
                              [ 17.11412496,  10.99675008,  11.2151875 ],
                              [ 10.99675008,  13.03587504,  11.2151875 ],
                              [ 15.075     ,  13.03587504,  11.2151875 ],
                              [ 19.15324992,  13.03587504,  11.2151875 ],
                              [ 13.03587504,  15.075     ,  11.2151875 ],
                              [ 17.11412496,  15.075     ,  11.2151875 ],
                              [ 10.99675008,  17.11412496,  11.2151875 ],
                              [ 15.075     ,  17.11412496,  11.2151875 ],
                              [ 19.15324992,  17.11412496,  11.2151875 ],
                              [ 13.03587504,  19.15324992,  11.2151875 ],
                              [ 17.11412496,  19.15324992,  11.2151875 ],
                              [ 10.99675008,  10.99675008,  13.2543125 ],
                              [ 15.075     ,  10.99675008,  13.2543125 ],
                              [ 19.15324992,  10.99675008,  13.2543125 ],
                              [ 13.03587504,  13.03587504,  13.2543125 ],
                              [ 17.11412496,  13.03587504,  13.2543125 ],
                              [ 10.99675008,  15.075     ,  13.2543125 ],
                              [ 15.075     ,  15.075     ,  13.2543125 ],
                              [ 19.15324992,  15.075     ,  13.2543125 ],
                              [ 13.03587504,  17.11412496,  13.2543125 ],
                              [ 17.11412496,  17.11412496,  13.2543125 ],
                              [ 10.99675008,  19.15324992,  13.2543125 ],
                              [ 15.075     ,  19.15324992,  13.2543125 ],
                              [ 19.15324992,  19.15324992,  13.2543125 ],
                              [ 13.03587504,  10.99675008,  15.2934375 ],
                              [ 17.11412496,  10.99675008,  15.2934375 ],
                              [ 10.99675008,  13.03587504,  15.2934375 ],
                              [ 15.075     ,  13.03587504,  15.2934375 ],
                              [ 19.15324992,  13.03587504,  15.2934375 ],
                              [ 13.03587504,  15.075     ,  15.2934375 ],
                              [ 17.11412496,  15.075     ,  15.2934375 ],
                              [ 10.99675008,  17.11412496,  15.2934375 ],
                              [ 15.075     ,  17.11412496,  15.2934375 ],
                              [ 19.15324992,  17.11412496,  15.2934375 ],
                              [ 13.03587504,  19.15324992,  15.2934375 ],
                              [ 17.11412496,  19.15324992,  15.2934375 ],
                              [ 10.99675008,  10.99675008,  17.3325625 ],
                              [ 15.075     ,  10.99675008,  17.3325625 ],
                              [ 19.15324992,  10.99675008,  17.3325625 ],
                              [ 13.03587504,  13.03587504,  17.3325625 ],
                              [ 17.11412496,  13.03587504,  17.3325625 ],
                              [ 10.99675008,  15.075     ,  17.3325625 ],
                              [ 15.075     ,  15.075     ,  17.3325625 ],
                              [ 19.15324992,  15.075     ,  17.3325625 ],
                              [ 13.03587504,  17.11412496,  17.3325625 ],
                              [ 17.11412496,  17.11412496,  17.3325625 ],
                              [ 10.99675008,  19.15324992,  17.3325625 ],
                              [ 15.075     ,  19.15324992,  17.3325625 ],
                              [ 19.15324992,  19.15324992,  17.3325625 ],
                              [ 13.03587504,  10.99675008,  19.3716875 ],
                              [ 17.11412496,  10.99675008,  19.3716875 ],
                              [ 10.99675008,  13.03587504,  19.3716875 ],
                              [ 15.075     ,  13.03587504,  19.3716875 ],
                              [ 19.15324992,  13.03587504,  19.3716875 ],
                              [ 13.03587504,  15.075     ,  19.3716875 ],
                              [ 17.11412496,  15.075     ,  19.3716875 ],
                              [ 10.99675008,  17.11412496,  19.3716875 ],
                              [ 15.075     ,  17.11412496,  19.3716875 ],
                              [ 19.15324992,  17.11412496,  19.3716875 ],
                              [ 13.03587504,  19.15324992,  19.3716875 ],
                              [ 17.11412496,  19.15324992,  19.3716875 ],
                              [ 10.99675008,  10.99675008,  21.4108125 ],
                              [ 15.075     ,  10.99675008,  21.4108125 ],
                              [ 19.15324992,  10.99675008,  21.4108125 ],
                              [ 13.03587504,  13.03587504,  21.4108125 ],
                              [ 17.11412496,  13.03587504,  21.4108125 ],
                              [ 10.99675008,  15.075     ,  21.4108125 ],
                              [ 15.075     ,  15.075     ,  21.4108125 ],
                              [ 19.15324992,  15.075     ,  21.4108125 ],
                              [ 13.03587504,  17.11412496,  21.4108125 ],
                              [ 17.11412496,  17.11412496,  21.4108125 ],
                              [ 10.99675008,  19.15324992,  21.4108125 ],
                              [ 15.075     ,  19.15324992,  21.4108125 ],
                              [ 19.15324992,  19.15324992,  21.4108125 ],
                              [ 13.03587504,  10.99675008,  23.4499375 ],
                              [ 17.11412496,  10.99675008,  23.4499375 ],
                              [ 10.99675008,  13.03587504,  23.4499375 ],
                              [ 15.075     ,  13.03587504,  23.4499375 ],
                              [ 19.15324992,  13.03587504,  23.4499375 ],
                              [ 13.03587504,  15.075     ,  23.4499375 ],
                              [ 17.11412496,  15.075     ,  23.4499375 ],
                              [ 10.99675008,  17.11412496,  23.4499375 ],
                              [ 15.075     ,  17.11412496,  23.4499375 ],
                              [ 19.15324992,  17.11412496,  23.4499375 ],
                              [ 13.03587504,  19.15324992,  23.4499375 ],
                              [ 17.11412496,  19.15324992,  23.4499375 ],
                              [ 10.99675008,  10.99675008,  25.4890625 ],
                              [ 15.075     ,  10.99675008,  25.4890625 ],
                              [ 19.15324992,  10.99675008,  25.4890625 ],
                              [ 13.03587504,  13.03587504,  25.4890625 ],
                              [ 17.11412496,  13.03587504,  25.4890625 ],
                              [ 10.99675008,  15.075     ,  25.4890625 ],
                              [ 15.075     ,  15.075     ,  25.4890625 ],
                              [ 19.15324992,  15.075     ,  25.4890625 ],
                              [ 13.03587504,  17.11412496,  25.4890625 ],
                              [ 17.11412496,  17.11412496,  25.4890625 ],
                              [ 10.99675008,  19.15324992,  25.4890625 ],
                              [ 15.075     ,  19.15324992,  25.4890625 ],
                              [ 19.15324992,  19.15324992,  25.4890625 ],
                              [ 13.03587504,  10.99675008,  27.5281875 ],
                              [ 17.11412496,  10.99675008,  27.5281875 ],
                              [ 10.99675008,  13.03587504,  27.5281875 ],
                              [ 15.075     ,  13.03587504,  27.5281875 ],
                              [ 19.15324992,  13.03587504,  27.5281875 ],
                              [ 13.03587504,  15.075     ,  27.5281875 ],
                              [ 17.11412496,  15.075     ,  27.5281875 ],
                              [ 10.99675008,  17.11412496,  27.5281875 ],
                              [ 15.075     ,  17.11412496,  27.5281875 ],
                              [ 19.15324992,  17.11412496,  27.5281875 ],
                              [ 13.03587504,  19.15324992,  27.5281875 ],
                              [ 17.11412496,  19.15324992,  27.5281875 ],
                              [ 10.99675008,  10.99675008,  29.5673125 ],
                              [ 15.075     ,  10.99675008,  29.5673125 ],
                              [ 19.15324992,  10.99675008,  29.5673125 ],
                              [ 13.03587504,  13.03587504,  29.5673125 ],
                              [ 17.11412496,  13.03587504,  29.5673125 ],
                              [ 10.99675008,  15.075     ,  29.5673125 ],
                              [ 15.075     ,  15.075     ,  29.5673125 ],
                              [ 19.15324992,  15.075     ,  29.5673125 ],
                              [ 13.03587504,  17.11412496,  29.5673125 ],
                              [ 17.11412496,  17.11412496,  29.5673125 ],
                              [ 10.99675008,  19.15324992,  29.5673125 ],
                              [ 15.075     ,  19.15324992,  29.5673125 ],
                              [ 19.15324992,  19.15324992,  29.5673125 ],
                              [ 13.03587504,  10.99675008,  31.6064375 ],
                              [ 17.11412496,  10.99675008,  31.6064375 ],
                              [ 10.99675008,  13.03587504,  31.6064375 ],
                              [ 15.075     ,  13.03587504,  31.6064375 ],
                              [ 19.15324992,  13.03587504,  31.6064375 ],
                              [ 13.03587504,  15.075     ,  31.6064375 ],
                              [ 17.11412496,  15.075     ,  31.6064375 ],
                              [ 10.99675008,  17.11412496,  31.6064375 ],
                              [ 15.075     ,  17.11412496,  31.6064375 ],
                              [ 19.15324992,  17.11412496,  31.6064375 ],
                              [ 13.03587504,  19.15324992,  31.6064375 ],
                              [ 17.11412496,  19.15324992,  31.6064375 ],
                              [ 10.99675008,  10.99675008,  33.6455625 ],
                              [ 15.075     ,  10.99675008,  33.6455625 ],
                              [ 19.15324992,  10.99675008,  33.6455625 ],
                              [ 13.03587504,  13.03587504,  33.6455625 ],
                              [ 17.11412496,  13.03587504,  33.6455625 ],
                              [ 10.99675008,  15.075     ,  33.6455625 ],
                              [ 15.075     ,  15.075     ,  33.6455625 ],
                              [ 19.15324992,  15.075     ,  33.6455625 ],
                              [ 13.03587504,  17.11412496,  33.6455625 ],
                              [ 17.11412496,  17.11412496,  33.6455625 ],
                              [ 10.99675008,  19.15324992,  33.6455625 ],
                              [ 15.075     ,  19.15324992,  33.6455625 ],
                              [ 19.15324992,  19.15324992,  33.6455625 ],
                              [ 13.03587504,  10.99675008,  35.6846875 ],
                              [ 17.11412496,  10.99675008,  35.6846875 ],
                              [ 10.99675008,  13.03587504,  35.6846875 ],
                              [ 15.075     ,  13.03587504,  35.6846875 ],
                              [ 19.15324992,  13.03587504,  35.6846875 ],
                              [ 13.03587504,  15.075     ,  35.6846875 ],
                              [ 17.11412496,  15.075     ,  35.6846875 ],
                              [ 10.99675008,  17.11412496,  35.6846875 ],
                              [ 15.075     ,  17.11412496,  35.6846875 ],
                              [ 19.15324992,  17.11412496,  35.6846875 ],
                              [ 13.03587504,  19.15324992,  35.6846875 ],
                              [ 17.11412496,  19.15324992,  35.6846875 ],
                              [ 10.99675008,  10.99675008,  37.7238125 ],
                              [ 15.075     ,  10.99675008,  37.7238125 ],
                              [ 19.15324992,  10.99675008,  37.7238125 ],
                              [ 13.03587504,  13.03587504,  37.7238125 ],
                              [ 17.11412496,  13.03587504,  37.7238125 ],
                              [ 10.99675008,  15.075     ,  37.7238125 ],
                              [ 15.075     ,  15.075     ,  37.7238125 ],
                              [ 19.15324992,  15.075     ,  37.7238125 ],
                              [ 13.03587504,  17.11412496,  37.7238125 ],
                              [ 17.11412496,  17.11412496,  37.7238125 ],
                              [ 10.99675008,  19.15324992,  37.7238125 ],
                              [ 15.075     ,  19.15324992,  37.7238125 ],
                              [ 19.15324992,  19.15324992,  37.7238125 ],
                              [ 13.03587504,  10.99675008,  39.7629375 ],
                              [ 17.11412496,  10.99675008,  39.7629375 ],
                              [ 10.99675008,  13.03587504,  39.7629375 ],
                              [ 15.075     ,  13.03587504,  39.7629375 ],
                              [ 19.15324992,  13.03587504,  39.7629375 ],
                              [ 13.03587504,  15.075     ,  39.7629375 ],
                              [ 17.11412496,  15.075     ,  39.7629375 ],
                              [ 10.99675008,  17.11412496,  39.7629375 ],
                              [ 15.075     ,  17.11412496,  39.7629375 ],
                              [ 19.15324992,  17.11412496,  39.7629375 ],
                              [ 13.03587504,  19.15324992,  39.7629375 ],
                              [ 17.11412496,  19.15324992,  39.7629375 ],
                              [ 10.99675008,  10.99675008,  41.8020625 ],
                              [ 15.075     ,  10.99675008,  41.8020625 ],
                              [ 19.15324992,  10.99675008,  41.8020625 ],
                              [ 13.03587504,  13.03587504,  41.8020625 ],
                              [ 17.11412496,  13.03587504,  41.8020625 ],
                              [ 10.99675008,  15.075     ,  41.8020625 ],
                              [ 15.075     ,  15.075     ,  41.8020625 ],
                              [ 19.15324992,  15.075     ,  41.8020625 ],
                              [ 13.03587504,  17.11412496,  41.8020625 ],
                              [ 17.11412496,  17.11412496,  41.8020625 ],
                              [ 10.99675008,  19.15324992,  41.8020625 ],
                              [ 15.075     ,  19.15324992,  41.8020625 ],
                              [ 19.15324992,  19.15324992,  41.8020625 ],
                              [ 13.03587504,  10.99675008,  43.8411875 ],
                              [ 17.11412496,  10.99675008,  43.8411875 ],
                              [ 10.99675008,  13.03587504,  43.8411875 ],
                              [ 15.075     ,  13.03587504,  43.8411875 ],
                              [ 19.15324992,  13.03587504,  43.8411875 ],
                              [ 13.03587504,  15.075     ,  43.8411875 ],
                              [ 17.11412496,  15.075     ,  43.8411875 ],
                              [ 10.99675008,  17.11412496,  43.8411875 ],
                              [ 15.075     ,  17.11412496,  43.8411875 ],
                              [ 19.15324992,  17.11412496,  43.8411875 ],
                              [ 13.03587504,  19.15324992,  43.8411875 ],
                              [ 17.11412496,  19.15324992,  43.8411875 ],
                              [ 10.99675008,  10.99675008,  45.8803125 ],
                              [ 15.075     ,  10.99675008,  45.8803125 ],
                              [ 19.15324992,  10.99675008,  45.8803125 ],
                              [ 13.03587504,  13.03587504,  45.8803125 ],
                              [ 17.11412496,  13.03587504,  45.8803125 ],
                              [ 10.99675008,  15.075     ,  45.8803125 ],
                              [ 15.075     ,  15.075     ,  45.8803125 ],
                              [ 19.15324992,  15.075     ,  45.8803125 ],
                              [ 13.03587504,  17.11412496,  45.8803125 ],
                              [ 17.11412496,  17.11412496,  45.8803125 ],
                              [ 10.99675008,  19.15324992,  45.8803125 ],
                              [ 15.075     ,  19.15324992,  45.8803125 ],
                              [ 19.15324992,  19.15324992,  45.8803125 ],
                              [ 13.03587504,  10.99675008,  47.9194375 ],
                              [ 17.11412496,  10.99675008,  47.9194375 ],
                              [ 10.99675008,  13.03587504,  47.9194375 ],
                              [ 15.075     ,  13.03587504,  47.9194375 ],
                              [ 19.15324992,  13.03587504,  47.9194375 ],
                              [ 13.03587504,  15.075     ,  47.9194375 ],
                              [ 17.11412496,  15.075     ,  47.9194375 ],
                              [ 10.99675008,  17.11412496,  47.9194375 ],
                              [ 15.075     ,  17.11412496,  47.9194375 ],
                              [ 19.15324992,  17.11412496,  47.9194375 ],
                              [ 13.03587504,  19.15324992,  47.9194375 ],
                              [ 17.11412496,  19.15324992,  47.9194375 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

# Add metallic region
metallic_region_0 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 30.15*Angstrom,
    ymin = 0.0*Angstrom, ymax = 1.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_1 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 1.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_2 = BoxRegion(
    0.0*Volt,
    xmin = 29.15*Angstrom, xmax = 30.15*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_region_3 = BoxRegion(
    0.0*Volt,
    xmin = 0.0*Angstrom, xmax = 30.15*Angstrom,
    ymin = 29.15*Angstrom, ymax = 30.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

# Add dielectric region
dielectric_region_0 = BoxRegion(
    25.0,
    xmin = 10.0*Angstrom, xmax = 1.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_1 = BoxRegion(
    25.0,
    xmin = 10.0*Angstrom, xmax = 20.0*Angstrom,
    ymin = 1.0*Angstrom, ymax = 10.0*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_2 = BoxRegion(
    25.0,
    xmin = 20.0*Angstrom, xmax = 29.15*Angstrom,
    ymin = 1.0*Angstrom, ymax = 29.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_region_3 = BoxRegion(
    25.0,
    xmin = 10.0*Angstrom, xmax = 20.0*Angstrom,
    ymin = 20.0*Angstrom, ymax = 29.15*Angstrom,
    zmin = 10.0*Angstrom, zmax = 40.0*Angstrom,
)

dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3]
central_region.setDielectricRegions(dielectric_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    ]

