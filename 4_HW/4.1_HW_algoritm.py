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


# решение range
# func_1 ---- 0.3542557
# Самый долгий вариант
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# решение enumerate
# func_2 ---- 0.3422023999999999
# Быстрее, но не значительнее
def func_2(nums):
    new_arr = []
    for i, j in enumerate(nums):
        if j % 2 == 0:
            new_arr.append(j)
    return new_arr


# LC в связке с range
# func_3 ---- 0.29449310000000006
# функция показывает наулучший результат
def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# LC в связке с range
# func_4 ---- 0.3023156
# функция показывает наулучший результат
def func_4(nums):
    new_arr = [i for i, j in enumerate(nums) if j % 2 == 0]
    return new_arr


my_list = [i for i in range(1, 1000, 3)]

print(f'func_1 ---- {timeit("func_1(my_list)", globals=globals(), number=10000)}')
print(f'func_2 ---- {timeit("func_2(my_list)", globals=globals(), number=10000)}')
print(f'func_3 ---- {timeit("func_3(my_list)", globals=globals(), number=10000)}')
print(f'func_4 ---- {timeit("func_4(my_list)", globals=globals(), number=10000)}')
