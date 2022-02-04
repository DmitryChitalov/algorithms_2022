"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import random
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


num = [random.randint(0, 100) for i in range(10000)]
print(timeit("func_1(num)", number=1000, globals=globals()))  # 1.234651003
print(timeit("func_2(num)", number=1000, globals=globals()))  # 0.9411927690000002
# сделан массив случайных чисел из 10000 элементов, подразумевалось что
# LC работают гораздо быстрее, что и было получено в ходе измерений через timeit
