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
from task_2_2 import no_sort
from task_2_1 import heap_sort

m = 10
ARRAY_10_for_2_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_10_for_2_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_10_for_2_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
m = 100
ARRAY_100_for_2_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_100_for_2_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_100_for_2_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
m = 1000
ARRAY_1000_for_2_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_1000_for_2_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
ARRAY_1000_for_2_3 = [randint(-100, 100) for _ in range(2 * m + 1)]

print('_____________________________task 2_3.py_____________________________________')
print(f'Median of array with m = 10, median: {median(ARRAY_10_for_2_3[:])}', 'Timing: ',
      timeit('median(ARRAY_10_for_2_3[:])', globals=globals(), number=100))
print(f'Median of array with m = 100, median: {median(ARRAY_100_for_2_2[:])}', 'Timing: ',
      timeit('median(ARRAY_100_for_2_3[:])', globals=globals(), number=100))
print(f'Median of array with m = 1000, median: {median(ARRAY_1000_for_2_3[:])}', 'Timing: ',
      timeit('median(ARRAY_1000_for_2_3[:])', globals=globals(), number=100))

print('_____________________________task 2_1.py_____________________________________')
print(f'Median of array with m = 10, heap_sort: {heap_sort(ARRAY_10_for_2_1[:])}',
      timeit('heap_sort(ARRAY_10_for_2_1[:])', globals=globals(), number=100))
print(f'Median of array with m = 100, heap_sort: {heap_sort(ARRAY_100_for_2_1[:])}',
      timeit('heap_sort(ARRAY_100_for_2_1[:])', globals=globals(), number=100))
print(f'Median of array with m = 1000, heap_sort: {heap_sort(ARRAY_1000_for_2_1[:])}',
      timeit('heap_sort(ARRAY_1000_for_2_1[:])', globals=globals(), number=100))

print('_____________________________task 2_2.py_____________________________________')
print(f'Median of array with m = 10, no_sort: {no_sort(ARRAY_10_for_2_2[:])}',
      timeit('no_sort(ARRAY_10_for_2_2[:])', globals=globals(), number=100))
print(f'Median of array with m = 100, no_sort: {no_sort(ARRAY_100_for_2_2[:])}',
      timeit('no_sort(ARRAY_100_for_2_2[:])', globals=globals(), number=100))
print(f'Median of array with m = 1000, no_sort: {no_sort(ARRAY_1000_for_2_2[:])}',
      timeit('no_sort(ARRAY_1000_for_2_2[:])', globals=globals(), number=100))

print("""
    Встроенная функция поиска медианы справляется лучше всех, 
    так как выводит элемент, индекс которого равен результату деления длины массива на двое, 
    то есть не происходит перебор массива по элементам. Сложность: O(1)
    На втором месте по скорости выполнения сортировка Кучей. Сложность O(N log(N)) 
    Хуже всех происходит поиск медианы в неотсортированном массиве, 
    так как происходит перебор всех элементов массива попарно (в двух циклах). Сложность: O(N^2)""")
