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

Это файл для второго скрипта
"""

from random import randint, choice
from memory_profiler import profile

"""
Алгоритмы, урок 2, задание 4
Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Заменил рекурсию на цикл. Получилась экономия памяти

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    61     19.5 MiB     19.5 MiB           1   @profile
    62                                         def wrapper():
    63     20.1 MiB      0.5 MiB           1       res = geometric_progression_short(500)
    64                                             # res = geometric_progression(500)
    65     20.1 MiB      0.0 MiB           1       return res
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    62     19.5 MiB     19.5 MiB           1   @profile
    63                                         def wrapper():
    64                                             # res = geometric_progression_short(500)
    65     19.5 MiB      0.0 MiB           1       res = geometric_progression(500)
    66     19.5 MiB      0.0 MiB           1       return res
"""


@profile
def wrapper():
    # res = geometric_progression_short(500)
    res = geometric_progression(500)
    return res


def geometric_progression_short(n):
    return (-0.5) ** (n - 1) + geometric_progression_short(n - 1) if n else 0


def geometric_progression(n):
    i = 1
    sum_progression = 0
    while i <= n:
        sum_progression += (-0.5) ** (i - 1)
        i += 1
    return sum_progression


print(wrapper())

