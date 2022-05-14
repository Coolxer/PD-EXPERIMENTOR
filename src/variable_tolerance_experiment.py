# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą badanie wpływu wartości parametru tolerancji na wyniki doświadczeń

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

import os
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.table import draw_table

from .basic_experiment import do_basic_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_tolerances import draw_iterations_to_tolerances, draw_times_to_tolerances
from .charts.iterations_or_times_to_tolerances_SOR_only import (
    draw_iterations_to_tolerances_SOR_only,
    draw_times_to_tolerances_SOR_only,
)
from .charts.defines import *

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - size (int) - rozmiar URL
        - matrix_type (str) - typ macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerances (list) - lista dokładności w doświadczeniu
        - w_values (list) - lista wartości parametru 'w' do przetestowania
"""


def do_variable_tolerance_experiment(
    experiment_name: str, size: int, matrix_type: str, max_iterations: int, tolerances: list, w_values: list
) -> NoReturn:

    for tolerance in tolerances:
        do_basic_experiment(
            f"{experiment_name}/{tolerance}", size, matrix_type, max_iterations, float(tolerance), w_values
        )

    exp_dir = f"{get_data_dir()}/{experiment_name}"
    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienna tolerancja\nrozmiar URL = {size}\ntyp macierzy = {matrix_type}\nmaksymalna liczba iteracji = {max_iterations}\ndokładność= {tolerances}\nw = {w_values}\n"

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
    ) = do_group_experiment(exp_dir, "tolerance")

    # Utworzenie katalogów do przechowywania figur, wykresów i tabel
    os.mkdir(f"{exp_dir}/#res#")
    os.mkdir(f"{exp_dir}/#res#/eps")
    os.mkdir(f"{exp_dir}/#res#/fig")
    os.mkdir(f"{exp_dir}/#res#/tab")

    # Rysowanie wykresów
    draw_iterations_to_tolerances(jacobi_iterations, gauss_seidel_iterations, sor_iterations, tolerances)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations")

    draw_times_to_tolerances(jacobi_times, gauss_seidel_times, sor_times, tolerances)
    save_chart_to_file(f"{exp_dir}/#res#", "times")

    draw_iterations_to_tolerances_SOR_only(sor_iterations_only, tolerances, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations_SOR_only")

    draw_times_to_tolerances_SOR_only(sor_times_only, tolerances, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "times_SOR_only")

    # Tworzenie tabel
    draw_table(
        f"{exp_dir}/#res#/tab/iterations",
        DATA_LABELS_METHODS,
        tolerances,
        [jacobi_iterations, gauss_seidel_iterations, sor_iterations],
    )

    draw_table(
        f"{exp_dir}/#res#/tab/times",
        DATA_LABELS_METHODS,
        tolerances,
        [jacobi_times, gauss_seidel_times, sor_times],
    )

    draw_table(f"{exp_dir}/#res#/tab/iterations_SOR_only", ws, tolerances, sor_iterations_only)

    draw_table(f"{exp_dir}/#res#/tab/times_SOR_only", ws, tolerances, sor_times_only)
