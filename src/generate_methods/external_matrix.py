# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę konwertującą macierz pobraną ze źródeł zewnętrznych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from scipy.io import loadmat
from .diagonal_amplifier import strengthen_diagonal

from ..help_methods.file import choose_matlab_file

# Metoda służy do konwersji macierzy rzadkiej pobranej z kolekcji https://sparse.tamu.edu/
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony

"""
    Wyjście:
        - matrix (np.array) - macierz pobrana ze źródeł zewnętrznych 
"""


def external_matrix() -> np.array:
    # Utworzenie widoku wyboru pliku .mat (matlab)
    file = choose_matlab_file()

    # Załadowanie wybranego pliku matlab
    data = loadmat(file)

    # Deklaracja zmiennej do przechowania macierzy
    matrix = None

    # Pętla iterująca po obiekcie wczytanym z pliku aż do napotkania interesującego fragmentu
    for item in data["Problem"].item(0):
        # Jeśli znaleziono stosowny fragment obiektu to następuje pobranie macierzy
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            # Pobranie macierzy i przerwanie dalszych przeszukiwań obiektu
            matrix = item.toarray()
            break

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix, 0.1)

    # Zwrócenie macierzy pobranej ze źródeł zewnętrznych, gotowej do dalszego przetwarzania
    return matrix