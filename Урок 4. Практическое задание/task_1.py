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


lst = list(range(100000))
func_1(lst)
func_2(lst)
print(f'Время работы функции {func_1.__name__} - {timeit("func_1(lst)", globals=globals(), number=1000)}')
print(f'Время работы функции {func_2.__name__} - {timeit("func_2(lst)", globals=globals(), number=1000)}')

"""

В функции func_2 формирование списка сделал с помощью list comprehension, который быстрее for-циклов, 
что и демонстрирует замер, давая разницу  ~ 5 сек.
Время работы функции func_1 - 21.74166379999997
Время работы функции func_2 - 17.096172800000204

"""