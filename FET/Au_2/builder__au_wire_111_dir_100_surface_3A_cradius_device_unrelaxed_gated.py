# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [29.58, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.58, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[ 13.61271063,  13.61271063,   1.17728937],
                              [ 16.39820718,  14.35908218,   1.17728937],
                              [ 14.35908218,  16.39820718,   1.17728937],
                              [ 14.04362845,  12.00450345,   3.5318681 ],
                              [ 16.829125  ,  12.750875  ,   3.5318681 ],
                              [ 12.00450345,  14.04362845,   3.5318681 ],
                              [ 14.79      ,  14.79      ,   3.5318681 ],
                              [ 17.57549655,  15.53637155,   3.5318681 ],
                              [ 12.750875  ,  16.829125  ,   3.5318681 ],
                              [ 15.53637155,  17.57549655,   3.5318681 ],
                              [ 15.22091782,  13.18179282,   5.88644684],
                              [ 13.18179282,  15.22091782,   5.88644684],
                              [ 15.96728937,  15.96728937,   5.88644684]]*Angstrom

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
vector_a = [29.58, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.58, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                            Gold, Gold, Gold]

# Define coordinates
right_electrode_coordinates = [[ 13.61271063,  13.61271063,   1.17728937],
                               [ 16.39820718,  14.35908218,   1.17728937],
                               [ 14.35908218,  16.39820718,   1.17728937],
                               [ 14.04362845,  12.00450345,   3.5318681 ],
                               [ 16.829125  ,  12.750875  ,   3.5318681 ],
                               [ 12.00450345,  14.04362845,   3.5318681 ],
                               [ 14.79      ,  14.79      ,   3.5318681 ],
                               [ 17.57549655,  15.53637155,   3.5318681 ],
                               [ 12.750875  ,  16.829125  ,   3.5318681 ],
                               [ 15.53637155,  17.57549655,   3.5318681 ],
                               [ 15.22091782,  13.18179282,   5.88644684],
                               [ 13.18179282,  15.22091782,   5.88644684],
                               [ 15.96728937,  15.96728937,   5.88644684]]*Angstrom

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
vector_a = [29.58, 0.0, 0.0]*Angstrom
vector_b = [0.0, 29.58, 0.0]*Angstrom
vector_c = [0.0, 0.0, 49.4461534418]*Angstrom
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
                           Gold]

