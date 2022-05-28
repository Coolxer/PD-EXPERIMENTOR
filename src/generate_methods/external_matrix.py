# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę konwertującą macierz pobraną ze źródeł zewnętrznych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
import scipy.sparse
from scipy.io import loadmat
import h5py
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
    # data = h5py.File(file, "r")

    # Deklaracja zmiennej do przechowania macierzy
    matrix = None

    i = 0

    # mat 7.3
    # matrix = list(data["Problem"]["A"]["data"])

    # # Pętla iterująca po obiekcie wczytanym z pliku aż do napotkania interesującego fragmentu
    for item in data["Problem"].item(0):

        # Jeśli znaleziono stosowny fragment obiektu to następuje pobranie macierzy
        if isinstance(item, scipy.sparse.csc_matrix) or isinstance(item, scipy.sparse.csr_matrix):

            # Pobranie macierzy i przerwanie dalszych przeszukiwań obiektu
            matrix = item.toarray()
            break

    # Wzmocnienie głównej przekątnej macierzy
    matrix = strengthen_diagonal(matrix)

    # Zwrócenie macierzy pobranej ze źródeł zewnętrznych, gotowej do dalszego przetwarzania
    return matrix
