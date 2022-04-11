# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera:
#   - metodę zapisujacą dane tekstowe do pliku tekstowego
#   - metodę zapisującą macierz do pliku tekstowego
#   - metodę umożliwiającą wybór macierzy pliku .mat (matlab)

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
from tkinter import *
from tkinter.filedialog import askopenfilename
import numpy as np

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda zapisuje dane tekstowe do pliku tekstowego

"""
    Wejście:
        - dir (str) - nazwa katalogu
        - name (str) - nazwa pliku
        - data (str) - zawartość do zapisania
"""


def save_data_to_file(dir: str, name: str, data: str) -> NoReturn:

    # Otwarcie wskazanego pliku w trybie do zapisu
    file = open(f"{dir}/{name}.txt", "w")

    # Zapisanie zawartości do pliku
    file.write(str(data))

    # Zamknięcie pliku
    file.close()


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda zapisuje macierz / wektor NumPy do pliku tekstowego

"""
    Wejście:
        - dir (str) - nazwa katalogu
        - name (str) - nazwa pliku
        - matrix (np.ndarray) - macierz / wektor do zapisania
"""


def save_matrix_to_file(dir: str, name: str, matrix: np.ndarray) -> NoReturn:
    # Zapisanie macierzy / wektora do pliku tekstowego
    np.savetxt(f"{dir}/{name}.txt", matrix)


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wyjście:
        - file (str) - wczytany plik .mat (matlab)
"""

# Metoda wyświetla okno do wyboru pliku macierzy .mat (matlab)
def choose_matlab_file() -> str:

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

    # Zwrócenie wczytanego pliku
    return file


# -------------------------------------------------------------------------------------------------------------------------------------------------- #
