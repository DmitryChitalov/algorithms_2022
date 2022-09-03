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


def ind_odd_el(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def ind_odd_el_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    lst = [*range(10000)]
    print(f'Стандартный иттератор с функцией append: {timeit("ind_odd_el(lst)", globals=globals(), number=10000)}')
    print(f'List comprehension: {timeit("ind_odd_el_2(lst)", globals=globals(), number=10000)}')

''' 
Встроенные функции всегда отрабатывают быстрее, чем написанные вручную. В функции ind_odd_el_2 вместо
стандартного иттератора с функцией append мы используем list comprehension,
чем добиваемся выигрыша по времени 
Стандартный иттератор с функцией append: 10.292098300065845
List comprehension: 7.2434127000160515
'''