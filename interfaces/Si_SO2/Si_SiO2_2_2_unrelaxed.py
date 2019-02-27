# Set up lattice
vector_a = [21.3802935803, 0.0, 0.0]*Angstrom
vector_b = [-10.6901467902, 18.5158773809, 0.0]*Angstrom
vector_c = [0.0, 0.0, 10.0922771508]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen]

# Define coordinates
fractional_coordinates = [[ 0.        ,  0.        ,  0.        ],
                          [ 0.19354839,  0.03225806,  0.        ],
                          [ 0.38709677,  0.06451613, -0.        ],
                          [ 0.58064516,  0.09677419, -0.        ],
                          [ 0.77419355,  0.12903226, -0.        ],
                          [ 0.96774194,  0.16129032,  0.        ],
                          [ 0.16129032,  0.19354839,  0.        ],
                          [ 0.35483871,  0.22580645, -0.        ],
                          [ 0.5483871 ,  0.25806452,  0.        ],
                          [ 0.74193548,  0.29032258,  0.        ],
                          [ 0.93548387,  0.32258065,  0.        ],
                          [ 0.12903226,  0.35483871,  0.        ],
                          [ 0.32258065,  0.38709677,  0.        ],
                          [ 0.51612903,  0.41935484, -0.        ],
                          [ 0.70967742,  0.4516129 , -0.        ],
                          [ 0.90322581,  0.48387097, -0.        ],
                          [ 0.09677419,  0.51612903,  0.        ],
                          [ 0.29032258,  0.5483871 ,  0.        ],
                          [ 0.48387097,  0.58064516,  0.        ],
                          [ 0.67741935,  0.61290323, -0.        ],
                          [ 0.87096774,  0.64516129, -0.        ],
                          [ 0.06451613,  0.67741935,  0.        ],
                          [ 0.25806452,  0.70967742,  0.        ],
                          [ 0.4516129 ,  0.74193548,  0.        ],
                          [ 0.64516129,  0.77419355,  0.        ],
                          [ 0.83870968,  0.80645161,  0.        ],
                          [ 0.03225806,  0.83870968,  0.        ],
                          [ 0.22580645,  0.87096774,  0.        ],
                          [ 0.41935484,  0.90322581,  0.        ],
                          [ 0.61290323,  0.93548387, -0.        ],
                          [ 0.80645161,  0.96774194, -0.        ],
                          [-0.        , -0.        ,  0.2330018 ],
                          [ 0.19354839,  0.03225806,  0.2330018 ],
                          [ 0.38709677,  0.06451613,  0.2330018 ],
                          [ 0.58064516,  0.09677419,  0.2330018 ],
                          [ 0.77419355,  0.12903226,  0.2330018 ],
                          [ 0.96774194,  0.16129032,  0.2330018 ],
                          [ 0.16129032,  0.19354839,  0.2330018 ],
                          [ 0.35483871,  0.22580645,  0.2330018 ],
                          [ 0.5483871 ,  0.25806452,  0.2330018 ],
                          [ 0.74193548,  0.29032258,  0.2330018 ],
                          [ 0.93548387,  0.32258065,  0.2330018 ],
                          [ 0.12903226,  0.35483871,  0.2330018 ],
                          [ 0.32258065,  0.38709677,  0.2330018 ],
                          [ 0.51612903,  0.41935484,  0.2330018 ],
                          [ 0.70967742,  0.4516129 ,  0.2330018 ],
                          [ 0.90322581,  0.48387097,  0.2330018 ],
                          [ 0.09677419,  0.51612903,  0.2330018 ],
                          [ 0.29032258,  0.5483871 ,  0.2330018 ],
                          [ 0.48387097,  0.58064516,  0.2330018 ],
                          [ 0.67741935,  0.61290323,  0.2330018 ],
                          [ 0.87096774,  0.64516129,  0.2330018 ],
                          [ 0.06451613,  0.67741935,  0.2330018 ],
                          [ 0.25806452,  0.70967742,  0.2330018 ],
                          [ 0.4516129 ,  0.74193548,  0.2330018 ],
                          [ 0.64516129,  0.77419355,  0.2330018 ],
                          [ 0.83870968,  0.80645161,  0.2330018 ],
                          [ 0.03225806,  0.83870968,  0.2330018 ],
                          [ 0.22580645,  0.87096774,  0.2330018 ],
                          [ 0.41935484,  0.90322581,  0.2330018 ],
                          [ 0.61290323,  0.93548387,  0.2330018 ],
                          [ 0.80645161,  0.96774194,  0.2330018 ],
                          [ 0.46236559,  0.02150538,  0.31066907],
                          [ 0.65591398,  0.05376344,  0.31066907],
                          [ 0.84946237,  0.08602151,  0.31066907],
                          [ 0.04301075,  0.11827957,  0.31066907],
                          [ 0.23655914,  0.15053763,  0.31066907],
                          [ 0.43010753,  0.1827957 ,  0.31066907],
                          [ 0.62365591,  0.21505376,  0.31066907],
                          [ 0.8172043 ,  0.24731183,  0.31066907],
                          [ 0.01075269,  0.27956989,  0.31066907],
                          [ 0.20430108,  0.31182796,  0.31066907],
                          [ 0.39784946,  0.34408602,  0.31066907],
                          [ 0.59139785,  0.37634409,  0.31066907],
                          [ 0.78494624,  0.40860215,  0.31066907],
                          [ 0.97849462,  0.44086022,  0.31066907],
                          [ 0.17204301,  0.47311828,  0.31066907],
                          [ 0.3655914 ,  0.50537634,  0.31066907],
                          [ 0.55913978,  0.53763441,  0.31066907],
                          [ 0.75268817,  0.56989247,  0.31066907],
                          [ 0.94623656,  0.60215054,  0.31066907],
                          [ 0.13978495,  0.6344086 ,  0.31066907],
                          [ 0.33333333,  0.66666667,  0.31066907],
                          [ 0.52688172,  0.69892473,  0.31066907],
                          [ 0.72043011,  0.7311828 ,  0.31066907],
                          [ 0.91397849,  0.76344086,  0.31066907],
                          [ 0.10752688,  0.79569892,  0.31066907],
                          [ 0.30107527,  0.82795699,  0.31066907],
                          [ 0.49462366,  0.86021505,  0.31066907],
                          [ 0.68817204,  0.89247312,  0.31066907],
                          [ 0.88172043,  0.92473118,  0.31066907],
                          [ 0.07526882,  0.95698925,  0.31066907],
                          [ 0.2688172 ,  0.98924731,  0.31066907],
                          [ 0.3126    ,  0.0311    ,  0.46440234],
                          [ 0.94417895,  0.08373158,  0.46440234],
                          [ 0.57575789,  0.13636316,  0.46440234],
                          [ 0.20733684,  0.18899474,  0.46440234],
                          [ 0.83891579,  0.24162632,  0.46440234],
                          [ 0.47049474,  0.29425789,  0.46440234],
                          [ 0.10207368,  0.34688947,  0.46440234],
                          [ 0.73365263,  0.39952105,  0.46440234],
                          [ 0.36523158,  0.45215263,  0.46440234],
                          [ 0.99681053,  0.50478421,  0.46440234],
                          [ 0.62838947,  0.55741579,  0.46440234],
                          [ 0.25996842,  0.61004737,  0.46440234],
                          [ 0.89154737,  0.66267895,  0.46440234],
                          [ 0.52312632,  0.71531053,  0.46440234],
                          [ 0.15470526,  0.76794211,  0.46440234],
                          [ 0.78628421,  0.82057368,  0.46440234],
                          [ 0.41786316,  0.87320526,  0.46440234],
                          [ 0.04944211,  0.92583684,  0.46440234],
                          [ 0.68102105,  0.97846842,  0.46440234],
                          [ 0.08566842,  0.00494737,  0.52819202],
                          [ 0.71724737,  0.05757895,  0.52819202],
                          [ 0.34882632,  0.11021053,  0.52819202],
                          [ 0.98040526,  0.16284211,  0.52819202],
                          [ 0.61198421,  0.21547368,  0.52819202],
                          [ 0.24356316,  0.26810526,  0.52819202],
                          [ 0.87514211,  0.32073684,  0.52819202],
                          [ 0.50672105,  0.37336842,  0.52819202],
                          [ 0.1383    ,  0.426     ,  0.52819202],
                          [ 0.76987895,  0.47863158,  0.52819202],
                          [ 0.40145789,  0.53126316,  0.52819202],
                          [ 0.03303684,  0.58389474,  0.52819202],
                          [ 0.66461579,  0.63652632,  0.52819202],
                          [ 0.29619474,  0.68915789,  0.52819202],
                          [ 0.92777368,  0.74178947,  0.52819202],
                          [ 0.55935263,  0.79442105,  0.52819202],
                          [ 0.19093158,  0.84705263,  0.52819202],
                          [ 0.82251053,  0.89968421,  0.52819202],
                          [ 0.45408947,  0.95231579,  0.52819202],
                          [ 0.93332632,  0.02671053,  0.57914504],
                          [ 0.56490526,  0.07934211,  0.57914504],
                          [ 0.19648421,  0.13197368,  0.57914504],
                          [ 0.82806316,  0.18460526,  0.57914504],
                          [ 0.45964211,  0.23723684,  0.57914504],
                          [ 0.09122105,  0.28986842,  0.57914504],
                          [ 0.7228    ,  0.3425    ,  0.57914504],
                          [ 0.35437895,  0.39513158,  0.57914504],
                          [ 0.98595789,  0.44776316,  0.57914504],
                          [ 0.61753684,  0.50039474,  0.57914504],
                          [ 0.24911579,  0.55302632,  0.57914504],
                          [ 0.88069474,  0.60565789,  0.57914504],
                          [ 0.51227368,  0.65828947,  0.57914504],
                          [ 0.14385263,  0.71092105,  0.57914504],
                          [ 0.77543158,  0.76355263,  0.57914504],
                          [ 0.40701053,  0.81618421,  0.57914504],
                          [ 0.03858947,  0.86881579,  0.57914504],
                          [ 0.67016842,  0.92144737,  0.57914504],
                          [ 0.30174737,  0.97407895,  0.57914504],
                          [ 0.50797368,  0.00318947,  0.64293489],
                          [ 0.13955263,  0.05582105,  0.64293489],
                          [ 0.77113158,  0.10845263,  0.64293489],
                          [ 0.40271053,  0.16108421,  0.64293489],
                          [ 0.03428947,  0.21371579,  0.64293489],
                          [ 0.66586842,  0.26634737,  0.64293489],
                          [ 0.29744737,  0.31897895,  0.64293489],
                          [ 0.92902632,  0.37161053,  0.64293489],
                          [ 0.56060526,  0.42424211,  0.64293489],
                          [ 0.19218421,  0.47687368,  0.64293489],
                          [ 0.82376316,  0.52950526,  0.64293489],
                          [ 0.45534211,  0.58213684,  0.64293489],
                          [ 0.08692105,  0.63476842,  0.64293489],
                          [ 0.7185    ,  0.6874    ,  0.64293489],
                          [ 0.35007895,  0.74003158,  0.64293489],
                          [ 0.98165789,  0.79266316,  0.64293489],
                          [ 0.61323684,  0.84529474,  0.64293489],
                          [ 0.24481579,  0.89792632,  0.64293489],
                          [ 0.87639474,  0.95055789,  0.64293489],
                          [ 0.18243684,  0.01959474,  0.7067244 ],
                          [ 0.81401579,  0.07222632,  0.7067244 ],
                          [ 0.44559474,  0.12485789,  0.7067244 ],
                          [ 0.07717368,  0.17748947,  0.7067244 ],
                          [ 0.70875263,  0.23012105,  0.7067244 ],
                          [ 0.34033158,  0.28275263,  0.7067244 ],
                          [ 0.97191053,  0.33538421,  0.7067244 ],
                          [ 0.60348947,  0.38801579,  0.7067244 ],
                          [ 0.23506842,  0.44064737,  0.7067244 ],
                          [ 0.86664737,  0.49327895,  0.7067244 ],
                          [ 0.49822632,  0.54591053,  0.7067244 ],
                          [ 0.12980526,  0.59854211,  0.7067244 ],
                          [ 0.76138421,  0.65117368,  0.7067244 ],
                          [ 0.39296316,  0.70380526,  0.7067244 ],
                          [ 0.02454211,  0.75643684,  0.7067244 ],
                          [ 0.65612105,  0.80906842,  0.7067244 ],
                          [ 0.2877    ,  0.8617    ,  0.7067244 ],
                          [ 0.91927895,  0.91433158,  0.7067244 ],
                          [ 0.55085789,  0.96696316,  0.7067244 ],
                          [ 0.46180526,  0.01404211,  0.75767795],
                          [ 0.09338421,  0.06667368,  0.75767795],
                          [ 0.72496316,  0.11930526,  0.75767795],
                          [ 0.35654211,  0.17193684,  0.75767795],
                          [ 0.98812105,  0.22456842,  0.75767795],
                          [ 0.6197    ,  0.2772    ,  0.75767795],
                          [ 0.25127895,  0.32983158,  0.75767795],
                          [ 0.88285789,  0.38246316,  0.75767795],
                          [ 0.51443684,  0.43509474,  0.75767795],
                          [ 0.14601579,  0.48772632,  0.75767795],
                          [ 0.77759474,  0.54035789,  0.75767795],
                          [ 0.40917368,  0.59298947,  0.75767795],
                          [ 0.04075263,  0.64562105,  0.75767795],
                          [ 0.67233158,  0.69825263,  0.75767795],
                          [ 0.30391053,  0.75088421,  0.75767795],
                          [ 0.93548947,  0.80351579,  0.75767795],
                          [ 0.56706842,  0.85614737,  0.75767795],
                          [ 0.19864737,  0.90877895,  0.75767795],
                          [ 0.83022632,  0.96141053,  0.75767795],
                          [ 0.81100526,  0.01834211,  0.82146745],
                          [ 0.44258421,  0.07097368,  0.82146745],
                          [ 0.07416316,  0.12360526,  0.82146745],
                          [ 0.70574211,  0.17623684,  0.82146745],
                          [ 0.33732105,  0.22886842,  0.82146745],
                          [ 0.9689    ,  0.2815    ,  0.82146745],
                          [ 0.60047895,  0.33413158,  0.82146745],
                          [ 0.23205789,  0.38676316,  0.82146745],
                          [ 0.86363684,  0.43939474,  0.82146745],
                          [ 0.49521579,  0.49202632,  0.82146745],
                          [ 0.12679474,  0.54465789,  0.82146745],
                          [ 0.75837368,  0.59728947,  0.82146745],
                          [ 0.38995263,  0.64992105,  0.82146745],
                          [ 0.02153158,  0.70255263,  0.82146745],
                          [ 0.65311053,  0.75518421,  0.82146745],
                          [ 0.28468947,  0.80781579,  0.82146745],
                          [ 0.91626842,  0.86044737,  0.82146745],
                          [ 0.54784737,  0.91307895,  0.82146745],
                          [ 0.17942632,  0.96571053,  0.82146745],
                          [ 0.36347368,  0.02808947,  0.88525731],
                          [ 0.99505263,  0.08072105,  0.88525731],
                          [ 0.62663158,  0.13335263,  0.88525731],
                          [ 0.25821053,  0.18598421,  0.88525731],
                          [ 0.88978947,  0.23861579,  0.88525731],
                          [ 0.52136842,  0.29124737,  0.88525731],
                          [ 0.15294737,  0.34387895,  0.88525731],
                          [ 0.78452632,  0.39651053,  0.88525731],
                          [ 0.41610526,  0.44914211,  0.88525731],
                          [ 0.04768421,  0.50177368,  0.88525731],
                          [ 0.67926316,  0.55440526,  0.88525731],
                          [ 0.31084211,  0.60703684,  0.88525731],
                          [ 0.94242105,  0.65966842,  0.88525731],
                          [ 0.574     ,  0.7123    ,  0.88525731],
                          [ 0.20557895,  0.76493158,  0.88525731],
                          [ 0.83715789,  0.81756316,  0.88525731],
                          [ 0.46873684,  0.87019474,  0.88525731],
                          [ 0.10031579,  0.92282632,  0.88525731],
                          [ 0.73189474,  0.97545789,  0.88525731],
                          [ 0.23644737,  0.01187895,  0.93621032],
                          [ 0.86802632,  0.06451053,  0.93621032],
                          [ 0.49960526,  0.11714211,  0.93621032],
                          [ 0.13118421,  0.16977368,  0.93621032],
                          [ 0.76276316,  0.22240526,  0.93621032],
                          [ 0.39434211,  0.27503684,  0.93621032],
                          [ 0.02592105,  0.32766842,  0.93621032],
                          [ 0.6575    ,  0.3803    ,  0.93621032],
                          [ 0.28907895,  0.43293158,  0.93621032],
                          [ 0.92065789,  0.48556316,  0.93621032],
                          [ 0.55223684,  0.53819474,  0.93621032],
                          [ 0.18381579,  0.59082632,  0.93621032],
                          [ 0.81539474,  0.64345789,  0.93621032],
                          [ 0.44697368,  0.69608947,  0.93621032],
                          [ 0.07855263,  0.74872105,  0.93621032],
                          [ 0.71013158,  0.80135263,  0.93621032],
                          [ 0.34171053,  0.85398421,  0.93621032],
                          [ 0.97328947,  0.90661579,  0.93621032],
                          [ 0.60486842,  0.95924737,  0.93621032]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

