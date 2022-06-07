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

Это файл для первого скрипта
"""
from memory_profiler import profile
from timeit import timeit


@profile
def array_func(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.insert(-1, i)
    return new_arr


def gen_return(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


# Generator
@profile
def generator_func(nums):
    return gen_return(nums)


length = list(range(0, 40000))
array_func(length)
generator_func(length)


""""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     20.9 MiB     20.9 MiB           1   @profile
    37                                         def array_func(nums):
    38     20.9 MiB      0.0 MiB           1       new_arr = []
    39     22.0 MiB      0.0 MiB       40001       for i in range(len(nums)):
    40     22.0 MiB      0.6 MiB       40000           if nums[i] % 2 == 0:
    41     22.0 MiB      0.4 MiB       20000               new_arr.insert(-1, i)
    42     22.0 MiB      0.0 MiB           1       return new_arr

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    51     21.5 MiB     21.5 MiB           1   @profile
    52                                         def generator_func(nums):
    53     21.5 MiB      0.0 MiB           1       return gen_return(nums)
"""

# print(
#     timeit(
#         "array_func(list(range(0, 40000)))",
#         setup='from __main__ import array_func',
#         number=1000))
# print(
#     timeit(
#         "generator_func(list(range(0, 40000)))",
#         setup='from __main__ import generator_func',
#         number=1000))

"""
    4.3674467
    0.6844390999999996
    
    Аналитика:
        Заменили стандартный цикл на генератор, он позволяет уменьшить потребляемое кол-во памяти,
        плюс мы не создаём еще один массив внутри функции - new_arr
"""