# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę umożliwiającą tworzenie grupowych eksperymentów według stopnia

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file, save_chart_to_file
from .help_methods.translator import translate_matrix_names

from .single_experiment import do_single_experiment
from .help_methods.group_experiment import do_group_experiment

from .charts.iterations_or_times_to_types_grouped_by_order import (
    draw_iterations_to_types_grouped_by_order,
    draw_times_to_types_grouped_by_order,
)
from .charts.iterations_or_times_to_types_grouped_by_order_SOR_only import (
    draw_iterations_to_types_grouped_by_order_SOR_only,
    draw_times_to_types_grouped_by_order_SOR_only,
)

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - matrix_order (int) - stopień macierzy głównej
        - types (list) - lista typów macierzy w doświadczeniu

        - max_iterations (int) - maksymalna liczba iteracji
        - tolerance (float) - zadana dokładność przybliżonego rozwiązania
        - w_values (list) - lista wartości parametru 'w' do przetestowania
"""

# Metoda wykonuje grupowe doświadczenia obliczeniowe według stopnia
def do_group_by_order_experiment(
    experiment_name: str,
    matrix_order: int,
    types: list,
    max_iterations: int,
    tolerance: float,
    w_values: list,
) -> NoReturn:
    for type in types:
        do_single_experiment(f"{experiment_name}/{type}", type, matrix_order, max_iterations, tolerance, w_values)

    exp_dir = f"{get_data_dir()}/{experiment_name}"

    experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = grupowany według stopnia\nstopień macierzy A = {matrix_order}\nmaksymalna liczba iteracji =  {max_iterations}\nbadane wartości parametru 'w' = {w_values}\nbadane typy macierzy = {types}"
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

    draw_iterations_to_types_grouped_by_order(jacobi_iterations, gauss_seidel_iterations, sor_iterations, types)
    save_chart_to_file(f"{exp_dir}/group_by_order_iterations.png")

    draw_times_to_types_grouped_by_order(jacobi_times, gauss_seidel_times, sor_times, types)
    save_chart_to_file(f"{exp_dir}/group_by_order_times.png")

    draw_iterations_to_types_grouped_by_order_SOR_only(sor_iterations_only, types, ws)
    save_chart_to_file(f"{exp_dir}/group_by_order_iterations_SOR_only.png")

    draw_times_to_types_grouped_by_order_SOR_only(sor_times_only, types, ws)
    save_chart_to_file(f"{exp_dir}/group_by_order_times_SOR_only.png")
