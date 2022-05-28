# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik udostępnia najważniejsze elementy środowiska doświadczalnego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from .src.help_methods.types import *
from .src.help_methods.file import open_chart_file
from .src.help_methods.dir import get_data_dir
from .src.help_methods.matrix import get_matrix
from .src.help_methods.vector import get_vector

from .equiter.src.sor.method import sor

from .src.basic_experiment import do_basic_experiment
from .src.variable_size_experiment import do_variable_size_experiment
from .src.variable_type_experiment import do_variable_type_experiment
from .src.variable_density_experiment import do_variable_density_experiment
from .src.variable_tolerance_experiment import do_variable_tolerance_experiment
from .src.variable_x0_experiment import do_variable_x0_experiment
