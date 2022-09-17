from random import randint
from timeit import timeit
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


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data

m = 10
data_1 = [randint(-100, 100) for _ in range(21)]
print(f' Неотсортированный массив 10 элементов : {data_1}')
print(print(f'Отсортированный функцией массив 10 элементов : {gnome(data_1)}'))
print(timeit("gnome(data_1[:])", globals=globals(), number=1000))
print(data_1[m])
# время: 0.003609053000000001

m = 100
data_2 = [randint(-100, 100) for _ in range(201)]
print(timeit("gnome(data_2[:])", globals=globals(), number=1000))
print(data_2[m])
# время: 5.627953767999999

m = 1000
data_3 = [randint(-100, 100) for _ in range(2001)]
print(timeit("gnome(data_3[:])", globals=globals(), number=1000))
print(data_3[m])
# время: 859.2978025550001
