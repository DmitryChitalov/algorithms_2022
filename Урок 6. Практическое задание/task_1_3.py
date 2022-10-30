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

Это файл для третьего скрипта
"""

from memory_profiler import profile
from random import randrange
import numpy


#  Исходный код
@profile
def change():
    my_list = [randrange(1000) for _ in range(100000)]
    for i in range(0, len(my_list) // 2 * 2, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


#  Оптимизированный код
@profile
def change_numpy():
    my_list = numpy.array([randrange(1000) for _ in range(100000)])
    for i in range(0, len(my_list) // 2 * 2, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


if __name__ == '__main__':
    change()
    change_numpy()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     30.8 MiB     30.8 MiB           1   @profile
    41                                         def change():
    42     35.2 MiB      4.4 MiB      100003       my_list = [randrange(1000) for _ in range(100000)]
    43     35.2 MiB      0.0 MiB       50001       for i in range(0, len(my_list) // 2 * 2, 2):
    44     35.2 MiB      0.0 MiB       50000           my_list[i], my_list[i+1] = my_list[i+1], my_list[i]


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    49     30.8 MiB     30.8 MiB           1   @profile
    50                                         def change_numpy():
    51     34.5 MiB      2.7 MiB      100003       my_list = numpy.array([randrange(1000) for _ in range(100000)])
    52     33.5 MiB     -1.0 MiB       50001       for i in range(0, len(my_list) // 2 * 2, 2):
    53     33.5 MiB      0.0 MiB       50000           my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

"""

"""
Сократили использования памяти с помощью библиотеки NumPy и ф-ции array.
"""
