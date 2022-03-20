# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą macierz rzadką

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
from scipy.sparse import random
from .diagonal_amplifier import strengthen_diagonal

# Metoda generuje macierz rzadką, korzystając z biblioteki scipy
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony

"""
    Wejście:
        - n - rozmiar macierzy (liczba wierszy / kolumn)
        - dens - gęstość macierzy, przy czym 1 to macierz pełna, a 0 to macierz w pełni rzadka (zerowa)

    Wyjście:
        - m - macierz rzadka
"""


def sparse_matrix(n, dens):

    # Wygenerowanie rzadkiej macierzy kwadratowej o rozmiarze 'n x n'
    m = random(n, n, density=dens, format="csr").toarray()

    # Wzmocnienie głównej przekątnej macierzy
    m = strengthen_diagonal(m, 0.1)

    # Zwrócenie macierzy rzadkiej
    return m
