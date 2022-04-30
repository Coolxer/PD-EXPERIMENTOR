# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę sortowania 5 list równolegle

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple

"""
    Wejście:
        - list1 (list) - najistotniejsza lista, według której sortowane są pozostałe listy
        - list2 (list) - druga lista, będąca posortowana wedle listy 'list1'
        - list3 (list) - trzecia lista, będąca posortowana wedle listy 'list1'
        - list4 (list) - czwarta lista, będąca posortowana wedle listy 'list1'
        - list5 (list) - piąta lista, będąca posortowana wedle listy 'list1'

    Wyjście:
        - l1 (list) - posortowana lista 'list1'
        - l2 (list) - posortowana lista 'list2'
        - l3 (list) - posortowana lista 'list3'
        - l4 (list) - posortowana lista 'list4'
        - l5 (list) - posortowana lista 'list5'
"""

# Metoda służy to sortowania 3 list równolegle, wedle klucza sortowania pierwszej listy
def sort5(list1: list, list2: list, list3: list, list4: list, list5: list) -> Tuple[list, list, list, list, list]:

    # Połączenie list w jedną krotkę
    zipped_lists = zip(list1, list2, list3, list4, list5)

    # Posortowanie list
    sorted_lists = sorted(zipped_lists)

    # Rozpakowanie list do krotki
    tuples = zip(*sorted_lists)

    # Rozdzielenie poszczególnych list do zmiennych
    l1, l2, l3, l4, l5 = [list(tuple) for tuple in tuples]

    # Zwrócenie posortowanych list
    return l1, l2, l3, l4, l5
