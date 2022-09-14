"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from statistics import median
from timeit import timeit


def inp_m_get_my_lst(m):
    len_my_lst = 2 * m + 1
    orig_list = [randint(-100, 100) for _ in range(len_my_lst)]
    return orig_list


orig_list_10 = inp_m_get_my_lst(10)
print(f'median(orig_list_10): {median(orig_list_10)}.')
print('orig_list_10', orig_list_10)
# замеры 10
print(
    timeit(
        "median(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list_100 = inp_m_get_my_lst(100)
print(f'median(orig_list_100[:]): {median(orig_list_100[:])}.')
# замеры 100
print(
    timeit(
        "median(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list_1000 = inp_m_get_my_lst(1000)
print(f'median(orig_list_1000[:]): {median(orig_list_1000[:])}.')
# замеры 1000
print(
    timeit(
        "median(orig_list_1000[:])",
        globals=globals(),
        number=1000))

"""
median(orig_list_10[:]): -12.
0.0023120999999999836
median(orig_list_100[:]): 19.
0.024802800000000014
median(orig_list_1000[:]): 0.
0.45301279999999994
"""
#  Способ поиска медианы с помощью встроенной функции поиска медианы самый эффективый, и,
#  чем больше количество элементов в списке, тем эффективнее.
#  Для небольшого количества элементов, скорости исполнения алгоритма сравнимые (практически одинаковы).
#  Поиск медианы без сортировки второй по скорости.
#  Поиск медианы с помощью рекурсивной сортировки самый медленный.
