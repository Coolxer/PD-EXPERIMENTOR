# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę mapującą typ macierzy na odpowiednią metodę

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

from ..generate_methods.sparse_matrix import sparse_matrix
from ..generate_methods.random_matrix import random_matrix
from ..generate_methods.diagonal_matrix import diagonal_matrix
from ..generate_methods.band_matrix import band_matrix
from ..generate_methods.lower_triangular_matrix import lower_triangular_matrix
from ..generate_methods.upper_triangular_matrix import upper_triangular_matrix
from ..generate_methods.external_matrix import external_matrix

from .types import *


"""
    Wejście:
        - type (str) - typ macierzy
        - size (int) - rozmiar macierzy

    Wyjście:
        - matrix (np.ndarray) - macierz
"""

# Metoda mapuje nazwy macierzy i  zwraca macierz o wybranym typie
def get_matrix(type: str, size: int) -> np.ndarray:
    matrix = None

    if type == band:
        matrix = band_matrix(size)
    elif type == diagonal:
        matrix = diagonal_matrix(size)
    elif type == external:
        matrix = external_matrix()
    elif type == lower_triangular:
        matrix = lower_triangular_matrix(size)
    elif type == random:
        matrix = random_matrix(size)
    elif type == sparse:
        matrix = sparse_matrix(size, 0.25)
    elif type == upper_triangular:
        matrix = upper_triangular_matrix(size)

    return matrix
