"""
Поиск медианы без сортировки, массив из 10 эл-в: 0.0017420000000000005
Поиск медианы без сортировки, массив из 100 эл-в: 0.07501809999999999
Поиск медианы без сортировки, массив из 1000 эл-в: 6.4795162
"""
from random import randint
from timeit import timeit


def no_sort_median(lst):

    for i in range(len(lst) // 2):
        lst.remove(max(lst))

    return max(lst)


m = 5
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 10 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

m = 50
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 100 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

m = 500
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 1000 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

