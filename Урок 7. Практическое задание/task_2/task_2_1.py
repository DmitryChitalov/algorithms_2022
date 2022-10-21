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
    arr = [randint(-1000, 1000) for i in range(2 * n + 1)]
    for i in range(len(arr) - 1):
        while arr[i] > arr[i + 1] and i>=0:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i -= 1
    return arr[len(arr)//2+1]


print(gnome_sort(5))
print(timeit("gnome_sort(5)", globals=globals(), number=1000))  #0.0093312499957392 11 элементов
print(timeit("gnome_sort(50)", globals=globals(), number=1000)) #0.30554783300613053 101 элемент
print(timeit("gnome_sort(500)", globals=globals(), number=1000))#29.29951087500376 1001 элемент