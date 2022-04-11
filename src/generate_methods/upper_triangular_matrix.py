# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz górnotrójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .random_matrix import random_matrix

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz górno-trójkątna
"""

# Metoda generuje macierz górno-trójkątną na podstawie macierzy wygenerowanej w sposób losowy


def upper_triangular_matrix(size: int) -> np.ndarray:

    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = random_matrix(size)

    # Utworzenie macierzy górno-trójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.triu(matrix)

    # Zwrócenie macierzy górno-trójkątnej
    return matrix
