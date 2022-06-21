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


# замеры для m = 10
m = 10
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))

# замеры для m = 100
m = 100
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))

# замеры для m = 1000
m = 1000
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "max_del(array[:])",
        globals=globals(),
        number=1000))
'''
0.006817799999999999
0.3348047
21.2727815
'''
