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

# Найдём медиану массива с использованием модуля statistics и функции median.

def statistics_median(lst_obj):
    """ Возвращает медиану массива с использованием модуля statistics и функции median."""

    return median(lst_obj)

m = 10

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

#замеры 21
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))

m =100

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 201
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))

m = 1000

arr_origin = [randint(-100, 100) for _ in range(2*m + 1)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 2001
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))

"""
Функция median из модуля statistics даёт самый лучший результат по поиску медианы массива, цыфры ещё на порядок лучше,
чем при поиске удалением как в прошлом задании.

0.0021138000302016735 - 21 элементов
0.019462700001895428 - 201 элементов
0.019462700001895428 - 2001 элементов
"""