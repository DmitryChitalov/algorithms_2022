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

lst_10 = [randint(0, 1000) for _ in range(11)]
lst_100 = [randint(0, 1000) for _ in range(101)]
lst_1000 = [randint(0, 1000) for _ in range(1001)]


def Gnom_sort_median(lst_obj):
    i = 0
    len_obj = len(lst_obj)
    mediana = len(lst_obj) // 2
    while i + 1 < len_obj:
        if lst_obj[i + 1] >= lst_obj[i]:
            i += 1
        else:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    # print(sum(lst_obj) / len(lst_obj))
    return lst_obj[mediana]

print(Gnom_sort_median(lst_10))
print(Gnom_sort_median(lst_100))
print(Gnom_sort_median(lst_1000))
print(timeit("Gnom_sort_median(lst_10)", globals=globals(), number=1000))
print(timeit("Gnom_sort_median(lst_100)", globals=globals(), number=1000))
print(timeit("Gnom_sort_median(lst_1000)", globals=globals(), number=1000))

