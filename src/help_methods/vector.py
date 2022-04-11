# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę ułatwiającą ustawienie wektora wyrazów wolnych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
import numpy as np

from ..generate_methods.random_vector import random_vector

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wejście:
        - file (str) - ścieżka pliku zapisu wektora wyrazów wolnych
        - size (int) - rozmiar wektora (liczba wierszy / kolumn)

    Wyjście:
        - vector (np.ndarray) - wektor wyrazów wolnych
        - loaded (bool) - informacja czy wektor wyrazów wolnych został wczytany czy wygenerowany
"""

# Metoda sprawdza czy dla eksperymentu istnieje już wektor wyrazów wolnych
# Jeśli wektor istnieje to jest on wczytywany. W przeciwnym wypadku jest on generowany
def get_vector(file: str, size: int) -> np.ndarray:

    # Deklaracja zmiennej przechowującej wektor i zmiennej informującej czy wektor został wczytany czy wygenerowany
    vector = None
    loaded = None

    # Jeśli plik z wektorem wyrazów wolnych nie istnieje to jest on generowany
    if not os.path.exists(file):
        vector = random_vector(size)
        loaded = False

    else:  # Jeśli plik z wektorem wyrazów wolnych istnieje to jest on wczytywany
        vector = np.loadtxt(file, dtype=float)
        loaded = True

    # Zwrócenie wektora i zmiennej 'loaded'
    return vector, loaded
