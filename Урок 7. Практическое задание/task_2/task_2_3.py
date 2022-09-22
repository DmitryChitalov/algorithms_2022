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

from random import randint
from timeit import timeit
from statistics import median

# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))   # 0.0007430999539792538
print(f'Медиана - {median(orig_list[:])}')                              # Медиана - 23

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))   # 0.004520399961620569
print(f'Медиана - {median(orig_list[:])}')                              # Медиана - 4

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('median(orig_list[:])', globals=globals(), number=1000))   # 0.08666729996912181
print(f'Медиана - {median(orig_list[:])}')                              # Медиана - -2

"""
Эффективнее оказался способ с использованием встроенной функции median из модуля statistics
"""
