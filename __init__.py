# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik udostępnia najważniejsze elementy środowiska doświadczalnego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from .src.help_methods.types import *
from .src.help_methods.file import open_chart_file

from .src.basic_experiment import do_basic_experiment
from .src.variable_size_experiment import do_variable_size_experiment
from .src.variable_type_experiment import do_variable_type_experiment
from .src.variable_tolerance_experiment import do_variable_tolerance_experiment
from .src.variable_x0_experiment import do_variable_x0_experiment