# Define coordinates
central_region_coordinates = [[ 13.61271063,  13.61271063,   1.17728937],
                              [ 16.39820718,  14.35908218,   1.17728937],
                              [ 14.35908218,  16.39820718,   1.17728937],
                              [ 14.04362845,  12.00450345,   3.5318681 ],
                              [ 16.829125  ,  12.750875  ,   3.5318681 ],
                              [ 12.00450345,  14.04362845,   3.5318681 ],
                              [ 14.79      ,  14.79      ,   3.5318681 ],
                              [ 17.57549655,  15.53637155,   3.5318681 ],
                              [ 12.750875  ,  16.829125  ,   3.5318681 ],
                              [ 15.53637155,  17.57549655,   3.5318681 ],
                              [ 15.22091782,  13.18179282,   5.88644684],
                              [ 13.18179282,  15.22091782,   5.88644684],
                              [ 15.96728937,  15.96728937,   5.88644684],
                              [ 13.61271063,  13.61271063,   8.24102557],
                              [ 16.39820718,  14.35908218,   8.24102557],
                              [ 14.35908218,  16.39820718,   8.24102557],
                              [ 14.04362845,  12.00450345,  10.59560431],
                              [ 16.829125  ,  12.750875  ,  10.59560431],
                              [ 12.00450345,  14.04362845,  10.59560431],
                              [ 14.79      ,  14.79      ,  10.59560431],
                              [ 17.57549655,  15.53637155,  10.59560431],
                              [ 12.750875  ,  16.829125  ,  10.59560431],
                              [ 15.53637155,  17.57549655,  10.59560431],
                              [ 15.22091782,  13.18179282,  12.95018304],
                              [ 13.18179282,  15.22091782,  12.95018304],
                              [ 15.96728937,  15.96728937,  12.95018304],
                              [ 13.61271063,  13.61271063,  15.30476178],
                              [ 16.39820718,  14.35908218,  15.30476178],
                              [ 14.35908218,  16.39820718,  15.30476178],
                              [ 14.04362845,  12.00450345,  17.65934051],
                              [ 16.829125  ,  12.750875  ,  17.65934051],
                              [ 12.00450345,  14.04362845,  17.65934051],
                              [ 14.79      ,  14.79      ,  17.65934051],
                              [ 17.57549655,  15.53637155,  17.65934051],
                              [ 12.750875  ,  16.829125  ,  17.65934051],
                              [ 15.53637155,  17.57549655,  17.65934051],
                              [ 15.22091782,  13.18179282,  20.01391925],
                              [ 13.18179282,  15.22091782,  20.01391925],
                              [ 15.96728937,  15.96728937,  20.01391925],
                              [ 13.61271063,  13.61271063,  22.36849799],
                              [ 16.39820718,  14.35908218,  22.36849799],
                              [ 14.35908218,  16.39820718,  22.36849799],
                              [ 14.04362845,  12.00450345,  24.72307672],
                              [ 16.829125  ,  12.750875  ,  24.72307672],
                              [ 12.00450345,  14.04362845,  24.72307672],
                              [ 14.79      ,  14.79      ,  24.72307672],
                              [ 17.57549655,  15.53637155,  24.72307672],
                              [ 12.750875  ,  16.829125  ,  24.72307672],
                              [ 15.53637155,  17.57549655,  24.72307672],
                              [ 15.22091782,  13.18179282,  27.07765546],
                              [ 13.18179282,  15.22091782,  27.07765546],
                              [ 15.96728937,  15.96728937,  27.07765546],
                              [ 13.61271063,  13.61271063,  29.43223419],
                              [ 16.39820718,  14.35908218,  29.43223419],
                              [ 14.35908218,  16.39820718,  29.43223419],
                              [ 14.04362845,  12.00450345,  31.78681293],
                              [ 16.829125  ,  12.750875  ,  31.78681293],
                              [ 12.00450345,  14.04362845,  31.78681293],
                              [ 14.79      ,  14.79      ,  31.78681293],
                              [ 17.57549655,  15.53637155,  31.78681293],
                              [ 12.750875  ,  16.829125  ,  31.78681293],
                              [ 15.53637155,  17.57549655,  31.78681293],
                              [ 15.22091782,  13.18179282,  34.14139166],
                              [ 13.18179282,  15.22091782,  34.14139166],
                              [ 15.96728937,  15.96728937,  34.14139166],
                              [ 13.61271063,  13.61271063,  36.4959704 ],
                              [ 16.39820718,  14.35908218,  36.4959704 ],
                              [ 14.35908218,  16.39820718,  36.4959704 ],
                              [ 14.04362845,  12.00450345,  38.85054913],
                              [ 16.829125  ,  12.750875  ,  38.85054913],
                              [ 12.00450345,  14.04362845,  38.85054913],
                              [ 14.79      ,  14.79      ,  38.85054913],
                              [ 17.57549655,  15.53637155,  38.85054913],
                              [ 12.750875  ,  16.829125  ,  38.85054913],
                              [ 15.53637155,  17.57549655,  38.85054913],
                              [ 15.22091782,  13.18179282,  41.20512787],
                              [ 13.18179282,  15.22091782,  41.20512787],
                              [ 15.96728937,  15.96728937,  41.20512787],
                              [ 13.61271063,  13.61271063,  43.5597066 ],
                              [ 16.39820718,  14.35908218,  43.5597066 ],
                              [ 14.35908218,  16.39820718,  43.5597066 ],
                              [ 14.04362845,  12.00450345,  45.91428534],
                              [ 16.829125  ,  12.750875  ,  45.91428534],
                              [ 12.00450345,  14.04362845,  45.91428534],
                              [ 14.79      ,  14.79      ,  45.91428534],
                              [ 17.57549655,  15.53637155,  45.91428534],
                              [ 12.750875  ,  16.829125  ,  45.91428534],
                              [ 15.53637155,  17.57549655,  45.91428534],
                              [ 15.22091782,  13.18179282,  48.26886407],
                              [ 13.18179282,  15.22091782,  48.26886407],
                              [ 15.96728937,  15.96728937,  48.26886407]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )


