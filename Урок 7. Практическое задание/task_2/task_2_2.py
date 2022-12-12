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


def get_median(array: list, m):
    for x in range(m):
        array.remove(max(array))
    return max(array)


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
            "get_median(a[:], m)",
            globals=globals(),
            number=1000))
    print('100')
    print(
        timeit(
            "get_median(a2[:], m2)",
            globals=globals(),
            number=1000))
    print('1000')
    print(
        timeit(
            "get_median(a3[:], m3)",
            globals=globals(),
            number=1000))
