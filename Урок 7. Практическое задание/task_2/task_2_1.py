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
from timeit import timeit


def gnome_sort(lst_obj):
    """
    Гномья сортировка
    """
    i = 1
    while i < len(lst_obj):
        if not i or lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
            i -= 1
    return lst_obj[m]


m = 10
orig_list_10 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("gnome_sort(orig_list_10[:])", globals=globals(), number=100)}')

m = 100
orig_list_100 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("gnome_sort(orig_list_100[:])", globals=globals(), number=100)}')

m = 1000
orig_list_1000 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'При m = {m}: {timeit("gnome_sort(orig_list_1000[:])", globals=globals(), number=100)}')

# При m = 10: 0.0051567
# При m = 100: 0.38484999999999997
# При m = 1000: 49.0532472
