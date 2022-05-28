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

    maximum = max(sor_data)
    step = ceil(maximum / NUMBER_OF_TICKS) if indicator == Y_ITERATIONS_INDICATOR else (maximum / NUMBER_OF_TICKS)
    yticks = np.arange(0, ceil(maximum + step), step)
    plt.yticks(yticks)

    if indicator == Y_TIMES_INDICATOR:
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    plt.plot(
        ws,
        sor_data,
        linestyle="solid",
        color=COLORS_ITERATIONS_METHODS[1] if indicator == Y_ITERATIONS_INDICATOR else COLORS_TIMES_METHODS[1],
    )

    if SHOW_GRID:
        plt.grid()


def draw_iterations_to_SOR_only(sor_iterations: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_SOR_only(Y_ITERATIONS_INDICATOR, sor_iterations, ws)


def draw_times_to_SOR_only(sor_times: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_SOR_only(Y_TIMES_INDICATOR, sor_times, ws)
