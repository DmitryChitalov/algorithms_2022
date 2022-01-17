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
from random import randrange
from statistics import median


def create_lst(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]
    return lst


def find_median_builtin(lst):
    lst_median = median(lst)
    return lst_median


m1 = 10
lst1 = create_lst(m1)
print(timeit('find_median_builtin(lst1.copy())', globals=globals(), number=1000))  # 0.0006361000000000006

m2 = 100
lst2 = create_lst(m2)
print(timeit('find_median_builtin(lst2.copy())', globals=globals(), number=1000))  # 0.0064665

m3 = 1000
lst3 = create_lst(m3)
print(timeit('find_median_builtin(lst3.copy())', globals=globals(), number=1000))  # 0.1564238

"""Самым эффективным в плане скорости выполнения оказался третий способ - решение задачи с помощью встроенной функции 
поиска медианы. Самым медленным оказалось решение задачи с помощью гномьей сортировки. Причем, при увеличении
количества элементов, разница в скорости выполнения у всех трех медотов оказывается еще более очевидным."""
