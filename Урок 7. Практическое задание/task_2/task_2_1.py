"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from timeit import timeit
from random import randint
from statistics import median
# Есть хороший пакет с готовыми алгоритмами и другими полезными модулями
from algorithms.sort.heap_sort import max_heap_sort

m = 10
ARRAY_10 = [randint(-100, 100) for i in range(2 * m + 1)]
m = 100
ARRAY_100 = [randint(-100, 100) for j in range(2 * m + 1)]
m = 1000
ARRAY_1000 = [randint(-100, 100) for k in range(2 * m + 1)]

print(f'Median of array with m = 10: {median(ARRAY_10)}',
      timeit('max_heap_sort(ARRAY_10)', globals=globals(), number=100))
print(f'Median of array with m = 100: {median(ARRAY_100)}',
      timeit('max_heap_sort(ARRAY_100)', globals=globals(), number=100))
print(f'Median of array with m = 1000: {median(ARRAY_1000)}',
      timeit('max_heap_sort(ARRAY_1000)', globals=globals(), number=100))
