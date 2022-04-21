# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera metody umożliwiające tworzenie groupowych doświadczeń obliczeniowych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os

from .help_methods.dir import get_data_dir
from .help_methods.file import save_data_to_file
from .single_experiment import do_single_experiment
from .help_methods.chart import draw_chart, save_chart_to_file
from .help_methods.table import draw_table


"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu

        - tolerance (float) - zadana dokładność przybliżonego rozwiązania
        - max_iterations (int) - maksymalna liczba iteracji
        - w_values (list) - lista wartości parametru 'w' do przetestowania

        - matrix_type (str) [None] - typ macierzy głównej (podane tylko w przypadku eksperymentu grupowanego według typu)
        - sizes(list) [None] - lista rozmiarów układu w doświadczeniu  (podane tylko w przypadku eksperymentu grupowanego według typu)
        
        - matrix_size (int) [None] - rozmiar macierzy głównej (liczba wierszy / kolumn) (podane tylko w przypadku eksperymentu grupowanego według rozmiaru)
        - types (list) [None] - lista typów układu w doświadczeniu  (podane tylko w przypadku eksperymentu grupowanego według rozmiaru)

        - create_charts (bool) [False] - czy mają zostać utworzone wykresy graficzne (przydatne gdy eksperyment grupowy wykonywany jest w całości lub jest to jego koniec)
"""

# Metoda wykonuje grupowe doświadczenia obliczeniowe
def do_group_experiment(
    experiment_name: str,
    tolerance: float,
    max_iterations: int,
    w_values: list,
    matrix_type: str = None,
    sizes: list = None,
    matrix_size: int = None,
    types: list = None,
    create_charts: bool = False,
):
    experiment_description = None

    # Jeśli typ eksperymentu to 'grupowany według typu'
    if matrix_type is not None and sizes is not None:
        for size in sizes:
            do_single_experiment(f"{experiment_name}/{size}", matrix_type, size, tolerance, max_iterations, w_values)
        experiment_description = (
            f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = type_grouped\ntyp macierzy A = {matrix_type}"
        )

    # Jeśli typ eksperymentu to 'grupowany według rozmiaru'
    elif matrix_size is not None and types is not None:
        for type in types:
            do_single_experiment(f"{experiment_name}/{type}", type, matrix_size, tolerance, max_iterations, w_values)
        experiment_description = f"nazwa eksperymentu = {experiment_name}\ntyp eksperymentu = size_grouped\nrozmiar macierzy A = {matrix_size}"

    save_data_to_file(f"{get_data_dir()}/{experiment_name}", "general", experiment_description)

    # Ewentualne natychmiastowe utworzenie grupowych wykresów
    if create_charts:
        make_group_charts_and_tables(experiment_name)


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wejście (Parametry):
        - experiment_name (str) - nazwa eksperymentu
"""

