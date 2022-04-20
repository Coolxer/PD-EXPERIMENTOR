# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę rysującą wykres porównujący zbieżność metod i metodę umożliwiającą zapis wykresu do pliku

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import matplotlib.pyplot as plt

"""
    Wejście:
        - type (str) - typ wykresu (bar / linear)
        - title (str) - tytuł wyświetlanego wykresu
        - x_label (str) - oznaczenie osi x
        - y_label (str) - oznaczenie osi y (czas / liczba iteracji)

        - jacobi_data (list) - wyniki doświadczeń metodą Jacobiego
        - gauss_seidel_data (list) - wyniki doświadczeń metodą Gaussa-Seidela
        - sor_data (list) - wyniki doświadczeń metodą SOR
        - data_precision (int) - dokładność wyświetlanych danych na wykresie

        - x_values (list) [None] - wartości na osi x na wykresie liniowym
        - data_labels (list) ["Jacobi", "Gauss-Seidel", "SOR"] - opisy poszczególnych kolumn w wykresie kolumnowym lub serii w wykresie liniowym
        - colors (list) [default = "#D14960", "#7DC481", "#2C84C7"] - lista 3 kolorów serii wykresu
        - show_grid (bool) [default = False] - ewentualne wyświetlanie siatki wykresu
        - show_signatures (bool) [default = True] - ewentualne wyświetlanie wartości poszczególnych kolumn w wykresie kolumnowym
"""

# Metoda rysuje wykres porównujący zbieżność metod na podstawie liczby iteracji / czasu
def draw_chart(
    type: str,
    title: str,
    x_label: str,
    y_label: str,
    jacobi_data: float,
    gauss_seidel_data: float,
    sor_data: float,
    data_precision: int = 6,
    x_values: list = None,
    data_labels: list = ["Jacobi", "Gauss-Seidel", "SOR"],
    colors: list = ["#D14960", "#7DC481", "#2C84C7"],
    show_grid: bool = False,
    show_signatures: bool = True,
) -> NoReturn:

    # Utworzenie wykresu o podanym tytule i opisach osi
    fig = plt.figure()
    plt.title(title, weight="bold")
    plt.xlabel(x_label, weight="bold")
    plt.ylabel(y_label, weight="bold")

    # Jeśli typ wykresu to 'kolumnowy'
    if type == "bar":

        # Utworzenie tablicy  rezultatów
        if data_precision == 0:
            results = [int(jacobi_data), int(gauss_seidel_data), int(sor_data)]
        else:
            results = [
                round(float(jacobi_data), data_precision),
                round(float(gauss_seidel_data), data_precision),
                round(float(sor_data), data_precision),
            ]

        # Utworzenie kolumn dla poszczególnych wyników
        bars = plt.bar(data_labels, results)
        bars[0].set_color(colors[0])
        bars[1].set_color(colors[1])
        bars[2].set_color(colors[2])

        # Jeśli użytkownik chce pokazać sygnatury wartości poszczególnych kolumn
        if show_signatures:
            # Pętla dla każdego z wyników, w której ustawiane są sygnatury wartości
            for i in range(3):
                plt.text(i, results[i], results[i], fontsize="10", ha="center", va="bottom")

    # Jeśli typ wykresu to 'liniowy'
    elif type == "linear":

        # Utworzenie trzech serii danych
        plt.plot(x_values, jacobi_data, linestyle=(0, (5, 10)), marker="o", color=colors[0], label=data_labels[0])
        plt.plot(x_values, gauss_seidel_data, linestyle=(0, (5, 10)), marker="o", color=colors[1], label=data_labels[1])
        plt.plot(x_values, sor_data, linestyle=(0, (5, 10)), marker="o", color=colors[2], label=data_labels[2])

        # Ustawienie wartości na osi x
        plt.xticks(x_values)

        # Dopasowanie rozmiaru etykiet typu macierzy
        if x_label == "typ macierzy":
            fig.autofmt_xdate()

        # Wyświetlenie legendy
        plt.legend()

    # Ewentualne wyświetlenie siatki wykresu
    if show_grid:
        plt.grid()

    # Zamknięcie figury
    # plt.close(fig)


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wejście:
        - file (str) - ścieżka zapisu pliku graficznego
"""
# Metoda zapisuje aktualnie otwartą wykres do wskazanego pliku
def save_chart_to_file(file: str) -> NoReturn:
    plt.savefig(file, bbox_inches="tight")
    plt.close()
