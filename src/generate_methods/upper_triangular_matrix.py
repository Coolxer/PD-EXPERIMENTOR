# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz górnotrójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .random_matrix import random_matrix

# Metoda generuje macierz górnotrójkątną na podstawie macierzy wygenerowanej w sposób losowy

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.array) - macierz górnotrójkątna
"""


def upper_triangular_matrix(size: int) -> np.array:
    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = random_matrix(size)

    # Utworzenie macierzy górnotrójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.triu(matrix)

    # Zwrócenie macierzy górnotrójkątnej
    return matrix
