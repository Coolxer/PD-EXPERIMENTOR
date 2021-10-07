import os
from scipy.io import loadmat
from tkinter.filedialog import askopenfilename

from .diagonal_amplifier import strengthen_diagonal

# metoda służy do wykorzystania macierzy rzadkiej pobranej z kolekcji https://sparse.tamu.edu/
# macierz jest dodatkowo wzmocniona, aby warunek zbieżności konieczny dla przybliżonych metod stacjonarnych był spełniony
def external_matrix(file):

    file = askopenfilename(
        filetypes=(("Matlab files", "mat"),),
        title="Wybierz macierz pobraną z kolekcji macierzy rzadkich",
    )

    # load matlab file
    data = loadmat(file)

    for item in data["Problem"].item(0):
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            break

    # get matrix
    matrix = item.toarray()

    # diagonal strengthening
    matrix = strengthen_diagonal(matrix, 0.1)

    return matrix
