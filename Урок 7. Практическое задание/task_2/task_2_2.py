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


def find_median(m):
    my_list = list(randint(1, 100) for _ in range(2 * m + 1))
    while len(my_list) > m + 1:
        my_list.pop(my_list.index(max(my_list)))
    return len(my_list), max(my_list)


print(
    timeit(
        "find_median(10)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "find_median(100)",
        globals=globals(),
        number=1000))
print(
    timeit(
        "find_median(1000)",
        globals=globals(),
        number=1000))

'''
0.01786380005069077
0.3424142999574542
20.72079519997351
'''