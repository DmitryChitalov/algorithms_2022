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

""" 
Находим медиану с помощью гномьей сортировки
"""
def gnome_sort(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    print(lst)
    return lst[m]


m = 25
my_list = [randint(1, 200) for i in range(2 * m + 1)]

print(gnome_sort(my_list))

"""
Делаем замеры на массивах разной длины
"""


def gnome_sort_1(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


m_1 = 10
my_list_1 = [randint(1, 200) for _ in range(2 * m_1 + 1)]
print(
    timeit(
        "gnome_sort_1(my_list_1[:])",
        globals=globals(),
        number=100))


m_2 = 100
my_list_2 = [randint(1, 200) for _ in range(2 * m_2 + 1)]

print(
    timeit(
        "gnome_sort_1(my_list_2[:])",
        globals=globals(),
        number=100))


m_3 = 1000
my_list_3 = [randint(1, 200)for _ in range(2 * m_3 + 1)]

print(
    timeit(
        "gnome_sort_1(my_list_3[:])",
        globals=globals(),
        number=100))

"""
0.01186984399999999
0.817610874
77.587048461
"""