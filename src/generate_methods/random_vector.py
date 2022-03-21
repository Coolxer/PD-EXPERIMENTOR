# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą wektor o losowych wartościach

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

# Metoda geneuje wektor o podanym rozmiarze

"""
    Wejście:
        - size (int) - rozmiar wektora

    Wyjście:
        - vector (np.array) - wektor o losowych wartościach
"""


def random_vector(size: int) -> np.array:
    # Wygenerowanie wektora  o losowych wartościach
    vector = np.random.rand(size)

    # Zwrócenie wektora o losowych wartościach
    return vector
