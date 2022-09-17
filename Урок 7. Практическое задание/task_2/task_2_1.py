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
from heapq import heappop, heappush


mass_10 = [randint(1, 100) for i in range(2 * 5 + 1)]
mass_100 = [randint(1, 100) for j in range(2 * 50 + 1)]
mass_1000 = [randint(1, 100) for k in range(2 * 500 + 1)]


'''Гномья сортировка'''


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
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return mid


'''Сортировка Шелла'''


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return mid


'''Сортировка Кучей'''


def heap_sort(data):
    heap = []
    for element in data:
        heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    n = len(data)
    mid = n // 2
    if n % 2 == 1:
        return mid


print(timeit('gnome(mass_10[:])', globals=globals(), number=1000))
print(timeit('shell(mass_10[:])', globals=globals(), number=1000))
print(timeit('heap_sort(mass_10[:])', globals=globals(), number=1000))
print()
print(timeit('gnome(mass_100[:])', globals=globals(), number=1000))
print(timeit('shell(mass_100[:])', globals=globals(), number=1000))
print(timeit('heap_sort(mass_100[:])', globals=globals(), number=1000))
print()
print(timeit('gnome(mass_1000[:])', globals=globals(), number=1000))
print(timeit('shell(mass_1000[:])', globals=globals(), number=1000))
print(timeit('heap_sort(mass_1000[:])', globals=globals(), number=1000))

'''Из трех сортировок, самая быстрая сортировка Кучей, при любой длине массива'''
