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
from timeit import timeit
from random import randint

m = 10
ARRAY_10 = [randint(-100, 100) for i in range(2 * m + 1)]
m = 100
ARRAY_100 = [randint(-100, 100) for j in range(2 * m + 1)]
m = 1000
ARRAY_1000 = [randint(-100, 100) for k in range(2 * m + 1)]


def no_sort(arr):
    left = []
    right = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                left.append(arr[j])
            if arr[i] < arr[j]:
                right.append(arr[j])
            if arr[i] == arr[j] and i > j:
                left.append(arr[j])
            if arr[i] == arr[j] and i < j:
                right.append(arr[j])
        if len(left) == len(right):
            return arr[i]
        left.clear()
        right.clear()


if __name__ == '__main__':
    print(f'Median of array with m = 10: {no_sort(ARRAY_10[:])}',
          timeit('no_sort(ARRAY_10[:])', globals=globals(), number=100))
    print(f'Median of array with m = 100: {no_sort(ARRAY_100[:])}',
          timeit('no_sort(ARRAY_100[:])', globals=globals(), number=100))
    print(f'Median of array with m = 1000: {no_sort(ARRAY_1000[:])}',
          timeit('no_sort(ARRAY_1000[:])', globals=globals(), number=100))
