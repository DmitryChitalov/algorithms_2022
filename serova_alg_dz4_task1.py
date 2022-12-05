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


print(timeit("func_1([3, 0, 0, 0])", "from __main__ import func_1", number=1000000))


def func_2(numss):
    new_arr_2 = []
    for i, j in enumerate(numss):
        if j % 2 == 0:
            new_arr_2.append(i)
    return new_arr_2


print(timeit("func_2([3, 0, 0, 0])", "from __main__ import func_2", number=1000000))

nums = [5, 2, 8, 12]

new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]

print(timeit('''new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]''',
             globals=globals(),
             number=1000000))

'''"enumerate" замеры показали меньшее время работы функции,
"list comprehensions" - показал время наименьшее, по сравнению с двумя предыдущими
функциями.'''