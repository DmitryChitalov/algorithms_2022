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
from statistics import median
from timeit import timeit


if __name__ == "__main__":
    data = [randint(-100, 100) for i in range(11)]
    print(timeit("median(data[:])", number=1000, globals=globals()))
    data = [randint(-100, 100) for i in range(101)]
    print(timeit("median(data[:])", number=1000, globals=globals()))
    data = [randint(-100, 100) for i in range(1001)]
    print(timeit("median(data[:])", number=1000, globals=globals()))


"""
0.0016741999999999868
0.00827349999999999
0.13156179999999998

Встроенный поиск медианы с использованием sorted() оказался самым эффективным
"""