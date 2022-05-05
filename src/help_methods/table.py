# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę tworzącą tabelę wyników

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
import pandas as pd
import dataframe_image as dfi

"""
    Wejście:
        - path (str) - scieżka zapisu tabeli
        - column_headers (list) - nagłówki kolumn tabeli
        - row_headers (list) - nagłówki wierszy tabeli
        - data (list) - wyniki
"""

# Metoda tworzy tabelę wyników
def draw_table(
    path: str,
    column_headers: list,
    row_headers: list,
    data: list,
) -> NoReturn:

    # Utworzenie tabeli
    data_frame = pd.DataFrame(np.transpose(np.array(data)).tolist())

    # Ustawienie nagłówków kolumn tabeli
    data_frame.columns = column_headers

    # Ustawienie nagłówków wierszy tabeli
    data_frame.index = row_headers

    # Zapisanie tabeli do pliku
    dfi.export(data_frame, f"{path}.png")
