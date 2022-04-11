# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz dolnotrójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .random_matrix import random_matrix

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz dolno-trójkątna
"""

# Metoda generuje macierz dolnotrókątną na podstawie macierzy wygenerowanej w sposób losowy
def lower_triangular_matrix(size: int) -> np.ndarray:

    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = random_matrix(size)

    # Utworzenie macierzy dolno-trójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.tril(matrix)

    # Zwrócenie macierzy dolno-trójkątnej
    return matrix
