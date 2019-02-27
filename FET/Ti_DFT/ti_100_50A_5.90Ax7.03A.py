# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [29.9012, 0.0, 0.0]*Angstrom
vector_b = [0.0, 31.0252, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.2211782256]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium]

# Define coordinates
left_electrode_coordinates = [[ 13.4753    ,  14.341725  ,   0.42588243],
                              [ 16.4259    ,  14.341725  ,   0.42588243],
                              [ 13.4753    ,  19.025225  ,   0.42588243],
                              [ 16.4259    ,  19.025225  ,   0.42588243],
                              [ 13.4753    ,  11.999975  ,   2.12941213],
                              [ 16.4259    ,  11.999975  ,   2.12941213],
                              [ 13.4753    ,  16.683475  ,   2.12941213],
                              [ 16.4259    ,  16.683475  ,   2.12941213],
                              [ 12.        ,  14.341725  ,   2.98117698],
                              [ 14.9506    ,  14.341725  ,   2.98117698],
                              [ 17.9012    ,  14.341725  ,   2.98117698],
                              [ 14.9506    ,  19.025225  ,   2.98117698],
                              [ 17.9012    ,  19.025225  ,   2.98117698],
                              [ 12.        ,  19.02522496,   2.98117702],
                              [ 12.        ,  11.999975  ,   4.68470669],
                              [ 14.9506    ,  11.999975  ,   4.68470669],
                              [ 17.9012    ,  11.999975  ,   4.68470669],
                              [ 12.        ,  16.683475  ,   4.68470669],
                              [ 14.9506    ,  16.683475  ,   4.68470669],
                              [ 17.9012    ,  16.683475  ,   4.68470669],
                              [ 13.4753    ,  14.341725  ,   5.53647154],
                              [ 16.4259    ,  14.341725  ,   5.53647154],
                              [ 13.4753    ,  19.025225  ,   5.53647154],
                              [ 16.4259    ,  19.025225  ,   5.53647154],
                              [ 13.4753    ,  11.999975  ,   7.24000124],
                              [ 16.4259    ,  11.999975  ,   7.24000124],
                              [ 13.4753    ,  16.683475  ,   7.24000124],
                              [ 16.4259    ,  16.683475  ,   7.24000124],
                              [ 12.        ,  14.341725  ,   8.0917661 ],
                              [ 14.9506    ,  14.341725  ,   8.0917661 ],
                              [ 17.9012    ,  14.341725  ,   8.0917661 ],
                              [ 12.        ,  19.025225  ,   8.0917661 ],
                              [ 14.9506    ,  19.025225  ,   8.0917661 ],
                              [ 17.9012    ,  19.025225  ,   8.0917661 ],
                              [ 12.        ,  11.999975  ,   9.7952958 ],
                              [ 14.9506    ,  11.999975  ,   9.7952958 ],
                              [ 17.9012    ,  11.999975  ,   9.7952958 ],
                              [ 12.        ,  16.683475  ,   9.7952958 ],
                              [ 14.9506    ,  16.683475  ,   9.7952958 ],
                              [ 17.9012    ,  16.683475  ,   9.7952958 ]]*Angstrom

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
vector_a = [29.9012, 0.0, 0.0]*Angstrom
vector_b = [0.0, 31.0252, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.2211782256]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                            Titanium, Titanium, Titanium, Titanium]

