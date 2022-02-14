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
from random import randint
from timeit import timeit


def shell_sort_median(array):
    inc = len(array) // 2
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return array[(len(array) - 1) // 2]


if __name__ == "__main__":
    m = 10
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("shell_sort_median(data[:])", number=1000, globals=globals()))
    m = 100
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("shell_sort_median(data[:])", number=1000, globals=globals()))
    m = 1000
    data = [randint(-100, 100) for i in range(m*2+1)]
    print(timeit("shell_sort_median(data[:])", number=1000, globals=globals()))


"""
0.032452499999999995
0.6619172
10.861606400000001
"""

