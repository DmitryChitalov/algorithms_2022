"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(array):
    return [i for i in range(len(array)) if array[i] % 2 == 0]


import timeit
from random import randrange

array = [randrange(1000) for _ in range(10000)]
print(f"Время {timeit.timeit('func_1(array)', setup='from __main__ import func_1, array', number=1000):.5f} cek")
print(f"Время {timeit.timeit('func_2(array)', setup='from __main__ import func_2, array', number=1000):.5f} cек")

"""
Были сделаны следующие изменения: цикл заменен на LC.  
Время выполнения кода уменьшилось, процентов на 15-20
"""
