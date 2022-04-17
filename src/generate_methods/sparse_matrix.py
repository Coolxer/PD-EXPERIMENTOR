# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz rzadką

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from scipy.sparse import random
from .diagonal_amplifier import strengthen_diagonal

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)
        - dens (float) - gęstość macierzy, przy czym 1 to macierz pełna, a 0 to macierz w pełni rzadka (zerowa)

    Wyjście:
        - matrix (np.ndarray) - macierz rzadka
"""

# Metoda generuje macierz rzadką, korzystając z biblioteki scipy
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony
def sparse_matrix(size: int, dens: float) -> np.ndarray:

    # Wygenerowanie rzadkiej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = random(size, size, density=dens, format="csr").toarray()

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix, 0.1)

    # Zwrócenie macierzy rzadkiej
    return matrix
