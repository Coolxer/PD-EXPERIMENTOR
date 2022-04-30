# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę rysującą wykres

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from typing import NoReturn
import matplotlib.pyplot as plt
from .defines import *


def draw_errors_to_iterations_SOR_only(sor_errors: list, ws: list) -> NoReturn:

    plt.figure()
    plt.ylabel(Y_LABEL_ERROR, weight="bold")
    plt.xlabel(X_LABEL_ITERATIONS, weight="bold")

    lengths = list(map(lambda n: len(n), sor_errors))
    plt.xticks(range(0, max(lengths)))  # tutaj musi to być trochę inaczej zrobione, bo jest za dużo elementów

    i = 0
    for row in sor_errors:
        iterations = list(range(0, len(row)))

        plt.plot(
            iterations,
            row,
            linestyle="solid",
            color=W_COLORS[i],
            label=f"ω = {ws[i]}",
        )

        i = i + 1

    plt.legend()

    if SHOW_GRID:
        plt.grid()
