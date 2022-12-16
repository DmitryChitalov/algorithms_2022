"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

import statistics
from random import randint
from timeit import timeit

# замер 10:  0.0006606000024476089
m = 5
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print('исходный массив:', my_array)

print(
    timeit(
        "statistics.median(my_array)",
        globals=globals(),
        number=1000))

print(statistics.median(my_array))

# замер 100:  0.004127400003199
m = 50
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print('исходный массив:', my_array)

print(
    timeit(
        "statistics.median(my_array)",
        globals=globals(),
        number=1000))

print(statistics.median(my_array))

# замер 1000:  0.08094320000236621
m = 500
my_array = [randint(1, 100) for _ in range(2 * m + 1)]
print('исходный массив:', my_array)

print(
    timeit(
        "statistics.median(my_array)",
        globals=globals(),
        number=1000))

print(statistics.median(my_array))

# Самый эффективный по времени оказался способ с использованием встроенной функции median(),
# способ без сортировки на втором месте, способ с сортировкой самый медленный.
