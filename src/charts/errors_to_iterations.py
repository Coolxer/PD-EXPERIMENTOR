# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę rysującą wykres

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

from typing import NoReturn
import matplotlib.pyplot as plt
from .defines import *


def draw_errors_to_iterations(jacobi_errors: list, gauss_seidel_errors: list, sor_errors: list) -> NoReturn:

    plt.figure()
    plt.ylabel(Y_LABEL_ERROR, weight="bold")
    plt.xlabel(X_LABEL_ITERATIONS, weight="bold")
    plt.xticks(
        range(0, max(len(jacobi_errors), len(gauss_seidel_errors), len(sor_errors)))
    )  # tutaj musi to być trochę inaczej zrobione, bo jest za dużo elementów

    data = [jacobi_errors, gauss_seidel_errors, sor_errors]

    i = 0
    for row in data:
        iterations = list(range(0, len(row)))

        plt.plot(
            iterations,
            row,
            linestyle="solid",
            color=METHOD_COLORS[i],
            label=DATA_LABELS_METHODS[i],
        )

        i = i + 1

    plt.legend()

    if SHOW_GRID:
        plt.grid()
