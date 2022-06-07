"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на две равные по длине части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.

Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла, Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from statistics import median
from timeit import timeit

range_numbers10 = [randint(-100, 100) for _ in range(0, 2*10+1)]
range_numbers100 = [randint(-100, 100) for _ in range(0, 2*100+1)]
range_numbers1000 = [randint(-100, 100) for _ in range(0, 2*1000+1)]


# Гномья
def gnome_sort(arr, m):
    n = len(arr)
    i = 0
    while i < n:
        if i == 0:
            i = i + 1
        if arr[i] >= arr[i - 1]:
            i = i + 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    return arr[m]


# print(range_numbers10)
# print(median(range_numbers10))
# print(gnome_sort(range_numbers10, 10))
# print(median(range_numbers100))
# print(median(range_numbers1000))


print(
    timeit(
        "gnome_sort(range_numbers10[:], 10)",
        setup='from __main__ import gnome_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "gnome_sort(range_numbers100[:], 100)",
        setup='from __main__ import gnome_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "gnome_sort(range_numbers1000[:], 1000)",
        setup='from __main__ import gnome_sort',
        globals=globals(),
        number=100))

"""
0.0041797000000000015
0.3993154
41.5763291
"""