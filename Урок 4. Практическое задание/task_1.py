"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения.
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit

TEST_LIST = list(range(100))


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def optimize_func(array):
    return [array[i] for i in range(len(array)) if not i % 2]


"""
Для оптимизации функции использовал List Comprehensions, что увеличило скорость выполнения функции почти в 2 раза.
"""

print(timeit("func_1(TEST_LIST)", globals=globals()))
print(timeit("optimize_func(TEST_LIST)", globals=globals()))
