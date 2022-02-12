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


def get_median(array):
    m = (len(array) - 1) // 2
    while m > 0:
        array.remove(max(array))
        m -= 1
    return max(array)


if __name__ == "__main__":
    data = [randint(-100, 100) for i in range(11)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))
    data = [randint(-100, 100) for i in range(101)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))
    data = [randint(-100, 100) for i in range(1001)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))

"""
0.012486999999999998
0.2260848
12.3108064
"""