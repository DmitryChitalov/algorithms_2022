"""
Гномья сортировка, массив из 10 эл-в: 0.008193800000000001
Гномья сортировка, массив из 100 эл-в: 0.5651402000000001
Гномья сортировка, массив из 1000 эл-в: 68.85820460000001
"""
from random import randint
from timeit import timeit


def gnome_sort(lst, m):
    idx = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] <= lst[i + 1]:
            i, idx = idx, idx + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i -= 1
            if i < 0:
                i, idx = idx, idx + 1
    return lst[m]


m = 5
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 10 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')

m = 50
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 100 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')


m = 500
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 1000 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')



