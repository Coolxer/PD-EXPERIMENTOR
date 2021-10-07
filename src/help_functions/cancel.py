from shutil import rmtree
from sys import exit


# metoda usuwa wcześniej utworzony katalog i kończy działanie skryptu
'''
dir to katalog do usunięcia
'''
def cancel(dir):
    rmtree(dir)
    exit()
