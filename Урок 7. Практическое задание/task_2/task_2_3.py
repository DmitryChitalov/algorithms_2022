"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
import statistics
from random import randint
from timeit import timeit


m = 10
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "statistics.median(rand_list[:])",
        globals=globals(),
        number=100))


m = 100
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "statistics.median(rand_list[:])",
        globals=globals(),
        number=100))


m = 1000
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "statistics.median(rand_list[:])",
        globals=globals(),
        number=100))


'''
8.86249981704168e-05
0.0009031669978867285
0.015303125001082662

Наиболее быстрый способ - использование встроенной функции поиска медианы
'''