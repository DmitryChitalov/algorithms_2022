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


arr_origin = [randint(-100, 100) for _ in range(11)]
print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

#замеры 11
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(101)]

print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 101
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))


arr_origin = [randint(-100, 100) for _ in range(1001)]

print(arr_origin)
print(sorted(arr_origin[:]))
med = statistics_median(arr_origin[:])  # Вычисление медианы массива.
print(med)

# замеры 1001
print(
    timeit(
        "statistics_median(arr_origin[:])",
        globals=globals(),
        number=1000))

"""
Функция median из модуля statistics даёт самый лучший результат по поиску медианы массива, цыфры ещё на порядок лучше,
чем при поиске удалением как в прошлом задании.

0.0018495999975129962 - 11 элементов
0.00981560000218451 - 101 элементов
0.20207640004809946 - 1001 элементов
"""