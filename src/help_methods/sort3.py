# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę sortowanie 3 list równolegle

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple


# Metoda służy to sortowania 3 list równolegle, wedle klucza sortowania pierwszej listy

"""
    Wejście:
        - list1 (list) - najistotniejsza lista, według której sortowane są pozostałe listy
        - list2 (list) - druga lista, będąca posortowana wedle listy 'list1'
        - list3 (list) - trzecia lista, będąca posortowana wedle listy 'list1'

    Wyjście:
        - l1 (list) - posortowana lista 'list1'
        - l2 (list) - posortowana lista 'list2'
        - l3 (list) - posortowana lista 'list3'
"""


def sort3(list1: list, list2: list, list3: list) -> Tuple[list, list, list]:
    # Połączenie list w jedną krotkę
    zipped_lists = zip(list1, list2, list3)

    # Posortowanie list
    sorted_lists = sorted(zipped_lists)

    # Rozpakowanie list do krotki
    tuples = zip(*sorted_lists)

    # Rozdzielenie poszczególnych list do zmiennych
    l1, l2, l3 = [list(tuple) for tuple in tuples]

    # Zwrócenie posortowanych list
    return l1, l2, l3
