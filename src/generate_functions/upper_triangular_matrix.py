import numpy as np

from .random_matrix import random_matrix

# metoda generuje macierz górnotrójkątną na podstawie macierzy wygenerowanej w sposób losowy
def upper_triangular_matrix(n):
    m = random_matrix(n)

    return np.triu(m)
