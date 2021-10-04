import numpy as np


def strengthen_diagonal(matrix, value):
    D_abs = np.abs(np.diag(matrix))

    S = np.sum(np.abs(matrix), axis=1) - D_abs

    for i in range(np.shape(matrix)[0]):
        if(np.abs(matrix[i][i]) <= S[i]):
            matrix[i][i] = S[i] + value
            
    return matrix
