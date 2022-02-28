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


def gnome(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data, data[int((size - 1)/2)]


if __name__ == "__main__":

    orig_list_11 = [randint(-100, 100) for _ in range(11)]

    print(
        timeit(
            "gnome(orig_list_11[:])",
            globals=globals(),
            number=1000))

    orig_list_101 = [randint(-100, 100) for _ in range(101)]

    print(
        timeit(
            "gnome(orig_list_101[:])",
            globals=globals(),
            number=1000))

    orig_list_1001 = [randint(-100, 100) for _ in range(1001)]

    print(
        timeit(
            "gnome(orig_list_1001[:])",
            globals=globals(),
            number=1000))

    """
    На массиве из 1001 элемента время составило 112.62 секунды и
    это с учетом некоторойоптимизации алгоритма. А чем больше массив 
    - тем хуже.
    """