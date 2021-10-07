# matrices
from ..generate_functions.sparse_matrix import sparse_matrix
from ..generate_functions.random_matrix import random_matrix
from ..generate_functions.diagonal_matrix import diagonal_matrix
from ..generate_functions.band_matrix import band_matrix
from ..generate_functions.lower_triangular_matrix import lower_triangular_matrix
from ..generate_functions.upper_triangular_matrix import upper_triangular_matrix
from ..generate_functions.external_matrix import external_matrix

from ..generate_functions.random_vector import random_vector

from .matrix_type import types

# metoda zwraca macierz o wybranym typie
"""
matrix type oznacza typ macierzy
n oznacza rozmiar macierzy
"""


def get_matrix(matrix_type, n):
    A = None

    if matrix_type == "sparse":
        A = sparse_matrix(n, 0.25)
    elif matrix_type == "random":
        A = random_matrix(n)
    elif matrix_type == "diagonal":
        A = diagonal_matrix(n)
    elif matrix_type == "band":
        A = band_matrix(n)
    elif matrix_type == "lower_triangular":
        A = lower_triangular_matrix(n)
    elif matrix_type == "upper_triangular":
        A = upper_triangular_matrix(n)
    elif matrix_type == "external":
        A = external_matrix(file)

    return A
