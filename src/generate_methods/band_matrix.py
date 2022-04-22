# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz wstęgową

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

"""
    Wejście:
        - order (int) - stopień macierzy

    Wyjście:
        - matrix (np.ndarray) - macierz wstęgowa
"""

# Metoda generuje macierz wstęgową o podanym stopniu i stałej szerokości pasma 3,
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony.
def band_matrix(order: int) -> np.ndarray:

    # Utworzenie kwadratowej macierzy wypełnionej zerami o stopniu 'order'
    matrix = np.zeros((order, order))

    # Utworzenie wstęgi wokół głównej przekątnej
    matrix += np.diag(np.random.rand(order - 1), 1)
    matrix += np.diag(np.random.rand(order - 1), -1)

    # Wzmocnienie przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy wstęgowej
    return matrix
