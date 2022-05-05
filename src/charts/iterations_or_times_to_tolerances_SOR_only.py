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


def draw_iterations_or_times_to_tolerances_SOR_only(
    indicator: str, sor_data: list, tolerances: list, ws: list
) -> NoReturn:

    plt.figure()
    plt.ylabel(
        Y_LABEL_ITERATIONS if indicator == Y_ITERATIONS_INDICATOR else Y_LABEL_TIMES,
        weight="bold",
    )
    plt.xlabel(X_LABEL_TOLERANCE, weight="bold")
    plt.xticks([r + BAR_WIDTH_IN_MULTIPLE_SERIES for r in range(len(tolerances))], tolerances)

    maximum = max(max(n) for n in sor_data)
    step = ceil(maximum / NUMBER_OF_TICKS) if indicator == Y_ITERATIONS_INDICATOR else (maximum / NUMBER_OF_TICKS)
    yticks = np.arange(0, ceil(maximum + step), step)
    plt.yticks(yticks)

    if indicator == Y_TIMES_INDICATOR:
        plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    positions = np.arange(len(tolerances))

    i = 0
    for w in ws:
        plt.bar(
            positions,
            sor_data[i],
            color=COLORS_ITERATIONS_W[i] if indicator == Y_ITERATIONS_INDICATOR else COLORS_TIMES_W[i],
            width=BAR_WIDTH_IN_MULTIPLE_SERIES,
            label=f"ω = {w}",
        )

        positions = [x + BAR_WIDTH_IN_MULTIPLE_SERIES for x in positions]
        i = i + 1

    plt.legend()

    if SHOW_GRID:
        plt.grid()


def draw_iterations_to_tolerances_SOR_only(sor_iterations: list, tolerances: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_tolerances_SOR_only(Y_ITERATIONS_INDICATOR, sor_iterations, tolerances, ws)


def draw_times_to_tolerances_SOR_only(sor_times: list, tolerances: list, ws: list) -> NoReturn:
    draw_iterations_or_times_to_tolerances_SOR_only(Y_TIMES_INDICATOR, sor_times, tolerances, ws)
