"""Профилировка затрат памяти"""

from copy import deepcopy
from memory_profiler import profile

"1 Mebibyte = 1048576 Bytes"

# ссылки, поэтому gc не запускается
@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(10000))
    y = deepcopy(x)
    return y


"""
Line #    Mem usage    Increment   Line Contents
================================================
    10     35.6 MiB     35.6 MiB   @profile
    11                             def function_1():
    12                                 '''Выделяет доп память, не освобождается'''
    13     36.0 MiB      0.3 MiB       x = list(range(10000))
    14     36.1 MiB      0.2 MiB       y = deepcopy(x)
    15     36.1 MiB      0.0 MiB       return y
"""


@profile
def function_2():
    """Выделяет доп память, освобождается"""
    x = list(range(100000))
    y = deepcopy(x)
    del x
    y = None
    return y


"""
Line #    Mem usage    Increment   Line Contents
================================================
    18     35.9 MiB     35.9 MiB   @profile
    19                             def function_2():
    20                                 '''Выделяет доп память, освобождается'''
    21     39.7 MiB      3.8 MiB       x = list(range(100000))
    22     40.8 MiB      1.1 MiB       y = deepcopy(x)
    23     40.8 MiB      0.0 MiB       del x
    24     36.2 MiB      0.0 MiB       y = None
    25     36.2 MiB      0.0 MiB       return y
"""

if __name__ == "__main__":
    function_1()
    function_2()
