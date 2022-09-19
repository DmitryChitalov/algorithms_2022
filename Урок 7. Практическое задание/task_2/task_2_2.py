"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

def no_sort_med(lst):
    for _ in range(len(lst)//2):
        lst.remove(max(lst))
    return max(lst)


m = 10
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {no_sort_med(lst[:])}')
print(timeit("no_sort_med(lst[:])", globals=globals(), number=100)) # время выполнения 0.0006785779987694696

m = 100
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {no_sort_med(lst[:])}')
print(timeit("no_sort_med(lst[:])", globals=globals(), number=100)) # время выполнения 0.04703154999879189

m = 1000
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {no_sort_med(lst[:])}')
print(timeit("no_sort_med(lst[:])", globals=globals(), number=100)) # время выполнения 3.7743530020015896

#поиск через отсечение максимальных значений работает гораздо быстрее чем предварительная сортировка методом гнома и выбором элемента m