"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from statistics import median
from timeit import timeit
from heapq import heappop, heappush

range_numbers10 = [randint(-100, 100) for _ in range(0, 2 * 10 + 1)]
range_numbers100 = [randint(-100, 100) for _ in range(0, 2 * 100 + 1)]
range_numbers1000 = [randint(-100, 100) for _ in range(0, 2 * 1000 + 1)]


# Пирамидальная_сортировка
def heap_sort(arr, m):
    heap = []
    for ele in arr:
        heappush(heap, ele)

    sort = []
    while heap:
        sort.append(heappop(heap))

    return sort[m]


print(
    timeit(
        "heap_sort(range_numbers10[:], 10)",
        setup='from __main__ import heap_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "heap_sort(range_numbers100[:], 100)",
        setup='from __main__ import heap_sort',
        globals=globals(),
        number=100))

print(
    timeit(
        "heap_sort(range_numbers1000[:], 1000)",
        setup='from __main__ import heap_sort',
        globals=globals(),
        number=100))

"""
    Аналитика
    
    Гномья - O(n^2)
    https://ru.wikipedia.org/wiki/Гномья_сортировка
        0.0041797000000000015
        0.3993154
        41.5763291
    
    Шелла - Худшее время O(n^2), Лучшее время	O(n log^2 n)
    https://ru.wikipedia.org/wiki/Сортировка_Шелла
        0.0015565999999999983
        0.03125429999999999
        0.5737104
    
    Пирамидальная_сортировка - O(n log n)
    https://ru.wikipedia.org/wiki/Пирамидальная_сортировка
        0.0004634000000000027
        0.005853700000000003
        0.06604789999999999

    Самой быстрой и эффективной сортировкой оказалась - Пирамидальная_сортировка
    так как имеет сложность O(n log n)
"""