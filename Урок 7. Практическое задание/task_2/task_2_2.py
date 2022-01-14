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


def find_median(lst):
    for i in range(m):
        lst.remove(max(lst))
    return max(lst)


# Замеры в списке длиной 11

m = 5
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 101

m = 50
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Замеры в списке длиной 1001

m = 500
new_list = [randint(-100, 100) for i in range(2 * m + 1)]

print(timeit("find_median(new_list[:])", globals=globals(), number=1000))

# Результаты: 0.001 сек, 0.05 сек и 4.56 сек
