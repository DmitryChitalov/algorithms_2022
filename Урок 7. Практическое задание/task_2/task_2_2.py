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


from random import randint
from timeit import timeit


def median_search_2(lst):

    for _ in range(len(lst) // 2):
        lst.remove(max(lst))

    return max(lst)


if __name__ == '__main__':
    m = 5
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_2(obj_lst[:])", globals=globals(), number=100))

    m = 50
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_2(obj_lst[:])", globals=globals(), number=100))

    m = 500
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_2(obj_lst[:])", globals=globals(), number=100))

"""
0.00043690799999999974
0.015991382000000002
1.423940663
"""