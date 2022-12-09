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

import random
import statistics
from timeit import timeit
from memory_profiler import profile


def arr_gen(dim: int):
    return [random.randint(0, 100) for _ in range(0, 2 * dim + 1)]


def gnome_sort(arr: list):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if i > 0:
                i -= 1
            else:
                i += 1
        else:
            i += 1
    medi = arr[int((len(arr) - 1) / 2)]
    return arr, medi


@profile
def memory_profiling(arr: list):
    return gnome_sort(arr)


def get_var_name(var):
    globals_dict = globals()
    return [var_name for var_name in globals_dict if globals_dict[var_name] == var][0]


def main_func(arr: list):
    sorted_arr, median = gnome_sort(arr[:])
    print(f'\nИсходный массив {len(arr)} элемент:\n{arr}')
    print(f'Отсортированный массив:\n{sorted_arr}')
    print(f'Медиана, найденная с помощью "гномьей" сортировки: {median}')
    print(f'Медиана, найденная с помощью statistics.median сортировки: {statistics.median(arr)}')
    name = f'gnome_sort({get_var_name(arr)}[:])'
    print(f'Выполнение 100 повторений заняло: '
          f'{timeit(name, "from __main__ import gnome_sort", globals=globals(), number=100):.5f} сек')
    print('Профилирование памяти:')
    memory_profiling(arr[:])


if __name__ == '__main__':
    print('"Гномья" сортировка')
    num = 10
    my_arr = arr_gen(num)
    main_func(my_arr)
    num = 100
    my_arr = arr_gen(num)
    main_func(my_arr)
    num = 1000
    my_arr = arr_gen(num)
    main_func(my_arr)
