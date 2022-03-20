# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz górnotrójkątną

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np
from .random_matrix import random_matrix

# Metoda generuje macierz górnotrójkątną na podstawie macierzy wygenerowanej w sposób losowy

"""
    Wejście:
        - n - rozmiar macierzy (liczba wierszy / kolumn)

    Wyjście:
        - m - macierz górnotrójkątna
"""


def upper_triangular_matrix(n):
    # Wygenerowanie losowej macierzy kwadratowej o rozmiarze 'n x n'
    m = random_matrix(n)

    # Utworzenie macierzy górnotrójkątnej na podstawie wcześniej wygenerowanej macierzy
    m = np.triu(m)

    # Zwrócenie macierzy górnotrójkątnej
    return m
