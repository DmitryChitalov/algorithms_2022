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
import statistics

orig_list = [92, 89, 83, 69, 29, -25, -34, -49, -50, -100, 6]

def stat_median(lst_obj):
    return statistics.median(lst_obj)

# замеры 10
orig_list = [randint(-100, 100) for _ in range(10)]
print(
    timeit(
        "stat_median(orig_list[:])",
        globals=globals(),
        number=1000))
# замеры 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(
    timeit(
        "stat_median(orig_list[:])",
        globals=globals(),
        number=1000))
# замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "stat_median(orig_list[:])",
        globals=globals(),
        number=1000))
"""
0.0019038000609725714
0.0083147999830544
0.1833440000191331
"""
