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

Сортировка сделана методом Gnome для списков длиной 11, 101, 1001 элементов
Script listing   at lines :  66:87 ( длинные массивы обрезаны)

сделайте замеры на массивах
- Сделаны на массивах длиной 11, 101, 1001 элементов при numbers = 1000.
замеры времени:
#  for list of size 11
#  Sorting time (sec) = 0.004903600000000001
#
#  for list of size 101
#  Sorting time (sec) = 0.3836452
#
#  for list of size 1001
#  Sorting time (sec) = 37.4209624
#
"""
from random import randint
from timeit import timeit


def gnome_sort(sequence):
    index = 1
    i = 0
    n = len(sequence)
    while i < n:
        # print(sequence)
        if i + 1 == n:
            break
        if sequence[i] <= sequence[i + 1]:
            i, index = index, index + 1
        else:
            sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    return sequence

print(f'\n  --- Result of Gnome Sorting: ---')
for i in range(1, 4):
    list_len = 10 ** i + 1
    print(f'\n for list of size {list_len}')
    lst_object = [randint(-100, 100) for _ in range(list_len)]
    print(f' list_obj = {lst_object}')
    lst_object_sorted = gnome_sort(lst_object[:])
    print(f' Sorted list_obj = {lst_object_sorted}')
    i_median = int((list_len - 1) / 2)
    print(f' Median index = {i_median} ,  Median value  = {lst_object_sorted[i_median]}')
    print(' Sorting time (sec) = ', end='')
    print(timeit("gnome_sort(lst_object[:])", globals=globals(), number=1000))

#
#   --- Result of Gnome Sorting: ---
#
#  for list of size 11
#  list_obj = [-77, 100, -36, 77, 15, 39, -86, -73, 79, 65, -67]
#  Sorted list_obj = [-86, -77, -73, -67, -36, 15, 39, 65, 77, 79, 100]
#  Median index = 5 ,  Median value  = 15
#  Sorting time (sec) = 0.004903600000000001
#
#  for list of size 101
#  list_obj = [64, -3, -40, 33, 41, 53, 11, -89, 8, 48, 14, -42, 89, 24, 4, 87, 43, 58, -17, 3, -41, -74, 94, -83, -23, 80, -20, 17, 23, -95, 2, -58, -26, -28, -76, -69, 23, 51, 29, 38, 91, -60,
#  Sorted list_obj = [-97, -95, -89, -88, -84, -83, -83, -80, -80, -80, -78, -76, -75, -74, -72, -71, -69, -68, -63, -62, -60, -58, -57, -56, -51, -43, -42, -41, -40, -39, -33, -31, -30, -28, -26,
#  Median index = 50 ,  Median value  = 2
#  Sorting time (sec) = 0.3836452
#
#  for list of size 1001
#  list_obj = [91, 60, -50, -34, -81, 44, -81, -92, -42, -4, 25, -22, -22, 97, 29, 92, -97, -32, -63, -5, -68, -42, -30, -84, -40, -93, -69, -47, 94, 41, 15, 64, 94, 41, 75, -92, 17, -66, 31, -92,
#  Sorted list_obj = [-100, -100, -100, -100, -99, -99, -99, -99, -99, -98, -98, -98, -98, -98, -98, -97, -97, -97, -97, -96, -96, -96, -96, -96, -95, -95, -95, -95, -95, -95, -95, -95, -94, -93, -
#  Median index = 500 ,  Median value  = -1
#  Sorting time (sec) = 37.4209624
#
# Process finished with exit code 0

