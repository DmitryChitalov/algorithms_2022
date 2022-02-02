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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda i: i % 2 == 0, nums))
    return new_arr


def func_4(nums):
    new_arr = nums[::2]
    return new_arr


n = list(range(100))
print(timeit("func_1(n)", number=10000, globals=globals()))     # обычный способ
print(timeit("func_2(n)", number=10000, globals=globals()))     # list comprehension
print(timeit("func_3(n)", number=10000, globals=globals()))     # функция filter
print(timeit("func_4(n)", number=10000, globals=globals()))     # срез


# Наибольший эффект по скорости дало использование среза. Полагаю что связано это с тем что
# срез не проверял условие, а просто взял каждый второй индекс