# Define coordinates
right_electrode_coordinates = [[ 13.4753    ,  14.341725  ,   0.42588243],
                               [ 16.4259    ,  14.341725  ,   0.42588243],
                               [ 13.4753    ,  19.025225  ,   0.42588243],
                               [ 16.4259    ,  19.025225  ,   0.42588243],
                               [ 13.4753    ,  11.999975  ,   2.12941213],
                               [ 16.4259    ,  11.999975  ,   2.12941213],
                               [ 13.4753    ,  16.683475  ,   2.12941213],
                               [ 16.4259    ,  16.683475  ,   2.12941213],
                               [ 12.        ,  14.341725  ,   2.98117698],
                               [ 14.9506    ,  14.341725  ,   2.98117698],
                               [ 17.9012    ,  14.341725  ,   2.98117698],
                               [ 12.        ,  19.025225  ,   2.98117698],
                               [ 14.9506    ,  19.025225  ,   2.98117698],
                               [ 17.9012    ,  19.025225  ,   2.98117698],
                               [ 12.        ,  11.999975  ,   4.68470669],
                               [ 14.9506    ,  11.999975  ,   4.68470669],
                               [ 17.9012    ,  11.999975  ,   4.68470669],
                               [ 12.        ,  16.683475  ,   4.68470669],
                               [ 14.9506    ,  16.683475  ,   4.68470669],
                               [ 17.9012    ,  16.683475  ,   4.68470669],
                               [ 13.4753    ,  14.341725  ,   5.53647154],
                               [ 16.4259    ,  14.341725  ,   5.53647154],
                               [ 13.4753    ,  19.025225  ,   5.53647154],
                               [ 16.4259    ,  19.025225  ,   5.53647154],
                               [ 13.4753    ,  11.999975  ,   7.24000124],
                               [ 16.4259    ,  11.999975  ,   7.24000124],
                               [ 13.4753    ,  16.683475  ,   7.24000124],
                               [ 16.4259    ,  16.683475  ,   7.24000124],
                               [ 12.        ,  14.341725  ,   8.0917661 ],
                               [ 14.9506    ,  14.341725  ,   8.0917661 ],
                               [ 17.9012    ,  14.341725  ,   8.0917661 ],
                               [ 12.        ,  19.025225  ,   8.0917661 ],
                               [ 14.9506    ,  19.025225  ,   8.0917661 ],
                               [ 17.9012    ,  19.025225  ,   8.0917661 ],
                               [ 12.        ,  11.999975  ,   9.7952958 ],
                               [ 14.9506    ,  11.999975  ,   9.7952958 ],
                               [ 17.9012    ,  11.999975  ,   9.7952958 ],
                               [ 12.        ,  16.683475  ,   9.7952958 ],
                               [ 14.9506    ,  16.683475  ,   9.7952958 ],
                               [ 17.9012    ,  16.683475  ,   9.7952958 ]]*Angstrom

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
vector_a = [29.9012, 0.0, 0.0]*Angstrom
vector_b = [0.0, 31.0252, 0.0]*Angstrom
vector_c = [0.0, 0.0, 51.1058911281]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium, Titanium, Titanium, Titanium, Titanium,
                           Titanium, Titanium]

