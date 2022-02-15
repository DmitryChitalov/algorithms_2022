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


def array_gen(m):
    return [randint(-100, 100) for _ in range(2 * m + 1)]


def median_del_max_elem(lst):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return f'Медиана списка = {max(lst)}'


test_list_11 = array_gen(5)
test_list_101 = array_gen(50)
test_list_1001 = array_gen(500)

print(timeit("median_del_max_elem(test_list_11[:])", globals=globals(), number=1000))
print(timeit("median_del_max_elem(test_list_101[:])", globals=globals(), number=1000))
print(timeit("median_del_max_elem(test_list_1001[:])", globals=globals(), number=1000))

"""
0.0014527310013363604
0.051363287999265594
5.1892462040013925
"""
