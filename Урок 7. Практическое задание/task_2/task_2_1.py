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
from copy import deepcopy
from random import randint
from timeit import timeit


def array_median(lst_obj):
    """
Находит медиану массива методом сортировки "Расчёска"
    :param lst_obj: array
    :return: int
    """
    step = len(lst_obj)
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247331)
        flag, i = False, 0
        while i + step < len(lst_obj):
            if lst_obj[i] < lst_obj[i + step]:
                lst_obj[i], lst_obj[i + step] = lst_obj[i + step], lst_obj[i]
                flag = True
            i += 1
    return lst_obj[int((len(lst_obj)-1)/2)]


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
0.018672049000000003
--- на массиве из 101 элемента:
0.36158749
--- на массиве из 1001 элемента:
8.721983373999999
"""
