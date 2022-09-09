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


def test_list(m):
    return [randint(1, 10) for _ in range(2 * m + 1)]


def median_search(lst, count=0):
    mini = min(lst)
    maxi = max(lst)
    etalon = (mini + maxi) / 2
    q = min(lst, key=lambda x: abs(x - etalon))
    return f'Медиана: {q}'


test_list_10 = test_list(5)
test_list_100 = test_list(50)
test_list_1000 = test_list(500)
print(test_list_10)
print(median_search(test_list_10[:]))

print(timeit("median_search(test_list_10[:])", globals=globals(), number=10000))
print(timeit("median_search(test_list_100[:])", globals=globals(), number=10000))
print(timeit("median_search(test_list_1000[:])", globals=globals(), number=10000))
