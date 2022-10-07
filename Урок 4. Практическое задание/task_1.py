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


arr1 = [23, 2, 65, 72, 74, 8, 5, 33, 111, 6]
print(func_1(arr1))
print(timeit("func_1(arr1)", number=100000, globals=globals()))


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


arr2 = [23, 2, 65, 72, 74, 8, 5, 33, 111, 6]
print(func_2(arr2))
print(timeit("func_1(arr2)", number=100000, globals=globals()))

"""
Для оптимизации использовал list comprehension, скорость выполнения которого выше, чем у цикла for
замеры это подтвердили:
[1, 3, 4, 5, 9]
0.10498380800027007
[1, 3, 4, 5, 9]
0.09343883200017444
"""