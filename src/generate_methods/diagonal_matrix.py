# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz diagonalną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from random import random

"""
    Wejście:
        - order (int) - stopień macierzy

    Wyjście:
        - matrix (np.ndarray) - macierz diagonalna
"""

# Metoda generuje macierz diagonalną o podanym stopniu
def diagonal_matrix(order: int) -> np.ndarray:

    # Wygenerowanie kwadratowej macierzy stopnia 'order' składającej się z samych 0
    matrix = np.zeros((order, order))

    # Pętla iterująca po wierszach macierzy
    for i in range(np.shape(matrix)[0]):
        # Wylosowanie wartości z zakresu [0, 1] elementów macierzy leżących na głównej przekątnej
        matrix[i][i] = random()

    # Zwrócenie macierzy diagonalnej
    return matrix
