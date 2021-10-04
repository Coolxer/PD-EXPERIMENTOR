from scipy.sparse import random

from src.generator.diagonal_amplifier import strengthen_diagonal


def sparse_matrix(n, dens):
    m = random(n, n, density=dens, format='csr').toarray()

    m = strengthen_diagonal(m, 0.1)

    return m
