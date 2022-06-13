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

import random
from timeit import timeit


def my_med(my_list, m):
    seq = my_list[:]
    i, j, size = 1, 2, len(seq)
    while i < size:
        if seq[i - 1] <= seq[i]:
            i, j = j, j + 1
        else:
            seq[i - 1], seq[i] = seq[i], seq[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return seq[m]


if __name__ == '__main__':
    m1 = 10
    m2 = 100
    m3 = 1000
    my_list1 = list(round(random.random() * 100) for i in range(2 * m1 + 1))
    my_list2 = list(round(random.random() * 100) for i in range(2 * m2 + 1))
    my_list3 = list(round(random.random() * 100) for i in range(2 * m3 + 1))

    print(my_med(my_list1, m1), timeit('my_med(my_list1, m1)', globals=globals(), number=1000))
    print(my_med(my_list2, m2), timeit('my_med(my_list2, m2)', globals=globals(), number=1000))
    print(my_med(my_list3, m3), timeit('my_med(my_list3, m3)', globals=globals(), number=1000))
