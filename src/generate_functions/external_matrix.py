# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę konwertującą macierz pobraną ze źródeł zewnętrznych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import os
from tkinter import *
from tkinter.filedialog import askopenfilename

from scipy.io import loadmat
from .diagonal_amplifier import strengthen_diagonal

# Metoda służy do konwersji macierzy rzadkiej pobranej z kolekcji https://sparse.tamu.edu/
# Macierz jest dodatkowo wzmocniona, aby konieczny warunek zbieżności dla przybliżonych metod stacjonarnych był spełniony

"""
    Wyjście:
        - m - macierz pobrana ze źródeł zewnętrznych 
"""


def external_matrix():

    # Stworzenie instancji tk
    root = Tk()

    # Ukrycie graficznego okna głównego
    root.withdraw()

    # Utworzenie okna służącego do wyboru pliku macierzy
    file = askopenfilename(
        filetypes=(("Matlab files", "mat"),),
        title="Wybierz macierz pobraną z kolekcji macierzy rzadkich",
    )

    # Zniszczenie instancji tk
    root.destroy()

    # Załadowanie wybranego pliku matlab
    data = loadmat(file)

    # Pętla iterująca po obiekcie wczytanym z pliku aż do napotkania interesującego fragmentu
    for item in data["Problem"].item(0):

        # Jeśli znaleziono stosowny fragment obiektu to następuje pobranie macierzy
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            # Pobranie macierzy i przerwanie dalszych poszukiwań
            m = item.toarray()
            break

    # Wzmocnienie głównej przekątnej macierzy
    m = strengthen_diagonal(m, 0.1)

    # Zwrócenie macierzy pobranej ze źródeł zewnętrznych, gotowej do dalszego przetwarzania
    return m
