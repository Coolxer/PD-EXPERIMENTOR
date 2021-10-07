import numpy as np
import os

from ..help_functions.file import saveNormalDataToFile, saveMatrixToFile

# metoda geneuje wektor o podanym rozmiarze i zapisuje go do pliku
def random_vector(n):
    v = np.random.rand(n)
    saveMatrixToFile(f"{os.getcwd()}/src/exp", f"b_{n}", v)
    return v
