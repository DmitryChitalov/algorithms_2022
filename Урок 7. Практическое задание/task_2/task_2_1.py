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


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(array): # сортировка Кучей
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def find_median(array, m):
    heap_sort(array)
    return array[m]


m = 10
array = [randint(0, 100) for x in range(2 * m + 1)]
# print(array)
# print(heap_sort(array))
# print(median(array, 10))
print(timeit("find_median(array[:], m)", globals=globals(), number=1000)) #  0.020952700000000005

m = 100
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("find_median(array[:], m)", globals=globals(), number=1000)) # 0.332194

m = 1000
array = [randint(0, 100) for x in range(2 * m + 1)]
print(timeit("find_median(array[:], m)", globals=globals(), number=1000)) # 4.7947451
