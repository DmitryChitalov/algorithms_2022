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
ARRAY_10 = [randint(-1000, 1000) for z in range(2 * m + 1)]
m = 100
ARRAY_100 = [randint(-1000, 1000) for y in range(2 * m + 1)]
m = 1000
ARRAY_1000 = [randint(-1000, 1000) for x in range(2 * m + 1)]


def no_sort(arr):
    left = []
    right = []
    for n in range(len(arr)):
        for t in range(len(arr)):
            if arr[n] > arr[t]:
                left.append(arr[t])
            if arr[n] < arr[t]:
                right.append(arr[t])
            if arr[n] == arr[t] and n > t:
                left.append(arr[t])
            if arr[n] == arr[t] and n < t:
                right.append(arr[t])
        if len(left) == len(right):
            return arr[n]
        left.clear()
        right.clear()


if __name__ == '__main__':
    print(f'Median of array with m = 10: {no_sort(ARRAY_10[:])}',
          timeit('no_sort(ARRAY_10[:])', globals=globals(), number=100))
    print(f'Median of array with m = 100: {no_sort(ARRAY_100[:])}',
          timeit('no_sort(ARRAY_100[:])', globals=globals(), number=100))
    print(f'Median of array with m = 1000: {no_sort(ARRAY_1000[:])}',
          timeit('no_sort(ARRAY_1000[:])', globals=globals(), number=100))
