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
from numpy import median


def get_median(array):
    return median(array)


if __name__ == '__main__':
    # m = 10
    # lst = [randint(-100, 100) for _ in range(2 * m + 1)]
    # print(lst)
    # median = get_median(lst)
    # print(median)

    # замеры 10
    m = 5
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:])",
            globals=globals(),
            number=1000))

    # замеры 100
    m = 50
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:])",
            globals=globals(),
            number=1000))

    # замеры 1000
    m = 500
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

    print(
        timeit(
            "get_median(orig_list[:])",
            globals=globals(),
            number=1000))

"""
0.02771842399999999
0.05003141999999999
0.10991031299999998

Итого
на 10 и 100 быстрее всего сработало взятие максимумов
на 1000 быстрее всего сработала numpy.median()
"""
