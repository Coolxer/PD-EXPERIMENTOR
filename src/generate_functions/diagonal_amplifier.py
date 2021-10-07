import numpy as np

# metoda służy do wzmocnienia przekątnej dowolnej macierzy, tak aby był spełniony warunek zbieżności dla stacjonarnych metod prrzybliżonych rozwiązywania URL
'''
matrix to macierz wejściowa
value to wartość wzmocnienia głównej przekątnej macierzy
'''
def strengthen_diagonal(matrix, value):
    D_abs = np.abs(np.diag(matrix))

    S = np.sum(np.abs(matrix), axis=1) - D_abs

    for i in range(np.shape(matrix)[0]):
        if(np.abs(matrix[i][i]) <= S[i]):
            matrix[i][i] = S[i] + value
            
    return matrix
