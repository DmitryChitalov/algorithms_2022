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
    return array[n // 2 + 1]


# замеры для 11 элементов
array = [randint(1, 1000) for i in range(11)]

print(
    timeit(
        "shell_sort(array[:])",
        globals=globals(),
        number=1000))

# замеры для 101 элемента
array = [randint(1, 1000) for i in range(101)]

print(
    timeit(
        "shell_sort(array[:])",
        globals=globals(),
        number=1000))

# замеры для 1001 элемента
array = [randint(1, 1000) for i in range(1001)]

print(
    timeit(
        "shell_sort(array[:])",
        globals=globals(),
        number=1000))

'''
0.0060826999999999964
0.12475929999999999
2.5855697
'''