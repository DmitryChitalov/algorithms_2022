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

import statistics
from timeit import timeit
from memory_profiler import profile
from task_2_1 import arr_gen


def insertion_sort(lst_obj):
    for i in range(len(lst_obj)):
        v = lst_obj[i]
        j = i

        while (lst_obj[j-1] > v) and (j > 0):

            lst_obj[j] = lst_obj[j-1]
            j = j - 1

        lst_obj[j] = v
    return lst_obj


def shell_sort(arr: list):
    last_index = len(arr)
    h = len(arr) // 2
    while h > 0:
        for i in range(h, last_index, 1):
            j = i
            offset = j - h
            while offset >= 0 and arr[offset] > arr[j]:
                arr[offset], arr[j] = arr[j], arr[offset]
                j = offset
                offset = j - h
        h //= 2
    medi = arr[int((len(arr) - 1) / 2)]
    return arr, medi


def shell_sort_hibbard(arr: list):
    last_index = len(arr)
    k = 1
    h = 2 ** k - 1
    while h < last_index:
        for i in range(h, last_index, 1):
            j = i
            delta = j - h
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - h
        k += 1
        h = 2 ** k - 1
    medi = arr[int((len(arr) - 1) / 2)]
    return arr, medi


@profile
def memory_profiling(arr: list):
    return shell_sort(arr)


def get_var_name(var):
    globals_dict = globals()
    return [var_name for var_name in globals_dict if globals_dict[var_name] == var][0]


def main_func(arr: list, method='standard'):
    if method == 'standard':
        sorted_arr, median = shell_sort(arr[:])
        print(f'\nИсходный массив {len(arr)} элемент:\n{arr}')
        print(f'Отсортированный массив:\n{sorted_arr}')
        print(f'Медиана, найденная с помощью сортировки Шелла: {median}')
        print(f'Медиана, найденная с помощью statistics.median сортировки: {statistics.median(arr)}')
        name = f'shell_sort({get_var_name(arr)}[:])'
        print(f'Выполнение 100 повторений заняло: '
            f'{timeit(name, "from __main__ import shell_sort", globals=globals(), number=100):.5f} сек')
        print('Профилирование памяти:')
        memory_profiling(arr[:])
    elif method == 'hibbard':
        sorted_arr, median = shell_sort_hibbard(arr[:])
        print(f'\nИсходный массив {len(arr)} элемент:\n{arr}')
        print(f'Отсортированный массив:\n{sorted_arr}')
        print(f'Медиана, найденная с помощью сортировки Шелла (посл. Хиббарда): {median}')
        print(f'Медиана, найденная с помощью statistics.median сортировки: {statistics.median(arr)}')
        name = f'shell_sort_hibbard({get_var_name(arr)}[:])'
        print(f'Выполнение 100 повторений заняло: '
              f'{timeit(name, "from __main__ import shell_sort_hibbard", globals=globals(), number=100):.5f} сек')
        print('Профилирование памяти:')
        memory_profiling(arr[:])


if __name__ == '__main__':
    print('\nСортировка Шелла, последовательность h = 2 / N, 2 / h ...\n\n'
          '                   САМАЯ БЫСТРАЯ')
    m = 10
    my_arr = arr_gen(m)
    main_func(my_arr)
    m = 100
    my_arr = arr_gen(m)
    main_func(my_arr)
    m = 1000
    my_arr = arr_gen(m)
    main_func(my_arr)
    print('Сортировка Шелла, последовательность 2 ** n - 1')
    print('Примечание. Производительность ухудшилась. Возможно я где-то допустил ошибку.')
    m = 10
    my_arr = arr_gen(m)
    main_func(my_arr, method='hibbard')
    m = 100
    my_arr = arr_gen(m)
    main_func(my_arr, method='hibbard')
    m = 1000
    my_arr = arr_gen(m)
    main_func(my_arr, method='hibbard')
