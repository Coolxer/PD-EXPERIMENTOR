from scipy.sparse import random

from .diagonal_amplifier import strengthen_diagonal

# metoda generuje macierz rzadką, korzystając z biblioteki scipy
# macierz jest dodatkowo wzmocniona, aby warunek zbieżności konieczny dla przybliżonych metod stacjonarnych był spełniony
"""
n oznacza rozmiar macierzy
dens oznacza gęstość macierzy, przy czym 1 to macierz pełna, a 0 to macierz zerowa
"""


def sparse_matrix(n, dens):
    m = random(n, n, density=dens, format="csr").toarray()

    m = strengthen_diagonal(m, 0.1)

    return m
