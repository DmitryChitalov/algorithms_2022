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


def sort_func(lst):
    res = lst
    l_lst = []
    r_lst = []
    for i in range(len(res)):
        for j in range(len(res)):
            if res[i] > res[j]:
                l_lst.append(res[j])
            if res[i] < res[j]:
                r_lst.append(res[j])
            if res[i] == res[j] and i > j:
                l_lst.append(res[j])
            if res[i] == res[j] and i < j:
                r_lst.append(res[j])
        if len(l_lst) == len(r_lst):
            return res[i]
        l_lst.clear()
        r_lst.clear()



m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "sort_funct(lst[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "sort_func(lst[:])",
        globals=globals(),
        number=100))

# ---------------------------------------------------------------------------
m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "sort_func(lst[:])",
        globals=globals(),
        number=100))
# ---------------------------------------------------------------------------
"""
0.029642699999999994 10 элементов
3.7271031            100 элементов
320.855488543        1000 элементов
"""

