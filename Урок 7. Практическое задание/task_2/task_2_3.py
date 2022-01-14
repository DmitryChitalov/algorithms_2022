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
from timeit import timeit
from random import randint


def find_median(lst):
    return median(lst)


# Замеры в списке длиной 11

m = 5
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 101

m = 50
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 1001

m = 500
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Результаты: 0.00035 сек, 0.0022 сек и 0.031 сек
# Эффективнее всех оказался встроенный метод поиска медианы из модуля statistics. Медленнее всех
# оказалась гномья сортировка
