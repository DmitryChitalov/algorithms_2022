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


def shell_sort(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return arr


data = [randint(-100, 100) for _ in range(11)]
print(data)
print(shell_sort(data[:]))


# замеры 11
print(timeit("shell_sort(data[:])", globals=globals(), number=1000))    # 0.006307299998297822
print(shell_sort(data[:])[5])

# замеры 101
data = [randint(-100, 100) for _ in range(101)]
print(timeit("shell_sort(data[:])", globals=globals(), number=1000))    # 0.12683210000250256
print(shell_sort(data[:])[50])

# замеры 1001
data = [randint(-100, 100) for _ in range(1001)]
print(timeit("shell_sort(data[:])", globals=globals(), number=1000))    # 1.9637822000004235
print(shell_sort(data[:])[500])
