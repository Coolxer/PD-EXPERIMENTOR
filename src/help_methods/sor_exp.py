# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę wykonującą mnogą liczbę eksperymentów przy pomocy metody SOR.

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple
import numpy as np
from ...equiter.src.sor.method import sor

from .sort3 import sort3

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda SOR wymaga większej uwagi, ponieważ posiada dodatkowy parametr w
# Rozwiązanie poszukiwane jest z różną wartością tego parametru, a jako wynik przyjęty zostaje najlepszy rezultat

"""
    Wejście:
        - A (np.array) - macierz główna układu
        - b (np.array) - wektor wyrazów wolnych
        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność wyniku
        - w_vector (np.array) - wektor wartości parametru w

    Wyjście:
        - solution (np.array) - przybliżony wektor rozwiązania
        - iterations (int) - liczba wykonanych iteracji
        - time (float) - czas operacji

        Jeśli pojawi się błąd to metoda przerywa działanie i zwraca (None, None, None)
"""


def sor_exp(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    w_vector: np.array,
) -> Tuple(np.array, int, float):

    # Deklaracja list przechowujących wyniki cząstkowych eksperymentów metody SOR
    solutions = []
    iterations = []
    times = []

    # Pętla iterująca po wartościach parametru w
    for w in w_vector:
        print(f"    SOR: w: {w}")

        # Obliczenie rozwiązania metodą SOR z aktualną wartością parametru w
        solution, iteration, time = sor(A, b, max_iterations, tolerance, w)

        # Jeśli rozwiązanie dało błąd to należy przerwać dalsze obliczenia,
        if solution is None:
            return None, None, None

        # Dodanie rezultatów cząstkowych do list wyników
        solutions.append(solution)
        iterations.append(iteration)
        times.append(time)

    # Badania różnych wartości parametrów w mają na celu wyłonienie jednej konfiguracji
    # Możliwe są 3 perspektywy do wyboru (najgorsza, średnia, najlepsza)
    # Zdecydowano się wybrać najlepszą perspektywę (najlepsza zbieżność według liczby iteracji)
    # Ta perspektywa wydaje się być najbardziej odpowiednia, ponieważ metody Jacobiego i Gaussa-Seidela również dążą do doskonałości
    iterations_sorted, times_sorted, solutions_sorted = sort3(iterations, times, solutions)

    # Zwrócenie najlepszego rozwiązania, liczby wykonanych iteracji i czasu obliczeń
    return solutions_sorted[0], iterations_sorted[0], times_sorted[0]
