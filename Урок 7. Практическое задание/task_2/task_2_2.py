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


def find_median(n):
    array = [randint(-1000, 1000) for i in range(2 * n + 1)]
    for i in range(n):
        array.remove(max(array))
    return max(array)


print(find_median(5))
print(timeit("find_median(5)", globals=globals(), number=1000))  #0.025952199999999995
print(timeit("find_median(50)", globals=globals(), number=1000)) #0.247384
print(timeit("find_median(500)", globals=globals(), number=1000))#9.647211
