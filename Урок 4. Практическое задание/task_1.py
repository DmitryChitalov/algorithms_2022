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

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


print(timeit('func_1(lst)', setup='from __main__ import func_1, lst', number=100000))
print(timeit('func_2(lst)', setup='from __main__ import func_2, lst', number=100000))
'''
func_1 затрачивает время - 0.08019680005963892.
Выполнение операции через LC func_2 проходит быстрее - 0.04336240002885461,
из за отсутсвия необходимости использования присвоения .append(i)
'''
