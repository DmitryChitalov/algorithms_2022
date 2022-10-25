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

def sort_gnome(m):
    my_list = list(randint(1, 100) for _ in range(2 * m + 1))
    i = 0
    while i + 1 < len(my_list):
        if my_list[i + 1] >= my_list[i]:
            i += 1
        else:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            i = i - 1 if i > 0 else i + 1
    median = my_list[m]
    return my_list, median


print(
    timeit(
        "sort_gnome(10)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "sort_gnome(100)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "sort_gnome(1000)",
        globals=globals(),
        number=1000))

'''
0.04502020007930696
2.861987299984321
373.12543610006105
'''