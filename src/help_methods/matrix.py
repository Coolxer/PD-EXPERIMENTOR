# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający
#   - klasę i obiekt typu macierzy wejściowej
#   - metodę mapującą typ macierzy na odpowiednią metodę

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
from ..generate_methods.random_vector import random_vector

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Klasa określająca typ macierzy wejściowej
class Matrix_Type:
    def sparse(self):
        return "sparse"

    def random(self):
        return "random"

    def diagonal(self):
        return "diagonal"

    def band(self):
        return "band"

    def lower_triangular(self):
        return "lower_triangular"

    def upper_triangular(self):
        return "upper_triangular"

    def external(self):
        return "external"


# Obiekt typu macierzy wejściowej
matrix_type = Matrix_Type()


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda mapuje nazwy macierzy i  zwraca macierz o wybranym typie

"""
    Wejście:
        - type (str) - typ macierzy
        - size (int) - rozmiar macierzy

    Wyjście:
        - matrix (np.array) - macierz
"""


def get_matrix(type: str, size: int) -> np.array:
    matrix = None

    if type == "sparse":
        matrix = sparse_matrix(size, 0.25)
    elif type == "random":
        matrix = random_matrix(size)
    elif type == "diagonal":
        matrix = diagonal_matrix(size)
    elif type == "band":
        matrix = band_matrix(size)
    elif type == "lower_triangular":
        matrix = lower_triangular_matrix(size)
    elif type == "upper_triangular":
        matrix = upper_triangular_matrix(size)
    elif type == "external":
        matrix = external_matrix()

    return matrix