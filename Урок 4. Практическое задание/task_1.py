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

lst = list(range(0, 10))

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return map(lambda item: item[0], filter(lambda x: not x[1] % 2, enumerate(nums)))
t_1 = timeit('func_1(lst)', globals=globals(), number=1000)
t_2 = timeit('func_2(lst)', globals=globals(), number=1000)
print('Время выполнения append = ', round(t_1, 3))
print('Время выполнения map = ', round(t_2, 3))
# встроенная функция map() работает быстрее, чем метод append()
