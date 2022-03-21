# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz diagonalną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from random import random

# Metoda generuje macierz diagonalną o podanym rozmiarze

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.array) - macierz diagonalna
"""


def diagonal_matrix(size: int) -> np.array:
    # Wygenerowanie macierzy o rozmiarze 'n x n' składającej się z samych 0
    matrix = np.zeros((size, size))

    # Pętla iterująca po wierszach macierzy
    for i in range(np.shape(matrix)[0]):
        # Wylosowanie wartości elementów macierzy leżących na głównej przekątnej
        matrix[i][i] = random()

    # Zwrócenie macierzy diagonalnej
    return matrix
