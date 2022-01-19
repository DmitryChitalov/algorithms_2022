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
from numpy import average


# some_list = [-1, -2, -3, -5, 6, 7, 12]


def find_median(lst):
    t_list = lst
    # print(sorted(lst))
    for i in range(len(t_list)//2):
        t_list.remove(min(t_list))
    # print(t_list)
    return t_list[0]


m = 10
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))

m = 100
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))

m = 1000
some_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(timeit('find_median(some_list[:])', globals=globals(), number=100))


