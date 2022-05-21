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
    """Вариант с list comprehension ускоряет работу функции в 2,5 раза"""
    return [i for i in nums if i % 2 == 0]


if __name__ == '__main__':
    nums = list(range(1000))
    print(timeit("func_1(nums)", "from __main__ import func_1, nums", number=1000))  # 0.12146970700000001
    print(timeit("func_2(nums)", "from __main__ import func_2, nums", number=1000))  # 0.053170314999999996
