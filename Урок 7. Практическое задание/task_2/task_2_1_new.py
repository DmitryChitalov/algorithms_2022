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
from random import randint
from timeit import timeit


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return f'{data} - отсортированный список'

# по формуле


m_10 = 10

numbers_list = [randint(-100, 100) for i in range(2*m_10+1)]
print(f'{numbers_list} - исходный список m_10')
time_func = timeit("gnome(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции с m_10')
print(gnome(numbers_list))
print(f'Медианный элемент numbers_list: {numbers_list[m_10]}')


m_100 = 100

numbers_list = [randint(-100, 100) for i in range(2*m_100+1)]
time_func = timeit("gnome(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции c m_100 ')
gnome(numbers_list)
print(f'Медианный элемент numbers_list: {numbers_list[m_100]}')


m_1000 = 1000

numbers_list = [randint(-100, 100) for i in range(2*m_1000+1)]
time_func = timeit("gnome(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции c m_1000')
gnome(numbers_list)
print(f'Медианный элемент numbers_list: {numbers_list[m_1000]}')


# Нахождение медианы без формулы

numbers_list = [randint(-100, 100) for i in range(10)]
print(f'{numbers_list} - исходный список M')
print(gnome(numbers_list))
m = len(numbers_list) // 2 - 1
time_func = timeit("gnome(numbers_list[:])", globals=globals(), number=10000)
print(f'{time_func} - время выполнения функции c M')
print(f'Медианный элемент numbers_list: {numbers_list[int(m)]}')


# Аналитика
# по формуле
# [-12, -14, -6, -54, -95, -61, -85, 4, -11, 77, -56, -74, 0, -78, -50, 0, 51, 48, 80, -27, -99] -Исходный список m_10
# [-99, -95, -85, -78, -74, -61, -56, -54, -50, -27, -14, -12, -11, -6, 0, 0, 4, 48, 51, 77, 80] -отсортированный список
# 0.05978950019925833 - время выполнения функции с m_10
# Медианный элемент numbers_list: -14
# 0.5074362996965647 - время выполнения функции c m_100
# Медианный элемент numbers_list: -2
# 5.26074240077287 - время выполнения функции c m_1000
# Медианный элемент numbers_list: 0
# Нахождение медианы без формулы
# [87, 87, 90, 47, 44, 71, -1, -46, -66, -1] - исходный список M
# [-66, -46, -1, -1, 44, 47, 71, 87, 87, 90] - отсортированный список
# 0.03250730037689209 - время выполнения функции c M
# Медианный элемент numbers_list: 44