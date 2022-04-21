# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz dolno-trójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .full_matrix import full_matrix

"""
    Wejście:
        - size (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz dolno-trójkątna
"""

# Metoda generuje macierz dolno-trókątną na podstawie macierzy wygenerowanej w sposób losowy (wartości z zakresu [0, 1])
def lower_triangular_matrix(size: int) -> np.ndarray:

    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    matrix = full_matrix(size)

    # Utworzenie macierzy dolno-trójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.tril(matrix)

    # Zwrócenie macierzy dolno-trójkątnej
    return matrix
