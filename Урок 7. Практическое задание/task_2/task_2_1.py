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
from timeit import timeit
from random import randint


def sort_gnome(el):
    n, i = len(el), 0
    while True:
        if i + 1 == n:
            break
        if el[i + 1] >= el[i]:
            i += 1
        else:
            el[i], el[i + 1] = el[i + 1], el[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return el


print('замеры 10')
m = 5
orig_list_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("sort_gnome(orig_list_1[:])", globals=globals(), number=1000))

print('замеры 100')
m = 50
orig_list_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("sort_gnome(orig_list_2[:])", globals=globals(), number=1000))

print('замеры 1000')
m = 500
orig_list_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("sort_gnome(orig_list_3[:])", globals=globals(), number=1000))