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


def gnome(some_list):
    index = 1
    i = 0
    n = len(orig_list)
    while i < n - 1:
        if orig_list[i] <= orig_list[i + 1]:
            i, index = index, index + 1
        else:
            orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
            i -= 1
            if i < 0:
                i, index = index, index + 1
    return orig_list


m = 6
orig_list = [randint(1, 100) for _ in range(2*m + 1)]
print(orig_list)
print(gnome(orig_list))
print(f'медиана - {orig_list[m]}')


m = 5
orig_list = [randint(1, 100) for _ in range(2*m + 1)]
print(
    timeit(
        "gnome(orig_list[:])",
        globals=globals(),
        number=1000))
m = 50
orig_list = [randint(1, 100) for _ in range(2*m + 1)]
print(
    timeit(
        "gnome(orig_list[:])",
        globals=globals(),
        number=1000))
m = 500
orig_list = [randint(1, 100) for _ in range(2*m + 1)]
print(
    timeit(
        "gnome(orig_list[:])",
        globals=globals(),
        number=1000))
