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
import math
from random import randint
from timeit import timeit


def median_element(numbers_list):
    new_list = numbers_list[:]
    for i in range(len(numbers_list) // 2):
        new_list.remove(max(new_list))
    return max(new_list)


m_10 = 5

numbers_list = [randint(-100, 100) for i in range(2*m_10-1)]
print(f'{numbers_list} - исходный список m_10')
time_func = timeit("median_element(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_10')
print(f'{median_element(numbers_list)} - Медианный элемент')


m_100 = 50

numbers_list = [randint(-100, 100) for i in range(2*m_100-1)]
time_func = timeit("median_element(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_100')
print(f'{median_element(numbers_list)} - Медианный элемент')


m_1000 = 500

numbers_list = [randint(-100, 100) for i in range(2*m_1000-1)]
time_func = timeit("median_element(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_1000')
print(f'{median_element(numbers_list)} - Медианный элемент')


# Аналитика

# [-2, -86, -25, -2, 76, 88, 24, 4, 7] - исходный список m_10
# 0.03644869942218065 - время выполнения функции с m_10
# 4 - Медианный элемент
# 1.277185800485313 - время выполнения функции с m_100
# -10 - Медианный элемент
# 108.72144520003349 - время выполнения функции с m_1000
# 0 - Медианный элемент



# Сортировка методом Шелл
#
# def shell_sort(array):
#     n = len(array)
#     k = int(math.log2(n))
#     interval = 2 ** k - 1
#     while interval > 0:
#         for i in range(interval, n):
#             temp = array[i]
#             j = i
#             while j >= interval and array[j - interval] > temp:
#                 array[j] = array[j - interval]
#                 j -= interval
#             array[j] = temp
#         k -= 1
#         interval = 2 ** k - 1
#     return f'{array} - отсортированный список  '
#
#
# m_10 = 10
#
# numbers_list = [randint(-100, 100) for i in range(2*m_10+1)]
# print(f'{numbers_list} - исходный список m_10')
# print(shell_sort(numbers_list))
# time_func = timeit("shell_sort(numbers_list[:])", globals=globals(), number=10000)
# print(f'{time_func} - время выполнения функции с m_10')
# print(f'Медианный элемент numbers_list: {numbers_list[m_10]}')
#
# m_100 = 100
#
# numbers_list = [randint(-100, 100) for i in range(2*m_100+1)]
# print(f'{numbers_list} - исходный список m_100')
# print(shell_sort(numbers_list))
# time_func = timeit("shell_sort(numbers_list[:])", globals=globals(), number=10000)
# print(f'{time_func} - время выполнения функции с m_100')
# print(f'Медианный элемент numbers_list: {numbers_list[m_100]}')
#
# m_1000 = 1000
#
# numbers_list = [randint(-100, 100) for i in range(2*m_1000+1)]
# print(f'{numbers_list} - исходный список m_1000')
# print(shell_sort(numbers_list))
# time_func = timeit("shell_sort(numbers_list[:])", globals=globals(), number=10000)
# print(f'{time_func} - время выполнения функции с m_1000')
# print(f'Медианный элемент numbers_list: {numbers_list[m_1000]}')

# Аналитика
# [-7, 88, 65, 92, 78, -62, -31, 8, -65, 30, 36, 42, 50, -94, -49, 59, -21, 7, -31, -24, 77] - исходный список m_10
# [-94, -65, -62, -49, -31, -31, -24, -21, -7, 7, 8, 30, 36, 42, 50, 59, 65, 77, 78, 88, 92] - отсортированный список
# 0.16845740005373955 - время выполнения функции с m_10
# Медианный элемент numbers_list: 8
# 2.6494119996204972 - время выполнения функции с m_100
# Медианный элемент numbers_list: -5
# 38.94577859994024 - время выполнения функции с m_1000
# Медианный элемент numbers_list: -3
# Готово
# Process finished with exit code 0
