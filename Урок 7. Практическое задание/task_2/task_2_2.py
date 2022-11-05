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
from timeit import timeit

def find_median(arrnum):
    median = arrnum[:]
    for i in range(len(median) // 2):
        median.remove(min(median))
        median.remove(max(median))
    return median[0]


m = 10

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 0.0014112000353634357

m = 100

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 0.04501589993014932

m = 1000

arrnum = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit('find_median(arrnum[:])', globals=globals(), number=100)) # 4.3981516000349075