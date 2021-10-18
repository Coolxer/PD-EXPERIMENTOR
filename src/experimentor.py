# ############################################### SEKCJA IMPORTU ###############################################

# import modułów generalnych
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# import funkcji pomocnicznych
from .help_functions.file import saveNormalDataToFile, saveMatrixToFile
from .help_functions.draw import draw
from .help_functions.cancel import cancel
from .help_functions.sort3 import sort3

# import elementów związanych z macierzami
from .help_functions.matrix_type import types
from .help_functions.matrix_provider import get_matrix
from .generate_functions.random_vector import random_vector

# import metod z podmodułu @equiter
from ..equiter.src.jacobi.method import jacobi
from ..equiter.src.gauss_seidel.method import gauss_seidel
from ..equiter.src.sor.method import sor


def experiment(name, matrix_type, matrix_size):
    # ############################################### SEKCJA KONFIGURACJI ##########################################

    # uzyskanie katalogu wykonawczego
    DIR = os.path.dirname(os.path.dirname(__file__))

    # układ równań (generowany lub pobrany z zewnątrz)

    # macierz wejściowa układu
    A = get_matrix(matrix_type, matrix_size)

    # ustawienie wektora wyrazów wolnych
    b = None
    b_file = f"{DIR}/exp_results/b_{matrix_size}.txt"

    if not os.path.exists(b_file):
        b = random_vector(matrix_size)
    else:
        b = np.loadtxt(b_file, dtype=float)

    # parametry (jednakowe dla każej metody, ale w jest używane tylko w metodzie SOR)
    tol = 0.000001
    k = 10000
    w_vec = [1.1, 1.3, 1.5, 1.7, 1.9]

    # ############################################ SEKCJA TWORZENIA KATALOGÓW ######################################

    # stworzenie katalogu głównego dla danego typu macierzy
    main_dir = f"{DIR}/exp_results/{matrix_type}"
    if not os.path.exists(main_dir):
        os.mkdir(main_dir)

    # stworzenie katalogu głównego dla konkretnego badania
    dir = f"{DIR}/exp_results/{matrix_type}/{name}"
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)

    # stworzenie katalogu konfiguracyjnego
    config_dir = f"{dir}/config"
    os.mkdir(config_dir)

    # stworzenie katalogu wynikowego
    results_dir = f"{dir}/results"
    os.mkdir(results_dir)

    # ################################################### SEKCJA ZAPISU ############################################

    print("Zapisywanie macierzy ...")

    # zapis pliku A.txt
    saveMatrixToFile(config_dir, "A", A)

    # b.txt jest już zapisane

    print("Zapisywanie innych parametrow ...")

    # zapis pliku parameters.txt
    saveNormalDataToFile(
        config_dir, "parameters", f"tol = {tol}\nk = {k}\nw = {w_vec}"
    )

    # zapis pliku general.txt
    saveNormalDataToFile(
        config_dir,
        "general",
        f"name = {name}\ntype = {matrix_type}\nsize = {matrix_size}",
    )

    # ################################################ SEKCJA ROZWIĄZYWANIA ########################################

    print("Trwa rozwiazywanie ukladu metoda Jacobiego ...")
    jacobi_solution, jacobi_iterations, jacobi_times = jacobi(A, b, k, tol)

    if (
        jacobi_solution is None
        and jacobi_iterations is None
        and jacobi_times is None
    ):
        cancel(dir)

    print("Trwa rozwiazywanie ukladu metoda Gaussa-Seidela ...")

    (
        gauss_seidel_solution,
        gauss_seidel_iterations,
        gauss_seidel_times,
    ) = gauss_seidel(A, b, k, tol)

    if (
        gauss_seidel_solution is None
        and gauss_seidel_iterations is None
        and gauss_seidel_times is None
    ):
        cancel(dir)

    print("Trwa rozwiazywanie ukladu metoda SOR ...")

    sor_solution_list = []
    sor_iteration_list = []
    sor_time_list = []

    for w in w_vec:

        print(f"    SOR: w: {w}")

        sor_solution, sor_iterations, sor_times = sor(A, b, k, tol, w)

        if (
            sor_solution is None
            and sor_iterations is None
            and sor_times is None
        ):
            cancel(dir)

        sor_solution_list.append(sor_solution)
        sor_iteration_list.append(sor_iterations)
        sor_time_list.append(sor_times)

    # w przypadku metody SOR dochodzi dodatkowy parametr (relaksacji - w). Obliczenia dokonywane są dla kilku wartości tego parametru.
    # możliwe są 3 perspektywy do wyboru (najgorsza, średnia, najlepsza)
    # średnia perspektywa powodowała otrzymywanie niezadowalających rezultatów
    # zdecydowano się wybrać najlepszą perspektywę (najlepsza zbieżność według liczby iteracji) i dla metody SOR ten wynik jest wybierany
    # ta perspektywa będzie najbardziej obiektywna, ponieważ metody Jacobiego i Gaussa-Seidela również dążą do doskonałości

    (
        sor_iteration_list_sorted,
        sor_time_list_sorted,
        sor_solution_list_sorted,
    ) = sort3(sor_iteration_list, sor_time_list, sor_solution_list)

    sor_solution = sor_solution_list_sorted[0]
    sor_iterations = sor_iteration_list_sorted[0]
    sor_times = sor_time_list_sorted[0]

    # ################################################ SEKCJA ZAPISU WYNIKÓW #######################################

    print("Zapisywanie rezultatow ...")

    # stworzenie katalogu do zapisu ogólnych wyników tekstowych
    results_dir_txt = f"{results_dir}/txt"
    os.mkdir(results_dir_txt)

    # zapisywanie generalnych wyników w postaci tekstowej (times.txt i iterations.txt)
    saveNormalDataToFile(
        results_dir_txt,
        "iterations",
        f"jacobi = {jacobi_iterations}\ngauss_seidel = {gauss_seidel_iterations}\nsor = {sor_iterations}",
    )

    saveNormalDataToFile(
        results_dir_txt,
        "times",
        f"jacobi = {jacobi_times}\ngauss_seidel = {gauss_seidel_times}\nsor = {sor_times}",
    )

    # stworzenie katalogu do zapisu szczegółowych wyników (wektor wynikowy)
    results_dir_txt_solution = f"{results_dir_txt}/solution"
    os.mkdir(results_dir_txt_solution)

    # zapisywanie szczegółowych rezultatów (wektora wynikowego) dla każdej metody
    saveMatrixToFile(results_dir_txt_solution, "jacobi", jacobi_solution)
    saveMatrixToFile(
        results_dir_txt_solution, "gauss_seidel", gauss_seidel_solution
    )
    saveMatrixToFile(results_dir_txt_solution, "sor", sor_solution)

    # ################################################# SEKCJA WYKRESÓW ############################################

    print("Generowanie wykresow ...")

    # stworzenie katalogu dla wykresów
    results_dir_img = f"{results_dir}/img"
    os.mkdir(results_dir_img)

    # rysowanie wykresu iteracji
    draw(
        results_dir_img,
        "Wykres liczby wykonanych iteracji",
        "liczba iteracji",
        "iterations",
        jacobi_iterations,
        gauss_seidel_iterations,
        sor_iterations,
        show_signatures=True,
    )

    # rysowanie wykresu czasowego
    draw(
        results_dir_img,
        "Wykres czasu obliczeń",
        "czas obliczeń [s]",
        "times",
        np.around(jacobi_times, 4),
        np.around(gauss_seidel_times, 4),
        np.around(sor_times, 4),
        show_signatures=True,
    )

    # wyświetlenie wykresów
    plt.show()

    # zamknięcie okień graficznych
    plt.close("all")
