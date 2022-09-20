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


# Сортировка Шелла является оптимизированным вариантом сортировки вставками
def shell_sort(rand_list):
    n = len(rand_list)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = rand_list[i]
            j = i
            while j >= interval and rand_list[j - interval] > temp:
                rand_list[j] = rand_list[j - interval]
                j -= interval
            rand_list[j] = temp
        k -= 1
        interval = 2**k - 1
    return rand_list


m = 10
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "shell_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 100
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "shell_sort(rand_list[:])",
        globals=globals(),
        number=100))

m = 1000
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit(
        "shell_sort(rand_list[:])",
        globals=globals(),
        number=100))
'''
0.0014859580041957088
0.020601707998139318
0.24069087499810848
'''



