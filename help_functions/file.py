import os
import numpy as np


def saveNormalDataToFile(dir, name, content):
    file = open(f'{dir}/{name}.txt', 'w')
    file.write(str(content))
    file.close()


def saveMatrixToFile(dir, name, content):
    np.savetxt(f'{dir}/{name}.txt', content)
