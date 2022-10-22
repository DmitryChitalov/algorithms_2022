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

m = 5
origin_list_11 = [randint(-100, 100) for _ in range(2*m + 1)]

m = 50
origin_list_101 = [randint(-100, 100) for _ in range(2*m + 1)]

m = 500
origin_list_1001 = [randint(-100, 100) for _ in range(2*m + 1)]


def find_median(lst_obj):
    my_med = median(lst_obj)
    return my_med


# замеры для 11
print(
    timeit(
        "find_median(origin_list_11[:])",
        globals=globals(),
        number=1000))

# замеры для 101
print(
    timeit(
        "find_median(origin_list_101[:])",
        globals=globals(),
        number=1000))

# замеры для 1001
print(
    timeit(
        "find_median(origin_list_1001[:])",
        globals=globals(),
        number=1000))

# 0.0006553750135935843
# 0.0044763330079149455
# 0.06599670799914747

"""
Самый быстрый способ на основе замеров - функция median из библиотеки 
statistics, на втором месте оказался с пособ с поиском максимального элемента
и удалением его, на третьем месте гномья сортировка.
"""
