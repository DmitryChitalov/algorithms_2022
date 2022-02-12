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


def median_elem(el):
    for i in range(len(el) // 2):
        el.remove(max(el))
    return max(el)


print('замеры 10')
m = 5
orig_list_1 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_1[:])", globals=globals(), number=1000))

print('замеры 100')
m = 50
orig_list_2 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_2[:])", globals=globals(), number=1000))

print('замеры 1000')
m = 500
orig_list_3 = [randint(-100, 100) for _ in range(2 * m + 1)]
print(timeit("median_elem(orig_list_3[:])", globals=globals(), number=1000))