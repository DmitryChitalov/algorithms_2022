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
import timeit
from memory_profiler import profile

import numpy


@profile
def func_1():
    nums = [j * 10 for j in range(50000)]
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2():
    nums = numpy.array([j * 10 for j in range(50000)])
    new_arr = numpy.array
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            numpy.append(new_arr, i)
    return new_arr


func_1()
func_2()
'''
Заменил list на array из numpy. Значительный выигрыш по памяти и проигрыш по быстродействию.
# 0.06307230005040765
# 2.5453929000068456
'''
# print(timeit.timeit("func_1()", globals=globals(), number=10))
# print(timeit.timeit("func_2()", globals=globals(), number=10))

import timeit
from memory_profiler import profile

import numpy


@profile
def func_1():
    nums = [j * 10 for j in range(50000)]
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2():
    nums = numpy.array([j * 10 for j in range(50000)])
    new_arr = numpy.array
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            numpy.append(new_arr, i)
    return new_arr


func_1()
func_2()
'''
Заменил list на array из numpy. Значительный выигрыш по памяти и проигрыш по быстродействию.
# 0.06307230005040765
# 2.5453929000068456
'''
# print(timeit.timeit("func_1()", globals=globals(), number=10))
# print(timeit.timeit("func_2()", globals=globals(), number=10))
