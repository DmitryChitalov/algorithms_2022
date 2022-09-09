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

########################################################################
from random import randint
from statistics import median
from timeit import timeit


def built_in_func(n):
    """
    Функция Python statistics.median() берет выборку данных и возвращает ее медиану.
    median() автоматически обрабатывает вычисление медианы для выборок с нечетным или четным числом наблюдений.
    """
    return median([n])


m = 10
arr = [randint(0, 100) for i in range(2 * m + 1)]

print(timeit("built_in_func(arr)", globals=globals(), number=1000))  # 0.0012113000266253948

m = 100
arr = [randint(0, 100) for i in range(2 * m + 1)]

print(timeit("built_in_func(arr)", globals=globals(), number=1000))  # 0.0015507999924011528

m = 1000
arr = [randint(0, 100) for i in range(2 * m + 1)]

print(timeit("built_in_func(arr)", globals=globals(), number=1000))  # 0.0005707999807782471
