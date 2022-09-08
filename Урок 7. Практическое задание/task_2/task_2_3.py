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


def make_lst(m):
    return [randint(-100, 100) for i in range(2*m+1)]


print(timeit("median(make_lst(10))", globals=globals(), number=100))
print(timeit("median(make_lst(100))", globals=globals(), number=100))
print(timeit("median(make_lst(1000))", globals=globals(), number=100))

"""
встроенный метод из модуля statistics самый быстрый в исполнении
"""