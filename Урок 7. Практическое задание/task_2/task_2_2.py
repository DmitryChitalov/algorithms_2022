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

from timeit import timeit
from random import randint


def median(list, x):
    for _ in range(x):
        list.remove(max(list))
    return max(list)


x = 10
list1 = [randint(0, 100) for i in range(2 * x + 1)]
print(timeit("median(list1[:], x)", globals=globals(), number=100))

x = 100
list2 = [randint(0, 100) for i in range(2 * x + 1)]
print(timeit("median(list2[:], x)", globals=globals(), number=100))

x = 1000
list3 = [randint(0, 100) for i in range(2 * x + 1)]
print(timeit("median(list3[:], x)", globals=globals(), number=100))
# 0.0008408209999999985
# 0.059101734999999996
# 3.7655562220000003
