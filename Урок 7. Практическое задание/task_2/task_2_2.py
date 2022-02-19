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


def find_median(orig_array, m):
    for i in range(m):
        orig_array.remove(max(orig_array))
    return max(orig_array)


if __name__ == '__main__':
    m = 10
    orig_array = [randint(-100, 100) for i in range(2 * m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = orig_array', number=1000, globals=globals()))

    m = 100
    orig_array = [randint(-100, 100) for i in range(2 * m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = orig_array', number=1000, globals=globals()))

    m = 1000
    orig_array = [randint(-100, 100) for i in range(2 * m + 1)]
    print(timeit('find_median(array.copy(), m)', setup='array = orig_array', number=1000, globals=globals()))

"""
0.006526999999999998
0.421034
37.696649699999995
"""