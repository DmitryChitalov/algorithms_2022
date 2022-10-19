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

Сортировка сделана методом Gnome
Script listing   at lines :  80:102

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


def lst_generator():
    print('\n --- Generating Random List ---  ')
    lst_len = int(input(' Please enter int number (m) : '))
    print(f'\n List will be generated with length of 2m+1 = {2 * lst_len +1 } ')
    return [randint(-100, 100) for _ in range(2 * lst_len + 1)]


lst_object = lst_generator()
i_median = int((len(lst_object) - 1) / 2)
print(f' list_obj : \n {lst_object}')
lst_object_sorted = gnome_sort(lst_object[:])
print(f' list_obj_sorted : \n {lst_object_sorted}')
print(f' Median index = {i_median} ,  Median value  = {lst_object_sorted[i_median]}')
lst_object_sorted = gnome_sort(lst_object[:])

print(f'\n  --- Timing of Gnome Sorting: ---')
for i in range(1, 4):
    list_len = 10 ** i + 1
    print(f'\n for list of size {list_len}')
    lst_object = [randint(-100, 100) for _ in range(list_len)]
    # print(f' list_obj = {lst_object}')
    # lst_object_sorted = gnome_sort(lst_object[:])
    # print(f' Sorted list_obj = {lst_object_sorted}')
    print(' Sorting time (sec) = ', end='')
    print(timeit("gnome_sort(lst_object[:])", globals=globals(), number=1000))

#
# --- Generating Random List ---
# Please enter int number (m) : 7
#
# List will be generated with length of 2m+1 = 15
# list_obj :
# [47, 10, 61, -23, -79, -17, -13, -58, 88, -31, -50, 62, 83, -78, 69]
# list_obj_sorted :
# [-79, -78, -58, -50, -31, -23, -17, -13, 10, 47, 61, 62, 69, 83, 88]
# Median index = 7 ,  Median value  = -13
#
#  --- Timing of Gnome Sorting: ---
#
#  for list of size 11
#  Sorting time (sec) = 0.004903600000000001
#
#  for list of size 101
#  Sorting time (sec) = 0.3836452
#
#  for list of size 1001
#  Sorting time (sec) = 37.4209624
#
# Process finished with exit code 0

