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
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = (i for i, el in enumerate(nums) if el % 2 == 0)
    return new_arr


n = [i for i in range(1000)]

print(f"{timeit('func_1(n)', globals=globals(), number=1000)} - итерация")
print(f"{timeit('func_2(n)', globals=globals(), number=1000)} - list comprehension")
print(f"{timeit('func_3(n)', globals=globals(), number=1000)} - генератор")

"""
Списковые включения отрабатывают быстрее, чем реализация итераторов,
но генераторы работают максимально быстро
"""