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


def heap_sort(arr):
    len_arr = len(arr)
    max_heap(arr)
    for length in range(len_arr - 1, 0, -1):
        arr[0], arr[length] = arr[length], arr[0]
        heapify(arr, 0, length)
    return arr


def max_heap(arr):
    len_arr = len(arr)
    for el_idx in range(len_arr - 1, 0, -1):
        parent = (el_idx - 1) // 2
        heapify(arr, parent, len_arr)


def heapify(arr, idx, arr_len):
    l_child_idx = 2 * idx + 1
    r_child_idx = 2 * idx + 2
    largest = idx

    if l_child_idx < arr_len and arr[l_child_idx] > arr[idx]:
        largest = l_child_idx

    if r_child_idx < arr_len and arr[r_child_idx] > arr[largest]:
        largest = r_child_idx

    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, arr_len)


def find_median(arr, number):
    return heap_sort(arr)[number]


if __name__ == '__main__':
    numbers = (5, 50, 500)
    for number in numbers:
        array_2m_1 = [randint(-100, 100) for _ in range(2 * number + 1)]
        if number == 5:  # сам массив выводится только из 10 элементов
            print(f'Массив длинной {2 * number + 1} элементов: \n{array_2m_1}\n'
                  f'Медиана: {find_median(array_2m_1[:], number)}')
            print(f'Проверка: {sorted(array_2m_1)[number]}')  # проверяем встроенной сортировкой
        else:
            print(f'Массив длинной {2 * number + 1} элементов.')
        print('Замер:', timeit('find_median(array_2m_1[:], number)', globals=globals(), number=1000))
        print('-' * 30)

# Массив длинной 11 элементов:
# [56, -56, 70, 45, 11, -77, 4, 76, 30, -15, -48]
# Медиана: 11
# Проверка: 11
# Замер: 0.0195469000027515
# ------------------------------
# Массив длинной 101 элементов.
# Замер: 0.3236126999836415
# ------------------------------
# Массив длинной 1001 элементов.
# Замер: 4.8052078000037
# ------------------------------
