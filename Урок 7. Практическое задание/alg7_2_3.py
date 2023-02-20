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
from numpy import median


def lst_median_n(lst):
    return median(lst[:])


m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(timeit('lst_median_n(orig_list[:])', globals=globals(), number=1000))
print(lst_median_n(orig_list))


m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]

print(timeit('lst_median_n(orig_list[:])', globals=globals(), number=1000))
print(lst_median_n(orig_list))


m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]

print(timeit('lst_median_n(orig_list[:])', globals=globals(), number=1000))
print(lst_median_n(orig_list))

# встроенная функция отработала быстрее всех, особенно, разница видна с увеличнием длины массива
