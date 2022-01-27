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
     return [i for i in range(len(nums)) if nums[i] % 2 == 0]

numbers_10 = [i for i in range(10)]
numbers_100 = [i for i in range(100)]
numbers_1000 = [i for i in range(1000)]


print(
    timeit(
        "func_1(numbers_10)",
        setup="from __main__ import func_1, numbers_10", number=1000))

print(
    timeit(
        "func_2(numbers_10)",
        setup="from __main__ import func_2, numbers_10", number=1000))

print(
    timeit(
        "func_1(numbers_100)",
        setup="from __main__ import func_1, numbers_100", number=1000))
print(
    timeit(
        "func_2(numbers_100)",
        setup="from __main__ import func_2, numbers_100", number=1000))

print(
    timeit(
        "func_1(numbers_1000)",
        setup="from __main__ import func_1, numbers_1000", number=1000))

print(
    timeit(
        "func_2(numbers_1000)",
        setup="from __main__ import func_2, numbers_1000", number=1000))

'''
Первую функцию преобразовали через list comprehension.
Время исполнения на 1000 вызовах функции: 
Для списка из 10 элементов:
func_1 = 0.0014162999999999815 +
func_2 = 0.0015248999999999957
Для списка из 100 элементов:
func_1 = 0.010131000000000001
func_2 = 0.007781900000000008  +
Для списка из 1000 элементов:
func_1 = 0.12278860000000003  
func_2 = 0.09598319999999999  +
list comprehension показал лучшее время в двух случаях, с увеличением колличеством эллементов.
При работе с малыми колличествами эллементов функции практически одинаковые, цикл немного быстрее.
Итог: Применять тот или иной метод в зависимости от колличества элементов. 
'''
