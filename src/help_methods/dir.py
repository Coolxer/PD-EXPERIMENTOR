# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę zwracającą główny katalog eksperymentów

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os

"""
    Wyjście:
        - dir (str) - główny katalog eksperymentów
"""

# Metoda zwraca główny katalog eksperymentów
def get_data_dir() -> str:

    # Pobranie ścieżki
    dir = f"{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}/data"

    # Sprawdzenie czy katalog 'data' istnieje. Jeśli nie to zostanie on utworzony
    if not os.path.exists(dir):
        os.mkdir(dir)

    # Zwrócenie ścieżki katalogu 'data'
    return dir
