from timeit import timeit
from random import randint

"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
nums = [randint(1,10000) for i in range(1000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2]
    return new_arr

print(timeit("func_1(nums)",
        setup='from __main__ import func_1, nums',
        number=10000))

print(timeit("func_2(nums)",
        setup='from __main__ import func_2, nums',
        number=10000))

# Использование list comprehension быстрее эквивалентного цикла for,  потому что ему
# не нужно искать список и его метод добавления на каждой итерации. List comrehansion работает быстрее.
