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


def shell_sort(array):
    n = len(array)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            temp = array[i]
            j = i
            while j >= step and array[j - step] > temp:
                array[j] = array[j - step]
                j -= step
            array[j] = temp
        step //= 2
    return array


# замеры для m = 10
m = 10
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "shell_sort(array[:])[m]",
        globals=globals(),
        number=1000))

# замеры для m = 100
m = 100
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "shell_sort(array[:])[m]",
        globals=globals(),
        number=1000))

# замеры для m = 1000
m = 1000
array = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "shell_sort(array[:])[m]",
        globals=globals(),
        number=1000))

'''
0.014035800000000001
0.30291500000000005
5.763194800000001
'''