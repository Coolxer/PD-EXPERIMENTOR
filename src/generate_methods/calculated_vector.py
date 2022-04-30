# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę obliczającą wektor na podstawie macierzy i wektora

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

"""
    Wejście:
        - A (np.ndarray) - macierz główna

    Wyjście:
        - vector (np.ndarray) - wektor 
"""

# Metoda oblicza wektor na podstawie macierzy i wektora
def calculated_vector(A: np.ndarray) -> np.ndarray:

    # Pobranie stopnia macierzy A
    order = np.shape(A)[0]

    # Wygenerowanie wektora składającego się z samych 1
    x = np.ones(order)

    # Oblioczenie wektora
    vector = np.dot(A, x)

    # Zwrócenie wektora
    return vector
