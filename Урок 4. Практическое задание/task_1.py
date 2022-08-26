"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# def func_2(nums):
#     return f'{[i for i in range(len(nums)) if nums[i] % 2 == 0]}'

def func_3(nums):
    my_list = []
    for k,v in enumerate(nums):
        if v % 2 == 0:
            my_list.append(k)
    return my_list


my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(func_1(my_arr))
print(func_3(my_arr))
print(timeit.timeit('func_1(my_arr)', number=10000, globals=globals()))
print(timeit.timeit('func_3(my_arr)', number=10000, globals=globals()))

# Использовал enumerate.Получил кортеж, который в силу своей неизменяемости эффективнее списка при работе с памятью
