"""Сортировка вставками"""

from random import randint
from timeit import timeit


def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        v = lst_obj[i]
        j = i

        while (lst_obj[j-1] > v) and (j > 0):

            lst_obj[j] = lst_obj[j-1]
            j = j - 1

        lst_obj[j] = v
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "insertion_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.006171599999999999
0.5522702
52.527727
"""