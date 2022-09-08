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

# итератор с функцией append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# итератор с конкатенацией
def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr = new_arr + [i]
    return new_arr


# list comprehension
def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# замеры
some_arr = [el for el in range(10000)]
print('append:    ', timeit("func_1(some_arr[:])", globals=globals(), number=1000))
print('concat:    ', timeit("func_2(some_arr[:])", globals=globals(), number=1000))
print('list compr:', timeit("func_3(some_arr[:])", globals=globals(), number=1000))

'''
Замеры показали следующее:

append:     0.47209345900046173
concat:     17.749040790997242
list compr: 0.3588817919990106

Как и ожидалось наибольшее время показала функция с конкатенацией, 
а наименьшее - list comprehension
'''