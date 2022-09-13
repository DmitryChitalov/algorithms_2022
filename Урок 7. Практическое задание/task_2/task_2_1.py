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


def heapify(arr_, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr_[i] < arr_[left]:
        largest = left
    if right < n and arr_[largest] < arr_[right]:
        largest = right
    if largest != i:
        arr_[i], arr_[largest] = arr_[largest], arr_[i]
        heapify(arr_, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


m = 5
lst = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(f"Сортировка списка из 11 элементов: {timeit('heapsort(lst[:])', globals=globals(), number=100)}")
m = 50
lst = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(f"Сортировка списка из 111 элементов: {timeit('heapsort(lst[:])', globals=globals(), number=100)}")
m = 500
lst = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(f"Сортировка списка из 1111 элементов: {timeit('heapsort(lst[:])', globals=globals(), number=100)}")
m = 5
lst = [randint(-100, 100) for _ in range(m * 2 + 1)]
print(f'Неотсортированный список из 10 элементов: \n{lst}')
heapsort(lst)
print(f'Неотсортированный список из 10 элементов: \n{lst}')
print(f'Медиана: {lst[m]}')

'''
Сортировка списка из 11 элементов: 0.0019139000214636326
Сортировка списка из 111 элементов: 0.03263900009915233
Сортировка списка из 1111 элементов: 0.7920198000501841
Неотсортированный список из 10 элементов: 
[93, 82, -8, 54, -35, -9, 37, -78, 96, -66, -11]
Неотсортированный список из 10 элементов: 
[-78, -66, -35, -11, -9, -8, 37, 54, 82, 93, 96]
Медиана: -8
'''
