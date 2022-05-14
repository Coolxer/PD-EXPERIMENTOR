# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę służącą do prowadzenia pojedynczych eksperymentów

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import modułów generalnych
import os
import shutil
from typing import NoReturn
import numpy as np

# Import zmodyfikowanych metod z modułu @equiter (modyfikacja polegająca głównie na możliwości śledzenia w czasie rzeczywsitym)
from .tracking_methods.jacobi import jacobi
from .tracking_methods.gauss_seidel import gauss_seidel

# Import funkcji pomocniczych
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_matrix_to_file, save_chart_to_file
from .help_methods.vector import get_vector
from .help_methods.sor_exp import sor_exp
from .help_methods.matrix import get_matrix

# Import metod rysujących wykresy
from .charts.iterations_or_times_to_methods import draw_iterations_to_methods, draw_times_to_methods
from .charts.iterations_or_times_to_SOR_only import draw_iterations_to_SOR_only, draw_times_to_SOR_only
from .charts.errors_to_iterations import draw_errors_to_iterations
from .charts.errors_to_iterations_SOR_only import draw_errors_to_iterations_SOR_only


"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu
        - experiment_size (int) - rozmiar URL
        - matrix_type (str) - typ macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - dokładność przybliżonego rozwiązania
        - w_values (list) - lista wartości parametru 'w' do przetestowania

        - x0 (np.ndarray) [None] - początkowy wektor przybliżeń
        - calculate_b_vector(bool) [False] - czy wektor wyrazów wolnych b ma zostać obliczony na podstawie Ax (gdzie x = [1, 1, 1, 1]). W przeciwnym wypadku jest on generowany.
