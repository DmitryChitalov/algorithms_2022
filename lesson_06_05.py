from mimesis import Person
from memory_profiler import profile
# Заменила цикл и добавление в список на встроенную функцию map и кортеж, что сократило
# объем памяти с 4352.5117 MiB на 4351.8242 MiB


@profile(precision=4)
def func_1():
    names = (Person('en').name() for i in range(10 ** 4))
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names


""" 
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     6  36.4961 MiB  36.4961 MiB           1   @profile(precision=4)
     7                                         def func_1():  # -->458.4 MiB
     8 4352.5117 MiB 4314.1992 MiB       20003       names = (Person('en').name() for i in range(10 ** 4))
     9  36.5078 MiB   0.0000 MiB           1       upper_names = []
    10 4352.5117 MiB   1.7852 MiB       10001       for name in names:
    11 4352.5117 MiB   0.0312 MiB       10000           upper_names.append(name.upper())
    12 4352.5117 MiB   0.0000 MiB           1       return upper_names
"""


@profile(precision=4)
def func_2():
    names = (Person('en').name() for i in range(10 ** 4))
    return tuple(map(lambda name: str.upper(name), names))


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15  36.3008 MiB  36.3008 MiB           1   @profile(precision=4)
    16                                         def func_2():
    17 4351.8242 MiB 4313.9023 MiB       20003       names = (Person('en').name() for i in range(10 ** 4))
    18 4351.8242 MiB   1.6211 MiB       20001       return tuple(map(lambda name: str.upper(name), names))
"""