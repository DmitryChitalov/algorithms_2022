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


# Функция преобразования массива в кучу
def convert_to_heap(list_in, list_size, idx):
    max_idx = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    if left < list_size and list_in[idx] < list_in[left]:
        max_idx = left
    if right < list_size and list_in[max_idx] < list_in[right]:
        max_idx = right
    if max_idx != idx:
        list_in[idx], list_in[max_idx] = list_in[max_idx], list_in[idx]
        convert_to_heap(list_in, list_size, max_idx)


# Функция сортировки кучей
def heap_sort(list_in):
    list_size = len(list_in)
    for idx in range(list_size, -1, -1):
        convert_to_heap(list_in, list_size, idx)
    for idx in range(list_size - 1, 0, -1):
        list_in[idx], list_in[0] = list_in[0], list_in[idx]
        convert_to_heap(list_in, idx, 0)


def median_search(list_in):
    heap_sort(list_in)
    list_size = len(list_in)
    return list_in[list_size // 2]


if __name__ == '__main__':
    tlist = [12, 11, 13, 5, 6, 7, 1]
    print('Массив:', tlist, 'Медиана:', median_search(tlist))
    test_list10 = [randint(1, 10) for _ in range(11)]
    test_list100 = [randint(1, 100) for _ in range(101)]
    test_list1000 = [randint(1, 1000) for _ in range(1001)]
    print('Время выполнения на массиве длиной 10 элементов', timeit("median_search(test_list10[:])",
                                                                    globals=globals(), number=500))
    print('Время выполнения на массиве длиной 100 элементов', timeit("median_search(test_list100[:])",
                                                                    globals=globals(), number=500))
    print('Время выполнения на массиве длиной 1000 элементов', timeit("median_search(test_list1000[:])",
                                                                    globals=globals(), number=500))
    """
    Время выполнения на массиве длиной 10 элементов 0.02944860000000002
    Время выполнения на массиве длиной 100 элементов 0.5885148
    Время выполнения на массиве длиной 1000 элементов 8.498243500000001
    """
