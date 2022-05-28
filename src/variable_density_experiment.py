# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą tworzenie grupowych eksperymentów grupowanych według poziomu wypełnienia macierzy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.table import draw_table

from .basic_experiment import do_basic_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_densities import (
    draw_iterations_to_densities,
    draw_times_to_densities,
)
from .charts.defines import *


"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - size (int) - rozmiar URL
        - matrix_type (str) - typ macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność przybliżonego rozwiązania
        - w_values (list) - lista wartości parametru 'w' do przetestowania
         densities(list)  - lista rozmiarów URL
"""

# Metoda wykonuje doświadczenia ze zmiennym poziomem wypełnienia macierzy
def do_variable_density_experiment(
    experiment_name: str,
    size: int,
    matrix_type: str,
    max_iterations: int,
    tolerance: float,
    w_values: list,
    densities: list,
) -> NoReturn:

    for density in densities:
        do_basic_experiment(
            f"{experiment_name}/{density}",
            size,
            matrix_type,
            max_iterations,
            tolerance,
            w_values,
            sparse_density=density,
        )

    exp_dir = f"{get_data_dir()}/{experiment_name}"

    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienny poziom wypelnienia\nrozmiar URL = {size}\ntyp macierzy = {matrix_type}\nmaksymalna liczba iteracji =  {max_iterations}\ndokładność = {tolerance}\nw = {w_values}\n"
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
    ) = do_group_experiment(exp_dir, "density")

    # Utworzenie katalogów do przechowywania figur, wykresów i tabel
    os.mkdir(f"{exp_dir}/#res#")
    os.mkdir(f"{exp_dir}/#res#/fig")
    os.mkdir(f"{exp_dir}/#res#/png")
    os.mkdir(f"{exp_dir}/#res#/svg")
    os.mkdir(f"{exp_dir}/#res#/pdf")
    os.mkdir(f"{exp_dir}/#res#/tab")

    # Rysowanie wykresów
    draw_iterations_to_densities(jacobi_iterations, gauss_seidel_iterations, sor_iterations, densities)
    save_chart_to_file(f"{exp_dir}/#res#", "iterations")

    draw_times_to_densities(jacobi_times, gauss_seidel_times, sor_times, densities)
    save_chart_to_file(f"{exp_dir}/#res#", "times")

    # Tworzenie tabel
    draw_table(
        f"{exp_dir}/#res#/tab/iterations",
        DATA_LABELS_METHODS,
        densities,
        [jacobi_iterations, gauss_seidel_iterations, sor_iterations],
    )

    draw_table(
        f"{exp_dir}/#res#/tab/times",
        DATA_LABELS_METHODS,
        densities,
        [jacobi_times, gauss_seidel_times, sor_times],
    )
