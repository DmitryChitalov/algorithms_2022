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


def gnome_sort(n):
    array = [randint(-1000, 1000) for i in range(2 * n + 1)]
    for i in range(len(array) - 1):
        while array[i] > array[i + 1] and i >= 0:
            array[i], array[i + 1] = array[i + 1], array[i]
            i -= 1
    return array[len(array)//2+1]


print(gnome_sort(5))
print(timeit("gnome_sort(5)", globals=globals(), number=1000))  #0.025835199999999996
print(timeit("gnome_sort(50)", globals=globals(), number=1000)) #0.7044826
print(timeit("gnome_sort(500)", globals=globals(), number=1000))#74.6975678
