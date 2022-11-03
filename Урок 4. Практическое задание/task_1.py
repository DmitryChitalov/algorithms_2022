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


list1 = []

for i in range(1000):
    list1.append(i)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1(list1)", globals=globals(), number=1000))


def func_2(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


print(timeit("func_2(list1)", globals=globals(), number=1000))

# Цикл был заменен на list comprehensions который работает быстрее