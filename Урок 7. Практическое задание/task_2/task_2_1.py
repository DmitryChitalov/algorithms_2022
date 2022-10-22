"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


import math
from random import randint
from timeit import timeit


def shell_sort(array, m):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array[m]


m = 10
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(shell_sort(obj_list[:], m))
print(timeit("shell_sort(obj_list[:], m)", globals=globals(), number=1000))

m = 100
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(shell_sort(obj_list[:], m))
print(timeit("shell_sort(obj_list[:], m)", globals=globals(), number=1000))

m = 1000
obj_list = [randint(1, 100) for _ in range(2*m+1)]
print(shell_sort(obj_list[:], m))
print(timeit("shell_sort(obj_list[:], m)", globals=globals(), number=1000))

"""
10 элементов - 0.016677700000400364
100 элементов - 0.21560144100021716
100 элементов - 3.4418542719995457
"""