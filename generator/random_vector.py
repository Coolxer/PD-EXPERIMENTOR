import numpy as np
import os

from src.exp_help_functions.file import saveNormalDataToFile, saveMatrixToFile


def random_vector(n):
    v = np.random.rand(n)
    saveMatrixToFile(f'{os.getcwd()}/src/exp', f'b_{n}', v)
    return v
