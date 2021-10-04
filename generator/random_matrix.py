import numpy as np

from src.generator.diagonal_amplifier import strengthen_diagonal


def random_matrix(n):
    m = np.random.rand(n, n)

    m = strengthen_diagonal(m, 0.1)

    return m
