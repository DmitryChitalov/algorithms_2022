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
from random import sample

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

lst_1 = sample(range(1, 10000), 100)

print(func_1(lst_1))
print(timeit("func_1(lst_1)", number=100000, globals=globals()))
print(func_2(lst_1))
print(timeit("func_2(lst_1)", number=100000, globals=globals()))

"""
Функция ls (list comprehensions)  работает быстрее, чем  функция с добавлением элементов в список в цикле.
"""