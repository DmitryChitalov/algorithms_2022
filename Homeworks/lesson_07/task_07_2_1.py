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

from timeit import timeit
from random import randint


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if lst[i-1] <= lst[i]:
            i += 1
        else:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            if i > 1:
                i -= 1


def find_median_with_sort(lst):
    gnome_sort(lst)
    mean = int((len(lst)-1)/2)
    return lst[mean]


if __name__ == '__main__':

    lst_test_9 = [randint(-100, 100) for _ in range(9)]
    print(timeit("find_median_with_sort(lst_test_9[:])", globals=globals(), number=10))

    lst_test_99 = [randint(-100, 100) for _ in range(99)]
    print(timeit("find_median_with_sort(lst_test_99[:])", globals=globals(), number=10))

    lst_test_999 = [randint(-100, 100) for _ in range(999)]
    print(timeit("find_median_with_sort(lst_test_999[:])", globals=globals(), number=10))
