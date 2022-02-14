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
    n = (len(array) - 1) // 2
    while n > 0:
        array.remove(max(array))
        n -= 1
    return max(array)


if __name__ == "__main__":
    m = 10
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))
    m = 100
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))
    m = 1000
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("get_median(data[:])", number=1000, globals=globals()))

"""
0.0150145
0.7421613
54.3577522
"""