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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, x in enumerate(nums) if x % 2 == 0]


if __name__ == '__main__':
    my_nums = [randint(1, 1000) for my_num in range(1000)]

    print(timeit("func_1(my_nums)", number=10000, globals=globals()))
    print(timeit("func_2(my_nums)", number=10000, globals=globals()))

"""
List comprehension выигрывает по скорости из-за того, то не вызывает метод append у списка
"""