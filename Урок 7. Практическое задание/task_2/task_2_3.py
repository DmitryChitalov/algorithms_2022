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
from heapq import heappop, heappush
from random import randint
from timeit import timeit

# heappush(list, item) – используется для добавления элемента кучи и его повторной сортировки.
# heappop(список) – нужна для удаления и возврата элемента.
# heapfy() – используется для превращения данного списка в кучу.


def pyramid_sort(numbers_list):
    heap = []
    for i in numbers_list:
        heappush(heap, i)
    sort = []

    while heap:
        sort.append(heappop(heap))
    return sort


m_10 = 10
numbers_list = [randint(-100, 100) for i in range(2*m_10+1)]
print(f'{numbers_list} - исходный список m_10')
print(pyramid_sort(numbers_list))
time_func = timeit("pyramid_sort(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_10')
print(f'Медианный элемент numbers_list: {pyramid_sort(numbers_list)[m_10]}')

m_100 = 100
numbers_list = [randint(-100, 100) for i in range(2*m_100+1)]
print(f'{numbers_list} - исходный список m_100')
print(pyramid_sort(numbers_list))
time_func = timeit("pyramid_sort(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_100')
print(f'Медианный элемент numbers_list: {pyramid_sort(numbers_list)[m_100]}')

m_1000 = 1000
numbers_list = [randint(-100, 100) for i in range(2*m_1000+1)]
print(f'{numbers_list} - исходный список m_1000')
print(pyramid_sort(numbers_list))
time_func = timeit("pyramid_sort(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_1000')
print(f'Медианный элемент numbers_list: {pyramid_sort(numbers_list)[m_1000]}')

# Аналитика
# [-93, -87, -61, -23, -72, -2, 36, -83, 13, 90, -99, -69, -56, -95, 52, -74, 80, 33, -42, -81, -37] - исходный список m_10
# [-99, -95, -93, -87, -83, -81, -74, -72, -69, -61, -56, -42, -37, -23, -2, 13, 33, 36, 52, 80, 90]
# 0.07228169962763786 - время выполнения функции с m_10
# Медианный элемент numbers_list: -56

# 0.862890100106597 - время выполнения функции с m_100
# Медианный элемент numbers_list: -7

# 9.80386590026319 - время выполнения функции с m_1000
# Медианный элемент numbers_list: 1

# Итог по 7 уроку
# Из 3 алгоритмов сортировки, которую мы не рассматривали на уроке (Гномья, Шелла, Кучей),
# лучшим по времени оказалась гномья !!!

# 3 - Сортировка Кучей или Пирамидой
# 9.80386590026319 - время выполнения функции с m_1000

# 2 - Сортировка Шелла
# 38.94577859994024 - время выполнения функции с m_1000

# 1 - Сортировка Гномья
# 5.26074240077287 - время выполнения функции c m_1000
# Готово