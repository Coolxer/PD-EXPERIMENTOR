# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę służącą do prowadzenia pojedynczych eksperymentów

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import modułów generalnych
import os
import shutil
from typing import NoReturn
import matplotlib.pyplot as plt

# Import funkcji pomocniczych
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_matrix_to_file
from .help_methods.vector import get_vector
from .help_methods.sor_exp import sor_exp
from .help_methods.chart import draw_chart

# Import elementów związanych z macierzami
from .help_methods.matrix import get_matrix

# Import metod z podmodułu @equiter
from ..equiter.src.jacobi.method import jacobi
from ..equiter.src.gauss_seidel.method import gauss_seidel

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu
        - matrix_type (str) - typ macierzy głównej
        - matrix_size (int) - rozmiar macierzy głównej (liczba wierszy / kolumn)

        - tolerance (float) - dokładność przybliżonego rozwiązania
        - max_iterations (int) - maksymalna liczba iteracji
        - w_values (list) - lista wartości parametru 'w' do przetestowania
        - create_charts (bool) [True] - czy mają zostać utworzone wykresy graficzne (przydatne głównie do pojedynczych eksperymentów)
"""

# Metoda służąca do prowadzenia eksperymentów z biblioteką equiter
def do_single_experiment(
    experiment_name: str,
    matrix_type: str,
    matrix_size: int,
    tolerance: float,
    max_iterations: int,
    w_values: list,
    create_charts: bool = True,
) -> NoReturn:

    print("\n#############################################################")
    print(f"######### Eksperyment:  {experiment_name} ###########")

    # --------------------------------------------------------- Sekcja konfiguracji -------------------------------------------------------- #

    # Uzyskanie katalogu głównego eksperymentpw
    data_dir = get_data_dir()

    # Pobranie macierzy wejściowej układu
    print("Generowanie macierzy głównej ...")
    A = get_matrix(matrix_type, matrix_size)

    # Ustawienie wektora wyrazów wolnych
    print("Generowanie / Wczytywanie wektora wyrazów wolnych ...")
    b, was_b_loaded = get_vector(f"{data_dir}/b_{matrix_size}.txt", matrix_size)

    # ------------------------------------------------------- Sekcja rozwiązywania ------------------------------------------------------- #

    print("Rozwiązywanie układu metodą Jacobiego ...")
    jacobi_solution, jacobi_iterations, jacobi_time = jacobi(A, b, max_iterations, tolerance)

    if jacobi_solution is None:
        return

    print("Rozwiązywanie układu metodą Gaussa-Seidela ...")
    gauss_seidel_solution, gauss_seidel_iterations, gauss_seidel_time = gauss_seidel(A, b, max_iterations, tolerance)

    if gauss_seidel_solution is None:
        return

    print("Rozwiązywanie układu metodą SOR ...")
    sor_solution, sor_iterations, sor_time = sor_exp(A, b, max_iterations, tolerance, w_values)

    if sor_solution is None:
        return

    # -------------------------------------------------- Sekcja tworzenia katalogów -------------------------------------------------- #

    # Tworzenie katalogu głównego dla konkretnego badania
    this_exp_dir = f"{data_dir}/{experiment_name}"
    if os.path.exists(this_exp_dir):
        shutil.rmtree(this_exp_dir)
    os.makedirs(this_exp_dir)

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
    if create_charts:
        results_dir_img = f"{results_dir}/img"
        os.mkdir(results_dir_img)

    # ---------------------------------------------------- Sekcja zapisu parametrów --------------------------------------------------- #

    print("Zapisywanie generalnych informacji o eksperymencie ...")
    save_data_to_file(
        config_dir,
        "general",
        f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = single\ntyp macierzy A =  {matrix_type}\nrozmiar macierzy A = {matrix_size}",
    )

    print("Zapisywanie macierzy głównej ...")
    save_matrix_to_file(config_dir, "A", A)

    # Sprawdzenie czy wektor b został wczytany czy wygenerowany
    # Jeśli wektor został wygenerowany to należy go zapisać do pliku
    if not was_b_loaded:
        print("Zapisywanie wektora wyrazów wolnych ...")
        save_matrix_to_file(f"{data_dir}", f"b_{matrix_size}", b)

    print("Zapisywanie pozostałych parametrów (tolerancji, maks. liczby iteracji) ...")
    save_data_to_file(
        config_dir,
        "parameters",
        f"dokładność = {tolerance}\nmaksymalna liczba iteracji = {max_iterations}\nw = {w_values}",
    )

    # ------------------------------------------------------- Sekcja zapisu wyników ------------------------------------------------------ #

    print("Zapisywanie rezultatów według wskaźnika liczby wyk. iteracji ...")
    save_data_to_file(
        results_dir_txt,
        "iterations",
        f"jacobi = {jacobi_iterations}\ngauss_seidel = {gauss_seidel_iterations}\nsor = {sor_iterations}",
    )

    print("Zapisywanie rezultatów według wskaźnika czasu obliczeń ...")
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

    if not create_charts:
        print(f"\nEksperyment {experiment_name} zakończony sukcesem!")
        print("\n#############################################################")
        return

    print("Generowanie wykresu zbieżności według wskaźnika liczby wyk. iteracji ...")
    draw_chart(
        "bar",
        "Wykres liczby wykonanych iteracji",
        "metoda",
        "liczba iteracji [szt.]",
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
        0,
    )
    # Zapisanie wykresu iteracji
    plt.savefig(f"{results_dir_img}/iterations.png")

    print("Generowanie wykresu zbieżności według wskaźnika czasu obliczeń ...")
    draw_chart(
        "bar", "Wykres czasu obliczeń", "metoda", "czas obliczeń [s]", jacobi_time, gauss_seidel_time, sor_time, 6
    )
    # Zapisanie wykresu czasu
    plt.savefig(f"{results_dir_img}/times.png")

    # Zamknięcie okień graficznych
    plt.close("all")

    print(f"\nEksperyment {experiment_name} zakończony sukcesem!")
    print("#############################################################")
