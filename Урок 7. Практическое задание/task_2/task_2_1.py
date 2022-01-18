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


def gnome_sort(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def median(list, m):
    gnome_sort(list)
    return list[m]


x = 10
list1 = [randint(0, 100) for x in range(2 * x + 1)]
print(timeit("median(list1[:], x)", globals=globals(), number=10))

x = 100
list2 = [randint(0, 100) for x in range(2 * x + 1)]
print(timeit("median(list2[:], x)", globals=globals(), number=10))

x = 1000
list3 = [randint(0, 100) for x in range(2 * x + 1)]
print(timeit("median(list3[:], x)", globals=globals(), number=10))
# 0.00040276800000000473
# 0.046825505
# 4.677191360999999
