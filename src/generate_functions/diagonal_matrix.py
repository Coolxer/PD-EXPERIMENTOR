# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz diagonalną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np
from random import random

# Metoda generuje macierz diagonalną o podanym rozmiarze

"""
    Wejście:
        - n - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - m - macierz diagonalna
"""


def diagonal_matrix(n):
    # Wygenerowanie macierzy o rozmiarze 'n x n' składającej się z samych 0
    m = np.zeros((n, n))

    # Pętla iterująca po wierszach macierzy
    for i in range(np.shape(m)[0]):
        # Wylosowanie wartości elementów macierzy leżących na głównej przekątnej
        m[i][i] = random()

    # Zwrócenie macierzy diagonalnej
    return m
