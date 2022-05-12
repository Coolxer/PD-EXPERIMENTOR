# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą tworzenie grupowych eksperymentów grupowanych według typu macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.table import draw_table

from .basic_experiment import do_basic_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_sizes import (
    draw_iterations_to_sizes,
    draw_times_to_sizes,
)
from .charts.iterations_or_times_to_sizes_SOR_only import (
    draw_iterations_to_sizes_SOR_only,
    draw_times_to_sizes_SOR_only,
)
from .charts.defines import *


"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - sizes(list)  - lista rozmiarów URL
        - matrix_type (str) - typ macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność przybliżonego rozwiązania
        - w_values (list) - lista wartości parametru 'w' do przetestowania
"""

# Metoda wykonuje doświadczenia ze zmiennym rozmiarem URL
def do_variable_size_experiment(
    experiment_name: str,
    sizes: list,
    matrix_type: str,
    max_iterations: int,
    tolerance: float,
    w_values: list,
) -> NoReturn:

    for size in sizes:
        do_basic_experiment(f"{experiment_name}/{size}", size, matrix_type, max_iterations, tolerance, w_values)

    exp_dir = f"{get_data_dir()}/{experiment_name}"

    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienny rozmiar URL\nrozmiar URL = {sizes}\ntyp macierzy = {matrix_type}\nmaksymalna liczba iteracji =  {max_iterations}\ndokładność = {tolerance}\nw = {w_values}\n"
    save_data_to_file(exp_dir, "description", experiment_description)

    (
        ws,
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
        sor_iterations_only,
        jacobi_times,
        gauss_seidel_times,
        sor_times,
        sor_times_only,
    ) = do_group_experiment(exp_dir, "type")

    # Utworzenie katalogów do przechowywania figur, wykresów i tabel
    os.mkdir(f"{exp_dir}/#res#")
    os.mkdir(f"{exp_dir}/#res#/svg")
    os.mkdir(f"{exp_dir}/#res#/fig")
    os.mkdir(f"{exp_dir}/#res#/tab")

    # Rysowanie wykresów
    draw_iterations_to_sizes(jacobi_iterations, gauss_seidel_iterations, sor_iterations, sizes)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations")

    draw_times_to_sizes(jacobi_times, gauss_seidel_times, sor_times, sizes)
    save_chart_to_file(f"{exp_dir}/#res#", "times")

    draw_iterations_to_sizes_SOR_only(sor_iterations_only, sizes, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations_SOR_only")

    draw_times_to_sizes_SOR_only(sor_times_only, sizes, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "times_SOR_only")

    # Tworzenie tabel
    draw_table(
        f"{exp_dir}/#res#/tab/iterations",
        DATA_LABELS_METHODS,
        sizes,
        [jacobi_iterations, gauss_seidel_iterations, sor_iterations],
    )

    draw_table(
        f"{exp_dir}/#res#/tab/times",
        DATA_LABELS_METHODS,
        sizes,
        [jacobi_times, gauss_seidel_times, sor_times],
    )

    draw_table(f"{exp_dir}/#res#/tab/iterations_SOR_only", ws, sizes, sor_iterations_only)

    draw_table(f"{exp_dir}/#res#/tab/times_SOR_only", ws, sizes, sor_times_only)
