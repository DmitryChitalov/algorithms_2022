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

def find_median(arrnum):
    return median(arrnum[:])

m = 10

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 0.00030559999868273735

m = 100

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 0.0030718001071363688

m = 1000

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 0.03306139982305467

# Вывод: Самым эффективным способом является использование встроенной функции median