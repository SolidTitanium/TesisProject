import numpy as np #My beloved

#Esta implícito que las entradas en indices impares son negativas
def frontera(simplex):
    return tuple(tuple(vertex for vertex in simplex if vertex != pivot) for pivot in simplex)

#Representación conjuntista del complejo simplicial abstracto (csa)
csa = frozenset(((), (1,), (2,), (3,), (4,), (5,), (6,), 
                 (1, 2), (1, 3), (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (2, 3), (3, 5), (4, 5), (2, 4),
                 (1, 3, 5), (2, 3, 6), (1, 4, 5), (1, 2, 4), (2, 4, 6), (4, 5, 6)))

# csa = frozenset(((), (1,), (2,), (3,), (4,), (5,), (6,), 
#                  (1, 2), (1, 3), (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (2, 3), (3, 5), (4, 5), (2, 4),
#                  (1, 3, 5), (2, 3, 6), (1, 4, 5), (1, 2, 4), (2, 4, 6), (4, 5, 6), (1, 2, 3), (3, 5, 6)))

# csa = frozenset(((), (1,), (2,), (3,), (4,),
#                  (1, 2), (2, 3), (3, 4), (1, 4)))

# csa = frozenset(((), (1,), (2,), (3,), (4,), (5,), (6,), 
#                  (1, 2), (1, 3), (1, 5), (1, 4), (2, 6), (3, 6), (4, 6), (5, 6), (2, 3), (3, 5), (4, 5), (2, 4), (1, 6),
#                  (1, 3, 5), (2, 3, 6), (1, 4, 5), (1, 2, 4), (2, 4, 6), (4, 5, 6), (1, 2, 6), (1, 5, 6)))

#Dimensión del simplejo más grande con el que se trabaja
max_dim = max(tuple(len(simplex) for simplex in csa))

#Número de simplejos por dimensión
simplex_per_dim = tuple(tuple(len(simplex) for simplex in csa).count(dim) for dim in range(max_dim + 1))

#Preparación de las ecuaciónes que forman las matrices frontera
#Es una lista con un diccionario por cada dimensión del csa a excepción de la más grande y la más pequeña (el vacio y máx dim)
#Las llaves son los n-simplejos de dicha dimensión, cada uno tiene una lista con m ceros donde m es el número de simplejos de dimensión directamente inferior
#Cada lista sera poblada con 1, 0 o -1 en cada entrada según lo diga la función frontera (mirar notas)
eqs = [{simplex:[0 for _ in range(simplex_per_dim[important_dim + 1])] for simplex in csa if len(simplex) == important_dim} for important_dim in range(1, max_dim)]

#Loops mal hechos para aplicar la función frontera a los simplejos que corresponda y modificar eqs como se debe
for important_dim in range(2, max_dim + 1):
    count = 0
    for big_simplex in csa:
        if len(big_simplex) == important_dim:
            for i, small_simplex in enumerate(frontera(big_simplex)):
                if i%2 == 0:
                    eqs[important_dim - 2][small_simplex][count] = 1
                else:
                    eqs[important_dim - 2][small_simplex][count] = -1
            count = count + 1
    count = 0

#Lista de arreglos de numpy que representan las matrices frontera
d_matrix = [np.array(list(eq.values())) for eq in eqs]

#Calcular rangos y dimensiones de kernels de las matrices frontera
ranks = [np.linalg.matrix_rank(matrix) for matrix in d_matrix]
nulls = [simplex_per_dim[important_dim] - ranks[important_dim - 2] for important_dim in range(2, max_dim + 1)]

#Calcular los números de Betti y añadir los triviales
Betti = [nulls[dim - 1] - ranks[dim] for dim in range(1, len(ranks))]
Betti.insert(0, simplex_per_dim[1]-ranks[0])
Betti.append(nulls[-1])

#Imprimir
print(Betti)