"""Стандартная сортировка"""

from random import randint
from timeit import timeit

"""
Внутри Python использует Timsort – гибридный алгоритм сортировки, 
сочетающий сортировку вставками и сортировку слиянием. 
Смысл в том, что в реальном мире часто встречаются частично 
отсортированные данные, на которых Timsort работает ощутимо 
быстрее прочих алгоритмов сортировки. Сложность по времени: 
O(n log n) в худшем случае и O(n) – в лучшем.


list.sort() - Сортирует лист, но возвращает None
sorted(list) - Сортирует лист и возвращает его
"""


def reverse_sort(lst_obj):
    ordered_list = sorted(lst_obj)
    return ordered_list


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "reverse_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.0007880000000000109
0.005651299999999998
0.10248260000000001
"""
