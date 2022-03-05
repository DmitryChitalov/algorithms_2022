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
from numpy import median

##############################################################################
"""
Способ 3: с помощью встроенной функции поиска медианы из модуля numpy

Массив из 11 элементов: 0.02847
Массив из 101 элементов: 0.02737
Массив из 1001 элементов: 0.09175

Способ 3 является самым быстрым.
"""


# Тестирование
for i in range(1,4):
    n = 10**i + 1
    test_lst = [randint(-100, 100) for _ in range(n)]
    print(f'Массив из {n} элементов: {timeit("median(test_lst[:])", globals=globals(), number=1000):.5f}')
