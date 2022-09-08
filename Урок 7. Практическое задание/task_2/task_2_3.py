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
from timeit import timeit
from statistics import median


def built_in_median(some_li):
    return median(some_li[:])


# -----------------------------------------------------------------------------
m = 10
origin_list = [randint(0, 100) for _ in range(2 * m + 1)]
result = built_in_median(origin_list[:])
print(f"Медиана списка из 11 элементов: {result}")
result_time = timeit(stmt="built_in_median(origin_list[:])",
                     globals=globals(),
                     number=100)
print(f"{'%.8f' % result_time} seconds")
del origin_list

# -----------------------------------------------------------------------------
m = 100
origin_list = [randint(0, 100) for _ in range(2 * m + 1)]
# result = built_in_median(origin_list[:])
# print(f"median is: {result}")
result_time = timeit(stmt="built_in_median(origin_list[:])",
                     globals=globals(),
                     number=100)
print(f"{'%.8f' % result_time} seconds")
del origin_list

# -----------------------------------------------------------------------------
m = 1000
origin_list = [randint(0, 100) for _ in range(2 * m + 1)]
# result = built_in_median(origin_list[:])
# print(f"median is: {result}")
result_time = timeit(stmt="built_in_median(origin_list[:])",
                     globals=globals(),
                     number=100)
print(f"{'%.8f' % result_time} seconds")
del origin_list

"""
Медиана списка из 11 элементов: 51
0.00012540 seconds
0.00130520 seconds
0.01987760 seconds

Из трёх способов использование встроенной функции
оказалось самым эффективным способом!
"""
