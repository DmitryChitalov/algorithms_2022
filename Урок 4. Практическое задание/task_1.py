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

def func_2(nums):
    return list(range(0,len(nums),2))

t1 = Timer(stmt= "func_1(list(range(500)))", setup="from __main__ import func_1")
print(t1.timeit())

t2 = Timer(stmt= "func_2(list(range(500)))", setup="from __main__ import func_2")
print(t2.timeit())

#Замена цикла на заполнение списка через функцию range() ускорило работу функции