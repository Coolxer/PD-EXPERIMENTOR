# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę konwertującą macierz pobraną ze źródeł zewnętrznych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from scipy.io import loadmat
from .diagonal_amplifier import strengthen_diagonal

from ..help_methods.file import choose_matlab_file

"""
    Wyjście:
        - matrix (np.ndarray) - macierz pobrana ze źródeł zewnętrznych 
"""

# Metoda służy do konwersji macierzy rzadkiej pobranej z kolekcji https://sparse.tamu.edu/
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony
def external_matrix() -> np.ndarray:

    # Utworzenie widoku wyboru pliku .mat (matlab)
    file = choose_matlab_file()

    # Załadowanie wybranego pliku matlab
    data = loadmat(file)

    # Deklaracja zmiennej do przechowania macierzy
    matrix = None

    i = 0

    # Pętla iterująca po obiekcie wczytanym z pliku aż do napotkania interesującego fragmentu
    for item in data["Problem"].item(0):

        if i == 2:
            matrix = item.toarray()
            break

        i = i + 1

        """"
        # Jeśli znaleziono stosowny fragment obiektu to następuje pobranie macierzy
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>" or str(type(item)) == "<class 'numpy.float64'>":

            # Pobranie macierzy i przerwanie dalszych przeszukiwań obiektu
            matrix = item.toarray()
            break
        """

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy pobranej ze źródeł zewnętrznych, gotowej do dalszego przetwarzania
    return matrix
