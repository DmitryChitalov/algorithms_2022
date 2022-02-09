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


# Замена итератора из первой функции на list comprehension. Немного снизит время выполнения кода.
def func_2(nums):
    new_arr = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# Скопировать элементы массива из текущего в новый, но с проверкой делится ли элемент без остатка на 2.
# Снижает время выполнения кода примерно в 2 раза.
def func_3(nums):
    return [el for el in nums if el % 2 == 0]


# Срез массива с шагом 2, применимо только если числа в массиве стоят по порядку, начиная с 0.
# Значительно снижает время выполнения кода.
def func_4(nums):
    new_arr = nums[0:len(nums):2]
    return new_arr


my_list = list(range(10000))
print(timeit('func_1(my_list)', globals=globals(), number=1000))
print(timeit('func_2(my_list)', globals=globals(), number=1000))
print(timeit('func_3(my_list)', globals=globals(), number=1000))
print(timeit('func_4(my_list)', globals=globals(), number=1000))
"""
func_1 - 1.2774304
func_2 - 1.0799268999999998
func_3 - 0.544997
func_4 - 0.03562680000000018
"""
