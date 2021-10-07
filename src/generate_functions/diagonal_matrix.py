import numpy as np
from random import random


# metoda generuje macierz diagonalną o podanym rozmiarze
def diagonal_matrix(n):
    m = np.zeros((n, n))

    for i in range(np.shape(m)[0]):
        m[i][i] = random()

    return m
