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


def middle(arr):
    for i in range(len(arr)//2):
        arr.remove(max(arr))
    return max(arr)


data_11 = [randint(-100, 100) for _ in range(2 * 5 + 1)]
data_101 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
data_1001 = [randint(-100, 100) for _ in range(2 * 500 + 1)]

print(data_11)
print(sorted(data_11))
print('Значение медианы: ', middle(data_11))

print('Время выполнения функции при 11 элементах: ', timeit('middle(data_11[:])', number=1000, globals=globals()))
print('Время выполнения функции при 101 элементе ', timeit('middle(data_101[:])', number=1000, globals=globals()))
print('Время выполнения функции при 1001 элементе ', timeit('middle(data_1001[:])', number=1000, globals=globals()))
