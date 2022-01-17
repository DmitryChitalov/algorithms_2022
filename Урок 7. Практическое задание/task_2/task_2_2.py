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


def find_median(lst):
    if len(lst) % 2 == 0:
        center = []
        for i in lst:
            b = 0
            for j in lst:
                if i < j:
                    b += 1
            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2
    else:
        for i in lst:
            num = i
            b = 0
            for j in lst:
                if i < j:
                    b += 1
            if len(lst) == 2 * b + 1:
                return num


m = 10
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("find_median(array[:])", globals=globals(), number=1000))  # 0.0032130000000000023

m = 100
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("find_median(array[:])", globals=globals(), number=1000))  #  0.8905265

m = 1000
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("find_median(array[:])", globals=globals(), number=1000))  #  101.7426828
