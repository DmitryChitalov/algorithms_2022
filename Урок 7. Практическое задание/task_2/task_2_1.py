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


def find_median_shell(arr):
    gap = len(arr) // 2
    while gap:
        for i in range(gap, len(arr)):
            val = arr[i]
            pos = i
            while pos >= gap and arr[pos - gap] > val:
                arr[pos] = arr[pos - gap]
                pos -= gap
                arr[pos] = val
        gap = gap // 2
    return arr[len(arr)//2]


data_11 = [randint(-100, 100) for _ in range(2 * 5 + 1)]
data_101 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
data_1001 = [randint(-100, 100) for _ in range(2 * 500 + 1)]

print(data_11)
print(sorted(data_11))
print('Значение медианы: ', find_median_shell(data_11[:]))

print('Время выполнения сортировки Шелла на массиве из 11 элементов: ', timeit('find_median_shell(data_11[:])', number=1000, globals=globals()))
print('Время выполнения сортировки Шелла на массиве из 101 элементов: ', timeit('find_median_shell(data_101[:])', number=1000, globals=globals()))
print('Время выполнения сортировки Шелла на массиве из 1001 элементов: ', timeit('find_median_shell(data_1001[:])', number=1000, globals=globals()))