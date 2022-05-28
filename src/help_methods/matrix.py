# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę mapującą typ macierzy na odpowiednią metodę

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

from ..generate_methods.band_matrix import band_matrix
from ..generate_methods.diagonal_matrix import diagonal_matrix
from ..generate_methods.external_matrix import external_matrix
from ..generate_methods.full_matrix import full_matrix
from ..generate_methods.lower_triangular_matrix import lower_triangular_matrix
from ..generate_methods.sparse_matrix import sparse_matrix
from ..generate_methods.upper_triangular_matrix import upper_triangular_matrix

from .types import *
from .dir import get_data_dir

"""
    Wejście:
        - type (str) - typ macierzy
        - order (int) - stopień macierzy
        - load (bool) - czy macierz ma zostać wczytana
        - density (float) - poziom wypełnienia macierzy rzadkiej

    Wyjście:
        - matrix (np.ndarray) - macierz
"""

# Metoda mapuje nazwy macierzy i  zwraca macierz o wybranym typie
def get_matrix(type: str, order: int, load: bool = False, density: float = 0.05) -> np.ndarray:
    matrix = None

    if load:
        matrix = np.loadtxt(f"{get_data_dir()}/A_{type}_{order}.txt", dtype=float)
        return matrix

    if type == band:
        matrix = band_matrix(order)
    elif type == diagonal:
        matrix = diagonal_matrix(order)
    elif type == external:
        matrix = external_matrix()
    elif type == full:
        matrix = full_matrix(order)
    elif type == lower_triangular:
        matrix = lower_triangular_matrix(order)
    elif type == sparse:
        matrix = sparse_matrix(order, density)
    elif type == upper_triangular:
        matrix = upper_triangular_matrix(order)

    return matrix
