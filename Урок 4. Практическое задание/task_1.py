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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums_lst = list(range(0, 100))

print(timeit("func_1(nums_lst)", globals=globals(), number=100000))
print(timeit("func_2(nums_lst)", globals=globals(), number=100000))

"""
Заполнение списка быстрее проходит с помощью LC,
выигрываем по скорости т.к. не вызываем метод append
append = 0.898640899999009
LC = 0.630033800000092
"""
