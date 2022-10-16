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


def find_median(arr):
    while len(arr) > m + 1:
        arr.remove(max(arr))
    median = max(arr)
    return median


# замер 10:  0.0033837000009953044
m = 5
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))

# замер 100:  0.09009939999668859
m = 50
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))

# замер 1000:  7.3999244000006
m = 500
my_array = [randint(1, 100) for _ in range(2 * m + 1)]

print(
    timeit(
        "find_median(my_array[:])",
        globals=globals(),
        number=1000))

print('исходный массив:', my_array)
print('медиана: ', find_median(my_array[:]))
