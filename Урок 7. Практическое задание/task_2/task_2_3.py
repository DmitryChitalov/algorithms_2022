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

s = """\
my_list = [randint(-100, 100) for x in range(11)]
median(my_list[:])
"""

print('11 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(101)]
median(my_list[:])
"""

print('101 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')

s = """\
my_list = [randint(-100, 100) for x in range(1001)]
median(my_list[:])
"""

print('1001 elements ',
      timeit(s, globals=globals(), number=100), ' seconds ')


# C увеличением числа элементов увеличивается и время выполнения , что логично.
# Встроенные функции работают быстрее , чем написанные самостоятельно, как и ожидалось
# 11 elements  0.0017895909999999932  seconds
# 101 elements  0.014440469000000011  seconds
# 1001 elements  0.15063332799999998  seconds
