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


def func_2(num):
    return [i for i in range(len(num)) if num[i] % 2 == 0]


vals = [2, 2, 3, 5, 8, 9, 10]
print(func_2(vals))
# [0, 1, 4, 6]
print(timeit('func_2(vals)', globals=globals(), number=1000))
# 0.0009440999710932374
print(timeit('func_1(vals)', globals=globals(), number=1000))
# 0.001430200063623488
