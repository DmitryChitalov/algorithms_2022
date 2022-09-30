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


def without_sort(lst):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst


def merge_median(lst):
    middle = len(lst) // 2
    if len(lst) % 2 != 0:
        return lst[middle]


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(orig_list)
print(without_sort(orig_list))
print(merge_median(without_sort(orig_list)))
print(timeit("merge_median(without_sort(orig_list[:]))", globals=globals(), number=100))

m = 100
orig_list_2 = [randint(0, 100) for j in range(2 * m + 1)]
print(timeit("merge_median(without_sort(orig_list_2[:]))", globals=globals(), number=100))

m = 1000
orig_list_3 = [randint(0, 100) for k in range(2 * m + 1)]
print(timeit("merge_median(without_sort(orig_list_3[:]))", globals=globals(), number=100))

# 0.002743599994573742
# 0.27778060000855476
# 22.14555310003925
