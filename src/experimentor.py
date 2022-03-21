# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawieraja całą funkcjonalność środowiska doświadczalnego

# ------------------------------------------------------------- Sekcja importu ------------------------------------------------------------- #

# Import modułów generalnych
import os
import shutil
from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt

# Import funkcji pomocnicznych
from .help_methods.file import save_data_to_file, save_matrix_to_file
from .help_methods.chart import draw_chart
from .help_methods.sor_exp import sor_exp

# Import elementów związanych z macierzami
from .help_methods.matrix import get_matrix

# Import metod z podmodułu @equiter
from ..equiter.src.jacobi.method import jacobi
from ..equiter.src.gauss_seidel.method import gauss_seidel

from .help_methods.vector import get_vector

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Metoda służąca do prowadzenia eksperymentów z biblioteką equiter
"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu
        - matrix_type (str) - typ macierzy głównej
        - matrix_size (int) - rozmiar macierzy głównej (liczba wierszy / kolumn)
"""


def do_experiment(experiment_name: str, matrix_type: str, matrix_size: int) -> NoReturn:

    # Uzyskanie katalogu wykonawczego
    exec_dir = os.path.dirname(os.path.abspath(__file__))

    # --------------------------------------------------------- Sekcja konfiguracji -------------------------------------------------------- #

    # Pobranie macierzy wejściowej układu
    A = get_matrix(matrix_type, matrix_size)

    # Ustawienie wektora wyrazów wolnych
    b = get_vector(f"{exec_dir}/exp_results/b_{matrix_size}.txt", matrix_size)

    # Pozostałe parametry metod (w używane tylko w metodzie SOR)
    # Przyjęto kilka wartości w, ostatecznie zostanie przyjęta tylko wartość, dla której uzyskano najlepszy rezultat
    tolerance = 0.000001
    max_iterations = 10000
    w_vector = [1.1, 1.3, 1.5, 1.7, 1.9]

    # ------------------------------------------------------- Sekcja rozwiązywania ------------------------------------------------------- #

    print("Trwa rozwiazywanie ukladu metoda Jacobiego ...")
    jacobi_solution, jacobi_iterations, jacobi_time = jacobi(A, b, max_iterations, tolerance)

    if jacobi_solution is None:
        return

    print("Trwa rozwiazywanie ukladu metoda Gaussa-Seidela ...")
    gauss_seidel_solution, gauss_seidel_iterations, gauss_seidel_time = gauss_seidel(A, b, max_iterations, tolerance)

    if gauss_seidel_solution is None:
        return

    print("Trwa rozwiazywanie ukladu metoda SOR ...")
    sor_solution, sor_iterations, sor_time = sor_exp(A, b, max_iterations, tolerance, w_vector)

    if sor_solution is None:
        return

    # -------------------------------------------------- Sekcja tworzenia katalogów -------------------------------------------------- #

    # Sprawdzenie czy istnieje katalog dla eksperymentów => jeśli nie to zostanie utworzony (exp_results)
    general_exp_dir = f"{exec_dir}/exp_results"
    if not os.path.exists(general_exp_dir):
        os.mkdir(general_exp_dir)

    # Tworzenie katalogu głównego dla konkretnego badania
    this_exp_dir = f"{general_exp_dir}/{experiment_name}"
    if os.path.exists(this_exp_dir):
        shutil.rmtree(this_exp_dir)
    os.mkdir(this_exp_dir)

    # Tworzenie katalogu konfiguracyjnego (A, b, tolerance, max_iterations)
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

    # ---------------------------------------------------- Sekcja zapisu parametrów --------------------------------------------------- #

    print("Zapisywanie generalnych informacji o eksperymencie")
    save_data_to_file(config_dir, "general", f"name = {experiment_name}\ntype = {matrix_type}\nsize = {matrix_size}")

    print("Zapisywanie macierzy A ...")
    save_matrix_to_file(config_dir, "A", A)

    # wektor b został juz zapisany w pliku b.txt

    print("Zapisywanie pozostalych parametrow (tolerancji, maks. liczby iteracji) ...")
    save_data_to_file(
        config_dir, "parameters", f"tolerance = {tolerance}\nmax_iterations = {max_iterations}\nw = {w_vector}"
    )

    # ------------------------------------------------------- Sekcja zapisu wyników ------------------------------------------------------ #

    print("Zapisywanie rezultatow według wskaznika liczby wyk. iteracji ...")
    save_data_to_file(
        results_dir_txt,
        "iterations",
        f"jacobi = {jacobi_iterations}\ngauss_seidel = {gauss_seidel_iterations}\nsor = {sor_iterations}",
    )

    print("Zapisywanie rezultatow według wskaznika czasu obliczeń ...")
    save_data_to_file(
        results_dir_txt,
        "times",
        f"jacobi = {jacobi_time}\ngauss_seidel = {gauss_seidel_time}\nsor = {sor_time}",
    )

    print("Zapisywanie szczegółowych wyników ...")
    save_matrix_to_file(results_dir_txt_solution, "jacobi", jacobi_solution)
    save_matrix_to_file(results_dir_txt_solution, "gauss_seidel", gauss_seidel_solution)
    save_matrix_to_file(results_dir_txt_solution, "sor", sor_solution)

    # --------------------------------------------------- Sekcja tworzenia wykresów -------------------------------------------------- #

    print("Generowanie wykresu zbieznosci wedlug wskaznika liczby wyk. iteracji ...")
    draw_chart(
        results_dir_img,
        "iterations",
        "Wykres liczby wykonanych iteracji",
        "liczba iteracji",
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
    )

    print("Generowanie wykresu zbieznosci wedlug wskaznika czasu obliczen ...")
    draw_chart(
        results_dir_img,
        "czas obliczeń [s]",
        "Wykres czasu obliczeń",
        "times",
        np.around(jacobi_time, 4),
        np.around(gauss_seidel_time, 4),
        np.around(sor_time, 4),
    )

    # Wyświetlenie wykresów
    plt.show()

    # Zamknięcie okień graficznych
    plt.close("all")


# -------------------------------------------------------------------------------------------------------------------------------------------------- #
