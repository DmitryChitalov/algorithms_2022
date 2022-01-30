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
    return data


def get_mediana(arr, m):
    gnome(arr)
    return arr[m]



m = 10
arr_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_10[:], m)", globals=globals(), number=1000))

m = 100
arr_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_100[:], m)", globals=globals(), number=1000))

m = 1000
arr_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("get_mediana(arr_1000[:], m)", globals=globals(), number=30))

"""
Использовал улучшенную Гномью сортировку.
Результаты:
            m = 10 - 0.0893484
            m = 100 - 6.0004133
            m = 1000 - 24.0237852
"""

