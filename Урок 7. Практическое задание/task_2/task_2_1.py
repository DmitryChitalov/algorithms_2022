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


def median_search_1(lst):
    lst_obj = lst
    index = 1
    i = 0
    n = len(lst_obj)
    while i < n - 1:
        if lst_obj[i] <= lst_obj[i + 1]:
            i, index = index, index + 1
        else:
            lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1
    return lst_obj[m]


if __name__ == '__main__':
    m = 5
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_1(obj_lst[:])", globals=globals(), number=100))

    m = 50
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_1(obj_lst[:])", globals=globals(), number=100))

    m = 500
    obj_lst = [randint(0, 100) for _ in range(2 * m + 1)]
    print(timeit("median_search_1(obj_lst[:])", globals=globals(), number=100))

"""
0.001514916999999949
0.122654343
13.894106971
"""
