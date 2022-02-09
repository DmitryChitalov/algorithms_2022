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
from timeit import timeit
from random import randint


def median(lst, m):
    n, i = len(lst), 0
    while True:
        if i + 1 == n:
            break
        if lst[i+1] >= lst[i]:
            i += 1
        else:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return lst[m], lst


med = 5
my_list = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list, med)', globals=globals(), number=1000))

med = 50
my_list2 = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list2, med)', globals=globals(), number=1000))

med = 500
my_list3 = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list3, med)', globals=globals(), number=1000))
'''
0.0042977000000000015
0.0386933
0.5550214
'''