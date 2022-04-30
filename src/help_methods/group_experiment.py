# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik zawiera istotną część złożonych eksperymentów

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
import numpy as np
from typing import Tuple

"""
    Wejście (Parametry):
        - experiment_dir (str) - katalog głównego eksperymentu
        - experiment_type (str) - typ eksperymentu

    Wyjście (Wartości zwracane przez funkcję):
        - ws (list) - lista wartości parametru 'w'
        - jacobi_iterations (list) - lista wyników iteracji metody Jacobiego
        - gauss_seidel_iterations (list) - lista wyników iteracji metody Gaussa-Seidela
        - sor_iterations (list) - lista wyników iteracji metody SOR
        - sor_iterations_only (list) - lista wyników iteracji metody SOR dla różnych wartości parametru 'w'

        - jacobi_times (list) - lista wyników czasowych metody Jacobiego
        - gauss_seidel_times (list) - lista wyników czasowych metody Gaussa-Seidela
        - sor_times (list) - lista wyników czasowych metody SOR
        - sor_times_only (list) - lista wyników czasowych metody SOR dla różnych wartości parametru 'w'
"""


def do_group_experiment(experiment_dir, experiment_type) -> Tuple[list, list, list, list, list, list, list, list, list]:

    # Deklaracja listy do przechowywania wartości parametru 'w'
    ws = []

    # Deklaracja list do przechowywania wyników iteracji
    jacobi_iterations = []
    gauss_seidel_iterations = []
    sor_iterations = []
    sor_iterations_only = []

    # Deklaracja list do przechowywania wyników czasowych
    jacobi_times = []
    gauss_seidel_times = []
    sor_times = []
    sor_times_only = []

    # Przygotowanie listy katalogów poszczególnych podeksperymentów
    exp_dir_group = os.listdir(experiment_dir)

    # Deklaracja tablicy zawierającej elementy do usunięcia z listy katalogów
    dirs_to_remove = []

    # Iteracja po każdym elemencie w liście 'exp_dir_group'
    for dir in exp_dir_group:
        # Sprawdzenie czy dir faktycznie jest katalogiem, bo listdir() zwraca również pliki
        # Jeśli dir nie jest katalogiem to jest oznaczany do usunięcia z listy
        if not os.path.isdir(f"{experiment_dir}/{dir}"):
            dirs_to_remove.append(dir)

    # Faktyczne usunięcie elementów z listy
    exp_dir_group = [i for i in exp_dir_group if i not in dirs_to_remove]

    # Odpowiednie sortowanie listy w zależności od typu eksperymentu
    if experiment_type == "tolerance":
        exp_dir_group = sorted(list(map(lambda x: float(x), exp_dir_group)))
    elif experiment_type == "order":
        exp_dir_group = sorted(exp_dir_group)
    elif experiment_type == "type":
        exp_dir_group = sorted(list(map(lambda x: int(x), exp_dir_group)))

    w_prepared = False

    # Pętla iterująca po każdym podeksperymencie danego eksperymentu grupowego
    for dir in exp_dir_group:

        # Pobranie katalogu z wynikami
        exp_txt_results_dir = f"{experiment_dir}/{dir}/results/txt"

        try:
            # Odczytanie danych dot. iteracji z pliku i zapisanie ich do poszczególnych tablic
            iterations_file = open(f"{exp_txt_results_dir}/iterations.txt", "r")
            jacobi_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            gauss_seidel_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            sor_iterations.append(int(iterations_file.readline().split(" = ")[1]))
            iterations_file.close()

            sor_iterations_file = open(f"{exp_txt_results_dir}/sor_iterations.txt", "r")
            sor_iterations_only_row = []
            for line in sor_iterations_file.readlines():
                w, iteration = line.split(" = ")
                if not w_prepared:
                    ws.append(float(w))
                sor_iterations_only_row.append(int(iteration))
            sor_iterations_only.append(sor_iterations_only_row)
            sor_iterations_file.close()

            times_file = open(f"{exp_txt_results_dir}/times.txt", "r")
            jacobi_times.append(float(times_file.readline().split(" = ")[1]))
            gauss_seidel_times.append(float(times_file.readline().split(" = ")[1]))
            sor_times.append(float(times_file.readline().split(" = ")[1]))
            times_file.close()

            sor_times_files = open(f"{exp_txt_results_dir}/sor_times.txt", "r")
            sor_times_only_row = []
            for line in sor_times_files.readlines():
                _, time = line.split(" = ")
                sor_times_only_row.append(float(time))
            sor_times_only.append(sor_times_only_row)
            sor_times_files.close()
        except:
            print("Wymagane pliki do stworzenia wykresów nie istnieją!")
            return

        if not w_prepared:
            w_prepared = True

    sor_iterations_only = np.transpose(np.array(sor_iterations_only)).tolist()
    sor_times_only = np.transpose(np.array(sor_times_only)).tolist()

    return (
        ws,
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
        sor_iterations_only,
        jacobi_times,
        gauss_seidel_times,
        sor_times,
        sor_times_only,
    )
