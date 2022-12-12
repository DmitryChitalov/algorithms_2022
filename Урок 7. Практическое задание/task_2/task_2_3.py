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
from statistics import median
from timeit import timeit

m = 5  # 10 elems
m2 = 50  # 100 elems
m3 = 500  # 1000 elems
#
a = [randint(1, 100) for x in range(2 * m + 1)]
a2 = [randint(1, 100) for x in range(2 * m2 + 1)]
a3 = [randint(1, 100) for x in range(2 * m3 + 1)]

print(median(a))
print(median(a2))
print(median(a3))

print('10')
print(
    timeit(
        "median(a[:])",
        globals=globals(),
        number=1000))
print('100')
print(
    timeit(
        "median(a2[:])",
        globals=globals(),
        number=1000))
print('1000')
print(
    timeit(
        "median(a3[:])",
        globals=globals(),
        number=1000))


"""
Встроненный способ оказался быстрее всех как и следовало ожидать 

"""