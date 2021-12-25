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
    new_arr = [i for i in range(len((nums))) if nums[i] % 2 == 0]
    return new_arr

arr=[i for i in range(100)]
print(func_1(arr), '\n', timeit('func_1(arr)', globals=globals()))

# 3.93 сек на выполнение

print(func_2(arr), '\n', timeit('func_2(arr)', globals=globals()))

# 3.29 сек на выполнение. Получилось выполнить оптимизацию путем использования list comprehension, который
# сокращает синтаксис и является оптимизированной встроенной конструкцией

