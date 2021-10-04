# ############################################### IMPORT SECTION ###############################################

# general
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# help functions
from src.exp_help_functions.file import saveNormalDataToFile, saveMatrixToFile
from src.exp_help_functions.plot import generate_plot
from src.exp_help_functions.cancel import cancel
from src.mysort import sort3

# matrices
from src.exp_help_functions.matrix_type import types
from src.exp_help_functions.matrix_provider import get_matrix
from src.generator.random_vector import random_vector

# methods
from src.jacobi.method import jacobi
from src.gauss_seidel.method import gauss_seidel
from src.sor.method import sor

# ############################################## CONFIG SECTION ##############################################

# General Informations
LAB_NAME = '1000x1000'  # name of directory also
MATRIX_TYPE = types['external']
MATRIX_SIZE = 1000
FILE_NAME = 'olm1000'

# System of equations (generated or used from external source)
A = get_matrix(MATRIX_TYPE, MATRIX_SIZE, FILE_NAME)

# load b
b = None
b_file = f'{os.getcwd()}/src/exp/b_{MATRIX_SIZE}.txt'

if not os.path.exists(b_file):
    b = random_vector(MATRIX_SIZE)
else:
    b = np.loadtxt(b_file, dtype=float)

# Parameters (same for each method, of course w is using only in SOR)
tol = 0.000001
k = 10000
w_vec = [1.1, 1.3, 1.5, 1.7, 1.9]

# ########################################### CREATE DIRS SECTION ############################################

# create main dir
dir = f'{os.getcwd()}/src/exp/{MATRIX_TYPE}/{LAB_NAME}'
if os.path.exists(dir):
    shutil.rmtree(dir)
os.mkdir(dir)

# create config dir
config_dir = f'{dir}/config'
os.mkdir(config_dir)

# create results dir
results_dir = f'{dir}/results'
os.mkdir(results_dir)

# ########################################### SAVING DATA SECTION ############################################

print('Saving matrices ...')

# save A.txt
saveMatrixToFile(config_dir, 'A', A)

# b.txt is common for every type of matrix and it's already saved

print('Saving other parameters ...')

# save parameters.txt file
saveNormalDataToFile(config_dir, 'parameters',
                     f'tol = {tol}\nk = {k}\nw = {w_vec}')


# save general.txt file
saveNormalDataToFile(config_dir, 'general',
                     f'name = {LAB_NAME}\ntype = {MATRIX_TYPE}\nsize = {MATRIX_SIZE}')


# ############################################# SOLVING SECTION ##############################################

print('Solving with Jacobi method ...')

jacobi_solution, jacobi_iterations, jacobi_times = jacobi(A, b, k, tol)

if jacobi_solution is None and jacobi_iterations is None and jacobi_times is None:
    cancel(dir)

print('Solving with Gauss-Seidel method ...')

gauss_seidel_solution, gauss_seidel_iterations, gauss_seidel_times = gauss_seidel(
    A, b, k, tol)

if gauss_seidel_solution is None and gauss_seidel_iterations is None and gauss_seidel_times is None:
    cancel(dir)

print('Solving with SOR method ...')

sor_solution_list = []
sor_iteration_list = []
sor_time_list = []

for w in w_vec:

    print(f'    SOR: w: {w}')

    sor_solution, sor_iterations, sor_times = sor(A, b, k, tol, w)

    if sor_solution is None and sor_iterations is None and sor_times is None:
        cancel(dir)

    sor_solution_list.append(sor_solution)
    sor_iteration_list.append(sor_iterations)
    sor_time_list.append(sor_times)

# can be 3 perspective (the worst, mean , the best)
# average give bad results
# i think it will  be good if i would choose the best iterations (sort by it), because Jacobi and Gauss-Seidel try to make their best too

sor_iteration_list_sorted, sor_time_list_sorted, sor_solution_list_sorted = sort3(
    sor_iteration_list, sor_time_list, sor_solution_list)


sor_solution = sor_solution_list_sorted[0]
sor_iterations = sor_iteration_list_sorted[0]
sor_times = sor_time_list_sorted[0]


# ########################################## SAVING RESULTS SECTION ##########################################

print('Saving results ...')

# create dir for general txt results
results_dir_txt = f'{results_dir}/txt'
os.mkdir(results_dir_txt)


# save general txt results (times and iterations)
saveNormalDataToFile(results_dir_txt, 'iterations',
                     f'jacobi = {jacobi_iterations}\ngauss_seidel = {gauss_seidel_iterations}\nsor = {sor_iterations}')

saveNormalDataToFile(results_dir_txt, 'times',
                     f'jacobi = {jacobi_times}\ngauss_seidel = {gauss_seidel_times}\nsor = {sor_times}')

# create dir for detail results
results_dir_txt_solution = f'{results_dir_txt}/solution'
os.mkdir(results_dir_txt_solution)

# save detail results (x-vector) for each method
saveMatrixToFile(results_dir_txt_solution, 'jacobi', jacobi_solution)
saveMatrixToFile(results_dir_txt_solution,
                 'gauss_seidel', gauss_seidel_solution)
saveMatrixToFile(results_dir_txt_solution, 'sor', sor_solution)

# ############################################## PLOT SECTION ################################################

print('Generating plots ...')

# create dir for plots
results_dir_img = f'{results_dir}/img'
os.mkdir(results_dir_img)

# plot iterations
generate_plot(results_dir_img, 'Wykres liczby wykonanych iteracji', 'liczba iteracji', 'iterations', jacobi_iterations,
              gauss_seidel_iterations, sor_iterations, show_signatures=True)


# plot times
generate_plot(results_dir_img, 'Wykres czasu obliczeń', 'czas obliczeń [s]', 'times', np.around(jacobi_times, 4),
              np.around(gauss_seidel_times, 4), np.around(sor_times, 4), show_signatures=True)

# show plots
plt.show()

# close figures
plt.close('all')
