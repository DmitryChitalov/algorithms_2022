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
import random
import numpy as np
from timeit import repeat


def get_median(arr):
    return np.median(arr)

m=10
array_1 = np.array([i for i in random.choices(range(-100, 100), k=2*m + 1)])
m=100
array_2 = np.array([i for i in random.choices(range(-100, 100), k=2*m + 1)])
m=1000
array_3 = np.array([i for i in random.choices(range(-100, 100), k=2*m + 1)])

for array_, m in [('array_1', 10), ('array_2', 100), ('array_3', 1000)]:
    time_ = repeat(stmt=f'get_median({array_})', repeat=5, globals=globals(), number=1)
    print(f'For {m = } execution time = {time_}')