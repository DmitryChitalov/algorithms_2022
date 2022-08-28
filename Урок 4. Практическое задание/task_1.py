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

lst_nums = [25, 17, 96, 114, 85, 23, 22, 47, 78, 85, 41, 10]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, val in enumerate(nums) if val % 2 == 0]


def func_3(nums, ind=0, new_arr=[]):
    for i in nums:
        ind += 1
        if i % 2 == 0:
            new_arr.append(ind)
    return new_arr


print(timeit.timeit("func_1(lst_nums)", globals=globals(), number=1000))
print(timeit.timeit("func_2(lst_nums)", globals=globals(), number=1000))
print(timeit.timeit("func_3(lst_nums)", globals=globals(), number=1000))

"""
самым быстрым является способ 2 через генератор списка. попытка изменить способ получения индекса(способ 3)
даёт примерно то же самое время что и способ 1
"""