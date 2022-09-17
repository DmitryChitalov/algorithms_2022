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
from random import randint
from timeit import timeit
from statistics import median

mass_10 = [randint(1, 100) for i in range(2 * 5 + 1)]
mass_100 = [randint(1, 100) for j in range(2 * 50 + 1)]
mass_1000 = [randint(1, 100) for k in range(2 * 500 + 1)]


def median_search(data):
    return median(data[:])


print(timeit('median_search(mass_10[:])', globals=globals(), number=1000))
print()
print(timeit('median_search(mass_100[:])', globals=globals(), number=1000))
print()
print(timeit('median_search(mass_1000[:])', globals=globals(), number=1000))