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


'''print(timeit("func_1([el for el in range(1000)])", setup="from __main__ import func_1",
             number=1000))
0.23940300000000003'''


def func_2(nums):
    return [el for el in range(nums) if el % 2 != 0]


'''print(timeit("func_2(1000)", setup="from __main__ import func_1",
             number=1000))
0.1406892 lc выполняется быстрее чем append'''

'''print(timeit("[el for el in range(1000) if el%2!=0]", setup="from __main__ import func_1",
             number=1000))
0.0935733 lc без функции еще быстрее, потому что'''
