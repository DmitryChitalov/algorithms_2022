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

def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if not nums[i] % 2:
            new_arr.append(i)
    return new_arr

def func_3(nums):
    new_arr = [i for i in range(len(nums)) if not nums[i] % 2]
    return new_arr


def func_4(nums):
    new_arr = []
    l = len(nums) - 1
    while l:
        if not nums[l] % 2:
            new_arr.append(l)
        l = l - 1
    return new_arr

my_list = [3,2,5,6,4,8,9,11,6,9]
my_big_list = list(range(1, 100))

# print(func_1(my_list))
print('оригинальная функция')
print(timeit('func_1(my_list)', globals=globals()))
print(timeit('func_1(my_big_list)', globals=globals()))

# print(func_2(my_list))
print('Замена == 0 на not')
print(timeit('func_2(my_list)', globals=globals()))
print(timeit('func_2(my_big_list)', globals=globals()))

# print(func_3(my_list))
print('list comprehension')
print(timeit('func_3(my_list)', globals=globals()))
print(timeit('func_3(my_big_list)', globals=globals()))

# print(func_4(my_list))
print('while')
print(timeit('func_4(my_list)', globals=globals()))
print(timeit('func_4(my_big_list)', globals=globals()))


"""
Аналитика. 
1. Замена == 0 на not ускоряет работу функции. Проверка числа на 0 работает быстрее, чем сравнение целых чисел.
   Независимо от объёма данных.
2. List comprehensions работает быстрее, чем цикл for, на большом объёме данных, потому что это встроенная функция.
   Если объём даннных небольшой - оригинальная функция работает быстрее.
3. Цикл while работает быстрее на небольшом объёме данных, потому что не использует итерацию.
   На большом объёме данных оригинальная функция работает быстрее.
   
"""