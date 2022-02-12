"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def max_del(array):
    n = len(array)

    for i in range(n // 2):
        array.remove(max(array))
    return max(array)


# замеры для 11 элементов
array = [randint(1, 1000) for i in range(11)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))

# замеры для 101 элемента
array = [randint(1, 1000) for i in range(101)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))

# замеры для 1001 элемента
array = [randint(1, 1000) for i in range(1001)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))

'''
0.0033955999999999986
0.0960338
7.976641800000001
'''
