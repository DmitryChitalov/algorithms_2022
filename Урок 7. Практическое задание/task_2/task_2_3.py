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


m = 10
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))

m = 100
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))

m = 1000
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))


# 0.00009040000000000437
# 0.000988799999999998
# 0.0218782
