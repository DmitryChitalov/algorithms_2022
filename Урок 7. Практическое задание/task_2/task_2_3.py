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
import timeit
from random import randint
from statistics import median


def mid_find(lst_in):
    return median(lst_in)


orig_list_10 = [randint(-100, 100) for _ in range(11)]
orig_list_100 = [randint(-100, 100) for _ in range(101)]
orig_list_1000 = [randint(-100, 100) for _ in range(1001)]
print(timeit.timeit(stmt='mid_find(orig_list_10)', globals=globals()))
print(timeit.timeit(stmt='mid_find(orig_list_100)', globals=globals()))
print(timeit.timeit(stmt='mid_find(orig_list_1000)', globals=globals()))
