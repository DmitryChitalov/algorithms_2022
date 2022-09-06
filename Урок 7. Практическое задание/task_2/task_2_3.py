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
import random
from timeit import timeit

m = 5
some_array = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("sorted(some_array)[m]", globals=globals(), number=1))
m = 50
some_array2 = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("sorted(some_array2)[m]", globals=globals(), number=1))
m = 500
some_array3 = [random.randrange(-100, 100) for i in range(2*m + 1)]
print(timeit("sorted(some_array3)[m]", globals=globals(), number=1))

'''
Медленнее всего работает гномья сортировка, на втором месте второй способ, 
третий, встроенная сортировка, самый быстрый.
'''