"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from statistics import median
from random import randint
from timeit import timeit

m = 5
origin_list_11 = [randint(-100, 100) for _ in range(2*m + 1)]
print(origin_list_11)

m = 50
origin_list_101 = [randint(-100, 100) for _ in range(2*m + 1)]

m = 500
origin_list_1001 = [randint(-100, 100) for _ in range(2*m + 1)]


def median_gnom(lst_obj):
    i = 1
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj[int(len(lst_obj) / 2)]


# замеры для 11
print(
    timeit(
        "median_gnom(origin_list_11[:])",
        globals=globals(),
        number=1000))

# замеры для 101
print(
    timeit(
        "median_gnom(origin_list_101[:])",
        globals=globals(),
        number=1000))

# замеры для 1001
print(
    timeit(
        "median_gnom(origin_list_1001[:])",
        globals=globals(),
        number=1000))

# 0.00969624999561347
# 0.5288780830160249
# 54.3194157500111
