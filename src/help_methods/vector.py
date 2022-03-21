# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę ułatwiającą ustawienie wektora wyrazów wolnych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
import numpy as np

from .file import save_matrix_to_file
from ..generate_methods.random_vector import random_vector

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda sprawdza czy dla eksperymentu istnieje już wektor wyrazów wolnych
# Jeśli wektor istnieje to jest on wczytywany. W przeciwnym wypadku jest on generowany

"""
    Wejście:
        - file (str) - ścieżka pliku zapisu wektora wyrazów wolnych
        - size (int) - rozmiar wektora (liczba wierszy / kolumn)

    Wyjście:
        - vector (np.array) - wektor wyrazów wolnych
"""


def get_vector(file: str, size: int) -> np.array:
    # Deklaracja zmiennej przechowującej wektor
    vector = None

    # Jeśli plik z wektorem wyrazów wolnych nie istnieje to jest on generowany
    if not os.path.exists(file):
        print("Generowanie wektora wyrazów wolnych ...")
        vector = random_vector(size)

        print("Zapisywanie wektora wyrazów wolnych do pliku ...")
        save_matrix_to_file(file.rpartition("/"), f"b_{size}", vector)

    else:  # Jeśli plik z wektorem wyrazów wolnych istnieje to jest on wczytywany
        vector = np.loadtxt(file, dtype=float)

    # Zwrócenie wektora
    return vector
