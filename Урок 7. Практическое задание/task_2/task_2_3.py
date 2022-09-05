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
from statistics import median
from random import randint
from timeit import timeit


def stat_median(array):
    return median(array[:])


m = 10
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("stat_median(array[:])", globals=globals(), number=1000))  # 0.0006103999999999971

m = 100
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("stat_median(array[:])", globals=globals(), number=1000))  #  0.0054692000000000005

m = 1000
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("stat_median(array[:])", globals=globals(), number=1000)) # 0.13326010000000002

#  Наиболее эффективный способ с помощью встроенной функции median из statistics,
#  худший вариант для больших массивов алгоритм без сортировки
