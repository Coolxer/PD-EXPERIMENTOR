import numpy as np

from src.generator.diagonal_amplifier import strengthen_diagonal


def band_matrix(n):

    m = np.zeros((n, n))

    m += np.diag(np.random.rand(n - 1), 1)
    m += np.diag(np.random.rand(n - 1), -1)

    m = strengthen_diagonal(m, 0.1)

    return m
