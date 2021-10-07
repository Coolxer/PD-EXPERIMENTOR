import numpy as np

from .random_matrix import random_matrix

# metoda generuje macierz dolnotrókątną na podstawie macierzy wygenerowanej w sposób losowy
def lower_triangular_matrix(n):
    m = random_matrix(n)

    return np.tril(m)
