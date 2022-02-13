"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки max(), pop()

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def find_median(arr: list) -> int:
    arr_median = round(len(arr)/2)
    for _ in range(arr_median):
        arr.remove(max(arr))
    return max(arr)


if __name__ == "__main__":
    for m in (10, 100, 1000):
        arr = [randint(-10000, 100000) for _ in range(2 * m + 1)]
        #print(arr, find_median(arr))
        print(f'On number {m}: {timeit("find_median(arr[:])", globals=globals(), number=1000)}s')

    """
    Результаты:
        On number 10: 0.006586000000000002s
        On number 100: 0.36700950000000004s
        On number 1000: 34.6195522s
    """