"""

# Metoda służąca do prowadzenia klasyczynych bazowych eksperymentów
def do_basic_experiment(
    experiment_name: str,
    experiment_size: int,
    matrix_type: str,
    max_iterations: int,
    tolerance: float,
    w_values: list,
    x0: np.ndarray = None,
    calculate_b_vector: bool = True,
) -> NoReturn:

    print("\n#############################################################")
    print(f"######### Eksperyment:  {experiment_name} ###########")

    # --------------------------------------------------------- Sekcja konfiguracji -------------------------------------------------------- #

    # Uzyskanie katalogu głównego eksperymentpw
    data_dir = get_data_dir()

    # Pobranie macierzy wejściowej układu
    print("\nGenerowanie macierzy głównej ...")
    A = get_matrix(matrix_type, experiment_size)

    # Ustawienie wektora wyrazów wolnych
    print("Generowanie / Obliczanie / Wczytywanie wektora wyrazów wolnych ...")
    b, was_b_loaded = get_vector(
        f"{data_dir}/b_{experiment_size}.txt", experiment_size, A if calculate_b_vector else None
    )

    # ------------------------------------------------------- Sekcja rozwiązywania ------------------------------------------------------- #

    # Przygotowanie danych do powtarzania eksperymentów (w celu wyciągnięcia średniej i uniknięcia przypadkowości)
    experiment_repeats = 3

    solutions = [[], [], []]
    iterations = [0, 0, 0]
    times = [0, 0, 0]
    errors = [[], [], []]

    print("Rozwiązywanie układu metodą Jacobiego ...")
    for i in range(experiment_repeats):
        jacobi_solution, jacobi_iterations, jacobi_time, jacobi_errors = jacobi(A, b, max_iterations, tolerance, x0)

        if jacobi_solution is None:
            print("Błąd rozwiązania metodą Jacobiego")
            return

        # Dodanie wyników powtarzających się eksperymentów do tablic
        solutions[i] = jacobi_solution
        iterations[i] = jacobi_iterations
        times[i] = jacobi_time
        errors[i] = jacobi_errors

    # Obliczenie średnich z wyników iteracji i czasu
    jacobi_iterations = round(sum(iterations) / experiment_repeats)
    jacobi_time = round(sum(times) / experiment_repeats, 6)

    # Obliczenie średniego rezultatu
    jacobi_solution = []
    for i in range(len(solutions[0])):
        jacobi_solution.append(0)

        for j in range(experiment_repeats):
            jacobi_solution[i] += solutions[j][i]

        jacobi_solution[i] /= experiment_repeats

    # Obliczenie średniego błędu
    jacobi_errors = []
    for i in range(min(list(map(lambda x: len(x), errors)))):
        jacobi_errors.append(0)

        for j in range(experiment_repeats):
            jacobi_errors[i] += errors[j][i]

        jacobi_errors[i] /= experiment_repeats

    print("Rozwiązywanie układu metodą Gaussa-Seidela ...")
    for i in range(experiment_repeats):
        gauss_seidel_solution, gauss_seidel_iterations, gauss_seidel_time, gauss_seidel_errors = gauss_seidel(
            A, b, max_iterations, tolerance, x0
        )

        if gauss_seidel_solution is None:
            print("Błąd rozwiązania metodą Gaussa-Seidela")
            return

        # Dodanie wyników powtarzających się eksperymentów do tablic
        solutions[i] = gauss_seidel_solution
        iterations[i] = gauss_seidel_iterations
        times[i] = gauss_seidel_time
        errors[i] = gauss_seidel_errors

    # Obliczenie średnich z wyników iteracji i czasu
    gauss_seidel_iterations = round(sum(iterations) / experiment_repeats)
    gauss_seidel_time = round(sum(times) / experiment_repeats, 6)

    # Obliczenie średniego rezultatu
    gauss_seidel_solution = []
    for i in range(len(solutions[0])):
        gauss_seidel_solution.append(0)

        for j in range(experiment_repeats):
            gauss_seidel_solution[i] += solutions[j][i]

        gauss_seidel_solution[i] /= experiment_repeats

    # Obliczenie średniego błędu
    gauss_seidel_errors = []
    for i in range(min(list(map(lambda x: len(x), errors)))):
        gauss_seidel_errors.append(0)

        for j in range(experiment_repeats):
            gauss_seidel_errors[i] += errors[j][i]

        gauss_seidel_errors[i] /= experiment_repeats

    print("Rozwiązywanie układu metodą SOR ...")
    sor_solutions, sor_iterations, sor_times, ws, sor_errors, w_with_iterations, w_with_times, w_with_errors = sor_exp(
        A, b, max_iterations, tolerance, w_values, x0
    )

    if sor_solutions is None:
        return

    # -------------------------------------------------- Sekcja tworzenia katalogów -------------------------------------------------- #

    # Tworzenie katalogu głównego dla konkretnego badania
    this_exp_dir = f"{data_dir}/{experiment_name}"
    if os.path.exists(this_exp_dir):
        shutil.rmtree(this_exp_dir)
    os.makedirs(this_exp_dir)

    # Tworzenie katalogu konfiguracyjnego (A, b, max_iterations, tolerance)
    config_dir = f"{this_exp_dir}/config"
    os.mkdir(config_dir)

    # Tworzenie katalogu wynikowego
    results_dir = f"{this_exp_dir}/results"
    os.mkdir(results_dir)

    # Tworzenie katalogu do zapisu ogólnych wyników tekstowych
    results_dir_txt = f"{results_dir}/txt"
    os.mkdir(results_dir_txt)

    # Tworzenie katalogu do zapisu szczegółowych wyników tekstowych (wektorów wynikowych)
    results_dir_txt_solution = f"{results_dir_txt}/solution"
    os.mkdir(results_dir_txt_solution)

    # Tworzenie katalogu dla wykresów
    results_dir_img = f"{results_dir}/img"
    os.mkdir(results_dir_img)

    os.mkdir(f"{results_dir_img}/fig")
    os.mkdir(f"{results_dir_img}/png")
    os.mkdir(f"{results_dir_img}/svg")
    os.mkdir(f"{results_dir_img}/pdf")

    # ---------------------------------------------------- Sekcja zapisu parametrów --------------------------------------------------- #

    print("Zapisywanie informacji o eksperymencie ...")
    save_data_to_file(
        config_dir,
        "description",
        f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = podstawowy\nwektor b = {'obliczony' if calculate_b_vector else 'wygenerowany'}\ntyp macierzy =  {matrix_type}\nrozmiar URL = {experiment_size}\nmaksymalna liczba iteracji = {max_iterations}\ndokładność = {tolerance}\nw= {w_values}\nnajlepszy wynik dla 'w' =  {ws[0]}",
    )

    # Rezygnacja z zapisu macierzy 'A' i wektora wyrazów wolnych 'b'

    # print("Zapisywanie macierzy głównej ...")
    # save_matrix_to_file(config_dir, "A", A)

    # Sprawdzenie czy wektor b został wczytany czy wygenerowany
    # Jeśli wektor został wygenerowany to należy go zapisać do pliku
    # if not was_b_loaded:

    #    print("Zapisywanie wektora wyrazów wolnych ...")
    #    save_matrix_to_file(f"{data_dir}", f"b_{size}", b)

    # ------------------------------------------------------- Sekcja zapisu wyników ------------------------------------------------------ #

    print("Zapisywanie liczby wyk. iteracji ...")
    save_data_to_file(
        results_dir_txt,
        "iterations",
        f"jacobi = {jacobi_iterations}\ngauss_seidel = {gauss_seidel_iterations}\nsor = {sor_iterations[0]}",
    )
    save_data_to_file(results_dir_txt, "sor_iterations", w_with_iterations)

    print("Zapisywanie czasu obliczeń ...")
    save_data_to_file(
        results_dir_txt,
        "times",
        f"jacobi = {jacobi_time}\ngauss_seidel = {gauss_seidel_time}\nsor = {sor_times[0]}",
    )
    save_data_to_file(results_dir_txt, "sor_times", w_with_times)

    print("Zapisywanie błędów ...")
    save_data_to_file(
        results_dir_txt,
        "errors",
        f"jacobi = {jacobi_errors}\ngauss_seidel = {gauss_seidel_errors}\nsor = {sor_errors[0]}",
    )
    save_data_to_file(results_dir_txt, "sor_errors", w_with_errors)

    print("Zapisywanie szczegółowych wyników ...")
    save_matrix_to_file(results_dir_txt_solution, "jacobi", jacobi_solution)
    save_matrix_to_file(results_dir_txt_solution, "gauss_seidel", gauss_seidel_solution)
    save_matrix_to_file(results_dir_txt_solution, "sor", sor_solutions[0])

    # --------------------------------------------------- Sekcja tworzenia wykresów -------------------------------------------------- #

    print("Rysowanie wykresu liczby wyk. iteracji dla wszystkich metod ...")
    draw_iterations_to_methods(jacobi_iterations, gauss_seidel_iterations, sor_iterations[0])
    save_chart_to_file(results_dir_img, "iterations")

    print("Rysowanie wykresu czasu obliczeń dla wszystkich metod...")
    draw_times_to_methods(jacobi_time, gauss_seidel_time, sor_times[0])
    save_chart_to_file(results_dir_img, "times")

    print("Rysowanie wykresu liczby wyk. iteracji tylko dla metody SOR ...")
    draw_iterations_to_SOR_only(sor_iterations, ws)
    save_chart_to_file(results_dir_img, "sor_iterations")

    print("Rysowanie wykresu czasu obliczeń tylko dla metody SOR...")
    draw_times_to_SOR_only(sor_times, ws)
    save_chart_to_file(results_dir_img, "sor_times")

    print("Rysowanie wykresu błędu agregowanego dla wszystkich metod...")
    draw_errors_to_iterations(jacobi_errors, gauss_seidel_errors, sor_errors[0])
    save_chart_to_file(results_dir_img, "errors")

    print("Rysowanie wykresu błędu agregowanego tylko dla metody SOR...")
    draw_errors_to_iterations_SOR_only(sor_errors, ws)
    save_chart_to_file(results_dir_img, "sor_errors")

    print(f"\nEksperyment {experiment_name} zakończony sukcesem!")
    print("#############################################################")
