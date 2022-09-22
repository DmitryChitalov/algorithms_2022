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


def median_search(lst):
    array = lst[:]
    while len(array) > len(lst) // 2 + 1:
        array.remove(max(array))
    return max(array)


# 10 элементов
m = 5
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))     # 0.0002823000540956855
print(f'Медиана - {median_search(orig_list)}')                                  # Медиана - -34

# 100 элементов
m = 50
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))     # 0.009978899965062737
print(f'Медиана - {median_search(orig_list)}')                                  # Медиана - -8

# 1000 элементов
m = 500
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(timeit('median_search(orig_list[:])', globals=globals(), number=100))     # 0.6829406999750063
print(f'Медиана - {median_search(orig_list)}')                                  # Медиана - 0

"""
Проверка
"""
m = 10
orig_list = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(f'Неотсортированный список {orig_list}')
print(f'Медиана - {median_search(orig_list)}')
print(f'Отсортированный список {sorted(orig_list)}')
print(f'Медиана - {median_search(orig_list)}')
"""
Неотсортированный список [78, 3, -50, -80, -80, -97, 21, 90, 42, 8, 30, 63, -27, 24, 91, -7, 44, -9, -78, -54, -53]
Медиана - 3
Отсортированный список [-97, -80, -80, -78, -54, -53, -50, -27, -9, -7, 3, 8, 21, 24, 30, 42, 44, 63, 78, 90, 91]
Медиана - 3
"""
