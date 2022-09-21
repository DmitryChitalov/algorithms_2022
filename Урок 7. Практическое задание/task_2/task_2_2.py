"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


m = 5
lst5 = [randint(-100, 100) for _ in range(2*m+1)]   # список из 11 элементов
m2 = 50
lst50 = [randint(-100, 100) for _ in range(2*m2+1)]     # список из 101 элемента
m3 = 500
lst500 = [randint(-100, 100) for _ in range(2*m3+1)]    # список из 1001 элемента


def no_sort(data):
    data = data[:]
    max_elems = []
    min_elems = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                min_elems.append(data[i])
            if data[i] < data[j]:
                max_elems.append(data[j])
            if data[i] == data[j] and i > j:
                min_elems.append(data[j])
            if data[i] == data[j] and i < j:
                max_elems.append(data[j])
        if len(max_elems) == len(min_elems):
            return data[i]
        min_elems.clear()
        max_elems.clear()


print(lst5)
print(no_sort(lst5[:]))

print(
    timeit(
        "no_sort(lst5[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "no_sort(lst50[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "no_sort(lst500[:])",
        globals=globals(),
        number=100))


'''
0.0010910999999999976
0.0331461
6.4123645
'''
