# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz wstęgową

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

# Metoda generuje macierz wstęgową o podanym rozmiarze i stałej szerokości pasma 3,
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony.

"""
    Wejście:
         - n - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - m - macierz wstęgowa
"""


def band_matrix(n):

    # Utworzenie macierzy wypełnionej zerami o rozmiarze 'n x n'
    m = np.zeros((n, n))

    # Utworzenie wstęgi wokół głównej przekątnej
    m += np.diag(np.random.rand(n - 1), 1)
    m += np.diag(np.random.rand(n - 1), -1)

    # Wzmocnienie przekątnej macierzy
    m = strengthen_diagonal(m, 0.1)

    # Zwrócenie macierzy wstęgowej
    return m
