# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz wstęgową

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz wstęgowa
"""

# Metoda generuje macierz wstęgową o podanym rozmiarze i stałej szerokości pasma 3,
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony.
def band_matrix(size: int) -> np.ndarray:

    # Utworzenie macierzy wypełnionej zerami o rozmiarze 'n x n'
    matrix = np.zeros((size, size))

    # Utworzenie wstęgi wokół głównej przekątnej
    matrix += np.diag(np.random.rand(size - 1), 1)
    matrix += np.diag(np.random.rand(size - 1), -1)

    # Wzmocnienie przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy wstęgowej
    return matrix
