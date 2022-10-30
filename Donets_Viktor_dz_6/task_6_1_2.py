from memory_profiler import profile
from random import randint
import numpy as np
from copy import deepcopy
"""
Задание из курса Алгоритмы.
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""


@profile
def func_2():
    array_1 = deepcopy(array_0)
    elem, n = sorted([(i, array_1.count(i)) for i in set(array_1)],
                     key=lambda x: x[1])[-1]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {n} раз(а)'


@profile
def func_3():
    array_2 = np.array(array_0)
    elem, n = sorted([(i, array_2.tolist().count(i)) for i in set(array_2)],
                     key=lambda x: x[1])[-1]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {n} раз(а)'



array_0 = [randint(1, 10) for i in range(100000)]
print(func_2())
print(func_3())

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    27     33.1 MiB     33.1 MiB           1   @profile
    28                                         def func_2():
    29     33.9 MiB      0.8 MiB           1       array_1 = deepcopy(array_0)
    30     33.9 MiB      0.0 MiB          15       elem, n = sorted([(i, array_1.count(i)) for i in set(array_1)],
    31     33.9 MiB      0.0 MiB          22                        key=lambda x: x[1])[-1]
    32     33.9 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    33     33.9 MiB      0.0 MiB           1              f'оно появилось в массиве {n} раз(а)'


Чаще всего встречается число 1, оно появилось в массиве 10120 раз(а)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     32.5 MiB     32.5 MiB           1   @profile
    37                                         def func_3():
    38     32.5 MiB      0.0 MiB           1       array_2 = np.array(array_0)
    39     32.5 MiB     -1.4 MiB          15       elem, n = sorted([(i, array_2.tolist().count(i)) for i in set(array_2)],
    40     32.4 MiB     -0.2 MiB          22                        key=lambda x: x[1])[-1]
    41     32.4 MiB     -0.1 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    42     32.4 MiB      0.0 MiB           1              f'оно появилось в массиве {n} раз(а)'


Чаще всего встречается число 1, оно появилось в массиве 10120 раз(а)
"""

"""
При использовании модуля nampy против list comprehension
памяти используется меньше. 32.4 MiB против 33.9 MiB
"""