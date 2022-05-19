# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę wykonującą mnogą liczbę eksperymentów przy pomocy metody SOR.

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import Tuple
import numpy as np
from ..tracking_methods.sor import sor

"""
    Wejście:
        - A (np.ndarray) - macierz główna układu
        - b (np.ndarray) - wektor wyrazów wolnych
        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - dokładność przybliżonego rozwiązania
        - w_vector (np.ndarray) - wektor wartości parametru 'w'
        - x0 (np.ndarray) - początkowy wektor przybliżonego rozwiązania

    Wyjście:
        - solutions (list)) - przybliżone wektory rozwiązań
        - iterations (list) - liczby wykonanych iteracji
        - times (list) - czasy operacji
        - ws (list) - wartości parametru 'w'
        - errors (list) - błędy na poszczególnych etapach iteracji
        - w_with_iterations (str) - ciąg zawierający listę wartości 'w' i powiązane z nimi wyniki iteracji
        - w_with_times (str) - ciąg zawierający listę wartości 'w' i powiązane z nimi wyniki czasowe
        - w_with_errors(str) - ciąg zawierający listę wartości 'w' i powiązane z nimi błędy
        - index (int) - indeks najlepszych rezultatów

        Jeśli pojawi się błąd to metoda przerywa działanie i zwraca (None, None, None, None, None, None, None, None)
"""

# Metoda SOR wymaga większej uwagi, ponieważ posiada dodatkowy parametr 'w'
# Rozwiązanie poszukiwane jest z różną wartością tego parametru, a jako wynik przyjęty zostaje najlepszy rezultat
def sor_exp(
    A: np.ndarray, b: np.ndarray, max_iterations: int, tolerance: float, w_vector: np.ndarray, x0: np.ndarray
) -> Tuple[list, list, list, list, list, str, str]:

    # Deklaracja list przechowujących wyniki cząstkowych eksperymentów metody SOR i wartości parametru 'w'
    solutions = []
    iterations = []
    times = []
    w_values = []
    errors = []

    w_with_iterations = ""
    w_with_times = ""
    w_with_errors = ""

    experiment_repeats = 3

    # Pętla iterująca po wartościach parametru 'w'
    for w in w_vector:
        print(f"    - dla parametru 'w': {w}")

        # Przygotowanie do powtarzania eksperymentów
        ss = []
        it = []
        ts = []
        es = []

        for i in range(experiment_repeats):

            # Obliczenie rozwiązania metodą SOR z aktualną wartością parametru 'w'
            solution, iteration, time, error = sor(A, b, max_iterations, tolerance, w, x0)

            # Jeśli rozwiązanie dało błąd to należy przerwać dalsze obliczenia,
            if solution is None:
                print("Błąd rozwiązania metodą SOR")
                return None, None, None, None, None, None, None, None

            # Dodanie do tablic wyników powtarzanych eksperymentów
            ss.append(solution)
            it.append(iteration)
            ts.append(time)
            es.append(error)

        # Obliczenie średnich wyników iteracji i czasu
        iteration = round(sum(it) / experiment_repeats)
        time = round(sum(ts) / experiment_repeats, 6)

        # Obliczenie średnich rezultatów
        solution = []
        for i in range(len(ss[0])):
            solution.append(0)

            for j in range(experiment_repeats):
                solution[i] += ss[j][i]

            solution[i] /= experiment_repeats

        # Obliczenie średnich błędów
        error = []
        for i in range(min(list(map(lambda x: len(x), es)))):
            error.append(0)

            for j in range(experiment_repeats):
                error[i] += es[j][i]

            error[i] /= experiment_repeats

        # Dodanie rezultatów cząstkowych do list wyników
        solutions.append(solution)
        iterations.append(iteration)
        times.append(time)
        w_values.append(w)
        errors.append(error)

        # Utworzenie łańcuchów znaków wiążących wartości parametru 'w' z wynikami iteracji i czasu
        w_with_iterations += f"{w} = {iteration}\n"
        w_with_times += f"{w} = {time}\n"
        w_with_errors += f"{w} = {error}\n"

    # Zwrócenie rezultatów
    return (
        solutions,
        iterations,
        times,
        w_values,
        errors,
        w_with_iterations,
        w_with_times,
        w_with_errors,
        iterations.index(min(iterations)),
    )
