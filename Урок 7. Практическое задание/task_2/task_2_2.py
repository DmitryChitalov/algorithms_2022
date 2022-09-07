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
from random import choice, randint
from timeit import timeit


def median_no_sort(list_in, mean):
    if len(list_in) == 1:
        return list_in[0]
    pivot = choice(list_in)
    less = [el for el in list_in if el < pivot]
    over = [el for el in list_in if el > pivot]
    pivots = [el for el in list_in if el == pivot]

    if mean < len(less):
        return median_no_sort(less, mean)
    elif mean < len(less) + len(pivots):
        return pivots[0]
    else:
        return median_no_sort(over, mean - len(less) - len(pivots))


if __name__ == '__main__':
    tlist = [12, 11, 13, 5, 6, 7, 1]
    print('Массив:', tlist, 'Медиана:', median_no_sort(tlist, len(tlist) / 2))
    test_list10 = [randint(1, 10) for _ in range(11)]
    test_list100 = [randint(1, 100) for _ in range(101)]
    test_list1000 = [randint(1, 1000) for _ in range(1001)]
    print('Время выполнения на массиве длиной 10 элементов',
          timeit("median_no_sort(test_list10[:], len(test_list10[:]) / 2)", globals=globals(), number=500))
    print('Время выполнения на массиве длиной 100 элементов',
          timeit("median_no_sort(test_list100[:], len(test_list100[:]) / 2)", globals=globals(), number=500))
    print('Время выполнения на массиве длиной 1000 элементов',
          timeit("median_no_sort(test_list1000[:], len(test_list1000[:]) / 2)", globals=globals(), number=500))

    """
    Время выполнения на массиве длиной 10 элементов 0.015039200000000016
    Время выполнения на массиве длиной 100 элементов 0.07377239999999999
    Время выполнения на массиве длиной 1000 элементов 0.6065334
    """
