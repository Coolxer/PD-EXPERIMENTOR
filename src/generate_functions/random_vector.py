import numpy as np
import os

from ..help_functions.file import saveNormalDataToFile, saveMatrixToFile

# metoda geneuje wektor o podanym rozmiarze i zapisuje go do pliku
def random_vector(n):
    print("Generowanie wektora wyrazów wolnych ...")
    v = np.random.rand(n)

    print("Zapis wektora wyrazów wolnych do pliku ...")
    saveMatrixToFile(
        f"{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/exp_results",
        f"b_{n}",
        v,
    )
    return v
