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
from timeit import Timer
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """В предлагаемой функции цикл был заменен на list comprehension"""
    return [x for x in range(len(nums)) if nums[x] % 2 == 0]  # nums[x] это четные элементы, x это индексы


n = [34, 890, 562, 8998, 82, 773, 92, 91, 95, 84, 89, 75, 43, 94, 88, 75, 71, 95, 128, 845, 854]

"""Первый вариант расчета"""
t1 = Timer(stmt='func_1(n)', setup='from __main__ import func_1', globals=globals())
print('func_1()', t1.timeit(number=1000000), 'second')
t2 = Timer(stmt='func_2(n)', setup='from __main__ import func_2', globals=globals())
print('func_2()', t2.timeit(number=1000000), 'second')

print()
"""Второй вариант расчета"""
print(timeit("func_1(n)", globals=globals(), number=1000000))
print(timeit("func_2(n)", globals=globals(), number=1000000))

"""Результаты немного разнятся. Но отличие хорошо видно на большой выборке. list comprehension немного быстрее"""
