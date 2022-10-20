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
from decimal import Decimal
from timeit import timeit
from random import randint


def built_in_sort(data):
    median = statistics.median(map(Decimal, data))
    return median


orig_list_10 = [randint(1, 888) for _ in range(2 * 10 + 1)]
orig_list_100 = [randint(1, 888) for _ in range(2 * 100 + 1)]
orig_list_1000 = [randint(1, 888) for _ in range(2 * 1000 + 1)]

print(f"Original_massive_10 >>> {orig_list_10}")
print(
    f'Median >>> {built_in_sort(orig_list_10[:])}\n'
    f'Time >>> '
    f'{timeit("built_in_sort(orig_list_10[:])", globals=globals(), number=100)}')

# Original_massive_10 >>>
# [637, 269, 627, 843, 366, 270, 212, 234, 155, 633, 759, 835, 584, 522, 216, 316, 652, 710, 148, 2, 97]
# Median >>> 366
# Time >>> 0.000766493

print(f"Original_massive_100 >>> {orig_list_100}")
print(
    f'Median >>> {built_in_sort(orig_list_100[:])}\n'
    f'Time >>> '
    f'{timeit("built_in_sort(orig_list_100[:])", globals=globals(), number=100)}')

# Median >>> 458
# Time >>> 0.012023848000000004

print(f"Original_massive_1000 >>> {orig_list_1000}")
print(
    f'Median >>> {built_in_sort(orig_list_1000[:])}\n'
    f'Time >>> '
    f'{timeit("built_in_sort(orig_list_1000[:])", globals=globals(), number=100)}')

# Median >>> 441
# Time >>> 0.10763788299999999

"""Конечно, можно с уверенностью сказать, что самы оптимальный вариант получения
медианы - это использование встроенной функции, хотя бы потому, что нам не важна
сортировка в данном случае"""
