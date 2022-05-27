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
    return [idx for idx, i in enumerate(nums) if i % 2 == 0]


numss = [1,1,1,1,1,1,1,1,1]
print(func_1(numss))
print(func_2(numss))

print(
    timeit(
        "func_1([1,1,1,1,1,1,1,1,1])",
        setup='from __main__ import func_1',
        number=100000))

print(
    timeit(
        "func_2([1,1,1,1,1,1,1,1,1])",
        setup='from __main__ import func_2',
        number=100000))

"""
[]
[]
0.0986506
0.09083469999999999
мы не создаем список новый и применили List Comprehension - и это быстрее
"""
