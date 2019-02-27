# -------------------------------------------------------------
# Left electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [4.32563734556, 7.49222365763, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold]

# Define coordinates
left_electrode_coordinates = [[  2.88375823,   1.66493859,   1.17728937],
                              [  5.76751646,   1.66493859,   1.17728937],
                              [  8.65127469,   1.66493859,   1.17728937],
                              [  4.32563735,   4.16234648,   1.17728937],
                              [  7.20939558,   4.16234648,   1.17728937],
                              [ 10.09315381,   4.16234648,   1.17728937],
                              [  5.76751646,   6.65975436,   1.17728937],
                              [  8.65127469,   6.65975436,   1.17728937],
                              [ 11.53503292,   6.65975436,   1.17728937],
                              [ -0.        ,   0.        ,   3.5318681 ],
                              [  2.88375823,   0.        ,   3.5318681 ],
                              [  5.76751646,   0.        ,   3.5318681 ],
                              [  1.44187912,   2.49740789,   3.5318681 ],
                              [  4.32563735,   2.49740789,   3.5318681 ],
                              [  7.20939558,   2.49740789,   3.5318681 ],
                              [  2.88375823,   4.99481577,   3.5318681 ],
                              [  5.76751646,   4.99481577,   3.5318681 ],
                              [  8.65127469,   4.99481577,   3.5318681 ],
                              [  1.44187912,   0.8324693 ,   5.88644684],
                              [  4.32563735,   0.8324693 ,   5.88644684],
                              [  7.20939558,   0.8324693 ,   5.88644684],
                              [  2.88375823,   3.32987718,   5.88644684],
                              [  5.76751646,   3.32987718,   5.88644684],
                              [  8.65127469,   3.32987718,   5.88644684],
                              [  4.32563735,   5.82728507,   5.88644684],
                              [  7.20939558,   5.82728507,   5.88644684],
                              [ 10.09315381,   5.82728507,   5.88644684]]*Angstrom

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
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [4.32563734556, 7.49222365763, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.42971994036]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Hafnium,
                            Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
right_electrode_coordinates = [[  0.        ,   0.        ,   0.73828666],
                               [  5.56153373,   1.07031767,   0.73828666],
                               [  2.47179277,   2.14063533,   0.73828666],
                               [  8.0333265 ,   3.210953  ,   0.73828666],
                               [  4.94358554,   4.28127066,   0.73828666],
                               [ 10.50511927,   5.35158833,   0.73828666],
                               [  7.41537831,   6.42190599,   0.73828666],
                               [  1.85384458,   0.35677256,   1.47657331],
                               [  7.41537831,   1.42709022,   1.47657331],
                               [  4.32563735,   2.49740789,   1.47657331],
                               [  9.88717108,   3.56772555,   1.47657331],
                               [  6.79743011,   4.63804322,   1.47657331],
                               [  3.70768915,   5.70836088,   1.47657331],
                               [  9.26922288,   6.77867855,   1.47657331],
                               [  3.70768915,   0.71354511,   2.21485997],
                               [  9.26922288,   1.78386278,   2.21485997],
                               [  6.17948192,   2.85418044,   2.21485997],
                               [  3.08974096,   3.92449811,   2.21485997],
                               [  8.65127469,   4.99481577,   2.21485997],
                               [  5.56153373,   6.06513344,   2.21485997],
                               [ 11.12306746,   7.1354511 ,   2.21485997],
                               [  1.85384458,   0.35677256,   3.69143328],
                               [  7.41537831,   1.42709022,   3.69143328],
                               [  4.32563735,   2.49740789,   3.69143328],
                               [  9.88717108,   3.56772555,   3.69143328],
                               [  6.79743011,   4.63804322,   3.69143328],
                               [  3.70768915,   5.70836088,   3.69143328],
                               [  9.26922288,   6.77867855,   3.69143328]]*Angstrom

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
vector_a = [8.65127469112, 0.0, 0.0]*Angstrom
vector_b = [4.32563734556, 7.49222365763, 0.0]*Angstrom
vector_c = [0.0, 0.0, 18.5018975628]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
                           Gold, Gold, Gold, Gold, Gold, Hafnium, Hafnium, Hafnium, Hafnium,
                           Hafnium, Hafnium, Hafnium, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium,
                           Hafnium, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
                           Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
