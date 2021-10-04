import numpy as np

from src.generator.random_matrix import random_matrix


def upper_triangular_matrix(n):
    m = random_matrix(n)

    return np.triu(m)
