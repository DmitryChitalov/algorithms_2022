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

nums = [1,2,3,4]

print(timeit("func_1(nums)", globals=globals()))

print(timeit('''
new_arr = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        new_arr.append(i)
''', globals=globals()))


'''
Вывод: Использовал код на прямую и скорость не много увеличилась.
'''