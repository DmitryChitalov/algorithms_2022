"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    len_nums = len(nums)
    return [i for i in range(len_nums) if nums[i] % 2 == 0]


print(func_2((1, 2, 4, 5, 6)))
print(func_3((1, 2, 4, 5, 6)))

t1 = Timer(stmt='func_1', setup='from __main__ import func_1')
print("Не оптимизированная функция func_1", t1.timeit(number=10000000), 'seconds')

t1 = Timer(stmt='func_2', setup='from __main__ import func_2')
print("Оптимизированная функция func_2", t1.timeit(number=10000000), 'seconds')

t1 = Timer(stmt='func_3', setup='from __main__ import func_3')
print("Оптимизированная функция func_3", t1.timeit(number=10000000), 'seconds')

# Не оптимизированная функция func_1 0.2125482999254018 seconds
# Оптимизированная функция func_2 0.19864979991689324 seconds
# ВЫВОД: За счет использования LC нам удалось снизить время выполнения кода
