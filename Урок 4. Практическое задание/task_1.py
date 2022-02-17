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


def func_1_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if not nums[i] & 1:
            new_arr.append(i)
    return new_arr


def func_1_3(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if el % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_4(nums):
    new_arr = []
    for i, el in enumerate(nums):
        if not el & 1:
            new_arr.append(i)
    return new_arr


def func_2_1(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_2_2(nums):
    return [i for i in range(len(nums)) if not nums[i] & 1]


def func_2_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


def func_2_4(nums):
    return [i for i, el in enumerate(nums) if not el & 1]


list_comprehension = "списковое включение"
cycle_and_append = "цикл с append"
div_mod = "остаток от деления"
one_bit = "сравнение 1-го бита"
value_to_index = "доступ к элементу по индексу"
usage_enumerate = "использование enumerate"

text = [cycle_and_append, list_comprehension, value_to_index, usage_enumerate, div_mod, one_bit]

for i in range(4*2):
    cycle_or_lc = i // 4 + 1
    variant = i % 4 + 1
    print(f'func_{cycle_or_lc}_{variant} {timeit(f"func_{cycle_or_lc}_{variant}(range(10000))", globals=globals(), number=1000):>20} '
          f'{text[cycle_or_lc - 1]} + {text[2 + (i // 2 & 1)]} + {text[4 + (i & 1)]}')

"""
Результат:
Заменил операцию деления с остатком на сравнение 1-го бита, цикл с append на списковое включение,
а также взятие по индексу на enumerate/


func_1_1             8.389822 цикл с append + доступ к элементу по индексу + остаток от деления
func_1_2            7.0117157 цикл с append + доступ к элементу по индексу + сравнение 1-го бита
func_1_3    4.521797100000001 цикл с append + использование enumerate + остаток от деления
func_1_4   3.5689393000000003 цикл с append + использование enumerate + сравнение 1-го бита
func_2_1    7.406140300000001 списковое включение + доступ к элементу по индексу + остаток от деления
func_2_2    6.946449299999998 списковое включение + доступ к элементу по индексу + сравнение 1-го бита
func_2_3   3.9360196999999957 списковое включение + использование enumerate + остаток от деления
func_2_4    3.550892400000002 списковое включение + использование enumerate + сравнение 1-го бита

Использование enumerate вместо цикла по range и взятия элемента по индексу, судя по замерам, является предпочтительным.
Также замена остатка от деления на 2 на битовое сравнение с единицей позволяет ускорить работу программы.
Замена цикла с append на списковое включение также ускоряет работу.
"""