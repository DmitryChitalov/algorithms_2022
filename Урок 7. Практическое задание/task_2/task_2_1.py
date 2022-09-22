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


# сортировка Шелла
def shell_sort(lst):
    step = len(lst) // 2
    while step > 0:
        for i in range(step, len(lst)):
            j = i
            delta = j - step
            while delta >= 0 and lst[delta] > lst[j]:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst


# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))   # 0.005188999930396676
print(f'Медиана - {shell_sort(orig_list[:])[m]}')                           # медиана - 21

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))   # 0.11886179994326085
print(f'Медиана - {shell_sort(orig_list[:])[m]}')                           # Медиана - -11

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("shell_sort(orig_list[:])", globals=globals(), number=1000))   # 1.7492560999235138
print(f'Медиана - {shell_sort(orig_list[:])[m]}')                           # Медиана - 0
