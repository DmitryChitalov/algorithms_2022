"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""


from memory_profiler import profile
import numpy as np
from random import randint
from timeit import timeit


# Вариант с list
@profile
def list_append():
    my_list = []
    for i in range(100000):
        my_list.append(randint(1, 1000))


# Вариант с numpy array
@profile
def array_append():
    my_array = np.array([])
    for i in range(100000):
        np.append(my_array, randint(1, 1000))


print(timeit("list_append()", setup="from __main__ import list_append", number=1))
print(timeit("array_append()", setup="from __main__ import array_append", number=1))

"""
Массивы numpy занимают меньше места в памяти, но при этом заполняются медленнее, чем списки

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    41     31.0 MiB     31.0 MiB           1   @profile
    42                                         def list_append():
    43     31.0 MiB      0.0 MiB           1       my_list = []
    44     34.2 MiB      2.3 MiB      100001       for i in range(100000):
    45     34.2 MiB      0.9 MiB      100000           my_list.append(randint(1, 1000))
12.994985799989081
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    49     33.2 MiB     33.2 MiB           1   @profile
    50                                         def array_append():
    51     33.2 MiB      0.0 MiB           1       my_array = np.array([])
    52     33.2 MiB      0.0 MiB      100001       for i in range(100000):
    53     33.2 MiB      0.0 MiB      100000           np.append(my_array, randint(1, 1000))
20.88992390000203
"""