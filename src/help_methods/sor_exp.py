# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę wykonującą mnogą liczbę eksperymentów przy pomocy metody SOR.

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple
import numpy as np
from ...equiter.src.sor.method import sor

from .sort3 import sort3

"""
    Wejście:
        - A (np.ndarray) - macierz główna układu
        - b (np.ndarray) - wektor wyrazów wolnych
        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność wyniku
        - w_vector (np.ndarray) - wektor wartości parametru 'w'

    Wyjście:
        - solution (np.ndarray) - przybliżony wektor rozwiązania
        - iterations (int) - liczba wykonanych iteracji
        - time (float) - czas operacji

        Jeśli pojawi się błąd to metoda przerywa działanie i zwraca (None, None, None)
"""

# Metoda SOR wymaga większej uwagi, ponieważ posiada dodatkowy parametr 'w'
# Rozwiązanie poszukiwane jest z różną wartością tego parametru, a jako wynik przyjęty zostaje najlepszy rezultat
def sor_exp(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    w_vector: np.ndarray,
) -> Tuple[np.ndarray, int, float]:

    # Deklaracja list przechowujących wyniki cząstkowych eksperymentów metody SOR
    solutions = []
    iterations = []
    times = []

    # Pętla iterująca po wartościach parametru 'w'
    for w in w_vector:
        print(f"    - dla parametru 'w': {w}")

        # Obliczenie rozwiązania metodą SOR z aktualną wartością parametru 'w'
        solution, iteration, time = sor(A, b, max_iterations, tolerance, w)

        # Jeśli rozwiązanie dało błąd to należy przerwać dalsze obliczenia,
        if solution is None:
            return None, None, None

        # Dodanie rezultatów cząstkowych do list wyników
        solutions.append(solution)
        iterations.append(iteration)
        times.append(time)

    # Badania różnych wartości parametrów w mają na celu wyłonienie jednej konfiguracji
    # Do wyboru możliwe były 3 perspektywy (najgorsza, średnia, najlepsza)
    # Zdecydowano się wybrać najlepszą perspektywę (najlepsza zbieżność według liczby iteracji)
    # Ta perspektywa wydaje się być najbardziej odpowiednia, ponieważ metody Jacobiego i Gaussa-Seidela również dążą do doskonałości
    iterations_sorted, times_sorted, solutions_sorted = sort3(iterations, times, solutions)

    # Zwrócenie najlepszego rozwiązania, liczby wykonanych iteracji i czasu obliczeń
    return solutions_sorted[0], iterations_sorted[0], times_sorted[0]
