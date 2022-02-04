"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit
from random import randint
from numpy import array, where


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


def func_3(nums):
    intarray = array(nums)
    return where(intarray % 2 == 0)


my_nums = [randint(1, 1000) for my_num in range(1000)]

print(timeit("func_1(my_nums)", number=10000, globals=globals()))
print(timeit("func_2(my_nums)", number=10000, globals=globals()))
print(timeit("func_3(my_nums)", number=10000, globals=globals()))

"""
из встроенных функций вариант с list comprehension работает быстрее
вариант с использованием numpu работает быстре из-за внутренней оптимизации 
модуля numpy
"""
