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

nums = 0, 1, 2, 3, 4, 5, 6, 7
print(timeit('func_1(nums)', number=100000, globals=globals()))

def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

print(timeit('func_2(nums)', number=100000, globals=globals()))

# Первая функция: 0.20315479999408126
# Вторая функция: 0.1533573999768123
# За счет истопользования list comprehensions во втором варианте получилось снизить время выполнения кода.