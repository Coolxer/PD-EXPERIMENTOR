import numpy as np

from .diagonal_amplifier import strengthen_diagonal

# metoda generuje macierz o podanym rozmiarze i o losowych elementach
# macierz jest dodatkowo wzmocniona, aby warunek zbieżności konieczny dla przybliżonych metod stacjonarnych był spełniony
def random_matrix(n):
    m = np.random.rand(n, n)

    m = strengthen_diagonal(m, 0.1)

    return m
