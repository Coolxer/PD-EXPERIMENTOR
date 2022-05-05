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


def draw_iterations_or_times_to_methods(
    indicator: str, jacobi_data: int or float, gauss_seidel_data: int or float, sor_data: int or float
) -> NoReturn:
    plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_METHOD, weight="bold")

    maximum = max(jacobi_data, gauss_seidel_data, sor_data)
    step = ceil(maximum / NUMBER_OF_TICKS) if indicator == Y_ITERATIONS_INDICATOR else (maximum / NUMBER_OF_TICKS)
    yticks = np.arange(0, ceil(maximum + step), step)
    plt.yticks(yticks)

    if indicator == Y_TIMES_INDICATOR:
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    data = [jacobi_data, gauss_seidel_data, sor_data]
    bars = plt.bar(DATA_LABELS_METHODS, data, width=BAR_WIDTH_IN_SINGLE_SERIE)

    i = 0
    for bar in bars:
        bar.set_color(COLORS_ITERATIONS_METHODS[i] if indicator == Y_ITERATIONS_INDICATOR else COLORS_TIMES_METHODS[i])

        if SHOW_SIGNATURES:
            plt.annotate(
                int(bar.get_height())
                if indicator == Y_ITERATIONS_INDICATOR
                else format(round(bar.get_height(), TIME_PRECISION), f".{TIME_PRECISION}f"),
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha="center",
                va="center",
                size=10,
                xytext=(0, 4),
                textcoords="offset points",
            )

        i = i + 1

    if SHOW_GRID:
        plt.grid()


def draw_iterations_to_methods(
    jacobi_iterations: int,
    gauss_seidel_iterations: int,
    sor_iterations: int,
) -> NoReturn:

    draw_iterations_or_times_to_methods(
        Y_ITERATIONS_INDICATOR, jacobi_iterations, gauss_seidel_iterations, sor_iterations
    )


def draw_times_to_methods(
    jacobi_time: float,
    gauss_seidel_time: float,
    sor_time: float,
) -> NoReturn:

    draw_iterations_or_times_to_methods(Y_TIMES_INDICATOR, jacobi_time, gauss_seidel_time, sor_time)
