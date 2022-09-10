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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num = [el for el in range(10000)]


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(timeit('func_1(num)', globals=globals(), number=1000))    # 0.9179106999654323
print(timeit('func_1(num)', globals=globals(), number=10000))   # 8.310636900016107
print(timeit('func_2(num)', globals=globals(), number=1000))    # 0.6692180000245571
print(timeit('func_2(num)', globals=globals(), number=10000))   # 6.650976000004448

""" 
Преобразование кода в составители списков ускорило работу кода примерно на 15%
"""
