"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import random
from timeit import timeit


def max_med(obj, m):
    my_list = obj[:]
    while m > 0:
        my_list.pop(my_list.index(max(my_list)))
        m -= 1
    return my_list.pop(my_list.index(max(my_list)))


if __name__ == '__main__':
    m1 = 10
    m2 = 100
    m3 = 1000
    my_list1 = list(round(random.random() * 100) for i in range(2 * m1 + 1))
    my_list2 = list(round(random.random() * 100) for i in range(2 * m2 + 1))
    my_list3 = list(round(random.random() * 100) for i in range(2 * m3 + 1))

    print(max_med(my_list1, m1), timeit('max_med(my_list1, m1)', globals=globals(), number=100))
    print(max_med(my_list2, m2), timeit('max_med(my_list2, m2)', globals=globals(), number=100))
    print(max_med(my_list3, m3), timeit('max_med(my_list3, m3)', globals=globals(), number=100))
