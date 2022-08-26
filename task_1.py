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
    new_arr_2 = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr_2


my_arr = [10, 15, 20, 12, 15, 3115, 54, 45, 634]
print(timeit("func_1(my_arr)", globals=globals(), number=1000))  # 0.00245049997465685
print(timeit("func_2(my_arr)", globals=globals(), number=1000))  # 0.001971699995920062

""" списковое включение быстрее чем итератор с функцией append потому что 
вместо того, чтобы создавать пустой список и добавлять каждый элемент в конец,
мы просто определяем список и его содержимое одновременно"""
