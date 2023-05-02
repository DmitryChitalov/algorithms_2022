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



def gnome_sort(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1

    n = len(lst)
    index = n // 2
    if n % 2 != 0:
        return lst[index]
    return sum(lst[index - 1:index + 1]) / 2



m = 10
lst = [randint(0, 100) for i in range(2 * m + 1)]
print(gnome_sort(lst))
print(
    timeit(
        "gnome_sort(lst[:])",
        globals=globals(),
        number=20))


m = 100
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "gnome_sort(lst[:])",
        globals=globals(),
        number=20))


m = 1000
lst = [randint(0, 100) for i in range(2 * m + 1)]

print(
    timeit(
        "gnome_sort(lst[:])",
        globals=globals(),
        number=20))


"""
62 медиана
0.0002459999999999962 10 элементов
0.32186460000000006   100 элементов
41.298061700000005    1000 элементов
"""


