# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metody rysujące wykresy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from typing import NoReturn
import matplotlib.pyplot as plt
from .defines import *


def draw_iterations_or_times_to_SOR_only(indicator: str, sor_data: list, ws: list) -> NoReturn:

    plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_W_PARAMETER, weight="bold")
    plt.xticks(ws)

    bars = plt.bar(ws, sor_data, width=BAR_WIDTH_IN_MULTIPLE_SERIES)

    i = 0
    for bar in bars:
        bar.set_color(W_COLORS[i])

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


def draw_iterations_to_SOR_only(sor_iterations: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_SOR_only(Y_ITERATIONS_INDICATOR, sor_iterations, ws)


def draw_times_to_SOR_only(sor_times: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_SOR_only(Y_TIMES_INDICATOR, sor_times, ws)
