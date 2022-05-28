# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę rysującą wykres

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from math import ceil
from typing import NoReturn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from .defines import *


def draw_errors_to_iterations_SOR_only(sor_errors: list, ws: list) -> NoReturn:

    plt.figure()
    plt.ylabel(Y_LABEL_ERROR, weight="bold")
    plt.xlabel(X_LABEL_ITERATIONS, weight="bold")

    maximum_x = max(len(n) for n in sor_errors)
    step_x = ceil(maximum_x / NUMBER_OF_TICKS)
    xticks = np.arange(0, ceil(maximum_x + step_x), step_x)
    plt.xticks(xticks)

    maximum_y = max(max(n) for n in sor_errors)
    step_y = maximum_y / NUMBER_OF_TICKS
    yticks = np.arange(0, ceil(maximum_y + step_y), step_y)
    plt.yticks(yticks)

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.4f}"))

    i = 0
    for row in sor_errors:
        iterations = list(range(0, len(row)))

        plt.semilogy(
            iterations,
            row,
            linestyle="solid",
            linewidth=2,
            color=COLORS_ERRORS_W[i],
            label=f"ω = {ws[i]}",
        )

        i = i + 1

    plt.legend()

    if SHOW_GRID:
        plt.grid()
