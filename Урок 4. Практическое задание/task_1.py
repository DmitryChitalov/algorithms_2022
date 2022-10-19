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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr_2 = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr_2


array = [randint(0, 500) for i in range(1000)]

print(timeit("func_1(array)", globals=globals(), number=10000))
print(timeit("func_2(array)", globals=globals(), number=10000))

# 0.7459618999855593
# 0.5664637999725528
# Второй вариант через List Comprehension чуть быстрее, наверно, потому что нет вызовов метода append().
