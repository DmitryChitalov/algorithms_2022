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

import math
from random import randint
from timeit import timeit

m = 5
lst5 = [randint(-100, 100) for _ in range(2*m+1)]   # список из 11 элементов
m2 = 50
lst50 = [randint(-100, 100) for _ in range(2*m2+1)]     # список из 101 элемента
m3 = 500
lst500 = [randint(-100, 100) for _ in range(2*m3+1)]    # список из 1001 элемента


def gnome_sort(data):
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


def mediana_search_gnome(data):
    ind = int((len(data)-1)/2)
    return \
        f' Изначальный список:  {data} \n ' \
        f'Отсортированный список: {gnome_sort(data)}\n ' \
        f'Медиана: {gnome_sort(data)[ind]}'


print(mediana_search_gnome(lst5[:]))

print(
    timeit(
        "mediana_search_gnome(lst5[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_gnome(lst50[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_gnome(lst500[:])",
        globals=globals(),
        number=100))


'''
Замеры нахождения медианы с использованием Гномьей сортировки
0.0016641000000000017
0.1908042
8.0673933
'''


def shell_sort(data):
    n = len(data)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = data[i]
            j = i
            while j >= interval and data[j - interval] > temp:
                data[j] = data[j - interval]
                j -= interval
            data[j] = temp
        k -= 1
        interval = 2**k -1
    return data


def mediana_search_shell(data):
    ind = int((len(data)-1)/2)
    return \
        f' Изначальный список:  {data} \n ' \
        f'Отсортированный список: {shell_sort(data)}\n ' \
        f'Медиана: {shell_sort(data)[ind]}'


print(mediana_search_shell(lst5[:]))

print(
    timeit(
        "mediana_search_shell(lst5[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_shell(lst50[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_shell(lst500[:])",
        globals=globals(),
        number=100))


'''
Замеры нахождения медианы с использованием сортировки Шелла. Работает в разы быстрее Гномьей
0.0020067
0.023163899999999987
0.46345289999999995
'''


def heapify(data, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[i] < data[l]:
        largest = l
    if r < n and data[largest] < data[r]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


def heap_sort(data):
    n = len(data)
    for i in range(n // 2, -1, -1):
        heapify(data, n, i)
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    return data


def mediana_search_heap(data):
    ind = int((len(data)-1)/2)
    return \
        f' Изначальный список:  {data} \n ' \
        f'Отсортированный список: {heap_sort(data)}\n ' \
        f'Медиана: {heap_sort(data)[ind]}'


print(mediana_search_heap(lst5[:]))


print(
    timeit(
        "mediana_search_heap(lst5[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_heap(lst50[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "mediana_search_heap(lst500[:])",
        globals=globals(),
        number=100))


'''
Замеры скорости нахождения медианы с использованием сортировки Кучей.
По скорости средний варинат между Гномьей сортировкой и сортировкой Шелла
0.004193299999999997
0.05901519999999999
1.1140815
'''
