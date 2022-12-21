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


def find_median_without_sort(lst):
    mean = int((len(lst)-1)/2)
    for _ in range(mean):
        min_value = min(lst)
        lst.remove(min_value)
    return min(lst)


if __name__ == '__main__':

    lst_test_9 = [randint(-100, 100) for _ in range(9)]
    print(timeit("find_median_without_sort(lst_test_9[:])", globals=globals(), number=1000))

    lst_test_99 = [randint(-100, 100) for _ in range(99)]
    print(timeit("find_median_without_sort(lst_test_99[:])", globals=globals(), number=1000))

    lst_test_999 = [randint(-100, 100) for _ in range(999)]
    print(timeit("find_median_without_sort(lst_test_999[:])", globals=globals(), number=1))
