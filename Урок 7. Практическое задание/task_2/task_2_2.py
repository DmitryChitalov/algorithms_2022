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
from copy import deepcopy


def array_median(lst_obj):
    """
Находит медиану массива
    :param lst_obj: array
    :return: int
    """
    for _ in range(int(len(lst_obj) / 2)):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


test_list = [randint(-1000, 1000) for _ in range(101)]
test_list_1 = deepcopy(test_list)
# test_list = [1, 5, 2, 10, 14, 15, 6, 3, 7, 4, 8, 11, 16, 9, 12, 13, 17]

print(test_list)
print(array_median(test_list))
print(
    timeit(
        "array_median(test_list_1[:])",
        globals=globals(),
        number=1000))

"""
Замеры времени:
--- на массиве из 11 элементов:
0.004562643999999998
--- на массиве из 101 элемента:
0.148497288
--- на массиве из 1001 элемента:
14.104243986999998
"""
