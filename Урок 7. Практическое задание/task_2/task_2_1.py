"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решиоте задачу тремя спсобами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import random
from timeit import timeit


def shella_sort(array):
    gap = len(array) // 2

    while gap:
        for idx in range(gap, len(array)):
            current_val = array[idx]
            possition = idx

            while possition >= gap and array[possition - gap] > current_val:
                array[possition] = array[possition - gap]
                possition -= gap
                array[possition] = current_val

        gap //= 2

    return array


def find_median(array, m):
    shella_sort(array)
    return array[m]


if __name__ == '__main__':
    m = 5  # 10 elems
    m2 = 50  # 100 elems
    m3 = 500  # 1000 elems
    #
    a = [random.randint(1, 100) for x in range(2 * m + 1)]
    a2 = [random.randint(1, 100) for x in range(2 * m2 + 1)]
    a3 = [random.randint(1, 100) for x in range(2 * m3 + 1)]

    print('10')
    print(
        timeit(
            "find_median(a, m)",
            globals=globals(),
            number=1000))
    print('100')
    print(
        timeit(
            "find_median(a2, m2)",
            globals=globals(),
            number=1000))
    print('1000')
    print(
        timeit(
            "find_median(a3, m3)",
            globals=globals(),
            number=1000))
