# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą badanie wpływu x0 na wyniki doświadczeńw

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

import os
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.table import draw_table

from .basic_experiment import do_basic_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_x0s import draw_iterations_to_x0s, draw_times_to_x0s
from .charts.iterations_or_times_to_x0s_SOR_only import (
    draw_iterations_to_x0s_SOR_only,
    draw_times_to_x0s_SOR_only,
)
from .charts.defines import *

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - size (int) - rozmiar URL
        - matrix_type (str) - typ macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - tolerancja
        - w_values (list) - lista wartości parametru 'w' do przetestowania
        - x0s (list) - lista wektorów x0
"""


def do_variable_x0_experiment(
    experiment_name: str,
    size: int,
    matrix_type: str,
    max_iterations: int,
    tolerance: float,
    w_values: list,
    x0s: list,
) -> NoReturn:

    x0_signatures = []

    for x0 in x0s:
        do_basic_experiment(f"{experiment_name}/{x0[0]}", size, matrix_type, max_iterations, tolerance, w_values, x0)
        x0_signatures.append(x0[0])

    exp_dir = f"{get_data_dir()}/{experiment_name}"
    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienny wektor x0\nrozmiar URL = {size}\ntyp macierzy = {matrix_type}\nmaksymalna liczba iteracji = {max_iterations}\ntolerancja = {tolerance}\nw  = {w_values}\nx0 = {x0_signatures}"

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

    # tutaj musze miec dedykowane wykresyf

    # Rysowanie wykresów
    draw_iterations_to_x0s(jacobi_iterations, gauss_seidel_iterations, sor_iterations, x0_signatures)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations")

    draw_times_to_x0s(jacobi_times, gauss_seidel_times, sor_times, x0_signatures)
    save_chart_to_file(f"{exp_dir}/#res#", "times")

    draw_iterations_to_x0s_SOR_only(sor_iterations_only, x0_signatures, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "terations_SOR_only")

    draw_times_to_x0s_SOR_only(sor_times_only, x0_signatures, ws)
    save_chart_to_file(f"{exp_dir}/#res#", "times_SOR_only")

    # Tworzenie tabel
    draw_table(
        f"{exp_dir}/#res#/tab/iterations",
        DATA_LABELS_METHODS,
        x0_signatures,
        [jacobi_iterations, gauss_seidel_iterations, sor_iterations],
    )

    draw_table(
        f"{exp_dir}/#res#/tab/times",
        DATA_LABELS_METHODS,
        x0_signatures,
        [jacobi_times, gauss_seidel_times, sor_times],
    )

    draw_table(f"{exp_dir}/#res#/tab/iterations_SOR_only", ws, x0_signatures, sor_iterations_only)

    draw_table(f"{exp_dir}/#res#/tab/times_SOR_only", ws, x0_signatures, sor_times_only)
