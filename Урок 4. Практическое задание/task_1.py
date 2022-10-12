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
    return [index for index in range(len(nums)) if nums[index] % 2 == 0]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(timeit("func_1(a)", globals=globals(), number=100000))
print(timeit("func_2(a)", globals=globals(), number=100000))

"""
анализ:
func_2 работает быстрее, т.к. используется list comprehension
"""