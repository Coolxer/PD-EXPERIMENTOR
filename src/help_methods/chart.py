# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawierający metodę rysującą wykres porównujący zbieżność metod

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import matplotlib.pyplot as plt

"""
    Wejście:
        - dir (str) - katalog zapisu wykresu
        - name (str) - nazwa pliku wykresu
        - title (str) - tytuł wyświetlanego wykresu
        - indicator (str) - oznaczenie osi y (czas / liczba iteracji)

        - jacobi (float) - wyniki doświadczeń metodą Jacobiego
        - gauss_seidel (float) - wyniki doświadczeń metodą Gaussa-Seidela
        - sor (float) - wyniki doświadczeń metodą SOR

        - show_signatures (bool) [default = True] - ewentualne wyświetlanie wartości poszczególnych kolumn
"""

# Metoda rysuje wykres porównujący zbieżność metod na podstawie liczby iteracji / czasu
def draw_chart(
    dir: str,
    name: str,
    title: str,
    indicator: str,
    jacobi: float,
    gauss_seidel: float,
    sor: float,
    show_signatures: bool = True,
) -> NoReturn:

    # Utworzenie tablic nazw metod i ich rezultatów
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

    # Jeśli użytkownik chce pokazać sygnatury wartości poszczególnych kolumn
    if show_signatures:
        # Pętla dla każdego z wyników, w której ustawiane są sygnatury wartości
        for i in range(3):
            plt.text(i, results[i], results[i], fontsize="10", ha="center", va="bottom")

    # Zapisanie pliku wykresu pod wskazanym adresem
    plt.savefig(f"{dir}/{name}.png")
