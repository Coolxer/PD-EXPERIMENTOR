import os
from scipy.io import loadmat

from src.generator.diagonal_amplifier import strengthen_diagonal


def external_matrix(file):
    dir = os.getcwd()

    # load matlab file
    data = loadmat(f'{dir}/src/data/{file}.mat')

    for item in data['Problem'].item(0):
        if str(type(item)) == "<class 'scipy.sparse.csc.csc_matrix'>":
            break

    # get matrix
    matrix = item.toarray()

    # diagonal strengthening
    matrix = strengthen_diagonal(matrix, 0.1)

    return matrix
