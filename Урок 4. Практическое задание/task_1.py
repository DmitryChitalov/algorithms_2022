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
    new_arr = [x for x in range(len(nums)) if x % 2 == 0]


setup = 'from __main__ import '
my_list = [x for x in range(10000)]

print(f'Функция {func_1.__name__} выполнена за ', timeit('func_1(my_list)',
                                                         setup=setup + 'func_1, my_list', number=10000))

print(f'Функция {func_2.__name__} выполнена за ', timeit('func_2(my_list)',
                                                         setup=setup + 'func_2,' + ' my_list', number=10000))


"""   Итог:
            Функция func_1 выполнена за  26.5885274
            Функция func_2 выполнена за  15.337786299999998
            Практически в два раза уменьшили время выполнения алгоритма по заполнению списка индексами
            путем использования list comprehensions вместо append
            Не смотря на то, что оба алгоритма имеют сложноть O(n) - lc с одинаковыми входными данными
            выполняется быстрее.
"""