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
    new_arr = [i for i, j in enumerate(nums) if i % 2==0]

    return new_arr


nums = [j * 10 for j in range(51)]


print(func_2(nums))
# print(timeit.timeit("func_1(nums)", globals=globals(), number=1000))
# print(timeit.timeit("func_2(nums)", globals=globals(), number=1000))

"""
LC стабильно быстрее чем добавление в цикле в 1,5 - 2 раза.
Объяняется это тем что LC делается на С внутри интерпретатора, которая часто гораздо выше,
чем скорость выполнения байт-кода циклов for внутри PVM.
"""
