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

if __name__ == '__main__':

    nums = [i for i in range(100)]
    count = 100000
    print(f'Замер функции func_1: {timeit("func_1(nums)", number=count, globals=globals())}')  #  0.0011
    print(f'Замер функции func_speed: {timeit("func_2(nums)", number=count, globals=globals())}') # 0.0013

"""
Вывод: вместо цикла по массиву я применил list comprehension который в теории работает быстрее в силу того, что не вызывает
метод append у списка. Но по факту первый алгоритм работает немного быстрее.
"""