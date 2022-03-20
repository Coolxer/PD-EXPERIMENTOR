# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę generującą wektor o losowych wartościach

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import os
import numpy as np
from ..help_functions.file import saveMatrixToFile

# Metoda geneuje wektor o podanym rozmiarze i zapisuje go do pliku

"""
    Wejście:
        - n - rozmiar wektora

    Wyjście:
        - v - wektor o losowych wartościach
"""


def random_vector(n):
    # Generowanie wektora  o losowych wartościach
    print("Generowanie wektora wyrazów wolnych ...")
    v = np.random.rand(n)

    # Zapis wektora do pliku
    print("Zapis wektora wyrazów wolnych do pliku ...")
    saveMatrixToFile(
        f"{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/exp_results",
        f"b_{n}",
        v,
    )

    # Zwrócenie wektora o losowych wartościach
    return v
