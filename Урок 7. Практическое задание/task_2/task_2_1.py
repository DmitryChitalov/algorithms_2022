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

from math import log2
from random import randint
from timeit import timeit


def get_median_by_shell_sort(array, m):
    n = len(array)
    k = int(log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1

    return array[m]


if __name__ == '__main__':
    m = 10
    lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(lst)
    median = get_median_by_shell_sort(lst, m)
    print(median)

    # замеры 10
    m = 5
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median_by_shell_sort(orig_list[:], m)",
            globals=globals(),
            number=1000))

    # замеры 100
    m = 50
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median_by_shell_sort(orig_list[:], m)",
            globals=globals(),
            number=1000))

    # замеры 1000
    m = 500
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median_by_shell_sort(orig_list[:], m)",
            globals=globals(),
            number=1000))

"""
0.010446239000000003
0.145218277
2.5901635140000003
"""
