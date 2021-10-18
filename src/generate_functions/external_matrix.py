import os
from scipy.io import loadmat

from tkinter import *
from tkinter.filedialog import askopenfilename

from .diagonal_amplifier import strengthen_diagonal

# metoda służy do wykorzystania macierzy rzadkiej pobranej z kolekcji https://sparse.tamu.edu/
# macierz jest dodatkowo wzmocniona, aby warunek zbieżności konieczny dla przybliżonych metod stacjonarnych był spełniony
def external_matrix():

    # stworzenie instancji tk
    root = Tk()

    # ukrycie okna głównego
    root.withdraw()

    file = askopenfilename(
        filetypes=(("Matlab files", "mat"),),
        title="Wybierz macierz pobraną z kolekcji macierzy rzadkich",
    )

    # zniszenie instancji tk
    root.destroy()

    # załadowanie pliku matlab
    data = loadmat(file)

    for item in data["Problem"].item(0):
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            break

    # pobranie macierzy
    matrix = item.toarray()

    # wzmocnienie przekątnej macierzy
    matrix = strengthen_diagonal(matrix, 0.1)

    return matrix
