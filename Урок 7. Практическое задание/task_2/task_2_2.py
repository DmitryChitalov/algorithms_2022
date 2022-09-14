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
# from operator import itemgetter
from random import randint
from timeit import timeit


def inp_m_get_my_lst(m):
    len_my_lst = 2 * m + 1
    orig_list = [randint(-100, 100) for _ in range(len_my_lst)]
    return orig_list


def median_without_sorting(my_lst):
    copy_my_lst = my_lst[:]
    repetitions = len(my_lst[:]) // 2 + 1
    i = len(copy_my_lst)
    while i >= repetitions:
        # ind_min_el, min_pop_el = min(enumerate(copy_my_lst), key=itemgetter(1))
        # странно, но с этой строкой в 2 раза медленее по замерам.
        min_pop_el = min(copy_my_lst)
        ind_min_el = copy_my_lst.index(min_pop_el)
        if i != repetitions:
            copy_my_lst.pop(ind_min_el)
            i -= 1
        else:
            return copy_my_lst.pop(ind_min_el)


orig_list_10 = inp_m_get_my_lst(10)
print(f'median_without_sorting(orig_list_10): {median_without_sorting(orig_list_10)}.')
print('orig_list_10', orig_list_10)
# замеры 10
print(
    timeit(
        "median_without_sorting(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list_100 = inp_m_get_my_lst(100)
print(f'median_without_sorting(orig_list_100[:]): {median_without_sorting(orig_list_100[:])}.')
# замеры 100
print(
    timeit(
        "median_without_sorting(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list_1000 = inp_m_get_my_lst(1000)
print(f'median_without_sorting(orig_list_1000[:]): {median_without_sorting(orig_list_1000[:])}.')
# замеры 1000
print(
    timeit(
        "median_without_sorting(orig_list_1000[:])",
        globals=globals(),
        number=1000))

"""
median_without_sorting(orig_list_10[:]): -38.
0.021191700000000008
median_without_sorting(orig_list_100[:]): 7.
1.1645812
median_without_sorting(orig_list_1000[:]): 3.
88.9141718
"""
