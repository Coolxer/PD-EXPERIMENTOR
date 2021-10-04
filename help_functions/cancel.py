from shutil import rmtree
from sys import exit


def cancel(dir):
    rmtree(dir)
    exit()
