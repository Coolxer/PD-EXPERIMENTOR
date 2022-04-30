# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metody rysujące wykresy

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

import math
from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt
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

    if indicator == Y_ITERATIONS_INDICATOR:
        yticks = range(0, max(max(n) for n in sor_data))
        yticks = range(min(yticks), math.ceil(max(yticks)) + 1)
        plt.yticks(yticks)

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
