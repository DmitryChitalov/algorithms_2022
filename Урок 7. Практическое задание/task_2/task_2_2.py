from random import randint
from timeit import timeit
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

def median(data, m):
    while m > 0:
        data.pop(data.index(max(data)))
        m -= 1
    return data.pop(data.index(max(data)))

# m = 10
data_1 = [randint(-100, 100) for _ in range(21)]
print(timeit("median(data_1[:], 10)", globals=globals(), number=1000))
print(median(data_1, 10))
# время: 0.010820562999999978

# m = 100
data_2 = [randint(-100, 100) for _ in range(201)]
print(timeit("median(data_2[:], 100)", globals=globals(), number=1000))
print(median(data_2, 100))
# время: 0.601101051

# m = 1000
data_3 = [randint(-100, 100) for _ in range(2001)]
print(timeit("median(data_3[:], 1000)", globals=globals(), number=1000))
print(median(data_3, 1000))
# время: 57.151018901
