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
from statistics import median

m = 10
my_list_10 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(my_list_10[:])", globals=globals(), number=1000))
m = 100
my_list_100 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(my_list_100[:])", globals=globals(), number=1000))
m = 1000
my_list_1000 = [randint(0, 100) for x in range(2*m+1)]
print(timeit("median(my_list_1000[:])", globals=globals(), number=1000))


# Результаты:
# m 10 - 0.004026799999999997
# m 100 - 0.040113099999999985
# m 1000 - 0.6270933000000001
# Самый лучший способ решения