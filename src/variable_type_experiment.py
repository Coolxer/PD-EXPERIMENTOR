# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą tworzenie grupowych eksperymentów grupowanych według stopnia macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.table import draw_table
from .help_methods.translator import translate_matrix_names

from .basic_experiment import do_basic_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_types import (
    draw_iterations_to_types,
    draw_times_to_types,
)
from .charts.iterations_or_times_to_types_SOR_only import (
    draw_iterations_to_types_SOR_only,
    draw_times_to_types_SOR_only,
)
from .charts.defines import *

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - size (int) - rozmiar URL
        - types (list) - lista typów macierzy w doświadczeniu

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność przybliżonego rozwiązania
        - w_values (list) - lista wartości parametru 'w' do przetestowania
"""

# Metoda wykonuje grupowe doświadczenia obliczeniowe według stopnia
def do_variable_type_experiment(
    experiment_name: str,
    size: int,
    types: list,
    max_iterations: int,
    tolerance: float,
    w_values: list,
) -> NoReturn:
    for type in types:
        do_basic_experiment(f"{experiment_name}/{type}", size, type, max_iterations, tolerance, w_values)

    exp_dir = f"{get_data_dir()}/{experiment_name}"

    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienny typ macierzy\nrozmiar URL = {size}\ntyp macierzy = {types}\nmaksymalna liczba iteracji =  {max_iterations}\nw = {w_values}"
    save_data_to_file(f"{exp_dir}", "description", experiment_description)

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
    ) = do_group_experiment(exp_dir, "order")

    types = translate_matrix_names(types)

    # Utworzenie katalogów do przechowywania figur, wykresów i tabel
    os.mkdir(f"{exp_dir}/#res#")
    os.mkdir(f"{exp_dir}/#res#/eps")
    os.mkdir(f"{exp_dir}/#res#/fig")
    os.mkdir(f"{exp_dir}/#res#/tab")

    # Rysowanie wykresów
    draw_iterations_to_types(jacobi_iterations, gauss_seidel_iterations, sor_iterations, types)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations")

    draw_times_to_types(jacobi_times, gauss_seidel_times, sor_times, types)
    save_chart_to_file(f"{exp_dir}/#res#", "times")

    draw_iterations_to_types_SOR_only(sor_iterations_only, types, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations_SOR_only")

    draw_times_to_types_SOR_only(sor_times_only, types, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "times_SOR_only")

    # Tworzenie tabel
    draw_table(
        f"{exp_dir}/#res#/tab/iterations",
        DATA_LABELS_METHODS,
        types,
        [jacobi_iterations, gauss_seidel_iterations, sor_iterations],
    )

    draw_table(
        f"{exp_dir}/#res#/tab/times",
        DATA_LABELS_METHODS,
        types,
        [jacobi_times, gauss_seidel_times, sor_times],
    )

    draw_table(f"{exp_dir}/#res#/tab/iterations_SOR_only", ws, types, sor_iterations_only)

    draw_table(f"{exp_dir}/#res#/tab/times_SOR_only", ws, types, sor_times_only)
