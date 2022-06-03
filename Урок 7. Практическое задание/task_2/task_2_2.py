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

"""
Время выполнения:
При длине массива (2m + 1), где m = 5: 0.0005113000515848398 сек.
При длине массива (2m + 1), где m = 50: 0.011920100077986717 сек.
При длине массива (2m + 1), где m = 500: 0.7763685998506844 сек.
"""

from timeit import timeit
from random import randint


def search_median(lst_obj, m):
    for _ in range(len(lst_obj) - (m + 1)):
        lst_obj.remove(max(lst_obj))
    return f'медиана равна: {max(lst_obj)}'


m = 5
array_11 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(search_median(array_11[:], m))
print(f"Время выполнения со списком из {2 * m + 1} элементов: "
      f"{timeit(f'search_median(array_11[:], m)', globals=globals(), number=100)} сек.\n")

m = 50
array_101 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(search_median(array_101[:], m))
print(f"Время выполнения со списком из {2 * m + 1} элементов: "
      f"{timeit(f'search_median(array_101[:], m)', globals=globals(), number=100)} сек.\n")

m = 500
array_1001 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(search_median(array_1001[:], m))
print(f"Время выполнения со списком из {2 * m + 1} элементов: "
      f"{timeit(f'search_median(array_1001[:], m)', globals=globals(), number=100)} сек.")
