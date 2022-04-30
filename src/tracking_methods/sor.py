# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zmodyfikowanej metody pochodzącej z https://github.com/Coolxer/PD-EQUITER-LIBRARY
# Modyfikacja polega na usunięciu komentarzy oraz dodaniu śledzenia wartości błędu

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

import time
from typing import Tuple
import numpy as np
from ...equiter.src.common import common


def sor(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    w: float,
    x0: np.ndarray = None,
) -> Tuple[np.ndarray, int, float, list]:

    start_time, x, valid = common(A, b, max_iterations, tolerance, x0, w)

    if not valid:
        return None, None, None

    D = np.diag(np.diag(A))

    L = np.tril(A) - D

    U = np.triu(A) - D

    D_plus_wL_inv = np.linalg.inv(D + (w * L))

    wb = w * b

    wU_plus_w_min_1_dot_D = (w * U) + ((w - 1) * D)

    errors = []

    for iteration in range(max_iterations):

        x_old = x.copy()

        x = np.dot(D_plus_wL_inv, (wb - np.dot(wU_plus_w_min_1_dot_D, x_old)))

        error = np.linalg.norm(np.dot(A, x) - b) / np.linalg.norm(b)
        errors.append(error)

        if error < tolerance:
            break

    elapsed_time = time.time() - start_time

    return x, iteration + 1, round(elapsed_time, 6), errors
