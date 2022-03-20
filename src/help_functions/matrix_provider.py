# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę ułatwiającą wybór macierzy do eksperymentu

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
from ..generate_functions.sparse_matrix import sparse_matrix
from ..generate_functions.random_matrix import random_matrix
from ..generate_functions.diagonal_matrix import diagonal_matrix
from ..generate_functions.band_matrix import band_matrix
from ..generate_functions.lower_triangular_matrix import lower_triangular_matrix
from ..generate_functions.upper_triangular_matrix import upper_triangular_matrix
from ..generate_functions.external_matrix import external_matrix

from ..generate_functions.random_vector import random_vector

from .matrix_type import types

# Metoda mapuje nazwy macierzy i  zwraca macierz o wybranym typie

"""
    Wejście:
        - type - typ macierzy
        - n - rozmiar macierzy

    Wyjście:
        - m - macierz
"""


def get_matrix(type, n):
    m = None

    if type == "sparse":
        m = sparse_matrix(n, 0.25)
    elif type == "random":
        m = random_matrix(n)
    elif type == "diagonal":
        m = diagonal_matrix(n)
    elif type == "band":
        m = band_matrix(n)
    elif type == "lower_triangular":
        m = lower_triangular_matrix(n)
    elif type == "upper_triangular":
        m = upper_triangular_matrix(n)
    elif type == "external":
        m = external_matrix()

    return m
