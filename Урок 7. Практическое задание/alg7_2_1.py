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

# https://pythonist.ru/algoritmy-sortirovki-s-python/
from random import randint
from timeit import timeit
import math


def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array


m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(timeit('shellSort(orig_list[:])', globals=globals(), number=1000))
lst = shellSort(orig_list)
print(f'медиана равна {lst[m]}')

m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(timeit('shellSort(orig_list[:])', globals=globals(), number=1000))
lst = shellSort(orig_list)
print(f'медиана равна {lst[m]}')

m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(timeit('shellSort(orig_list[:])', globals=globals(), number=1000))
lst = shellSort(orig_list)
print(f'медиана равна {lst[m]}')
