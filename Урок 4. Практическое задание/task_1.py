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


def lc(nums):
    new_arr = [x for x in range(len(nums)) if x % 2 == 0]


setup = 'from __main__ import '
test_list = [x for x in range(10000)]

print(f'Функция func_1 - ',
      timeit('func_1(test_list)',
             setup=setup + 'func_1, test_list', number=10000))

print(f'Функция lc -',
      timeit('lc(test_list)',
             setup=setup + 'lc,' + ' test_list', number=10000))


# func_1 выполняется за 15.413346971
# lc выполняется за 9.000430900999998
# list comprehensions выполняется в 2 раза быстрее с одинаоквыми вводными
