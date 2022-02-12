"""Используем NumPy"""

from random import randint
from pympler import asizeof
from numpy import array

lst_obj = [randint(-100, 100) for _ in range(50000)]
print(asizeof.asizeof(lst_obj))  # -> 1165720 байт
lst_obj = [randint(0, 100) for _ in range(50000)]
print(asizeof.asizeof(lst_obj))  # -> 409720 байт


lst_obj = array([randint(-100, 100) for _ in range(50000)])
print(type(lst_obj))
print(asizeof.asizeof(lst_obj))  # -> 200096 байт
lst_obj = array([randint(0, 100) for _ in range(50000)])
print(asizeof.asizeof(lst_obj))  # -> 200096 байт
