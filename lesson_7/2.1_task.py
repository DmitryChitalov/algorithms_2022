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


def bin_heap(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        bin_heap(arr, n, largest)


def heap_sort(lst):
    n = len(lst)

    for i in range(n, -1, -1):
        bin_heap(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        bin_heap(lst, i, 0)
    return f'Median number is: {lst[m]}'


m = 10
fst_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('heap_sort(fst_lst[:])', globals=globals(), number=1000))  # 0.03

m = 100
sec_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('heap_sort(sec_lst[:])', globals=globals(), number=1000))  # 0.54

m = 1000
thrd_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(timeit('heap_sort(thrd_lst[:])', globals=globals(), number=1000))  # 8.14
