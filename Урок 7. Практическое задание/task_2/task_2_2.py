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


def get_median(m):
    my_list = [randint(0, (2 * m + 1)) for _ in range(2 * m + 1)]
    middle = round(len(my_list) / 2)
    while len(my_list) != middle:
        my_list.remove(max(my_list))
    return max(my_list)


print(timeit('get_median(5)', globals=globals(), number=100))
print(timeit('get_median(50)', globals=globals(), number=100))
print(timeit('get_median(500)', globals=globals(), number=100))
