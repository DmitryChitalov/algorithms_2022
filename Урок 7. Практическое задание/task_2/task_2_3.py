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


def median_elem(el):
    return median(el)


print('замеры 10')
m = 5
orig_list_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_1[:])", globals=globals(), number=1000))

print('замеры 100')
m = 50
orig_list_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_2[:])", globals=globals(), number=1000))

print('замеры 1000')
m = 500
orig_list_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_3[:])", globals=globals(), number=1000))

"""Поиск медианы быстрее всего функцией median из библиотеки statistics"""
