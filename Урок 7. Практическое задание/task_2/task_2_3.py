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



m = 5
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("median(lists_task[:])", globals=globals(), number=100))  # 0.00010878799999999855
print(lists_task[m])

m = 50
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("median(lists_task[:])", globals=globals(), number=100))  # 0.0010743300000000053
print(lists_task[m])

m = 500
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lists_task)
print(timeit("median(lists_task[:])", globals=globals(), number=100))  # 0.009438668000000004
print(lists_task[m])

# По итогам расчетов времени самым эффективным оказался 3 способ - использование встроенной функции медианы
