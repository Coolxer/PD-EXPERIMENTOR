# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz diagonalną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from random import random

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz diagonalna
"""

# Metoda generuje macierz diagonalną o podanym rozmiarze
def diagonal_matrix(size: int) -> np.ndarray:

    # Wygenerowanie macierzy o rozmiarze 'n x n' składającej się z samych 0
    matrix = np.zeros((size, size))

    # Pętla iterująca po wierszach macierzy
    for i in range(np.shape(matrix)[0]):
        # Wylosowanie wartości z zakresu [0, 1] elementów macierzy leżących na głównej przekątnej
        matrix[i][i] = random()

    # Zwrócenie macierzy diagonalnej
    return matrix
