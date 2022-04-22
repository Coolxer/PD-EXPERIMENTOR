# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą macierz górno-trójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .full_matrix import full_matrix

"""
    Wejście:
        - order (int) - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - matrix (np.ndarray) - macierz górno-trójkątna
"""

# Metoda generuje macierz górno-trójkątną na podstawie macierzy wygenerowanej w sposób losowy (wartości z zakresu [0, 1])
def upper_triangular_matrix(order: int) -> np.ndarray:

    # Wygenerowanie losowej macierzy kwadratowej o stopniu 'order'
    matrix = full_matrix(order)

    # Utworzenie macierzy górno-trójkątnej na podstawie wcześniej wygenerowanej macierzy
    matrix = np.triu(matrix)

    # Zwrócenie macierzy górno-trójkątnej
    return matrix
