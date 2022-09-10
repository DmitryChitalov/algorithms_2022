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
import statistics
from timeit import timeit


mass_1 = 2 * 10 + 1
mass_2 = 2 * 100 + 1
mass_3 = 2 * 1000 + 1
lst1 = [randint(-900, 900) for _ in range(mass_1)]
lst2 = [randint(-900, 900) for _ in range(mass_2)]
lst3 = [randint(-900, 900) for _ in range(mass_3)]



print(timeit('statistics.median(lst1)', globals=globals(), number=2))
print(timeit('statistics.median(lst2)', globals=globals(), number=2))
print(timeit('statistics.median(lst3)', globals=globals(), number=2))
'''Встроенные функции снова оправдали ожидания своей скоростью, но с малыми 
списками дела обстоят сложнее'''