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
from timeit import timeit
from random import randint


def median(lst):
    for i in range(len(lst)//2):
        lst.remove(max(lst))
    return max(lst)


my_list = [randint(-100, 100) for _ in range(2 * 5 + 1)]
print(timeit('median(my_list)', globals=globals(), number=1000))

my_list2 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
print(timeit('median(my_list2)', globals=globals(), number=1000))

my_list3 = [randint(-100, 100) for _ in range(2 * 500 + 1)]
print(timeit('median(my_list3)', globals=globals(), number=1000))
'''
0.0009389000000000064
0.0011957000000000079
0.03301849999999999
'''