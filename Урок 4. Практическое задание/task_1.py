"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

""" 
---Что сделал и выводы---
Для оптимизации кода воспользовался list comprehension.
Это позволило сократить время выполнения кода и немного улучшить его читаемость.
"""
from timeit import timeit  # Импорт timeit

lst_num = [i for i in range(0, 1001)]  # Генерация списка


def func_1(nums):  # Исходная функция
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print('Время выполнения функции func_1')
print(
    timeit(
        "func_1(lst_num)",
        setup='from __main__ import func_1, lst_num',
        number=10000))


def func_2(lst_nums):  # Функция с использованием list comprehension
    return [i for i in range(len(lst_nums)) if lst_nums[i] % 2 == 0]


print('Время выполнения функции func_2')
print(
    timeit(
        "func_2(lst_num)",
        setup='from __main__ import func_2, lst_num',
        number=10000))
