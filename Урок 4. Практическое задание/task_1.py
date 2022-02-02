"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = list(filter(lambda i: nums[i] % 2 == 0, range(len(nums))))
    return new_arr


def func_3(nums):
    new_arr = []
    for i, num in enumerate(nums):
        if num % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_4(nums):
    new_arr = []
    [new_arr.append(i) for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_5(nums):
    new_arr = []
    [new_arr.append(i) for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr


if __name__ == '__main__':
    print(timeit.timeit(
        stmt='func_1(range(1, 1000))',
        setup='from __main__ import func_1',
        number=10000))
    print(timeit.timeit(
        stmt='func_2(range(1, 1000))',
        setup='from __main__ import func_2',
        number=10000))
    print(timeit.timeit(
        stmt='func_3(range(1, 1000))',
        setup='from __main__ import func_3',
        number=10000))
    print(timeit.timeit(
        stmt='func_4(range(1, 1000))',
        setup='from __main__ import func_4',
        number=10000))
    print(timeit.timeit(
        stmt='func_5(range(1, 1000))',
        setup='from __main__ import func_5',
        number=10000))

# import модуля перенес вверх кода (в предыдущем варианте ДЗ был после инструкции if __name__ == '__main__)

# В прошлом варианте ДЗ ориентировался на описание модуля timeit https://docs.python.org/3/library/timeit.html,
# там приведен пример (в конце, предпоследний), в котором import модуля - после иструкции if __name__ == '__main__':

# Мои результаты:
# 1.139483 базовый цикл с range, len
# 1.4697597 filter c приведением к list
# 0.6994737 enumerate в цикле
# 1.1736919000000001 LC с range, len
# 0.7208781000000002 LC c enumerate

