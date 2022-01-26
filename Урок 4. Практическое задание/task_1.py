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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

def func_3(nums):
    new_arr = [v for k, v in enumerate(nums) if not k % 2]
    return new_arr

nums = [randint(0, 1000) for i in range(1000)]


print('func_1', timeit('func_1(nums)', number=1000, globals=globals()))
print('func_2', timeit('func_2(nums)', number=1000, globals=globals()))
print('func_3', timeit('func_3(nums)', number=1000, globals=globals()))

'''
Вывод: list comprehension быстрее цикла for т.к. не добавляет
елемент в список методом append 
'''


