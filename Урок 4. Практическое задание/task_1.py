from timeit import timeit
"""
Задание 1.

    Приведен код, который позволяет сохранить в
    массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]


setup = 'from __main__ import '
new_list = [i for i in range(10000)]

print(f'Функция {func_1.__name__} выполнена за ', timeit('func_1(new_list)',
                                                         setup=setup + 'func_1, new_list', number=10000))

print(f'Функция {func_2.__name__} выполнена за ', timeit('func_2(new_list)',
                                                         setup=setup + 'func_2,' + ' new_list', number=10000))
"""     Аналитика
    1 функция выполнена за  11.0207844 в то время как 2 выполнена за  7.301035000000001
    Время сократилось почти в 1.5 раза , это происходит за счет того что 
    скорость List comprehension быстрее for-циклов
"""