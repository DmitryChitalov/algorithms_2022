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
import timeit
from random import randint


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if lst[i] >= lst[i - 1]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            if i > 1:
                i -= 1
    return lst


def mid_find(lst_in):
    gnome_sort(lst_in)
    ln = len(lst_in)
    if ln % 2 == 0:
        first = lst_in[ln // 2 - 1]
        second = lst_in[ln // 2]
        return (first + second) / 2
    else:
        return lst_in[ln // 2]


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit.timeit(stmt='mid_find(orig_list_10)', globals=globals(), number=10000))
print(timeit.timeit(stmt='mid_find(orig_list_100)', globals=globals(), number=10000))
print(timeit.timeit(stmt='mid_find(orig_list_1000)', globals=globals(), number=10000))
