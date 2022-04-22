# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz dolno-trójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .full_matrix import full_matrix

"""
    Wejście:
        - order (int) - stopień macierzy

    Wyjście:
        - matrix (np.ndarray) - macierz dolno-trójkątna
"""

# Metoda generuje macierz dolno-trókątną na podstawie macierzy wygenerowanej w sposób losowy (wartości z zakresu [0, 1])
def lower_triangular_matrix(order: int) -> np.ndarray:

    # Wygenerowanie pełnej macierzy kwadratowej o stopniu 'order'
    matrix = full_matrix(order)

    # Utworzenie macierzy dolno-trójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.tril(matrix)

    # Zwrócenie macierzy dolno-trójkątnej
    return matrix
