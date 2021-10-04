# matrices
from src.generator.sparse_matrix import sparse_matrix
from src.generator.random_matrix import random_matrix
from src.generator.diagonal_matrix import diagonal_matrix
from src.generator.band_matrix import band_matrix
from src.generator.lower_triangular_matrix import lower_triangular_matrix
from src.generator.upper_triangular_matrix import upper_triangular_matrix
from src.generator.external_matrix import external_matrix

from src.generator.random_vector import random_vector

from src.exp_help_functions.matrix_type import types


def get_matrix(matrix_type, size, name=None):
    A = None

    if matrix_type == 'sparse':
        A = sparse_matrix(size, 0.25)
    elif matrix_type == 'random':
        A = random_matrix(size)
    elif matrix_type == 'diagonal':
        A = diagonal_matrix(size)
    elif matrix_type == 'band':
        A = band_matrix(size)
    elif matrix_type == 'lower_triangular':
        A = lower_triangular_matrix(size)
    elif matrix_type == 'upper_triangular':
        A = upper_triangular_matrix(size)
    elif matrix_type == 'external' and name is not None:
        A = external_matrix(name)

    return A
