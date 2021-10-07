import numpy as np

from .diagonal_amplifier import strengthen_diagonal


# metoda generuje macierz wstęgowa o podanym rozmiarze i szerokości pasma 3, wygenerowaną w sposób losowy
# macierz jest dodatkowo wzmocniona, aby warunek zbieżności konieczny dla przybliżonych metod stacjonarnych był spełniony
def band_matrix(n):

    m = np.zeros((n, n))

    m += np.diag(np.random.rand(n - 1), 1)
    m += np.diag(np.random.rand(n - 1), -1)

    m = strengthen_diagonal(m, 0.1)

    return m
