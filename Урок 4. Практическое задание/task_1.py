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


def func_1(nums_list):
    new_arr = []
    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums_list):
    return [nums_list[i] for i in range(len(nums_list)) if not i % 2]


a = [1, 2, 3, 4, 5, 6, 7]
print('Время выполнения func_1:')
print(f'Для 1000 запусков: {timeit("func_1(a)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("func_1(a)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("func_1(a)", globals=globals(), number=100000)}')
print('-' * 50)
print('Время выполнения func_2:')
print(f'Для 1000 запусков: {timeit("func_2(a)", globals=globals(), number=1000)}')
print(f'Для 10000 запусков: {timeit("func_2(a)", globals=globals(), number=10000)}')
print(f'Для 100000 запусков: {timeit("func_2(a)", globals=globals(), number=100000)}')
print('-' * 50)
print('Вывод: func_2 выполняется быстрее func_1, \n'
      'за счет того, что в func_2 не создается новый список, что дает экономию времени.')
