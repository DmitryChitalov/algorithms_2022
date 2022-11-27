"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


test_list = [i for i in range(10**3)]
# print(test_list)

t1 = Timer(stmt="func_1(test_list)", setup="from __main__ import func_1, test_list")
print("append -", t1.timeit(number=100000), "sec")
# print(func_1(test_list))
print('-'*100)

"""
append - 6.450531599999522 sec
"""


# Можно использовать генератор с ф-ей enumerate:
def test_lst_compr_enum(nums):
    new_arr = [key for key, value in enumerate(nums) if not value % 2]
    return new_arr


t2 = Timer(stmt="test_lst_compr_enum(test_list)", setup="from __main__ import test_lst_compr_enum, test_list")
print("list comprehension + enumerate -", t2.timeit(number=100000), "sec")
# print(test_lst_compr_enum(test_list))
print('-'*100)

"""
list comprehension + enumerate - 5.299689699997543 sec
"""
