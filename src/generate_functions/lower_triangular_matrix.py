# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz dolnotrójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np
from .random_matrix import random_matrix

# Metoda generuje macierz dolnotrókątną na podstawie macierzy wygenerowanej w sposób losowy

"""
    Wejście:
        - n - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - m - macierz dolnotrójkątna
"""


def lower_triangular_matrix(n):
    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    m = random_matrix(n)

    # Utworzenie macierzy dolnotrójkątnej na podstawie wcześniej wygenerowanej macierzy
    m = np.tril(m)

    # Zwrócenie macierzy dolnotrójkątnej
    return m
