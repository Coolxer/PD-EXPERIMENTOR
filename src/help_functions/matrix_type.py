# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający słownik macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

types = {
    "sparse": "sparse",  # rzadka, wygenerowana przy pomocy zewnętrznej biblioteki
    "random": "random",  # pełna wygenerowana w sposób losowy
    "diagonal": "diagonal",  # diagonalna, wygenerowana w sposób losowy
    "band": "band",  # wstęgowa (pasmowa) o szerokości 3
    "lower_triangular": "lower_triangular",  # dolnotrójkątna
    "upper_triangular": "upper_triangular",  # górnotrójkątna
    "external": "external",  # zewnętrzna, pobrana ze źródeł zewnętrznych
}
