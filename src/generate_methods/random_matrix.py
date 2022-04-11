# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz o losowych wartościach

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

# Metoda generuje macierz o podanym rozmiarze i o losowych wartościach
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz losowa
"""


def random_matrix(size: int) -> np.ndarray:
    
    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = np.random.rand(size, size)

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix, 0.1)

    # Zwrócenie macierzy o losowych wartościach
    return matrix
