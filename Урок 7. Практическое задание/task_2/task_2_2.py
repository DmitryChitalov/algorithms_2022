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
# from statistics import median
from timeit import timeit

range_numbers10 = [randint(-100, 100) for _ in range(0, 2 * 10 + 1)]
range_numbers100 = [randint(-100, 100) for _ in range(0, 2 * 100 + 1)]
range_numbers1000 = [randint(-100, 100) for _ in range(0, 2 * 1000 + 1)]


# Шелла
def shell_sort(arr, m):
    n = len(arr)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = arr[i]
            j = i
            while j >= h and arr[j - h] > t:
                arr[j] = arr[j - h]
                j -= h

            arr[j] = t
        h = h // 2
    return arr[m]


print(
    timeit(
        "shell_sort(range_numbers10[:], 10)",
        setup='from __main__ import shell_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "shell_sort(range_numbers100[:], 100)",
        setup='from __main__ import shell_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "shell_sort(range_numbers1000[:], 1000)",
        setup='from __main__ import shell_sort',
        globals=globals(),
        number=100))

"""
0.0015565999999999983
0.03125429999999999
0.5737104
"""
