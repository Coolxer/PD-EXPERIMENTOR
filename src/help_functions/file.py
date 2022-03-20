# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę zapisujacą dane tekstowe do pliku tekstowego
# Plik zawiera także metodę zapisującą macierz do pliku tekstowego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import os
import numpy as np


# Metoda zapisuje dane tekstowe do pliku tekstowego

"""
    Wejście:
        - dir - nazwa katalogu
        - name - nazwa pliku
        - content - zawartość do zapisania
"""


def saveNormalDataToFile(dir, name, content):
    # Otwarcie wskazanego pliku w trybie do zapisu
    file = open(f"{dir}/{name}.txt", "w")

    # Zapisanie zawartości do pliku
    file.write(str(content))

    # Zamknięcie pliku
    file.close()


# Metoda zapisuje macierze NumPy do pliku tekstowego

"""
    Wejście:
        - dir - nazwa katalogu
        - name - nazwa pliku
        - content - zawartość do zapisania
"""


def saveMatrixToFile(dir, name, content):
    # Zapisanie macierzy do pliku tekstowego
    np.savetxt(f"{dir}/{name}.txt", content)
