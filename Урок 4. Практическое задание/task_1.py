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


def func_opt(nums):
    return [i for i in nums if i % 2 == 0]


numbers = [el for el in range(100)]

print(
    timeit(
        "func_1(numbers[:])",
        globals=globals(),
        number=1000
    )
)

print(
    timeit(
        "func_opt(numbers[:])",
        globals=globals(),
        number=1000
    )
)

'''
до оптимизации суммарное время выполнения было 0.010827400023117661.
Для оптимизации был применен метод list comprehensions, после чего суммарное время выполнения стало 0.006784299970604479
'''
