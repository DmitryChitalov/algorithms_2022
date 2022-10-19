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


def gnome(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


orig_list_10 = [randint(1, 888) for _ in range(2 * 10 + 1)]
orig_list_100 = [randint(1, 888) for _ in range(2 * 100 + 1)]
orig_list_1000 = [randint(1, 888) for _ in range(2 * 1000 + 1)]

print(f"Original_massive_10 >>> {orig_list_10}")
print(
    f'Sorted_massive_10 >>> {gnome(orig_list_10[:])}\n'
    f'Median >>> {gnome(orig_list_10[:])[10]}\n'
    f'Time >>> '
    f'{timeit("gnome(orig_list_10[:])", globals=globals(), number=100)}')

# Sorted_massive_10 >>>
# [64, 77, 94, 128, 164, 164, 168, 182, 213, 246, 307, 329, 339, 357, 412, 462, 539, 551, 857, 879, 881]
# Median >>> 307
# Time >>> 0.004539323999999997

print(f"Original_massive_100 >>> {orig_list_100}")
print(
    f'Sorted_massive_100 >>> {gnome(orig_list_100[:])}\n'
    f'Median >>> {gnome(orig_list_100[:])[100]}\n'
    f'Time >>> '
    f'{timeit("gnome(orig_list_100[:])", globals=globals(), number=100)}')

# Median >>> 528
# Time >>> 0.386815961

print(f"Original_massive_1000 >>> {orig_list_1000}")
print(
    f'Sorted_massive_1000 >>> {gnome(orig_list_1000[:])}\n'
    f'Median >>> {gnome(orig_list_1000[:])[1000]}\n'
    f'Time >>> '
    f'{timeit("gnome(orig_list_1000[:])", globals=globals(), number=100)}')

# Median >>> 423
# Time >>> 49.240380591000005

"""Для решения была использована оптимизированная гномья сортировка с запоминанием
позиций начала обменов и быстрому возврату к этим позициям после их завершения"""
