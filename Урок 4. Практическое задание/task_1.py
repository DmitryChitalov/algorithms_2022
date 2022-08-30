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


def func_list(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


lst = list(range(1000))
print(timeit('func_1(lst)', globals=globals(), number=10000))
print(timeit('func_list(lst)', globals=globals(), number=10000))

"""
Вывод: удалось ускорить задачу, применив list comprehensions,
который выполняется быстрее, чем  добавление элементов в список в цикле по очереди.
"""

