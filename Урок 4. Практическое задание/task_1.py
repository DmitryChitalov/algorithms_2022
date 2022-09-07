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
    """четные элементы"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """Сохранение индексов четных элементов"""
    new_arr = []
    for i, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_3(nums):
    """Сохранение индексов четных элементов"""
    new_arr = [i for i, val in enumerate(nums) if val % 2 == 0]
    return new_arr


num = range(100)
print(timeit('func_1(num)', globals=globals()))
print(timeit('func_2(num)', globals=globals()))
print(timeit('func_3(num)', globals=globals()))

""" 
19.78885569999693
 - время функции func_1, происходит выбор элемента из списка по индексу
 
13.687750300043263
 - время функции func_2, через enumerate не происходит поиск элемента по индексу.
 
9.901547499990556
 - время функции func_3, новый список формируется с помощью list comprehensions
"""
