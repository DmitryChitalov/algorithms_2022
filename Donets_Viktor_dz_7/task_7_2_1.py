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
from heapq import heappop, heappush
from timeit import timeit


# Буду использовать сортировку Кучей
def heap_sort(lst_obj):
    heap = []
    for i in lst_obj:
        heappush(heap, i)
    sort_lst = []
    while heap:
        sort_lst.append(heappop(heap))
    return sort_lst


m = int(input('Введите натуральное число: '))
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(orig_list)
print(heap_sort(orig_list))
print(f'Медиана массива равна: {heap_sort(orig_list)[m]} ')


# при 10 значениях
m = 10
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "heap_sort(orig_list[:])",
          globals=globals(),
          number=1000))
# при 100
m = 100
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "heap_sort(orig_list[:])",
          globals=globals(),
          number=1000))
# при 1000
m = 1000
orig_list = [randint(0, 1000) for _ in range(2 * m + 1)]
print(
    timeit(
          "heap_sort(orig_list[:])",
          globals=globals(),
          number=1000))

"""
Введите натуральное число: 15
[588, 383, 314, 193, 544, 639, 527, 61, 532, 916, 647, 437, 892, 230, 227, 801,
 101, 170, 581, 859, 175, 239, 5, 240, 769, 679, 352, 38, 257, 264, 681]
[5, 38, 61, 101, 170, 175, 193, 227, 230, 239, 240, 257, 264, 314, 352, 383, 
437, 527, 532, 544, 581, 588, 639, 647, 679, 681, 769, 801, 859, 892, 916]
Медиана массива равна: 383 
0.0056268999996973434
0.061243999999533116
0.7096019999999044
"""
