# Set up lattice
vector_a = [30.0, 0.0, 0.0]*Angstrom
vector_b = [0.0, 30.0, 0.0]*Angstrom
vector_c = [0.0, 0.0, 2.88903]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silver, Silver, Silver, Silver, Silver, Silver, Silver, Silver,
            Silver, Silver, Silver, Silver, Silver, Silver]

# Define coordinates
fractional_coordinates = [[ 0.40369913,  0.3978575 ,  0.74999967],
                          [ 0.40369913,  0.5340475 ,  0.74999967],
                          [ 0.5       ,  0.3978575 ,  0.74999967],
                          [ 0.5       ,  0.5340475 ,  0.74999967],
                          [ 0.59630087,  0.3978575 ,  0.74999967],
                          [ 0.59630087,  0.5340475 ,  0.74999967],
                          [ 0.35554869,  0.4659525 ,  0.25000033],
                          [ 0.35554869,  0.6021425 ,  0.25000033],
                          [ 0.45184956,  0.4659525 ,  0.25000033],
                          [ 0.45184956,  0.6021425 ,  0.25000033],
                          [ 0.54815044,  0.4659525 ,  0.25000033],
                          [ 0.54815044,  0.6021425 ,  0.25000033],
                          [ 0.64445131,  0.4659525 ,  0.25000033],
                          [ 0.64445131,  0.6021425 ,  0.25000033]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

