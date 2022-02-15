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


m = 5
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("find_median(lists_task[:])", globals=globals(), number=100))  # 0.0006769469999999972
print(lists_task[m])

m = 50
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("find_median(lists_task[:])", globals=globals(), number=100))  # 0.024510897000000004
print(lists_task[m])

m = 500
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("find_median(lists_task[:])", globals=globals(), number=100))  # 1.860450414
print(lists_task[m])
