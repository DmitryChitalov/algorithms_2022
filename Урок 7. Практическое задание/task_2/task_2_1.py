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


def find_median(orig_array, m):
    gnome_sort(orig_array)
    return orig_array[m]


if __name__ == '__main__':
    x = 10
    orig_array = [randint(0, 100) for x in range(2 * x + 1)]
    print(timeit("find_median(orig_array[:], x)", globals=globals(), number=10))

    x = 100
    orig_array = [randint(0, 100) for x in range(2 * x + 1)]
    print(timeit("find_median(orig_array[:], x)", globals=globals(), number=10))

    x = 1000
    orig_array = [randint(0, 100) for x in range(2 * x + 1)]
    print(timeit("find_median(orig_array[:], x)", globals=globals(), number=10))

"""
0.0005097000000000018
0.0480848
4.592765900000001
"""
