import os
import numpy as np


# metoda zapisuje zwykłe dane do pliku tekstowego
'''
dir to nazwa katalogu
name to nazwa pliku
content to zawartość do zapisania
'''
def saveNormalDataToFile(dir, name, content):
    file = open(f'{dir}/{name}.txt', 'w')
    file.write(str(content))
    file.close()

# metoda zapisuje macierze NumPy do pliku tekstowego
'''
dir to nazwa katalogu
name to nazwa pliku
content to zawartość do zapisania
'''
def saveMatrixToFile(dir, name, content):
    np.savetxt(f'{dir}/{name}.txt', content)
