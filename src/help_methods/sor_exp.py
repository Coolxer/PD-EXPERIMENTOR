# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę wykonującą mnogą liczbę eksperymentów przy pomocy metody SOR.

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple
import numpy as np
from ..tracking_methods.sor import sor

from .sort5 import sort5

"""
    Wejście:
        - A (np.ndarray) - macierz główna układu
        - b (np.ndarray) - wektor wyrazów wolnych
        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - dokładność przybliżonego rozwiązania
        - w_vector (np.ndarray) - wektor wartości parametru 'w'

    Wyjście:
        - solutions (list)) - przybliżone wektory rozwiązań
        - iterations (list) - liczby wykonanych iteracji
        - times (list) - czasy operacji
        - ws (list) - wartości parametru 'w'
        - errors (list) - błędy na poszczególnych etapach iteracji
        - w_with_iterations (str) - ciąg zawierający listę wartości 'w' i powiązane z nimi wyniki iteracji
        -  w_with_times (str) - ciąg zawierający listę wartości 'w' i powiązane z nimi wyniki czasowe

        Jeśli pojawi się błąd to metoda przerywa działanie i zwraca (None, None, None, None)
"""

# Metoda SOR wymaga większej uwagi, ponieważ posiada dodatkowy parametr 'w'
# Rozwiązanie poszukiwane jest z różną wartością tego parametru, a jako wynik przyjęty zostaje najlepszy rezultat
def sor_exp(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    w_vector: np.ndarray,
) -> Tuple[list, list, list, list, list, str, str]:

    # Deklaracja list przechowujących wyniki cząstkowych eksperymentów metody SOR i wartości parametru 'w'
    solutions = []
    iterations = []
    times = []
    w_values = []
    errors = []

    w_with_iterations = ""
    w_with_times = ""

    # Pętla iterująca po wartościach parametru 'w'
    for w in w_vector:
        print(f"    - dla parametru 'w': {w}")

        # Obliczenie rozwiązania metodą SOR z aktualną wartością parametru 'w'
        solution, iteration, time, error = sor(A, b, max_iterations, tolerance, w)

        # Jeśli rozwiązanie dało błąd to należy przerwać dalsze obliczenia,
        if solution is None:
            return None, None, None, None

        # Dodanie rezultatów cząstkowych do list wyników
        solutions.append(solution)
        iterations.append(iteration)
        times.append(time)
        w_values.append(w)
        errors.append(error)

        w_with_iterations += f"{w} = {iteration}\n"
        w_with_times += f"{w} = {time}\n"

    # Badania różnych wartości parametrów w mają na celu wyłonienie jednej konfiguracji
    # Do wyboru możliwe były 3 perspektywy (najgorsza, średnia, najlepsza)
    # Zdecydowano się wybrać najlepszą perspektywę (najlepsza zbieżność według liczby iteracji)
    # Ta perspektywa wydaje się być najbardziej odpowiednia, ponieważ metody Jacobiego i Gaussa-Seidela również dążą do doskonałości
    iterations_sorted, times_sorted, solutions_sorted, w_sorted, errors_sorted = sort5(
        iterations, times, solutions, w_values, errors
    )

    # Zwrócenie rezultatów
    return solutions_sorted, iterations_sorted, times_sorted, w_sorted, errors_sorted, w_with_iterations, w_with_times
