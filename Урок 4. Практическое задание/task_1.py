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


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


numbers = [55, 22, 17, 21, 99, 35, 28, 14, 31, 22, 21]

# Второй код выполняется немного быстрее, т.к. был использован list comprehension, который работает быстрее, чем
# итератор с функцией append.
print(timeit(stmt='func_1(numbers)', setup='from __main__ import func_1, numbers', number=1000000))  # 2.993225600000187
print(timeit(stmt='func_2(numbers)', setup='from __main__ import func_2, numbers', number=1000000))  # 2.624095000000125
