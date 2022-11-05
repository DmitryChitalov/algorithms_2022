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

def gnome(data):
    l = 1
    size = len(data)
    while l < size:
        if data[l - 1] <= data[l]:
            l += 1
        else:
            data[l - 1], data[l] = data[l], data[l - 1]
            if l > 1:
                l -= 1
    return data

m = 10

median = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('gnome(median[:])', globals=globals(), number=100)) # 0.013843500055372715

m = 100

median_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('gnome(median_2[:])', globals=globals(), number=100)) # 0.8132964000105858

m = 1000

median_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('gnome(median_3[:])', globals=globals(), number=100)) # 77.76532300002873