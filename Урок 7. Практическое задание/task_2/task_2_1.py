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

"""
Сортировка кучей.

10 + 1 элемент: 0.016885499999999998
100 + 1 элемент: 0.2880647
1000 + 1 элемент: 4.718992399999999
"""

from random import randint
from timeit import timeit
from heapsort import heap_sort


def find_median(m):
    heap_sort(original_array.copy())
    return original_array[m]


if __name__ == '__main__':
    m = 5
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('find_median(m)', number=1000, globals=globals()))

    m = 50
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('find_median(m)', number=1000, globals=globals()))

    m = 500
    original_array = [randint(-100, 99) for i in range(2 * m + 1)]
    print(timeit('find_median(m)', number=1000, globals=globals()))