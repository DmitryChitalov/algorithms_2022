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


def without_sort(lst_obj):
    copy_lst = lst_obj
    for i in range(len(lst_obj) // 2):
        copy_lst.remove(min(copy_lst))
    return min(copy_lst)


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("without_sort(orig_list_10[:])", globals=globals(), number=1000)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("without_sort(orig_list_100[:])", globals=globals(), number=1000)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("without_sort(orig_list_1000[:])", globals=globals(), number=1000)}')

"""
При m = 10: 0.0068201999999999985
При m = 100: 0.3582706
При m = 1000: 36.0078283
"""