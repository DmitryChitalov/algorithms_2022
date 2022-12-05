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
from statistics import median
import numpy


def get_lst(m):
    return [randint(-100, 100) for i in range(2 * m + 1)]


# замер 11 statistics
print(timeit("statistics.median(get_lst(5))", globals=globals(), number=1000))

# замер 101 statistics
print(timeit("statistics.median(get_lst(50))", globals=globals(), number=1000))

# замер 1001 statistics
print(timeit("statistics.median(get_lst(500))", globals=globals(), number=1000))

print('-' * 100)

# замер 11 numpy
print(timeit("numpy.median(get_lst(5))", globals=globals(), number=1000))

# замер 101 numpy
print(timeit("numpy.median(get_lst(50))", globals=globals(), number=1000))

# замер 1001 numpy
print(timeit("numpy.median(get_lst(500))", globals=globals(), number=1000))

'''
0.008264899952337146
0.06223960011266172
0.7923091999255121
----------------------------------------------------------------------------------------------------
0.027896199841052294
0.10187190002761781
0.825284699909389

На небольших объемах данных работать можно всеми тремя способами, хотя даже на таких объемах заметна разница.
Варианты с сортировкой и через удаление максимальных значений работают значительно медленнее чем
функция numpy.median и встроенная функция statistics.median.
При сравнении numpy.median и statistics.median видно, что выигрывает statistics.median

'''