central_region_coordinates = [[  2.88375823,   1.66493859,   1.17728937],
                              [  5.76751646,   1.66493859,   1.17728937],
                              [  8.65127469,   1.66493859,   1.17728937],
                              [  4.32563735,   4.16234648,   1.17728937],
                              [  7.20939558,   4.16234648,   1.17728937],
                              [ 10.09315381,   4.16234648,   1.17728937],
                              [  5.76751646,   6.65975436,   1.17728937],
                              [  8.65127469,   6.65975436,   1.17728937],
                              [ 11.53503292,   6.65975436,   1.17728937],
                              [ -0.        ,   0.        ,   3.5318681 ],
                              [  2.88375823,   0.        ,   3.5318681 ],
                              [  5.76751646,   0.        ,   3.5318681 ],
                              [  1.44187912,   2.49740789,   3.5318681 ],
                              [  4.32563735,   2.49740789,   3.5318681 ],
                              [  7.20939558,   2.49740789,   3.5318681 ],
                              [  2.88375823,   4.99481577,   3.5318681 ],
                              [  5.76751646,   4.99481577,   3.5318681 ],
                              [  8.65127469,   4.99481577,   3.5318681 ],
                              [  1.44187912,   0.8324693 ,   5.88644684],
                              [  4.32563735,   0.8324693 ,   5.88644684],
                              [  7.20939558,   0.8324693 ,   5.88644684],
                              [  2.88375823,   3.32987718,   5.88644684],
                              [  5.76751646,   3.32987718,   5.88644684],
                              [  8.65127469,   3.32987718,   5.88644684],
                              [  4.32563735,   5.82728507,   5.88644684],
                              [  7.20939558,   5.82728507,   5.88644684],
                              [ 10.09315381,   5.82728507,   5.88644684],
                              [  2.88375823,   1.66493859,   8.24102557],
                              [  5.76751646,   1.66493859,   8.24102557],
                              [  8.65127469,   1.66493859,   8.24102557],
                              [  4.32563735,   4.16234648,   8.24102557],
                              [  7.20939558,   4.16234648,   8.24102557],
                              [ 10.09315381,   4.16234648,   8.24102557],
                              [  5.76751646,   6.65975436,   8.24102557],
                              [  8.65127469,   6.65975436,   8.24102557],
                              [ 11.53503292,   6.65975436,   8.24102557],
                              [ -0.        ,   0.        ,  10.59560431],
                              [  2.88375823,   0.        ,  10.59560431],
                              [  5.76751646,   0.        ,  10.59560431],
                              [  1.44187912,   2.49740789,  10.59560431],
                              [  4.32563735,   2.49740789,  10.59560431],
                              [  7.20939558,   2.49740789,  10.59560431],
                              [  2.88375823,   4.99481577,  10.59560431],
                              [  5.76751646,   4.99481577,  10.59560431],
                              [  8.65127469,   4.99481577,  10.59560431],
                              [  0.        ,   0.        ,  12.59560431],
                              [  5.56153373,   1.07031767,  12.59560431],
                              [  2.47179277,   2.14063533,  12.59560431],
                              [  8.0333265 ,   3.210953  ,  12.59560431],
                              [  4.94358554,   4.28127066,  12.59560431],
                              [ 10.50511927,   5.35158833,  12.59560431],
                              [  7.41537831,   6.42190599,  12.59560431],
                              [  1.85384458,   0.35677256,  13.33389097],
                              [  7.41537831,   1.42709022,  13.33389097],
                              [  4.32563735,   2.49740789,  13.33389097],
                              [  9.88717108,   3.56772555,  13.33389097],
                              [  6.79743011,   4.63804322,  13.33389097],
                              [  3.70768915,   5.70836088,  13.33389097],
                              [  9.26922288,   6.77867855,  13.33389097],
                              [  0.        ,   0.        ,  14.81046428],
                              [  5.56153373,   1.07031767,  14.81046428],
                              [  2.47179277,   2.14063533,  14.81046428],
                              [  8.0333265 ,   3.210953  ,  14.81046428],
                              [  4.94358554,   4.28127066,  14.81046428],
                              [ 10.50511927,   5.35158833,  14.81046428],
                              [  7.41537831,   6.42190599,  14.81046428],
                              [  1.85384458,   0.35677256,  15.54875094],
                              [  7.41537831,   1.42709022,  15.54875094],
                              [  4.32563735,   2.49740789,  15.54875094],
                              [  9.88717108,   3.56772555,  15.54875094],
                              [  6.79743011,   4.63804322,  15.54875094],
                              [  3.70768915,   5.70836088,  15.54875094],
                              [  9.26922288,   6.77867855,  15.54875094],
                              [  3.70768915,   0.71354511,  16.28703759],
                              [  9.26922288,   1.78386278,  16.28703759],
                              [  6.17948192,   2.85418044,  16.28703759],
                              [  3.08974096,   3.92449811,  16.28703759],
                              [  8.65127469,   4.99481577,  16.28703759],
                              [  5.56153373,   6.06513344,  16.28703759],
                              [ 11.12306746,   7.1354511 ,  16.28703759],
                              [  1.85384458,   0.35677256,  17.76361091],
                              [  7.41537831,   1.42709022,  17.76361091],
                              [  4.32563735,   2.49740789,  17.76361091],
                              [  9.88717108,   3.56772555,  17.76361091],
                              [  6.79743011,   4.63804322,  17.76361091],
                              [  3.70768915,   5.70836088,  17.76361091],
                              [  9.26922288,   6.77867855,  17.76361091]]*Angstrom

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

