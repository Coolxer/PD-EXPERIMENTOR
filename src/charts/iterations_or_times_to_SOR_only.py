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


def draw_iterations_or_times_to_SOR_only(indicator: str, sor_data: list, ws: list) -> NoReturn:

    plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_W_PARAMETER, weight="bold")
    plt.xticks(ws)

    maximum = max(sor_data)
    step = ceil(maximum / NUMBER_OF_TICKS) if indicator == Y_ITERATIONS_INDICATOR else (maximum / NUMBER_OF_TICKS)
    yticks = np.arange(0, ceil(maximum + step), step)
    plt.yticks(yticks)

    if indicator == Y_TIMES_INDICATOR:
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    bars = plt.bar(ws, sor_data, width=BAR_WIDTH_IN_MULTIPLE_SERIES)

    i = 0
    for bar in bars:
        bar.set_color(COLORS_ITERATIONS_W[i] if indicator == Y_ITERATIONS_INDICATOR else COLORS_TIMES_W[i])

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
