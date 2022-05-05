# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metody rysujące wykresy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from math import ceil
from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from .defines import *


def draw_iterations_or_times_to_tolerances(
    indicator: str, jacobi_data: list, gauss_seidel_data: list, sor_data: list, tolerances: list
) -> NoReturn:

    plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_TOLERANCE, weight="bold")
    plt.xticks([r + BAR_WIDTH_IN_MULTIPLE_SERIES for r in range(len(tolerances))], tolerances)

    maximum = max(max(jacobi_data), max(gauss_seidel_data), max(sor_data))
    step = ceil(maximum / NUMBER_OF_TICKS) if indicator == Y_ITERATIONS_INDICATOR else (maximum / NUMBER_OF_TICKS)
    yticks = np.arange(0, ceil(maximum + step), step)
    plt.yticks(yticks)

    if indicator == Y_TIMES_INDICATOR:
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    data = [jacobi_data, gauss_seidel_data, sor_data]
    positions = np.arange(len(tolerances))

    i = 0
    for method in DATA_LABELS_METHODS:
        plt.bar(
            positions,
            data[i],
            color=COLORS_ITERATIONS_METHODS[i] if indicator == Y_ITERATIONS_INDICATOR else COLORS_TIMES_METHODS[i],
            width=BAR_WIDTH_IN_MULTIPLE_SERIES,
            label=method,
        )

        positions = [x + BAR_WIDTH_IN_MULTIPLE_SERIES for x in positions]

        i = i + 1

    plt.legend()

    if SHOW_GRID:
        plt.grid()


def draw_iterations_to_tolerances(
    jacobi_iterations: list, gauss_seidel_iterations: list, sor_iterations: list, tolerances: list
) -> NoReturn:
    draw_iterations_or_times_to_tolerances(
        Y_ITERATIONS_INDICATOR, jacobi_iterations, gauss_seidel_iterations, sor_iterations, tolerances
    )


def draw_times_to_tolerances(
    jacobi_times: list, gauss_seidel_times: list, sor_times: list, tolerances: list
) -> NoReturn:
    draw_iterations_or_times_to_tolerances(Y_TIMES_INDICATOR, jacobi_times, gauss_seidel_times, sor_times, tolerances)
