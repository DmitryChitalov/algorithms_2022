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


def find_median(lst):
    arr = lst.copy()
    while len(arr) > len(lst) // 2 + 1:
        arr.remove(max(arr))
    return max(arr)


# 10
m = 5
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'{timeit("find_median(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (10): {find_median(my_list[:])}')
print('_' * 50)

# 100
m = 50
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'{timeit("find_median(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (100): {find_median(my_list[:])}')
print('_' * 50)

# 1000
m = 500
my_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'{timeit("find_median(my_list[:])", globals=globals(), number=100)} сек.')
print(f'Медиана (1000): {find_median(my_list[:])}')

# 0.00026887500000000175 сек.
# 0.009896958 сек.
# 0.594641875 сек.

# отнсительно неплохо показывает себя на больших списках
