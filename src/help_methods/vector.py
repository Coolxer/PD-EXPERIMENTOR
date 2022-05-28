# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę ułatwiającą ustawienie wektora wyrazów wolnych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

from ..generate_methods.random_vector import random_vector
from ..generate_methods.calculated_vector import calculated_vector
from .dir import get_data_dir

"""
    Wejście:
        - size (int) - rozmiar wektora (liczba wierszy / kolumn)
        - A(np.ndarray) [None] - macierz główna układu (jeśli podana, tzn., że chcemy obliczyć wektor wyrazów wolnych b na podstawie Ax, a nie generować w sposób losowy)

    Wyjście:
        - vector (np.ndarray) - wektor wyrazów wolnych
"""

# Metoda sprawdza czy dla eksperymentu istnieje już wektor wyrazów wolnych
# Jeśli wektor istnieje to jest on wczytywany. W przeciwnym wypadku jest on generowany
# Ewentualnie można także taki wektor wyliczyć
def get_vector(size: int, A: np.ndarray = None) -> np.ndarray:

    # Deklaracja zmiennej przechowującej wektor i zmiennej informującej czy wektor został wczytany czy wygenerowany
    vector = None

    if A is not None:
        vector = calculated_vector(A)
    else:
        # Jeśli plik z wektorem wyrazów wolnych nie istnieje to jest on generowany
        # if not os.path.exists(file):
        #     vector = random_vector(size)

        # else:  # Jeśli plik z wektorem wyrazów wolnych istnieje to jest on wczytywany
        #    vector = np.loadtxt(file, dtype=float)

        vector = np.loadtxt(f"{get_data_dir()}/b_{size}.txt", dtype=float)

    # Zwrócenie wektora i zmiennej 'loaded'
    return vector
