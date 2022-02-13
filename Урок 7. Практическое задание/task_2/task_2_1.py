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
from heapq import heappop, heappush
from random import randint
from timeit import timeit


def median_by_heap_sort(arr: list, median: int) -> int:
    """
    Heap sort. returns median integer of dedicated array
    :param m: int
    :param array: list
    :return: list
    """
    heap = []
    for element in arr:
        heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heappop(heap))
    #print(f"sorted: {ordered}, median: {ordered[median]}")
    return ordered[median]


if __name__ == "__main__":
    for m in (10, 100, 1000):
        arr = [randint(-10000, 100000) for _ in range(2 * m + 1)]
        print(f'On number {m}: {timeit("median_by_heap_sort(arr[:], m)", globals=globals(), number=1000)}s')

    """
    Результаты:
        On number 10: 0.005794500000000001s
        On number 100: 0.0689686s
        On number 1000: 0.858354s   
    
    """