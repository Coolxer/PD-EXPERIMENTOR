# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę tworzącą tabelę wyników

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import pandas as pd
import dataframe_image as dfi

"""
    Wejście:
        - path (str) - scieżka zapisu tabeli
        - name (str) - nazwa pliku tabeli
        - column_headers (list) - nagłówki kolumn tabeli
        - row_headers (list) - nagłówki wierszy tabeli
        - jacobi_data (list) - wyniki dot. metody Jacobiego
        - gauss_seidel_data (list) - wyniki dot. metody Gaussa-Seidela
        - sor_data (list) - wyniki dot. metody SOR
"""

# Metoda tworzy tabelę wyników
def draw_table(
    path: str,
    name: str,
    column_headers: list,
    row_headers: list,
    jacobi_data: list,
    gauss_seidel_data: list,
    sor_data: list,
) -> NoReturn:

    # Utworzenie tabeli
    data_frame = pd.DataFrame(list(zip(jacobi_data, gauss_seidel_data, sor_data)))

    # Ustawienie nagłówków kolumn tabeli
    data_frame.columns = column_headers

    # Ustawienie nagłówków wierszy tabeli
    data_frame.index = row_headers

    # Zapisanie tabeli do pliku
    dfi.export(data_frame, f"{path}/{name}.png")
