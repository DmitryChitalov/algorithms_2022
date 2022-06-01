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

from random import randint
from timeit import timeit


def get_median(array, m):
    for _ in range(m + 1):
        max_ = array.pop(array.index(max(array)))

    return max_


if __name__ == '__main__':
    m = 10
    lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(lst)
    median = get_median(lst, m)
    print(median)

    # замеры 10
    m = 5
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:], m)",
            globals=globals(),
            number=1000))

    # замеры 100
    m = 50
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:], m)",
            globals=globals(),
            number=1000))

    # замеры 1000
    m = 500
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:], m)",
            globals=globals(),
            number=1000))

"""
0.0037669020000000025   # быстрее шелла
0.11629710399999998     # быстрее шелла
9.478593894             # медленнее шелла
"""
