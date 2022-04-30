# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę rysujące wykresy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt
from .defines import *


def draw_iterations_or_times_to_types_grouped_by_order(
    indicator: str, jacobi_data: list, gauss_seidel_data: list, sor_data: list, types: list
) -> NoReturn:

    fig = plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_TYPE, weight="bold")
    plt.xticks([r + BAR_WIDTH_IN_MULTIPLE_SERIES for r in range(len(types))], types)

    data = [jacobi_data, gauss_seidel_data, sor_data]
    positions = np.arange(len(types))

    i = 0
    for method in DATA_LABELS_METHODS:
        plt.bar(
            positions,
            data[i],
            color=METHOD_COLORS[i],
            width=BAR_WIDTH_IN_MULTIPLE_SERIES,
            label=method,
        )

        positions = [x + BAR_WIDTH_IN_MULTIPLE_SERIES for x in positions]
        i = i + 1

    fig.autofmt_xdate()

    plt.legend()

    if SHOW_GRID:
        plt.grid()


def draw_iterations_to_types_grouped_by_order(
    jacobi_iterations: list, gauss_seidel_iterations: list, sor_iterations: list, types: list
) -> NoReturn:
    draw_iterations_or_times_to_types_grouped_by_order(
        Y_ITERATIONS_INDICATOR, jacobi_iterations, gauss_seidel_iterations, sor_iterations, types
    )


def draw_times_to_types_grouped_by_order(
    jacobi_times: list, gauss_seidel_times: list, sor_times: list, types: list
) -> NoReturn:
    draw_iterations_or_times_to_types_grouped_by_order(
        Y_TIMES_INDICATOR, jacobi_times, gauss_seidel_times, sor_times, types
    )
