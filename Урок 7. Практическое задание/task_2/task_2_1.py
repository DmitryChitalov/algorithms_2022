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
############################################################################
# Гномья сортировка:

import random
from timeit import timeit


def select_median(lst_obj, m):
    lst_obj = gnome_sort(lst_obj)
    return lst_obj[m]


def gnome_sort(lst_obj):
    i = 1
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            tmp = lst_obj[i]
            lst_obj[i] = lst_obj[i - 1]
            lst_obj[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return lst_obj


m = 6
orig_lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
select_median(orig_lst, m)

# замеры 10
print('select_median_10: ',
      timeit(
          "select_median(orig_lst[:], m)",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 10 + 1)]
# замеры 100
print('select_median_100: ',
      timeit(
          "select_median(orig_lst[:], m)",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 100 + 1)]
# замеры 1000
print('select_median_1000: ',
      timeit(
          "select_median(orig_lst[:], m)",
          globals=globals(),
          number=1000))

"""
Это алгоритм нахождения медианы с помощью Гномьй сортировки.
Сделал замеры времени реализаций.

select_median_10:  0.047020862002682406
select_median_100:  2.1340817169984803
select_median_1000:  249.87234992899903
"""
