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

import random
from timeit import timeit


def find_median(my_array):
    avg_val = sum(my_array) / len(my_array)
    next_to_avg_val = my_array[0]
    for i in my_array:
        if abs(i - avg_val) < abs(i - next_to_avg_val):
            next_to_avg_val = i
    return next_to_avg_val

m = 5
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]

print(timeit("find_median(some_array[:])", globals=globals(), number=1))
m = 50
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("find_median(some_array[:])", globals=globals(), number=1))
m = 500
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]

