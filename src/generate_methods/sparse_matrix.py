# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz rzadką

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
import scipy.sparse
import random
from .diagonal_amplifier import strengthen_diagonal

"""
    Wejście:
        - order (int) - stopień macierzy

    Wyjście:
        - matrix (np.ndarray) - macierz rzadka
"""

# Metoda generuje macierz rzadką, korzystając z biblioteki scipy
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony
def sparse_matrix(order: int) -> np.ndarray:

    # Wygenerowanie rzadkiej macierzy kwadratowej o stopniu 'order' i wypełnieniu w przedziale [0, 0.2]
    matrix = scipy.sparse.random(order, order, density=random.uniform(0, 0.2), format="csr").toarray()

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy rzadkiej
    return matrix
