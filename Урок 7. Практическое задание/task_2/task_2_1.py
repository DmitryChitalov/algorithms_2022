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
from timeit import timeit

# Применил Гномью сортировку - если i элемент списка больше i+1, они меняются и делается один шаг назад


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if i == 0:
            i = 1
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
    return lst


# Алгоритм можно оптимизировать, если запомнить место, с которого начиналось отступление назад и возвращаться сразу туда

def optimized_gnome_sort(lst):
    i, j = 1, 2
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst


def find_median(lst):
    optimized_gnome_sort(lst)
    return lst[m]


# m = 100
# new_list = [randint(-100, 100) for i in range(2 * m + 1)]
# print(timeit("optimized_gnome_sort(new_list[:])", globals=globals(), number=1000))
# print(timeit("gnome_sort(new_list[:])", globals=globals(), number=1000))

# В списке из 201 элемента разница во времени составила 8.36 - 5.41 = 2.95 сек в пользу оптимизированного варианта

# Замеры в списке длиной 11

m = 5
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 101

m = 50
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 1001

m = 500
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Результаты: 0.0039 сек, 0.317 сек и 35.9 сек
