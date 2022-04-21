# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz pełną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .diagonal_amplifier import strengthen_diagonal


"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz losowa
"""

# Metoda generuje macierz pełną o podanym rozmiarze i o losowych wartościach z zakresu [0, 1]
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony
def full_matrix(size: int) -> np.ndarray:

    # Wygenerowanie pełnej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = np.random.rand(size, size)

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy pełnej
    return matrix
