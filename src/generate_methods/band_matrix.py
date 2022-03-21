# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz wstęgową

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

# Metoda generuje macierz wstęgową o podanym rozmiarze i stałej szerokości pasma 3,
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony.

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.array) - macierz wstęgowa
"""


def band_matrix(size: int) -> np.array:
    # Utworzenie macierzy wypełnionej zerami o rozmiarze 'n x n'
    matrix = np.zeros((size, size))

    # Utworzenie wstęgi wokół głównej przekątnej
    matrix += np.diag(np.random.rand(size - 1), 1)
    matrix += np.diag(np.random.rand(size - 1), -1)

    # Wzmocnienie przekątnej macierzy
    matrix = strengthen_diagonal(matrix, 0.1)

    # Zwrócenie macierzy wstęgowej
    return matrix
