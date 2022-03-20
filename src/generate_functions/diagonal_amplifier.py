# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę wzmacniającą główną przekątną macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import numpy as np

# Metoda służy do wzmacniania głównej przekątnej dowolnej macierzy,  aby był spełniony
# konieczny  warunek zbieżności dla stacjonarnych metod prrzybliżonych rozwiązywania URL

"""
    Wejście:
        - matrix - macierz do wzmocnienia
        - value  - wartość wzmocnienia głównej przekątnej macierzy

    Wyjście:
        - m - wzmocniona przekątniowo macierz
"""


def strengthen_diagonal(matrix, value):

    # Utworzenie kopii macierzy wejściowej
    m = matrix.copy()

    # Wyznaczenie wartości absolutnych głównej przekątnej macierzy
    D_abs = np.abs(np.diag(m))

    # Obliczenie sumy wartości absolutnych wszystkich elementów każdego wiersza
    # za wyjątkiem elementów leżących na głównej przekątnej macierzy
    S = np.sum(np.abs(m), axis=1) - D_abs

    # Pętla iterująca po każdym wierszu macierzy
    for i in range(np.shape(m)[0]):

        # Jeśli wartość absolutna elementu leżącego na głównej przekątnej
        # jest mniejsza bądź równa sumie wartości absolutnych w tym wierszu
        # to element leżący na głównej przekątnej stanowi tę sumę powiększoną o 'value'
        # to sprawia, że macierz staje się diagonalnie dominująca
        if np.abs(m[i][i]) <= S[i]:
            m[i][i] = S[i] + value

    # Zwrócenie  macierzy wzmocnionej
    return m
