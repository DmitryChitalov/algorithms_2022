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
from timeit import timeit
from random import randint

m = 10
ARRAY_10 = [randint(-100, 100) for i in range(2 * m + 1)]
m = 100
ARRAY_100 = [randint(-100, 100) for j in range(2 * m + 1)]
m = 1000
ARRAY_1000 = [randint(-100, 100) for k in range(2 * m + 1)]


def heap_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_heapify(arr, i)
    return arr[len(arr) // 2]


def max_heapify(arr, end):
    last_parent = (end - 1) // 2

    for parent in range(last_parent, -1, -1):
        current_parent = parent

        while current_parent <= last_parent:
            child = 2 * current_parent + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child = child + 1
            if arr[child] > arr[current_parent]:
                arr[current_parent], arr[child] = arr[child], arr[current_parent]
                current_parent = child
            else:
                break
    arr[0], arr[end] = arr[end], arr[0]


if __name__ == '__main__':
    print(f'Median of array with m = 10: {heap_sort(ARRAY_10[:])}',
          timeit('heap_sort(ARRAY_10[:])', globals=globals(), number=100))
    print(f'Median of array with m = 100: {heap_sort(ARRAY_100[:])}',
          timeit('heap_sort(ARRAY_100[:])', globals=globals(), number=100))
    print(f'Median of array with m = 1000: {heap_sort(ARRAY_1000[:])}',
          timeit('heap_sort(ARRAY_1000[:])', globals=globals(), number=100))
