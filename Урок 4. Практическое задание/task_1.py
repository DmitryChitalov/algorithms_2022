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
    return [num for num in nums if num % 2 == 0]


if __name__ == '__main__':
    num_list = list(range(100))
    print(timeit("func_1(num_list)", setup='from __main__ import func_1, num_list', number=10000))
    print(timeit("func_2(num_list)", setup='from __main__ import func_2, num_list', number=10000))

# в func_2 используется list comprehensions, отсутствует создание пустого списка и не используется append
# поэтому func_2 отрабатывает быстрее
