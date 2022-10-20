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
from random import randint
from timeit import timeit
import math

# Замеры 10
m = 5

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]


def median_shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return f"Медианой списка {array} является число: {array[m]}"


print(median_shell_sort(random_list[:]))

print(
    timeit(
        "median_shell_sort(random_list)",
        globals=globals(),
        number=1000))

# Замеры 100
m = 50

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(median_shell_sort(random_list[:]))

print(
    timeit(
        "median_shell_sort(random_list)",
        globals=globals(),
        number=1000))

# Замеры 1000
m = 500

random_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(median_shell_sort(random_list[:]))

print(
    timeit(
        "median_shell_sort(random_list)",
        globals=globals(),
        number=1000))

"""
Время выполнения:

Массив из 10 элементов - 0.006695199990645051
Массив из 100 элементов - 0.06743200006894767
Массив из 1000 элементов - 1.095961500192061
"""
