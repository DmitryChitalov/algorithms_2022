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
    return [i for i in nums if i % 2 == 0]


my_lst = [i for i in range(10000)]

print(timeit('func_1(my_lst[:])', globals=globals(), number=10000))

print(timeit('func_2(my_lst[:])', globals=globals(), number=10000))

"""
func_2 - list comprehension, list comprehension значительно быстрее и лаконичнее в написании, 
чем традиционный итератор с функцией append

"""
