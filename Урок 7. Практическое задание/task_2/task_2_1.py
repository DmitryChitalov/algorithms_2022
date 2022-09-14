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

import random
from timeit import timeit


def gnome_sort(my_array):
    l = len(my_array)
    i = 1
    while i < l:
        if i == 0:
            i = 1
        if my_array[i] > my_array[i-1]:
            my_array[i], my_array[i-1] = my_array[i-1], my_array[i]
            i -= 1
        else:
            i += 1
    return my_array


m = 5
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("(gnome_sort(some_array[:]))[m]", globals=globals(), number=1))
m = 50
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("(gnome_sort(some_array[:]))[m]", globals=globals(), number=1))
m = 500
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("(gnome_sort(some_array[:]))[m]", globals=globals(), number=1))

