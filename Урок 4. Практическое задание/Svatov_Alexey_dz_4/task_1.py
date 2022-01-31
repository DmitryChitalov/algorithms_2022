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
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


nums_old = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(timeit("func_1(nums_old)", setup='from __main__ import func_1, nums_old', number=100000))
# время=0.9244872720000785

print(timeit("func_2(nums_old)", setup='from __main__ import func_2, nums_old', number=100000))
# время=0.35628081799995925

"""
Обычный цикл for in заменён list comprehention (lc), который работает быстрее цикла.
Это является одним из приёмов, применяемых при рефакторинге.
"""
