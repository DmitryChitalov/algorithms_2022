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

from random import randint
from timeit import timeit
from statistics import median

lst_10 = [randint(0, 1000) for _ in range(11)]
lst_100 = [randint(0, 1000) for _ in range(101)]
lst_1000 = [randint(0, 1000) for _ in range(1001)]


def get_mediana(lst_obj):
    return median(lst_obj)


print(get_mediana(lst_10))
print(get_mediana(lst_100))
print(get_mediana(lst_1000))
print(timeit("get_mediana(lst_10)", globals=globals(), number=1000))
print(timeit("get_mediana(lst_100)", globals=globals(), number=1000))
print(timeit("get_mediana(lst_1000)", globals=globals(), number=1000))