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
from statistics import median


def search_median(arr):
    for i in range(len(arr) // 2):
        arr.remove(max(arr))
    return max(arr)


m = 5
m_list = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('search_median(m_list[:])', globals=globals(), number=1000))  # 0.01
m = 50
m_list2 = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('search_median(m_list2[:])', globals=globals(), number=1000))  # 0.05
m = 500
m_list3 = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('search_median(m_list3[:])', globals=globals(), number=1000))  # 4.64
