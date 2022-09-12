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


test_nums = [x for x in range(10**3)]

print(f'Время выполнения "{func_1.__name__}: {timeit("func_1(test_nums)", globals=globals(), number=1000)}')


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(f'Время выполнения "{func_2.__name__}: {timeit("func_2(test_nums)", globals=globals(), number=1000)}')

"""
АНАЛИТИКА
Listcomp формирует список быстрее, чем "штатная" функция append, следовательно
скорость выполнения func_2 должна быть выше, что и подтверждается замерами:

Время выполнения "func_1: 0.1949395
Время выполнения "func_2: 0.1583195
"""
