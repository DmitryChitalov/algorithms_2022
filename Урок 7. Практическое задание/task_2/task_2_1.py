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


def get_median(m):
    my_list = [randint(0, (2 * m + 1)) for _ in range(2 * m + 1)]

    def gnome(my_list):
        i, size = 1, len(my_list)
        while i < size:
            if my_list[i - 1] <= my_list[i]:
                i += 1
            else:
                my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
                if i > 1:
                    i -= 1
        return my_list

    my_list = gnome(my_list)
    return my_list[m]



print(timeit('get_median(5)', globals=globals(), number=100))
print(timeit('get_median(50)', globals=globals(), number=100))
print(timeit('get_median(500)', globals=globals(), number=100))
