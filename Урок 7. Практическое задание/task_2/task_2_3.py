"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

import statistics
from task_2_1 import arr_gen
from timeit import timeit
from memory_profiler import profile


def heapify(arr: list, arr_lenght: int, old_root: int):
    root = old_root
    left = 2 * old_root + 1
    right = 2 * old_root + 2
    if left < arr_lenght and arr[old_root] < arr[left]:
        root = left
    if right < arr_lenght and arr[root] < arr[right]:
        root = right
    if root != old_root:
        arr[old_root], arr[root] = arr[root], arr[old_root]
        heapify(arr, arr_lenght, root)


def heap_sort(arr: list):
    length = len(arr)
    for root in range(length, -1, -1):
        heapify(arr, length, root)
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    medi = arr[int((len(arr) - 1) / 2)]
    return arr, medi


@profile
def memory_profiling(arr: list):
    return heap_sort(arr)


def get_var_name(var):
    globals_dict = globals()
    return [var_name for var_name in globals_dict if globals_dict[var_name] == var][0]


def main_func(arr: list):
    sorted_arr, median = heap_sort(arr[:])
    print(f'\nИсходный массив {len(arr)} элемент:\n{arr}')
    print(f'Отсортированный массив:\n{sorted_arr}')
    print(f'Медиана, найденная с помощью сортировки кучей: {median}')
    print(f'Медиана, найденная с помощью statistics.median сортировки: {statistics.median(arr)}')
    name = f'heap_sort({get_var_name(arr)}[:])'
    print(f'Выполнение 100 повторений заняло: '
          f'{timeit(name, "from __main__ import heap_sort", globals=globals(), number=100):.5f} сек')
    print('Профилирование памяти:')
    memory_profiling(arr[:])


if __name__ == '__main__':
    print('Cортировка кучей')
    num = 10
    my_arr = arr_gen(num)
    main_func(my_arr)
    num = 100
    my_arr = arr_gen(num)
    main_func(my_arr)
    num = 1000
    my_arr = arr_gen(num)
    main_func(my_arr)
