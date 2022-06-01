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

from timeit import timeit
from random import randint
from statistics import median


def find_median(lst):
    return median(lst)


my_list = [randint(-100, 100) for _ in range(2 * 5 + 1)]
print(timeit('find_median(my_list)', globals=globals(), number=1000))

my_list2 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
print(timeit('find_median(my_list2)', globals=globals(), number=1000))

my_list3 = [randint(-100, 100) for _ in range(2 * 500 + 1)]
print(timeit('find_median(my_list3)', globals=globals(), number=1000))

# 0.0006062999999999902
# 0.003935900000000006
# 0.0597076

# Вывод - самое оптимальное решение во втором случае.