# Define coordinates
central_region_coordinates = [[ 13.4753    ,  14.341725  ,   0.42588243],
                              [ 16.4259    ,  14.341725  ,   0.42588243],
                              [ 13.4753    ,  19.025225  ,   0.42588243],
                              [ 16.4259    ,  19.025225  ,   0.42588243],
                              [ 13.4753    ,  11.999975  ,   2.12941213],
                              [ 16.4259    ,  11.999975  ,   2.12941213],
                              [ 13.4753    ,  16.683475  ,   2.12941213],
                              [ 16.4259    ,  16.683475  ,   2.12941213],
                              [ 12.        ,  14.341725  ,   2.98117698],
                              [ 14.9506    ,  14.341725  ,   2.98117698],
                              [ 17.9012    ,  14.341725  ,   2.98117698],
                              [ 14.9506    ,  19.025225  ,   2.98117698],
                              [ 17.9012    ,  19.025225  ,   2.98117698],
                              [ 12.        ,  19.02522496,   2.98117702],
                              [ 12.        ,  11.999975  ,   4.68470669],
                              [ 14.9506    ,  11.999975  ,   4.68470669],
                              [ 17.9012    ,  11.999975  ,   4.68470669],
                              [ 12.        ,  16.683475  ,   4.68470669],
                              [ 14.9506    ,  16.683475  ,   4.68470669],
                              [ 17.9012    ,  16.683475  ,   4.68470669],
                              [ 13.4753    ,  14.341725  ,   5.53647154],
                              [ 16.4259    ,  14.341725  ,   5.53647154],
                              [ 13.4753    ,  19.025225  ,   5.53647154],
                              [ 16.4259    ,  19.025225  ,   5.53647154],
                              [ 13.4753    ,  11.999975  ,   7.24000124],
                              [ 16.4259    ,  11.999975  ,   7.24000124],
                              [ 13.4753    ,  16.683475  ,   7.24000124],
                              [ 16.4259    ,  16.683475  ,   7.24000124],
                              [ 12.        ,  14.341725  ,   8.0917661 ],
                              [ 14.9506    ,  14.341725  ,   8.0917661 ],
                              [ 17.9012    ,  14.341725  ,   8.0917661 ],
                              [ 12.        ,  19.025225  ,   8.0917661 ],
                              [ 14.9506    ,  19.025225  ,   8.0917661 ],
                              [ 17.9012    ,  19.025225  ,   8.0917661 ],
                              [ 12.        ,  11.999975  ,   9.7952958 ],
                              [ 14.9506    ,  11.999975  ,   9.7952958 ],
                              [ 17.9012    ,  11.999975  ,   9.7952958 ],
                              [ 12.        ,  16.683475  ,   9.7952958 ],
                              [ 14.9506    ,  16.683475  ,   9.7952958 ],
                              [ 17.9012    ,  16.683475  ,   9.7952958 ],
                              [ 13.4753    ,  14.341725  ,  10.64706065],
                              [ 16.4259    ,  14.341725  ,  10.64706065],
                              [ 13.4753    ,  19.025225  ,  10.64706065],
                              [ 16.4259    ,  19.025225  ,  10.64706065],
                              [ 13.4753    ,  11.999975  ,  12.35059036],
                              [ 16.4259    ,  11.999975  ,  12.35059036],
                              [ 13.4753    ,  16.683475  ,  12.35059036],
                              [ 16.4259    ,  16.683475  ,  12.35059036],
                              [ 12.        ,  14.341725  ,  13.20235521],
                              [ 14.9506    ,  14.341725  ,  13.20235521],
                              [ 17.9012    ,  14.341725  ,  13.20235521],
                              [ 12.        ,  19.025225  ,  13.20235521],
                              [ 14.9506    ,  19.025225  ,  13.20235521],
                              [ 17.9012    ,  19.025225  ,  13.20235521],
                              [ 12.        ,  11.999975  ,  14.90588491],
                              [ 14.9506    ,  11.999975  ,  14.90588491],
                              [ 17.9012    ,  11.999975  ,  14.90588491],
                              [ 12.        ,  16.683475  ,  14.90588491],
                              [ 14.9506    ,  16.683475  ,  14.90588491],
                              [ 17.9012    ,  16.683475  ,  14.90588491],
                              [ 13.4753    ,  14.341725  ,  15.75764976],
                              [ 16.4259    ,  14.341725  ,  15.75764976],
                              [ 13.4753    ,  19.025225  ,  15.75764976],
                              [ 16.4259    ,  19.025225  ,  15.75764976],
                              [ 13.4753    ,  11.999975  ,  17.46117947],
                              [ 16.4259    ,  11.999975  ,  17.46117947],
                              [ 13.4753    ,  16.683475  ,  17.46117947],
                              [ 16.4259    ,  16.683475  ,  17.46117947],
                              [ 12.        ,  14.341725  ,  18.31294432],
                              [ 14.9506    ,  14.341725  ,  18.31294432],
                              [ 17.9012    ,  14.341725  ,  18.31294432],
                              [ 12.        ,  19.025225  ,  18.31294432],
                              [ 14.9506    ,  19.025225  ,  18.31294432],
                              [ 17.9012    ,  19.025225  ,  18.31294432],
                              [ 12.        ,  11.999975  ,  20.01647403],
                              [ 14.9506    ,  11.999975  ,  20.01647403],
                              [ 17.9012    ,  11.999975  ,  20.01647403],
                              [ 12.        ,  16.683475  ,  20.01647403],
                              [ 14.9506    ,  16.683475  ,  20.01647403],
                              [ 17.9012    ,  16.683475  ,  20.01647403],
                              [ 13.4753    ,  14.341725  ,  20.86823888],
                              [ 16.4259    ,  14.341725  ,  20.86823888],
                              [ 13.4753    ,  19.025225  ,  20.86823888],
                              [ 16.4259    ,  19.025225  ,  20.86823888],
                              [ 13.4753    ,  11.999975  ,  22.57176858],
                              [ 16.4259    ,  11.999975  ,  22.57176858],
                              [ 13.4753    ,  16.683475  ,  22.57176858],
                              [ 16.4259    ,  16.683475  ,  22.57176858],
                              [ 12.        ,  14.341725  ,  23.42353343],
                              [ 14.9506    ,  14.341725  ,  23.42353343],
                              [ 17.9012    ,  14.341725  ,  23.42353343],
                              [ 12.        ,  19.025225  ,  23.42353343],
                              [ 14.9506    ,  19.025225  ,  23.42353343],
                              [ 17.9012    ,  19.025225  ,  23.42353343],
                              [ 12.        ,  11.999975  ,  25.12706314],
                              [ 14.9506    ,  11.999975  ,  25.12706314],
                              [ 17.9012    ,  11.999975  ,  25.12706314],
                              [ 12.        ,  16.683475  ,  25.12706314],
                              [ 14.9506    ,  16.683475  ,  25.12706314],
                              [ 17.9012    ,  16.683475  ,  25.12706314],
                              [ 13.4753    ,  14.341725  ,  25.97882799],
                              [ 16.4259    ,  14.341725  ,  25.97882799],
                              [ 13.4753    ,  19.025225  ,  25.97882799],
                              [ 16.4259    ,  19.025225  ,  25.97882799],
                              [ 13.4753    ,  11.999975  ,  27.68235769],
                              [ 16.4259    ,  11.999975  ,  27.68235769],
                              [ 13.4753    ,  16.683475  ,  27.68235769],
                              [ 16.4259    ,  16.683475  ,  27.68235769],
                              [ 12.        ,  14.341725  ,  28.53412255],
                              [ 14.9506    ,  14.341725  ,  28.53412255],
                              [ 17.9012    ,  14.341725  ,  28.53412255],
                              [ 12.        ,  19.025225  ,  28.53412255],
                              [ 14.9506    ,  19.025225  ,  28.53412255],
                              [ 17.9012    ,  19.025225  ,  28.53412255],
                              [ 12.        ,  11.999975  ,  30.23765225],
                              [ 14.9506    ,  11.999975  ,  30.23765225],
                              [ 17.9012    ,  11.999975  ,  30.23765225],
                              [ 12.        ,  16.683475  ,  30.23765225],
                              [ 14.9506    ,  16.683475  ,  30.23765225],
                              [ 17.9012    ,  16.683475  ,  30.23765225],
                              [ 13.4753    ,  14.341725  ,  31.0894171 ],
                              [ 16.4259    ,  14.341725  ,  31.0894171 ],
                              [ 13.4753    ,  19.025225  ,  31.0894171 ],
                              [ 16.4259    ,  19.025225  ,  31.0894171 ],
                              [ 13.4753    ,  11.999975  ,  32.79294681],
                              [ 16.4259    ,  11.999975  ,  32.79294681],
                              [ 13.4753    ,  16.683475  ,  32.79294681],
                              [ 16.4259    ,  16.683475  ,  32.79294681],
                              [ 12.        ,  14.341725  ,  33.64471166],
                              [ 14.9506    ,  14.341725  ,  33.64471166],
                              [ 17.9012    ,  14.341725  ,  33.64471166],
                              [ 12.        ,  19.025225  ,  33.64471166],
                              [ 14.9506    ,  19.025225  ,  33.64471166],
                              [ 17.9012    ,  19.025225  ,  33.64471166],
                              [ 12.        ,  11.999975  ,  35.34824136],
                              [ 14.9506    ,  11.999975  ,  35.34824136],
                              [ 17.9012    ,  11.999975  ,  35.34824136],
                              [ 12.        ,  16.683475  ,  35.34824136],
                              [ 14.9506    ,  16.683475  ,  35.34824136],
                              [ 17.9012    ,  16.683475  ,  35.34824136],
                              [ 13.4753    ,  14.341725  ,  36.20000622],
                              [ 16.4259    ,  14.341725  ,  36.20000622],
                              [ 13.4753    ,  19.025225  ,  36.20000622],
                              [ 16.4259    ,  19.025225  ,  36.20000622],
                              [ 13.4753    ,  11.999975  ,  37.90353592],
                              [ 16.4259    ,  11.999975  ,  37.90353592],
                              [ 13.4753    ,  16.683475  ,  37.90353592],
                              [ 16.4259    ,  16.683475  ,  37.90353592],
                              [ 12.        ,  14.341725  ,  38.75530077],
                              [ 14.9506    ,  14.341725  ,  38.75530077],
                              [ 17.9012    ,  14.341725  ,  38.75530077],
                              [ 12.        ,  19.025225  ,  38.75530077],
                              [ 14.9506    ,  19.025225  ,  38.75530077],
                              [ 17.9012    ,  19.025225  ,  38.75530077],
                              [ 12.        ,  11.999975  ,  40.45883048],
                              [ 14.9506    ,  11.999975  ,  40.45883048],
                              [ 17.9012    ,  11.999975  ,  40.45883048],
                              [ 12.        ,  16.683475  ,  40.45883048],
                              [ 14.9506    ,  16.683475  ,  40.45883048],
                              [ 17.9012    ,  16.683475  ,  40.45883048],
                              [ 13.4753    ,  14.341725  ,  41.31059533],
                              [ 16.4259    ,  14.341725  ,  41.31059533],
                              [ 13.4753    ,  19.025225  ,  41.31059533],
                              [ 16.4259    ,  19.025225  ,  41.31059533],
                              [ 13.4753    ,  11.999975  ,  43.01412503],
                              [ 16.4259    ,  11.999975  ,  43.01412503],
                              [ 13.4753    ,  16.683475  ,  43.01412503],
                              [ 16.4259    ,  16.683475  ,  43.01412503],
                              [ 12.        ,  14.341725  ,  43.86588988],
                              [ 14.9506    ,  14.341725  ,  43.86588988],
                              [ 17.9012    ,  14.341725  ,  43.86588988],
                              [ 12.        ,  19.025225  ,  43.86588988],
                              [ 14.9506    ,  19.025225  ,  43.86588988],
                              [ 17.9012    ,  19.025225  ,  43.86588988],
                              [ 12.        ,  11.999975  ,  45.56941959],
                              [ 14.9506    ,  11.999975  ,  45.56941959],
                              [ 17.9012    ,  11.999975  ,  45.56941959],
                              [ 12.        ,  16.683475  ,  45.56941959],
                              [ 14.9506    ,  16.683475  ,  45.56941959],
                              [ 17.9012    ,  16.683475  ,  45.56941959],
                              [ 13.4753    ,  14.341725  ,  46.42118444],
                              [ 16.4259    ,  14.341725  ,  46.42118444],
                              [ 13.4753    ,  19.025225  ,  46.42118444],
                              [ 16.4259    ,  19.025225  ,  46.42118444],
                              [ 13.4753    ,  11.999975  ,  48.12471415],
                              [ 16.4259    ,  11.999975  ,  48.12471415],
                              [ 13.4753    ,  16.683475  ,  48.12471415],
                              [ 16.4259    ,  16.683475  ,  48.12471415],
                              [ 12.        ,  14.341725  ,  48.976479  ],
                              [ 14.9506    ,  14.341725  ,  48.976479  ],
                              [ 17.9012    ,  14.341725  ,  48.976479  ],
                              [ 12.        ,  19.025225  ,  48.976479  ],
                              [ 14.9506    ,  19.025225  ,  48.976479  ],
                              [ 17.9012    ,  19.025225  ,  48.976479  ],
                              [ 12.        ,  11.999975  ,  50.6800087 ],
                              [ 14.9506    ,  11.999975  ,  50.6800087 ],
                              [ 17.9012    ,  11.999975  ,  50.6800087 ],
                              [ 12.        ,  16.683475  ,  50.6800087 ],
                              [ 14.9506    ,  16.683475  ,  50.6800087 ],
                              [ 17.9012    ,  16.683475  ,  50.6800087 ]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )


