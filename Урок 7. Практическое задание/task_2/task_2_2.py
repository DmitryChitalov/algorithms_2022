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


def median_search(m):
    data = [randint(0, 10000) for _ in range(2 * m + 1)]
    i = 1
    while i <= m:
        max_el_index = max(list(enumerate(data, 0)), key=lambda j: j[1])[0]
        data.pop(max_el_index)
        i += 1
    return max(list(enumerate(data, 0)), key=lambda j: j[1])[1]


# замер 11
print(timeit("median_search(5)", globals=globals(), number=1000))

# замер 101
print(timeit("median_search(50)", globals=globals(), number=1000))

# замер 1001
print(timeit("median_search(500)", globals=globals(), number=1000))

"""
0.022315579000860453
0.5901705840005889
32.83318424099889
"""


