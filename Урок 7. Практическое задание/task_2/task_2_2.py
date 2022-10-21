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
    arr = [randint(-1000, 1000) for i in range(2 * n + 1)]
    for i in range(n):
        arr.remove(max(arr))
    return max(arr)


print(find_median(5))
print(timeit("find_median(5)", globals=globals(), number=1000))  #0.006613834004383534 11 элементов
print(timeit("find_median(50)", globals=globals(), number=1000)) #0.0817542080039857 101 элемент
print(timeit("find_median(500)", globals=globals(), number=1000))#4.378883541998221 1001 элемент