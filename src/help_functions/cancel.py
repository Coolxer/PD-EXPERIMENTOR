# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę usuwającą wcześniej utworzony katalog i kończącą pracę skryptu

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
from shutil import rmtree
from sys import exit


# Metoda usuwa wcześniej utworzony katalog i kończy działanie skryptu

"""
    Wejście:
        - dir - ścieżka katalogu do usunięcia
"""


def cancel(dir):
    # Usunięcie wskazanego katalogu
    rmtree(dir)

    # Zakończenie skryptu
    exit()
