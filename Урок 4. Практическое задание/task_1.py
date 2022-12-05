"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

"""
Оптимальным для заполнения данного списка является традиционный итератор, аналитика для 1000 вызовов:
время выполнения итератора: 0.0007946999999999954
время выполнения lc: 0.0015949999999999992
"""

from timeit import timeit


# традиционный итератор с функцией append:
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# list comprehension:
def func_lst_comp(nums):
    my_lst = [i for i in range(0,len(nums)) if nums[i] % 2 == 0]
    return my_lst


lst_numbers = [1, 2, 3, 4, 5]
print(func_1(lst_numbers))
print(func_lst_comp(lst_numbers))

print(timeit("func_1(lst_numbers)", setup="from __main__ import func_1, lst_numbers", number=1000))
print(timeit("func_lst_comp(lst_numbers)", setup="from __main__ import func_lst_comp, lst_numbers", number=1000))
