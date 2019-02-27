# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [32.6513, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.8273, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 13.44189177,  12.83247676,   1.17728937],
                              [ 16.32565   ,  12.83247676,   1.17728937],
                              [ 19.20940823,  12.83247676,   1.17728937],
                              [ 12.00001265,  15.32988465,   1.17728937],
                              [ 14.88377088,  15.32988465,   1.17728937],
                              [ 17.76752912,  15.32988465,   1.17728937],
                              [ 20.65128735,  15.32988465,   1.17728937],
                              [ 13.44189177,  17.82729253,   1.17728937],
                              [ 16.32565   ,  17.82729253,   1.17728937],
                              [ 19.20940823,  17.82729253,   1.17728937],
                              [ 12.00001265,  13.66494606,   3.5318681 ],
                              [ 14.88377088,  13.66494606,   3.5318681 ],
                              [ 17.76752912,  13.66494606,   3.5318681 ],
                              [ 20.65128735,  13.66494606,   3.5318681 ],
                              [ 13.44189177,  16.16235394,   3.5318681 ],
                              [ 16.32565   ,  16.16235394,   3.5318681 ],
                              [ 19.20940823,  16.16235394,   3.5318681 ],
                              [ 12.00001265,  12.00000747,   5.88644684],
                              [ 14.88377088,  12.00000747,   5.88644684],
                              [ 17.76752912,  12.00000747,   5.88644684],
                              [ 20.65128735,  12.00000747,   5.88644684],
                              [ 13.44189177,  14.49741535,   5.88644684],
                              [ 16.32565   ,  14.49741535,   5.88644684],
                              [ 19.20940823,  14.49741535,   5.88644684],
                              [ 12.00001265,  16.99482324,   5.88644684],
                              [ 14.88377088,  16.99482324,   5.88644684],
                              [ 17.76752912,  16.99482324,   5.88644684],
                              [ 20.65128735,  16.99482324,   5.88644684]]*Angstrom

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
vector_b = [0.0, 29.8273, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 13.44189177,  12.83247676,   1.17728937],
                               [ 16.32565   ,  12.83247676,   1.17728937],
                               [ 19.20940823,  12.83247676,   1.17728937],
                               [ 14.88377088,  15.32988465,   1.17728937],
                               [ 17.76752912,  15.32988465,   1.17728937],
                               [ 20.65128735,  15.32988465,   1.17728937],
                               [ 13.44189177,  17.82729253,   1.17728937],
                               [ 16.32565   ,  17.82729253,   1.17728937],
                               [ 19.20940823,  17.82729253,   1.17728937],
                               [ 12.00001265,  13.66494606,   3.5318681 ],
                               [ 14.88377088,  13.66494606,   3.5318681 ],
                               [ 17.76752912,  13.66494606,   3.5318681 ],
                               [ 20.65128735,  13.66494606,   3.5318681 ],
                               [ 13.44189177,  16.16235394,   3.5318681 ],
                               [ 16.32565   ,  16.16235394,   3.5318681 ],
                               [ 19.20940823,  16.16235394,   3.5318681 ],
                               [ 12.00001265,  12.00000747,   5.88644684],
                               [ 14.88377088,  12.00000747,   5.88644684],
                               [ 17.76752912,  12.00000747,   5.88644684],
                               [ 20.65128735,  12.00000747,   5.88644684],
                               [ 13.44189177,  14.49741535,   5.88644684],
                               [ 16.32565   ,  14.49741535,   5.88644684],
                               [ 19.20940823,  14.49741535,   5.88644684],
                               [ 12.00001265,  16.99482324,   5.88644684],
                               [ 14.88377088,  16.99482324,   5.88644684],
                               [ 17.76752912,  16.99482324,   5.88644684],
                               [ 20.65128735,  16.99482324,   5.88644684]]*Angstrom

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
vector_b = [0.0, 29.8273, 0.0]*Angstrom
vector_c = [0.0, 0.0, 70.6373620597]*Angstrom
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
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
central_region_coordinates = [[ 13.44189177,  12.83247676,   1.17728937],
                              [ 16.32565   ,  12.83247676,   1.17728937],
                              [ 19.20940823,  12.83247676,   1.17728937],
                              [ 12.00001265,  15.32988465,   1.17728937],
                              [ 14.88377088,  15.32988465,   1.17728937],
                              [ 17.76752912,  15.32988465,   1.17728937],
                              [ 20.65128735,  15.32988465,   1.17728937],
                              [ 13.44189177,  17.82729253,   1.17728937],
                              [ 16.32565   ,  17.82729253,   1.17728937],
                              [ 19.20940823,  17.82729253,   1.17728937],
                              [ 12.00001265,  13.66494606,   3.5318681 ],
                              [ 14.88377088,  13.66494606,   3.5318681 ],
                              [ 17.76752912,  13.66494606,   3.5318681 ],
                              [ 20.65128735,  13.66494606,   3.5318681 ],
                              [ 13.44189177,  16.16235394,   3.5318681 ],
                              [ 16.32565   ,  16.16235394,   3.5318681 ],
                              [ 19.20940823,  16.16235394,   3.5318681 ],
                              [ 12.00001265,  12.00000747,   5.88644684],
                              [ 14.88377088,  12.00000747,   5.88644684],
                              [ 17.76752912,  12.00000747,   5.88644684],
                              [ 20.65128735,  12.00000747,   5.88644684],
                              [ 13.44189177,  14.49741535,   5.88644684],
                              [ 16.32565   ,  14.49741535,   5.88644684],
                              [ 19.20940823,  14.49741535,   5.88644684],
                              [ 12.00001265,  16.99482324,   5.88644684],
                              [ 14.88377088,  16.99482324,   5.88644684],
                              [ 17.76752912,  16.99482324,   5.88644684],
                              [ 20.65128735,  16.99482324,   5.88644684],
                              [ 13.44189177,  12.83247676,   8.24102557],
                              [ 16.32565   ,  12.83247676,   8.24102557],
                              [ 19.20940823,  12.83247676,   8.24102557],
                              [ 12.00001265,  15.32988465,   8.24102557],
                              [ 14.88377088,  15.32988465,   8.24102557],
                              [ 17.76752912,  15.32988465,   8.24102557],
                              [ 20.65128735,  15.32988465,   8.24102557],
                              [ 13.44189177,  17.82729253,   8.24102557],
                              [ 16.32565   ,  17.82729253,   8.24102557],
                              [ 19.20940823,  17.82729253,   8.24102557],
                              [ 12.00001265,  13.66494606,  10.59560431],
                              [ 14.88377088,  13.66494606,  10.59560431],
                              [ 17.76752912,  13.66494606,  10.59560431],
                              [ 20.65128735,  13.66494606,  10.59560431],
                              [ 13.44189177,  16.16235394,  10.59560431],
                              [ 16.32565   ,  16.16235394,  10.59560431],
                              [ 19.20940823,  16.16235394,  10.59560431],
                              [ 12.00001265,  12.00000747,  12.95018304],
                              [ 14.88377088,  12.00000747,  12.95018304],
                              [ 17.76752912,  12.00000747,  12.95018304],
                              [ 20.65128735,  12.00000747,  12.95018304],
                              [ 13.44189177,  14.49741535,  12.95018304],
                              [ 16.32565   ,  14.49741535,  12.95018304],
                              [ 19.20940823,  14.49741535,  12.95018304],
                              [ 12.00001265,  16.99482324,  12.95018304],
                              [ 14.88377088,  16.99482324,  12.95018304],
                              [ 17.76752912,  16.99482324,  12.95018304],
                              [ 20.65128735,  16.99482324,  12.95018304],
                              [ 13.44189177,  12.83247676,  15.30476178],
                              [ 16.32565   ,  12.83247676,  15.30476178],
                              [ 19.20940823,  12.83247676,  15.30476178],
                              [ 12.00001265,  15.32988465,  15.30476178],
                              [ 14.88377088,  15.32988465,  15.30476178],
                              [ 17.76752912,  15.32988465,  15.30476178],
                              [ 20.65128735,  15.32988465,  15.30476178],
                              [ 13.44189177,  17.82729253,  15.30476178],
                              [ 16.32565   ,  17.82729253,  15.30476178],
                              [ 19.20940823,  17.82729253,  15.30476178],
                              [ 12.00001265,  13.66494606,  17.65934051],
                              [ 14.88377088,  13.66494606,  17.65934051],
                              [ 17.76752912,  13.66494606,  17.65934051],
                              [ 20.65128735,  13.66494606,  17.65934051],
                              [ 13.44189177,  16.16235394,  17.65934051],
                              [ 16.32565   ,  16.16235394,  17.65934051],
                              [ 19.20940823,  16.16235394,  17.65934051],
                              [ 12.00001265,  12.00000747,  20.01391925],
                              [ 14.88377088,  12.00000747,  20.01391925],
                              [ 17.76752912,  12.00000747,  20.01391925],
                              [ 20.65128735,  12.00000747,  20.01391925],
                              [ 13.44189177,  14.49741535,  20.01391925],
                              [ 16.32565   ,  14.49741535,  20.01391925],
                              [ 19.20940823,  14.49741535,  20.01391925],
                              [ 12.00001265,  16.99482324,  20.01391925],
                              [ 14.88377088,  16.99482324,  20.01391925],
                              [ 17.76752912,  16.99482324,  20.01391925],
                              [ 20.65128735,  16.99482324,  20.01391925],
                              [ 13.44189177,  12.83247676,  22.36849799],
                              [ 16.32565   ,  12.83247676,  22.36849799],
                              [ 19.20940823,  12.83247676,  22.36849799],
                              [ 12.00001265,  15.32988465,  22.36849799],
                              [ 14.88377088,  15.32988465,  22.36849799],
                              [ 17.76752912,  15.32988465,  22.36849799],
                              [ 20.65128735,  15.32988465,  22.36849799],
                              [ 13.44189177,  17.82729253,  22.36849799],
                              [ 16.32565   ,  17.82729253,  22.36849799],
                              [ 19.20940823,  17.82729253,  22.36849799],
                              [ 12.00001265,  13.66494606,  24.72307672],
                              [ 14.88377088,  13.66494606,  24.72307672],
                              [ 17.76752912,  13.66494606,  24.72307672],
                              [ 20.65128735,  13.66494606,  24.72307672],
                              [ 13.44189177,  16.16235394,  24.72307672],
                              [ 16.32565   ,  16.16235394,  24.72307672],
                              [ 19.20940823,  16.16235394,  24.72307672],
                              [ 12.00001265,  12.00000747,  27.07765546],
                              [ 14.88377088,  12.00000747,  27.07765546],
                              [ 17.76752912,  12.00000747,  27.07765546],
                              [ 20.65128735,  12.00000747,  27.07765546],
                              [ 13.44189177,  14.49741535,  27.07765546],
                              [ 16.32565   ,  14.49741535,  27.07765546],
                              [ 19.20940823,  14.49741535,  27.07765546],
                              [ 12.00001265,  16.99482324,  27.07765546],
                              [ 14.88377088,  16.99482324,  27.07765546],
                              [ 17.76752912,  16.99482324,  27.07765546],
                              [ 20.65128735,  16.99482324,  27.07765546],
                              [ 13.44189177,  12.83247676,  29.43223419],
                              [ 16.32565   ,  12.83247676,  29.43223419],
                              [ 19.20940823,  12.83247676,  29.43223419],
                              [ 12.00001265,  15.32988465,  29.43223419],
                              [ 14.88377088,  15.32988465,  29.43223419],
                              [ 17.76752912,  15.32988465,  29.43223419],
                              [ 20.65128735,  15.32988465,  29.43223419],
                              [ 13.44189177,  17.82729253,  29.43223419],
                              [ 16.32565   ,  17.82729253,  29.43223419],
                              [ 19.20940823,  17.82729253,  29.43223419],
                              [ 12.00001265,  13.66494606,  31.78681293],
                              [ 14.88377088,  13.66494606,  31.78681293],
                              [ 17.76752912,  13.66494606,  31.78681293],
                              [ 20.65128735,  13.66494606,  31.78681293],
                              [ 13.44189177,  16.16235394,  31.78681293],
                              [ 16.32565   ,  16.16235394,  31.78681293],
                              [ 19.20940823,  16.16235394,  31.78681293],
                              [ 12.00001265,  12.00000747,  34.14139166],
                              [ 14.88377088,  12.00000747,  34.14139166],
                              [ 17.76752912,  12.00000747,  34.14139166],
                              [ 20.65128735,  12.00000747,  34.14139166],
                              [ 13.44189177,  14.49741535,  34.14139166],
                              [ 16.32565   ,  14.49741535,  34.14139166],
                              [ 19.20940823,  14.49741535,  34.14139166],
                              [ 12.00001265,  16.99482324,  34.14139166],
                              [ 14.88377088,  16.99482324,  34.14139166],
                              [ 17.76752912,  16.99482324,  34.14139166],
                              [ 20.65128735,  16.99482324,  34.14139166],
                              [ 18.32566265,  16.91365747,  35.3187    ],
                              [ 13.44189177,  12.83247676,  36.4959704 ],
                              [ 16.32565   ,  12.83247676,  36.4959704 ],
                              [ 19.20940823,  12.83247676,  36.4959704 ],
                              [ 12.00001265,  15.32988465,  36.4959704 ],
                              [ 14.88377088,  15.32988465,  36.4959704 ],
                              [ 17.76752912,  15.32988465,  36.4959704 ],
                              [ 20.65128735,  15.32988465,  36.4959704 ],
                              [ 13.44189177,  17.82729253,  36.4959704 ],
                              [ 16.32565   ,  17.82729253,  36.4959704 ],
                              [ 19.20940823,  17.82729253,  36.4959704 ],
                              [ 12.00001265,  13.66494606,  38.85054913],
                              [ 14.88377088,  13.66494606,  38.85054913],
                              [ 17.76752912,  13.66494606,  38.85054913],
                              [ 20.65128735,  13.66494606,  38.85054913],
                              [ 13.44189177,  16.16235394,  38.85054913],
                              [ 16.32565   ,  16.16235394,  38.85054913],
                              [ 19.20940823,  16.16235394,  38.85054913],
                              [ 12.00001265,  12.00000747,  41.20512787],
                              [ 14.88377088,  12.00000747,  41.20512787],
                              [ 17.76752912,  12.00000747,  41.20512787],
                              [ 20.65128735,  12.00000747,  41.20512787],
                              [ 13.44189177,  14.49741535,  41.20512787],
                              [ 16.32565   ,  14.49741535,  41.20512787],
                              [ 19.20940823,  14.49741535,  41.20512787],
                              [ 12.00001265,  16.99482324,  41.20512787],
                              [ 14.88377088,  16.99482324,  41.20512787],
                              [ 17.76752912,  16.99482324,  41.20512787],
                              [ 20.65128735,  16.99482324,  41.20512787],
                              [ 13.44189177,  12.83247676,  43.5597066 ],
                              [ 16.32565   ,  12.83247676,  43.5597066 ],
                              [ 19.20940823,  12.83247676,  43.5597066 ],
                              [ 12.00001265,  15.32988465,  43.5597066 ],
                              [ 14.88377088,  15.32988465,  43.5597066 ],
                              [ 17.76752912,  15.32988465,  43.5597066 ],
                              [ 20.65128735,  15.32988465,  43.5597066 ],
                              [ 13.44189177,  17.82729253,  43.5597066 ],
                              [ 16.32565   ,  17.82729253,  43.5597066 ],
                              [ 19.20940823,  17.82729253,  43.5597066 ],
                              [ 12.00001265,  13.66494606,  45.91428534],
                              [ 14.88377088,  13.66494606,  45.91428534],
                              [ 17.76752912,  13.66494606,  45.91428534],
                              [ 20.65128735,  13.66494606,  45.91428534],
                              [ 13.44189177,  16.16235394,  45.91428534],
                              [ 16.32565   ,  16.16235394,  45.91428534],
                              [ 19.20940823,  16.16235394,  45.91428534],
                              [ 12.00001265,  12.00000747,  48.26886407],
                              [ 14.88377088,  12.00000747,  48.26886407],
                              [ 17.76752912,  12.00000747,  48.26886407],
                              [ 20.65128735,  12.00000747,  48.26886407],
                              [ 13.44189177,  14.49741535,  48.26886407],
                              [ 16.32565   ,  14.49741535,  48.26886407],
                              [ 19.20940823,  14.49741535,  48.26886407],
                              [ 12.00001265,  16.99482324,  48.26886407],
                              [ 14.88377088,  16.99482324,  48.26886407],
                              [ 17.76752912,  16.99482324,  48.26886407],
                              [ 20.65128735,  16.99482324,  48.26886407],
                              [ 13.44189177,  12.83247676,  50.62344281],
                              [ 16.32565   ,  12.83247676,  50.62344281],
                              [ 19.20940823,  12.83247676,  50.62344281],
                              [ 12.00001265,  15.32988465,  50.62344281],
                              [ 14.88377088,  15.32988465,  50.62344281],
                              [ 17.76752912,  15.32988465,  50.62344281],
                              [ 20.65128735,  15.32988465,  50.62344281],
                              [ 13.44189177,  17.82729253,  50.62344281],
                              [ 16.32565   ,  17.82729253,  50.62344281],
                              [ 19.20940823,  17.82729253,  50.62344281],
                              [ 12.00001265,  13.66494606,  52.97802154],
                              [ 14.88377088,  13.66494606,  52.97802154],
                              [ 17.76752912,  13.66494606,  52.97802154],
                              [ 20.65128735,  13.66494606,  52.97802154],
                              [ 13.44189177,  16.16235394,  52.97802154],
                              [ 16.32565   ,  16.16235394,  52.97802154],
                              [ 19.20940823,  16.16235394,  52.97802154],
                              [ 12.00001265,  12.00000747,  55.33260028],
                              [ 14.88377088,  12.00000747,  55.33260028],
                              [ 17.76752912,  12.00000747,  55.33260028],
                              [ 20.65128735,  12.00000747,  55.33260028],
                              [ 13.44189177,  14.49741535,  55.33260028],
                              [ 16.32565   ,  14.49741535,  55.33260028],
                              [ 19.20940823,  14.49741535,  55.33260028],
                              [ 12.00001265,  16.99482324,  55.33260028],
                              [ 14.88377088,  16.99482324,  55.33260028],
                              [ 17.76752912,  16.99482324,  55.33260028],
                              [ 20.65128735,  16.99482324,  55.33260028],
                              [ 13.44189177,  12.83247676,  57.68717902],
                              [ 16.32565   ,  12.83247676,  57.68717902],
                              [ 19.20940823,  12.83247676,  57.68717902],
                              [ 12.00001265,  15.32988465,  57.68717902],
                              [ 14.88377088,  15.32988465,  57.68717902],
                              [ 17.76752912,  15.32988465,  57.68717902],
                              [ 20.65128735,  15.32988465,  57.68717902],
                              [ 13.44189177,  17.82729253,  57.68717902],
                              [ 16.32565   ,  17.82729253,  57.68717902],
                              [ 19.20940823,  17.82729253,  57.68717902],
                              [ 12.00001265,  13.66494606,  60.04175775],
                              [ 14.88377088,  13.66494606,  60.04175775],
                              [ 17.76752912,  13.66494606,  60.04175775],
                              [ 20.65128735,  13.66494606,  60.04175775],
                              [ 13.44189177,  16.16235394,  60.04175775],
                              [ 16.32565   ,  16.16235394,  60.04175775],
                              [ 19.20940823,  16.16235394,  60.04175775],
                              [ 12.00001265,  12.00000747,  62.39633649],
                              [ 14.88377088,  12.00000747,  62.39633649],
                              [ 17.76752912,  12.00000747,  62.39633649],
                              [ 20.65128735,  12.00000747,  62.39633649],
                              [ 13.44189177,  14.49741535,  62.39633649],
                              [ 16.32565   ,  14.49741535,  62.39633649],
                              [ 19.20940823,  14.49741535,  62.39633649],
                              [ 12.00001265,  16.99482324,  62.39633649],
                              [ 14.88377088,  16.99482324,  62.39633649],
                              [ 17.76752912,  16.99482324,  62.39633649],
                              [ 20.65128735,  16.99482324,  62.39633649],
                              [ 13.44189177,  12.83247676,  64.75091522],
                              [ 16.32565   ,  12.83247676,  64.75091522],
                              [ 19.20940823,  12.83247676,  64.75091522],
                              [ 14.88377088,  15.32988465,  64.75091522],
                              [ 17.76752912,  15.32988465,  64.75091522],
                              [ 20.65128735,  15.32988465,  64.75091522],
                              [ 13.44189177,  17.82729253,  64.75091522],
                              [ 16.32565   ,  17.82729253,  64.75091522],
                              [ 19.20940823,  17.82729253,  64.75091522],
                              [ 12.00001265,  13.66494606,  67.10549396],
                              [ 14.88377088,  13.66494606,  67.10549396],
                              [ 17.76752912,  13.66494606,  67.10549396],
                              [ 20.65128735,  13.66494606,  67.10549396],
                              [ 13.44189177,  16.16235394,  67.10549396],
                              [ 16.32565   ,  16.16235394,  67.10549396],
                              [ 19.20940823,  16.16235394,  67.10549396],
                              [ 12.00001265,  12.00000747,  69.46007269],
                              [ 14.88377088,  12.00000747,  69.46007269],
                              [ 17.76752912,  12.00000747,  69.46007269],
                              [ 20.65128735,  12.00000747,  69.46007269],
                              [ 13.44189177,  14.49741535,  69.46007269],
                              [ 16.32565   ,  14.49741535,  69.46007269],
                              [ 19.20940823,  14.49741535,  69.46007269],
                              [ 12.00001265,  16.99482324,  69.46007269],
                              [ 14.88377088,  16.99482324,  69.46007269],
                              [ 17.76752912,  16.99482324,  69.46007269],
                              [ 20.65128735,  16.99482324,  69.46007269]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )



dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00000747 *Angstrom,  ymax =  18.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  18.82729253 *Angstrom,  ymax =  28.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00000747 *Angstrom,  ymax =  18.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  21.65128735 *Angstrom,
        ymin =  11.00000747 *Angstrom,  ymax =  1.00000747 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  11.00000747 *Angstrom,  ymax =  1.00000747 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.00001265 *Angstrom,  xmax =  1.00001265 *Angstrom,
        ymin =  18.82729253 *Angstrom,  ymax =  28.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  18.82729253 *Angstrom,  ymax =  28.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  21.65128735 *Angstrom,  xmax =  31.65128735 *Angstrom,
        ymin =  11.00000747 *Angstrom,  ymax =  1.00000747 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.00001265 *Angstrom,  xmax =  1.26500000004e-05 *Angstrom,
        ymin =  1.00000747 *Angstrom,  ymax =  28.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  28.82729253 *Angstrom,  ymax =  29.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  31.65128735 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00000747 *Angstrom,  ymax =  28.82729253 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  1.26500000004e-05 *Angstrom,  xmax =  32.65128735 *Angstrom,
        ymin =  1.00000747 *Angstrom,  ymax =  7.4699999999e-06 *Angstrom,
        zmin =  9.730036345 *Angstrom,  zmax =  59.730036345 *Angstrom,
)
metallic_regions = [metallic_region_0, metallic_region_1, metallic_region_2, metallic_region_3]
central_region.setMetallicRegions(metallic_regions)


device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

