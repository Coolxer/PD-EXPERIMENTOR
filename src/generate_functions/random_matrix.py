# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz o losowych wartościach

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal

# Metoda generuje macierz o podanym rozmiarze i o losowych wartościach
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony

"""
    Wejście:
        - n - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - m - macierz losowa
"""


def random_matrix(n):
    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    m = np.random.rand(n, n)

    # Wzmocnienie głównej przekątnej macierzy
    m = strengthen_diagonal(m, 0.1)

    # Zwrócenie macierzy o losowych wartościach elementów
    return m
