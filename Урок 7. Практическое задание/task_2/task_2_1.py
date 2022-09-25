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

from random import randint
from timeit import timeit


# гномья сортировка
def dwarf_sort(lst):
    n, i = len(lst), 0
    while i + 1 < n:
        if lst[i + 1] >= lst[i]:
            i += 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return lst


# 10
m = 5
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(dwarf_sort(my_list[:]))
print(f'{timeit("dwarf_sort(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (10): {dwarf_sort(my_list[:])[m]}')
print('_' * 50)

# 100
m = 50
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(dwarf_sort(my_list[:]))
print(f'{timeit("dwarf_sort(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (100): {dwarf_sort(my_list[:])[m]}')
print('_' * 50)

# 1000
m = 500
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(dwarf_sort(my_list[:]))
print(f'{timeit("dwarf_sort(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (1000): {dwarf_sort(my_list[:])[m]}')


# 0.0007526249999999998 сек.
# 0.053056959 сек.
# 6.158973792 сек.