dielectric_region_0 = BoxRegion(
        25.0 ,
        xmin =  11.00450345 *Angstrom,  xmax =  1.00450345 *Angstrom,
        ymin =  11.00450345 *Angstrom,  ymax =  18.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_1 = BoxRegion(
        25.0 ,
        xmin =  11.00450345 *Angstrom,  xmax =  18.57549655 *Angstrom,
        ymin =  18.57549655 *Angstrom,  ymax =  28.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_2 = BoxRegion(
        25.0 ,
        xmin =  18.57549655 *Angstrom,  xmax =  28.57549655 *Angstrom,
        ymin =  11.00450345 *Angstrom,  ymax =  18.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_3 = BoxRegion(
        25.0 ,
        xmin =  11.00450345 *Angstrom,  xmax =  18.57549655 *Angstrom,
        ymin =  11.00450345 *Angstrom,  ymax =  1.00450345 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_4 = BoxRegion(
        25.0 ,
        xmin =  11.00450345 *Angstrom,  xmax =  1.00450345 *Angstrom,
        ymin =  11.00450345 *Angstrom,  ymax =  1.00450345 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_5 = BoxRegion(
        25.0 ,
        xmin =  11.00450345 *Angstrom,  xmax =  1.00450345 *Angstrom,
        ymin =  18.57549655 *Angstrom,  ymax =  28.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_6 = BoxRegion(
        25.0 ,
        xmin =  18.57549655 *Angstrom,  xmax =  28.57549655 *Angstrom,
        ymin =  18.57549655 *Angstrom,  ymax =  28.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_region_7 = BoxRegion(
        25.0 ,
        xmin =  18.57549655 *Angstrom,  xmax =  28.57549655 *Angstrom,
        ymin =  11.00450345 *Angstrom,  ymax =  1.00450345 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
dielectric_regions = [dielectric_region_0, dielectric_region_1, dielectric_region_2, dielectric_region_3, dielectric_region_4, dielectric_region_5, dielectric_region_6, dielectric_region_7]
central_region.setDielectricRegions(dielectric_regions)


#Metal regions...
metallic_region_0 = BoxRegion(
        0.0 *Volt,
        xmin =  1.00450345 *Angstrom,  xmax =  0.00450345 *Angstrom,
        ymin =  1.00450345 *Angstrom,  ymax =  28.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
metallic_region_1 = BoxRegion(
        0.0 *Volt,
        xmin =  0.00450345 *Angstrom,  xmax =  29.57549655 *Angstrom,
        ymin =  28.57549655 *Angstrom,  ymax =  29.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
metallic_region_2 = BoxRegion(
        0.0 *Volt,
        xmin =  28.57549655 *Angstrom,  xmax =  29.57549655 *Angstrom,
        ymin =  1.00450345 *Angstrom,  ymax =  28.57549655 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
)
metallic_region_3 = BoxRegion(
        0.0 *Volt,
        xmin =  0.00450345 *Angstrom,  xmax =  29.57549655 *Angstrom,
        ymin =  1.00450345 *Angstrom,  ymax =  0.00450345 *Angstrom,
        zmin =  9.134432035 *Angstrom,  zmax =  39.134432035 *Angstrom,
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


