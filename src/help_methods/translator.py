# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę tłumaczącą nazwy typów macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wejście:
        - eng_matrix_names (str): kluczowe nazwy macierzy w j. angielskim

    Wyjście:
        - pl_matrix_names (str): nazwy macierzy w języku polskim
"""

# Macierz zamienia kluczowe nazwy macierzy na poprawne nazwy w j. polskim
def translate_matrix_names(eng_matrix_names: list) -> list:
    pl_matrix_names = []

    for name in eng_matrix_names:
        if name == "band":
            pl_matrix_names.append("wstęgowa")
        elif name == "diagonal":
            pl_matrix_names.append("diagonalna")
        elif name == "full":
            pl_matrix_names.append("pełna")
        elif name == "lower_triangular":
            pl_matrix_names.append("dolno-trójkątna")
        elif name == "sparse":
            pl_matrix_names.append("rzadka")
        elif name == "upper_triangular":
            pl_matrix_names.append("górno-trójkątna")
        else:
            continue

    return pl_matrix_names
