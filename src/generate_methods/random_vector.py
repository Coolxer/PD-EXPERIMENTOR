# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę generującą wektor

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np

"""
    Wejście:
        - size (int) - rozmiar wektora

    Wyjście:
        - vector (np.ndarray) - wektor o losowych wartościach
"""

# Metoda generuje wektor o podanym rozmiarze
def random_vector(size: int) -> np.ndarray:

    # Wygenerowanie wektora  o losowych wartościach z zakresu [0, 1]
    vector = np.random.rand(size)

    # Zwrócenie wektora 
    return vector
