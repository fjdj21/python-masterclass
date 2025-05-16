import inspect
from nested_data2 import ruler

def print_ruler(with_line_number=True):
    if with_line_number:
        print(ruler, f"(line {inspect.currentframe().f_back.f_lineno})")
    else:
        print(ruler)
