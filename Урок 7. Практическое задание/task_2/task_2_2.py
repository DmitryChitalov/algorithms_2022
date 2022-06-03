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
#################################################################
"""
Решение задачи без сортировки.
Этот алгоритм, называемый «quickselect», разработан Тони Хоаром:
"""
import random
from timeit import timeit


def quickselect_median(lst_obj, pivot_fn=random.choice):
    if len(lst_obj) % 2 == 1:
        return quickselect(lst_obj, len(lst_obj) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(lst_obj, len(lst_obj) / 2 - 1, pivot_fn) +
                      quickselect(lst_obj, len(lst_obj) / 2, pivot_fn))


def quickselect(lst_obj, k, pivot_fn):
    if len(lst_obj) == 1:
        return lst_obj[0]

    pivot = pivot_fn(lst_obj)

    lows = [el for el in lst_obj if el < pivot]
    highs = [el for el in lst_obj if el > pivot]
    pivots = [el for el in lst_obj if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


m = 6
"""
array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив {array}')
print(f'Отсортированный массив {sorted(array)}')
print(f'Медиана {quickselect_median(array)}')
"""
orig_lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
# замеры 10
print('quickselect_median_10: ',
      timeit(
          "quickselect_median(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 10 + 1)]
# замеры 100
print('quickselect_median_100: ',
      timeit(
          "quickselect_median(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 100 + 1)]
# замеры 1000
print('quickselect_median_1000: ',
      timeit(
          "quickselect_median(orig_lst[:])",
          globals=globals(),
          number=1000))
"""
Это алгоритм нахождения медианы медиан.
Сделал замеры времени реализаций.

quickselect_median_10:  0.016604286000074353
quickselect_median_100:  0.09866102800151566
quickselect_median_1000:  0.7615820380015066
"""
