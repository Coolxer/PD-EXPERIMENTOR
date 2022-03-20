# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę rysującą wykres porównujący zbieżność metod

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import matplotlib.pyplot as plt


# Metoda rysuje wykres porównujący zbieżność metod na podstawie liczby iteracji / czasu (indicator)

"""
    Wejście:
        - path - ścieżka zapisu
        - title - tytuł wyświetlanego wykresu
        - indicator - oznaczenie osi y
        - indicator_en - nazwa pliku wykresu
        - jacobi - wyniki doświadczeń metodą Jacobiego
        - gauss_seidel - wyniki doświadczeń metodą Gaussa-Seidela
        - sor - wyniki doświadczeń metodą SOR
        - show_signatures [default = False] - ewentualne wyświetlanie wartości poszczególnych kolumn
"""


def draw(path, title, indicator, indicator_en, jacobi, gauss_seidel, sor, show_signatures=False):

    # Utworzenie tablic metod i ich rezultatów
    methods = ["Jacobi", "Gauss-Seidel", "SOR"]
    results = [jacobi, gauss_seidel, sor]

    # Utworzenie wykresu o podanym tytule i opisach osi
    plt.figure(title)
    plt.title(title, weight="bold")
    plt.xlabel("metoda", weight="bold")
    plt.ylabel(indicator, weight="bold")
    # plt.grid(True)

    # Utworzenie słupków kolumnowych dla poszczególnych wyników
    bars = plt.bar(methods, results)
    bars[0].set_color("#D14960")
    bars[1].set_color("#7DC481")
    bars[2].set_color("#2C84C7")

    # Jeśli użytkownik chce pokazać sygnatury wartośći poszczególnych kolumn
    if show_signatures:
        # Pętla dla każdego z wyników, w której ustawiane są sygnatury wartości
        for i in range(3):
            plt.text(i, results[i], results[i], fontsize="10", ha="center", va="bottom")

    # Zapisanie pliku wykresu pod wskazanym adresem
    plt.savefig(f"{path}/{indicator_en}.png")
