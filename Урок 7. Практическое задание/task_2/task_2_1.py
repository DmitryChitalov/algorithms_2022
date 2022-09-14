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
from random import randint
from sys import setrecursionlimit
from timeit import timeit

setrecursionlimit(10000)


def gnome_sorts(my_list):
    index = 1
    i = 0
    n = len(my_list)
    while i < n - 1:
        if my_list[i] <= my_list[i + 1]:
            i, index = index, index + 1
        else:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    return my_list


def my_median(my_lst):
    len_my_lst = len(my_lst)
    sort_my_copy_lst = gnome_sorts(my_lst[:])
    return sort_my_copy_lst[len_my_lst // 2]


def inp_m_get_my_lst(m):
    len_my_lst = 2 * m + 1
    orig_list = [randint(-100, 100) for _ in range(len_my_lst)]
    return orig_list


orig_list_10 = inp_m_get_my_lst(10)
print(f'gnome_sorts(orig_list_10[:]): {gnome_sorts(orig_list_10[:])}.')
print(f'my_median(orig_list_10): {my_median(orig_list_10)}.')
print('orig_list_10 ', orig_list_10)
# замеры 10
print(
    timeit(
        "my_median(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list_100 = inp_m_get_my_lst(100)
print(f'my_median(orig_list_100[:]): {my_median(orig_list_100[:])}.')
# замеры 100
print(
    timeit(
        "my_median(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list_1000 = inp_m_get_my_lst(1000)
print(f'my_median(orig_list_1000[:]): {my_median(orig_list_1000[:])}.')
# замеры 1000
print(
    timeit(
        "my_median(orig_list_1000[:])",
        globals=globals(),
        number=1000))

"""
gnome_sorts(orig_list_10[:]): [-73, -72, -70, -53, -37, -20, -16, -13, 0, 2, 11, 33, 34, 34, 57, 72, 79, 83, 91, 97, 100].
my_median(orig_list_10): 11.
orig_list_10  [100, -70, -20, 34, 72, -72, -73, -37, 57, -13, -53, 0, 83, 11, 2, 33, 79, -16, 34, 91, 97]
0.06191299999999997
my_median(orig_list_100[:]): -7.
7.5726251
my_median(orig_list_1000[:]): 0.
909.2737175999999
"""
