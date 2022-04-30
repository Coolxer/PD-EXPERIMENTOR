# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą badanie wpływu wartości parametru tolerancji na wyniki doświadczeń

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file

from .single_experiment import do_single_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_tolerances import draw_iterations_to_tolerances, draw_times_to_tolerances
from .charts.iterations_or_times_to_tolerances_SOR_only import (
    draw_iterations_to_tolerances_SOR_only,
    draw_times_to_tolerances_SOR_only,
)

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - matrix_type (str) - typ macierzy głównej
        - matrix_order (int) - stopień macierzy głównej

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerances (list) - lista dokładności w doświadczeniu
        - w_values (list) - lista wartości parametru 'w' do przetestowania
"""


def do_tolerance_experiment(
    experiment_name: str, matrix_type: str, matrix_order: int, max_iterations: int, tolerances: list, w_values: list
) -> NoReturn:

    for tolerance in tolerances:
        do_single_experiment(
            f"{experiment_name}/{tolerance}", matrix_type, matrix_order, max_iterations, tolerance, w_values
        )

    exp_dir = f"{get_data_dir()}/{experiment_name}"
    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = zmienna tolerancja\ntyp macierzy A = {matrix_type}\nstopień macierzy A = {matrix_order}\nmaksymalna liczba iteracji = {max_iterations}\nbadane wartości parametru 'w'  = {w_values}\nbadane dokładności = {tolerances}"

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

    draw_iterations_to_tolerances(jacobi_iterations, gauss_seidel_iterations, sor_iterations, tolerances)
    save_chart_to_file(f"{exp_dir}/tolerance_iterations.png")

    draw_times_to_tolerances(jacobi_times, gauss_seidel_times, sor_times, tolerances)
    save_chart_to_file(f"{exp_dir}/tolerance_times.png")

    draw_iterations_to_tolerances_SOR_only(sor_iterations_only, tolerances, ws)
    save_chart_to_file(f"{exp_dir}/tolerance_iterations_SOR_only.png")

    draw_times_to_tolerances_SOR_only(sor_times_only, tolerances, ws)
    save_chart_to_file(f"{exp_dir}/tolerance_times_SOR_only.png")
