"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import random
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


res = [random.randint(1, 1000) for i in range(100)]

# tst = timeit.Timer(stmt='func_1(res)', setup='from __main__ import func_1')

print(timeit.timeit('func_1(res)', globals=globals()))
print(timeit.timeit('func_2(res)', globals=globals()))

"""
list comprehension работает быстрее чем обработка списка в цикле. Получается алгоритм работает в два раза быстрее
"""