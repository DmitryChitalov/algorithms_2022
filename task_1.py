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

nums = [i for i in range(30)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(i for i in nums if i % 2 == 0)
    return new_arr


print(timeit("func_1(nums)", globals=globals()))
print(timeit("func_2(nums)", globals=globals()))
print(timeit("func_3(nums)", globals=globals()))

"""
Замеры времени:
8.199235600000002
4.8105236
5.6505282999999995

Вывод: код выполняется почти в два раза быстрее, если использовать списковое включение
"""
