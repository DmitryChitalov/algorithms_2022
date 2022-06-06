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
Путем удаления максимальных элементов:
"""
import random
from timeit import timeit


def without_sort(lst_obj):
    tmp_lst = lst_obj
    for i in range(len(lst_obj) // 2):
        tmp_lst.remove(max(tmp_lst))
    return max(tmp_lst)


m = 6
orig_lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
# замеры 10
print('without_sort_10: ',
      timeit(
          "without_sort(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 10 + 1)]
# замеры 100
print('without_sort_100: ',
      timeit(
          "without_sort(orig_lst[:])",
          globals=globals(),
          number=1000))

orig_lst = [random.randint(-100, 100) for _ in range(2 * m * 100 + 1)]
# замеры 1000
print('without_sort_1000: ',
      timeit(
          "without_sort(orig_lst[:])",
          globals=globals(),
          number=1000))
"""
Это алгоритм удаления максимальных элементов.
Сделал замеры времени реализаций.

without_sort_10:  0.006392543000401929
without_sort_100:  0.2294311089972325
without_sort_1000:  19.123655307001172
"""
