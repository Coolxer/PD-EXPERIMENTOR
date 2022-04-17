# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metodę aktualizującą wszystkie wykresy pojedynczych doświadczeń do spełnienia wymogów formalnych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
from typing import NoReturn
import matplotlib.pyplot as plt

from .help_methods.dir import get_data_dir
from .help_methods.chart import draw_chart

"""
    Wejście (Parametry):
        - title_iterations (str) - tytuł wyświetlanego wykresu iteracji
        - title_times (str) - tytuł wyświetlanego wykresu czasu

        - x_label (str) - oznaczenie osi x
        - y_label_iterations (str) - oznaczenie osi y wykresu iteracji
        - y_label_times (str) - oznaczenie osi y wykresu czasu

        - data_labels (list) ["Jacobi", "Gauss-Seidel", "SOR"] - opisy poszczególnych kolumn w wykresie kolumnowym
        - colors (list) [default = "#D14960", "#7DC481", "#2C84C7"] - lista 3 kolorów serii wykresu
        - show_grid (bool) [default = False] - ewentualne wyświetlanie siatki wykresu
        - show_signatures (bool) [default = True] - ewentualne wyświetlanie wartości poszczególnych kolumn w wykresie kolumnowym
"""

# Metoda aktualizuje wszystkie wykresy pojedynczych doświadczeń do spełnienia wymogów formalnych
def update_charts(
    title_iterations: str,
    title_times: str,
    x_label: str,
    y_label_iterations: str,
    y_label_times: str,
    data_labels: list,
    colors: list,
    show_grid: bool,
    show_signatures: bool,
) -> NoReturn:

    # Pobranie głównego katalogu 'data'
    exp_dir = get_data_dir()

    # Iterowanie po każdym katalogu w folderze 'data'
    for dir in sorted(os.listdir(exp_dir)):
        current_exp_dir = f"{exp_dir}/{dir}"

        # Jeśli 'dir' nie jest katalogiem to należy przejść do następnego elementu
        if not os.path.isdir(current_exp_dir):
            continue

        # Jeśli w głównym katalogu eksperymentu istnieje plik 'general.txt' to oznacza, że jest to eksperyment grupowy
        # Wtedy należy pominąć ten katalog i przejść do następnego
        general_file_path = f"{current_exp_dir}/general.txt"
        if os.path.exists(general_file_path):
            continue

        # Próba odczytu pliku zawierającego wyniki dot. liczby iteracji i zapisanie tych danych do zmiennych
        try:
            iterations_file = open(f"{current_exp_dir}/results/txt/iterations.txt", "r")

            iterations_data = []
            for line in iterations_file.readlines():
                iterations_data.append(int(line.split(" = ")[1]))

            iterations_file.close()

            jacobi_iterations, gauss_seidel_iterations, sor_iterations = iterations_data

        except:
            continue

        # Próba odczytu pliku zawierającego wyniki dot. czasów i zapisanie tych danych do zmiennych
        try:
            times_file = open(f"{current_exp_dir}/results/txt/times.txt", "r")

            times_data = []
            for line in times_file.readlines():
                times_data.append(line.split(" = ")[1])

            times_file.close()

            jacobi_time, gauss_seidel_time, sor_time = times_data
        except:
            continue

        # Pobranie ścieżki zapisu wykresów i ewentualne utworzenie katalogu jeśli dotychczas nie istniał
        img_path = f"{current_exp_dir}/results/img"
        if not os.path.exists(img_path):
            os.makedirs(img_path)

        # Przerysowanie wykresu liczby iteracji zgodnie z aktualnymi wymogami
        draw_chart(
            "bar",
            title_iterations,
            x_label,
            y_label_iterations,
            jacobi_iterations,
            gauss_seidel_iterations,
            sor_iterations,
            0,
            None,
            data_labels,
            colors,
            show_grid,
            show_signatures,
        )

        # Zapisanie wykresu iteracji
        plt.savefig(f"{img_path}/iterations.png")

        # Przerysowanie wykresu czasowego zgodnie z aktualnymi wymogami
        draw_chart(
            "bar",
            title_times,
            x_label,
            y_label_times,
            jacobi_time,
            gauss_seidel_time,
            sor_time,
            6,
            None,
            data_labels,
            colors,
            show_grid,
            show_signatures,
        )

        # Zapisanie wykresu czasu
        plt.savefig(f"{img_path}/times.png")