# Metoda tworzy wykresy i tabele dla grupowych doświadczeń
def make_group_charts_and_tables(experiment_name):

    # Uzyskanie katalogu eksperymentu
    exp_dir = f"{get_data_dir()}/{experiment_name}"

    # Sprawdzenie czy istnieje katalog eksperymentu
    if not os.path.exists(exp_dir):
        print("Eksperyment o podanej nazwie nie istnieje!")
        return

    # Deklaracja tablic do przechowywania wyników iteracji
    jacobi_iterations = []
    gauss_seidel_iterations = []
    sor_iterations = []

    # Deklaracja tablic do przechowywania wyników czasowych
    jacobi_times = []
    gauss_seidel_times = []
    sor_times = []

    try:
        # Otwarcie pliku 'general.txt' przechowującego m.in. informację o typie eksperymentu
        general_txt_file = open(f"{exp_dir}/general.txt", "r")

        # Odczyt pliku 'general.txt'
        data_file = general_txt_file.readlines()

        # Pobranie typu eksperymentu
        experiment_type = str(data_file[1].split(" = ")[1])

        # Zamknięcie pliku 'general.txt'
        general_txt_file.close()
    except:
        print("Plik general.txt nie istnieje")
        return

    # Przygotowanie listy katalogów poszczególnych podeksperymentów
    exp_dir_group = os.listdir(exp_dir)

    # Deklaracja tablicy zawierającej elementy do usunięcia z listy katalogów
    dirs_to_remove = []

    # Iteracaj po każdym elemencie w liście dir
    for dir in exp_dir_group:
        # Sprawdzenie czy dir faktycznie jest katalogiem, bo listdir() zwraca również pliki
        # Jeśli dir nie jest katalogiem to jest oznaczany do usunięcia z listy
        if not os.path.isdir(f"{exp_dir}/{dir}"):
            dirs_to_remove.append(dir)

    # Faktyczne usunięcie elementów z listy
    exp_dir_group = [i for i in exp_dir_group if i not in dirs_to_remove]

    # Jeśli typ eksperymentu dotyczy grupowania według typu to sortowanie odbywa się za pomocą wartości liczbowych
    if experiment_type.strip() == "type_grouped":
        exp_dir_group = sorted(list(map(lambda x: int(x), exp_dir_group)))
        x_label = "stopień macierzy"

    # Jeśli typ eksperymentu dotyczy grupowania według rozmiaru to sortowanie odbywa się za pomocą łańcuchów znakowych
    # Dodatkowo nadawane są własne nazwy (spolszczone)
    elif experiment_type.strip() == "size_grouped":
        exp_dir_group = sorted(exp_dir_group)
        x_label = "typ macierzy"

    # Pętla iterująca po każdym podeksperymencie danego eksperymentu grupowego
    for dir in exp_dir_group:

        # Pobranie katalogu z wynikami
        exp_txt_results_dir = f"{exp_dir}/{dir}/results/txt"

        try:
            # Odczytanie danych dot. iteracji z pliku i zapisanie ich do poszczególnych tablic
            iterations_file = open(f"{exp_txt_results_dir}/iterations.txt", "r")
            jacobi_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            gauss_seidel_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            sor_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            iterations_file.close()

            # Odczytanie danych dot. czasów z pliku i zapisanie ich do poszczególnych tablic
            times_file = open(f"{exp_txt_results_dir}/times.txt", "r")
            jacobi_times.append(float(times_file.readline().split(" = ")[1]))
            gauss_seidel_times.append(float(times_file.readline().split(" = ")[1]))
            sor_times.append(float(times_file.readline().split(" = ")[1]))
            times_file.close()
        except:
            print("Wymagane pliki do stworzenia wykresów nie istnieją!")
            return

    # Jeśli typ eksperymentu dotyczy grupowania według rozmiaru to nazwy macierzy zostają spolszczone
    if experiment_type.strip() == "size_grouped":
        exp_dir_group = translate_matrix_names(exp_dir_group)

    # Narysowanie wykresu liczby iteracji
    draw_chart(
        "linear",
        "Liczba wykonanych iteracji",
        x_label,
        "liczba iteracji",
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
        0,
        exp_dir_group,
    )

    # Zapisanie wykresu liczby iteracji w pliku
    save_chart_to_file(f"{exp_dir}/iterations_chart.png")

    # Narysowanie wykresu czasu obliczeń
    draw_chart(
        "linear",
        "Czas obliczeń",
        x_label,
        "czas [s]",
        jacobi_times,
        gauss_seidel_times,
        sor_times,
        6,
        exp_dir_group,
    )

    # Zapisanie wykresu czasu obliczeń w pliku
    save_chart_to_file(f"{exp_dir}/times_chart.png")

    # Utworzenie tabeli wyników dot. liczby wyk. iteracji
    draw_table(
        exp_dir,
        "iterations_table",
        ["Jacobi", "Gauss-Seidel", "SOR"],
        exp_dir_group,
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
    )

    # Utworzenie tabeli wyników dot. czasu obliczeń
    draw_table(
        exp_dir,
        "times_table",
        ["Jacobi", "Gauss-Seidel", "SOR"],
        exp_dir_group,
        jacobi_times,
        gauss_seidel_times,
        sor_times,
    )


# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Wejście:
        - eng_matrix_names (str): kluczowe nazwy macierzy w j. angielskim

    Wyjście:
        - pl_matrix_names (str): nazwy macierzy w języku polskim
"""

# Macierz zamienia kluczowe nazwy macierzy na poprawne nazwy w j. polskim
def translate_matrix_names(eng_matrix_names: list) -> list:
    pl_matrix_names = []

    for name in eng_matrix_names:
        if name == "band":
            pl_matrix_names.append("wstęgowa")
        elif name == "diagonal":
            pl_matrix_names.append("diagonalna")
        elif name == "full":
            pl_matrix_names.append("pełna")
        elif name == "lower_triangular":
            pl_matrix_names.append("dolno-trójkątna")
        elif name == "sparse":
            pl_matrix_names.append("rzadka")
        elif name == "upper_triangular":
            pl_matrix_names.append("górno-trójkątna")
        else:
            continue

    return pl_matrix_names