dielectric_region_0 = BoxRegion(
        80.0 ,
        xmin =  11.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  10.999975 *Angstrom,  ymax =  20.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        80.0 ,
        xmin =  11.0 *Angstrom,  xmax =  18.9012 *Angstrom,
        ymin =  20.025225 *Angstrom,  ymax =  30.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        80.0 ,
        xmin =  18.9012 *Angstrom,  xmax =  28.9012 *Angstrom,
        ymin =  10.999975 *Angstrom,  ymax =  20.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        80.0 ,
        xmin =  11.0 *Angstrom,  xmax =  18.9012 *Angstrom,
        ymin =  10.999975 *Angstrom,  ymax =  0.999975 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        80.0 ,
        xmin =  11.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  10.999975 *Angstrom,  ymax =  0.999975 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        80.0 ,
        xmin =  11.0 *Angstrom,  xmax =  1.0 *Angstrom,
        ymin =  20.025225 *Angstrom,  ymax =  30.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        80.0 ,
        xmin =  18.9012 *Angstrom,  xmax =  28.9012 *Angstrom,
        ymin =  20.025225 *Angstrom,  ymax =  30.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        80.0 ,
        xmin =  18.9012 *Angstrom,  xmax =  28.9012 *Angstrom,
        ymin =  10.999975 *Angstrom,  ymax =  0.999975 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.0 *Angstrom,  xmax =  0.0 *Angstrom,
        ymin =  0.999975 *Angstrom,  ymax =  30.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  0.0 *Angstrom,  xmax =  29.9012 *Angstrom,
        ymin =  30.025225 *Angstrom,  ymax =  31.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  28.9012 *Angstrom,  xmax =  29.9012 *Angstrom,
        ymin =  0.999975 *Angstrom,  ymax =  30.025225 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  0.0 *Angstrom,  xmax =  29.9012 *Angstrom,
        ymin =  0.999975 *Angstrom,  ymax =  -2.50000000008e-05 *Angstrom,
        zmin =  10.34000435 *Angstrom,  zmax =  40.34000435 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )
basis_set = [
    GGABasis.Titanium_DoubleZetaPolarized,
    ]


