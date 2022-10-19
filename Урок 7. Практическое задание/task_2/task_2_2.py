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
from timeit import timeit
from random import randint


def unsorted(data, n):
    pass


orig_list_10 = [randint(1, 888) for _ in range(2 * 10 + 1)]
orig_list_100 = [randint(1, 888) for _ in range(2 * 100 + 1)]
orig_list_1000 = [randint(1, 888) for _ in range(2 * 1000 + 1)]

print(f"Original_massive_10 >>> {orig_list_10}")
print(
    f'Median >>> {unsorted(orig_list_10[:], 10)}\n'
    f'Time >>> '
    f'{timeit("unsorted(orig_list_10[:], 5)", globals=globals(), number=100)}')

print(f"Original_massive_100 >>> {orig_list_100}")
print(
    f'Median >>> {unsorted(orig_list_100[:], 100)}\n'
    f'Time >>> '
    f'{timeit("unsorted(orig_list_100[:], 100)", globals=globals(), number=100)}')

print(f"Original_massive_1000 >>> {orig_list_1000}")
print(
    f'Median >>> {unsorted(orig_list_1000[:], 1000)}\n'
    f'Time >>> '
    f'{timeit("unsorted(orig_list_1000[:], 1000)", globals=globals(), number=100)}')
