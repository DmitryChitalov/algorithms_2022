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
from timeit import timeit
from random import randrange


def create_lst(m):
    lst = [randrange(-100, 100) for _ in range(2 * m + 1)]
    return lst


# Гномья сортировка
def find_median_gnome(lst, m):
    i, j, size = 1, 2, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst[m]


m1 = 10
lst1 = create_lst(m1)
print(timeit('find_median_gnome(lst1.copy(), m1)', globals=globals(), number=1000))  # 0.020183

m2 = 100
lst2 = create_lst(m2)
print(timeit('find_median_gnome(lst2.copy(), m2)', globals=globals(), number=1000))  # 1.3294885

m3 = 1000
lst3 = create_lst(m3)
print(timeit('find_median_gnome(lst3.copy(), m3)', globals=globals(), number=1000))  # 161.0634322
