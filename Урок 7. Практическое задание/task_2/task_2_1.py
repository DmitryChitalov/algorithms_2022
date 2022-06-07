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


def heapify(arr, n, i):
    """
    Функция преобразовывает массив в двоичную кучу

    :param arr: массив, передающийся в функцию
    :param n: размер кучи
    :param i: индекс
    :return:
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return f'Медианой является число: {arr[m]}'


m = 5
m_list = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('heap_sort(m_list[:])', globals=globals(), number=1000))  # 0.01

m = 50
m_list2 = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('heap_sort(m_list2[:])', globals=globals(), number=1000))  # 0.22

m = 500
m_list3 = [randint(-1000, 1000) for _ in range(2*m+1)]
print(timeit('heap_sort(m_list3[:])', globals=globals(), number=1000))  # 3.57
