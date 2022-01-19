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
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data[m]


m = 10
some_list = [randint(-100, 100) for i in range(2 * m + 1)]


# def gnome_median(sort_data):
#     return sort_data[m]


m = 10
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('gnome(some_list[:])', globals=globals(), number=100))

m = 100
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('gnome(some_list[:])', globals=globals(), number=100))

m = 1000
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('gnome(some_list[:])', globals=globals(), number=100))

