# Set up lattice
vector_a = [19.026118926, 0.0, 0.0]*Angstrom
vector_b = [0.0, -25.1797218012, 0.0]*Angstrom
vector_c = [0.0, 0.0, 24.4150289254]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Hafnium, Hafnium, Hafnium,
            Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium,
            Hafnium, Hafnium, Hafnium, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Hafnium, Hafnium, Oxygen, Oxygen, Hafnium, Hafnium, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Oxygen, Oxygen, Oxygen, Oxygen, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Hafnium, Hafnium, Hafnium, Oxygen,
            Oxygen, Oxygen, Hafnium, Hafnium, Gold, Gold, Gold, Gold, Gold,
            Gold, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Hafnium, Oxygen, Oxygen, Hafnium,
            Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium,
            Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium, Hafnium,
            Hafnium, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen, Oxygen]

# Define coordinates
fractional_coordinates = [[ 0.25      ,  0.24120908,  0.22636312],
                          [ 0.45      ,  0.24120908,  0.22636312],
                          [ 0.65      ,  0.24120908,  0.22636312],
                          [ 0.35      ,  0.36620908,  0.22636312],
                          [ 0.55      ,  0.36620908,  0.22636312],
                          [ 0.25      ,  0.49120908,  0.22636312],
                          [ 0.45      ,  0.49120908,  0.22636312],
                          [ 0.65      ,  0.49120908,  0.22636312],
                          [ 0.35      ,  0.61620908,  0.22636312],
                          [ 0.55      ,  0.61620908,  0.22636312],
                          [ 0.25      ,  0.74120908,  0.22636312],
                          [ 0.45      ,  0.74120908,  0.22636312],
                          [ 0.65      ,  0.74120908,  0.22636312],
                          [ 0.35      ,  0.19954241,  0.28684117],
                          [ 0.55      ,  0.19954241,  0.28684117],
                          [ 0.25      ,  0.32454241,  0.28684117],
                          [ 0.45      ,  0.32454241,  0.28684117],
                          [ 0.65      ,  0.32454241,  0.28684117],
                          [ 0.35      ,  0.44954241,  0.28684117],
                          [ 0.55      ,  0.44954241,  0.28684117],
                          [ 0.25      ,  0.57454241,  0.28684117],
                          [ 0.45      ,  0.57454241,  0.28684117],
                          [ 0.65      ,  0.57454241,  0.28684117],
                          [ 0.35      ,  0.69954241,  0.28684117],
                          [ 0.55      ,  0.69954241,  0.28684117],
                          [ 0.25      ,  0.82454241,  0.28684117],
                          [ 0.45      ,  0.82454241,  0.28684117],
                          [ 0.65      ,  0.82454241,  0.28684117],
                          [ 0.25      ,  0.24120908,  0.3170802 ],
                          [ 0.45      ,  0.24120908,  0.3170802 ],
                          [ 0.65      ,  0.24120908,  0.3170802 ],
                          [ 0.35      ,  0.36620908,  0.3170802 ],
                          [ 0.55      ,  0.36620908,  0.3170802 ],
                          [ 0.25      ,  0.49120908,  0.3170802 ],
                          [ 0.45      ,  0.49120908,  0.3170802 ],
                          [ 0.65      ,  0.49120908,  0.3170802 ],
                          [ 0.35      ,  0.61620908,  0.3170802 ],
                          [ 0.55      ,  0.61620908,  0.3170802 ],
                          [ 0.25      ,  0.74120908,  0.3170802 ],
                          [ 0.45      ,  0.74120908,  0.3170802 ],
                          [ 0.65      ,  0.74120908,  0.3170802 ],
                          [ 0.24670901,  0.73160912,  0.34048569],
                          [ 0.44670901,  0.73160912,  0.34048569],
                          [ 0.64670901,  0.73160912,  0.34048569],
                          [ 0.29670901,  0.20623183,  0.34149234],
                          [ 0.49670901,  0.20623183,  0.34149234],
                          [ 0.34670901,  0.70228844,  0.38345738],
                          [ 0.54670901,  0.70228844,  0.38345738],
                          [ 0.34670901,  0.79025049,  0.38345738],
                          [ 0.54670901,  0.79025049,  0.38345738],
                          [ 0.39670901,  0.23555252,  0.38446403],
                          [ 0.59670901,  0.23555252,  0.38446403],
                          [ 0.37595503,  0.29562298,  0.38637231],
                          [ 0.5903051 ,  0.29562298,  0.38637231],
                          [ 0.37595503,  0.41015   ,  0.38637231],
                          [ 0.5903051 ,  0.41015   ,  0.38637231],
                          [ 0.37595503,  0.524677  ,  0.38637231],
                          [ 0.5903051 ,  0.524677  ,  0.38637231],
                          [ 0.37595503,  0.639204  ,  0.38637231],
                          [ 0.5903051 ,  0.639204  ,  0.38637231],
                          [ 0.26877999,  0.35288649,  0.44542933],
                          [ 0.48313006,  0.35288649,  0.44542933],
                          [ 0.26877999,  0.46741349,  0.44542933],
                          [ 0.48313006,  0.46741349,  0.44542933],
                          [ 0.26877999,  0.58194051,  0.44542933],
                          [ 0.48313006,  0.58194051,  0.44542933],
                          [ 0.34670901,  0.73160912,  0.46940076],
                          [ 0.54670901,  0.73160912,  0.46940076],
                          [ 0.39670901,  0.20623183,  0.47040742],
                          [ 0.59670901,  0.20623183,  0.47040742],
                          [ 0.37595503,  0.29562298,  0.50448637],
                          [ 0.5903051 ,  0.29562298,  0.50448637],
                          [ 0.37595503,  0.41015   ,  0.50448637],
                          [ 0.5903051 ,  0.41015   ,  0.50448637],
                          [ 0.37595503,  0.524677  ,  0.50448637],
                          [ 0.5903051 ,  0.524677  ,  0.50448637],
                          [ 0.37595503,  0.639204  ,  0.50448637],
                          [ 0.5903051 ,  0.639204  ,  0.50448637],
                          [ 0.24670901,  0.70228844,  0.51237245],
                          [ 0.44670901,  0.70228844,  0.51237245],
                          [ 0.64670901,  0.70228844,  0.51237245],
                          [ 0.24670901,  0.79025049,  0.51237245],
                          [ 0.44670901,  0.79025049,  0.51237245],
                          [ 0.64670901,  0.79025049,  0.51237245],
                          [ 0.49670901,  0.23555252,  0.51337911],
                          [ 0.29670901,  0.23555252,  0.51337911],
                          [ 0.26877999,  0.58194051,  0.5635434 ],
                          [ 0.48313006,  0.58194051,  0.5635434 ],
                          [ 0.26877999,  0.35288649,  0.5635434 ],
                          [ 0.48313006,  0.35288649,  0.5635434 ],
                          [ 0.26877999,  0.46741349,  0.5635434 ],
                          [ 0.48313006,  0.46741349,  0.5635434 ],
                          [ 0.24670901,  0.73160912,  0.59831583],
                          [ 0.44670901,  0.73160912,  0.59831583],
                          [ 0.64670901,  0.73160912,  0.59831583],
                          [ 0.29670901,  0.20623183,  0.59932249],
                          [ 0.49670901,  0.20623183,  0.59932249],
                          [ 0.37595503,  0.29562298,  0.62260043],
                          [ 0.5903051 ,  0.29562298,  0.62260043],
                          [ 0.37595503,  0.41015   ,  0.62260043],
                          [ 0.5903051 ,  0.41015   ,  0.62260043],
                          [ 0.37595503,  0.524677  ,  0.62260043],
                          [ 0.5903051 ,  0.524677  ,  0.62260043],
                          [ 0.37595503,  0.639204  ,  0.62260043],
                          [ 0.5903051 ,  0.639204  ,  0.62260043],
                          [ 0.34670901,  0.70228844,  0.64128752],
                          [ 0.34670901,  0.79025049,  0.64128752],
                          [ 0.54670901,  0.79025049,  0.64128752],
                          [ 0.54670901,  0.70228844,  0.64128752],
                          [ 0.59670901,  0.23555252,  0.64229418],
                          [ 0.39670901,  0.23555252,  0.64229418],
                          [ 0.25      ,  0.25879092,  0.6829198 ],
                          [ 0.45      ,  0.25879092,  0.6829198 ],
                          [ 0.65      ,  0.25879092,  0.6829198 ],
                          [ 0.35      ,  0.38379092,  0.6829198 ],
                          [ 0.55      ,  0.38379092,  0.6829198 ],
                          [ 0.25      ,  0.50879092,  0.6829198 ],
                          [ 0.45      ,  0.50879092,  0.6829198 ],
                          [ 0.65      ,  0.50879092,  0.6829198 ],
                          [ 0.35      ,  0.63379092,  0.6829198 ],
                          [ 0.55      ,  0.63379092,  0.6829198 ],
                          [ 0.25      ,  0.75879092,  0.6829198 ],
                          [ 0.45      ,  0.75879092,  0.6829198 ],
                          [ 0.65      ,  0.75879092,  0.6829198 ],
                          [ 0.35      ,  0.21712425,  0.71315883],
                          [ 0.55      ,  0.21712425,  0.71315883],
                          [ 0.25      ,  0.34212425,  0.71315883],
                          [ 0.45      ,  0.34212425,  0.71315883],
                          [ 0.65      ,  0.34212425,  0.71315883],
                          [ 0.35      ,  0.46712425,  0.71315883],
                          [ 0.55      ,  0.46712425,  0.71315883],
                          [ 0.25      ,  0.59212425,  0.71315883],
                          [ 0.45      ,  0.59212425,  0.71315883],
                          [ 0.65      ,  0.59212425,  0.71315883],
                          [ 0.35      ,  0.71712425,  0.71315883],
                          [ 0.55      ,  0.71712425,  0.71315883],
                          [ 0.25      ,  0.25879092,  0.77363688],
                          [ 0.45      ,  0.25879092,  0.77363688],
                          [ 0.65      ,  0.25879092,  0.77363688],
                          [ 0.35      ,  0.38379092,  0.77363688],
                          [ 0.55      ,  0.38379092,  0.77363688],
                          [ 0.25      ,  0.50879092,  0.77363688],
                          [ 0.45      ,  0.50879092,  0.77363688],
                          [ 0.65      ,  0.50879092,  0.77363688],
                          [ 0.35      ,  0.63379092,  0.77363688],
                          [ 0.55      ,  0.63379092,  0.77363688],
                          [ 0.25      ,  0.75879092,  0.77363688],
                          [ 0.45      ,  0.75879092,  0.77363688],
                          [ 0.65      ,  0.75879092,  0.77363688]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )
basis_set = [
    GGABasis.Gold_DoubleZetaPolarized,
    GGABasis.Hafnium_DoubleZetaPolarized,
    GGABasis.Oxygen_DoubleZetaPolarized,
    ]

