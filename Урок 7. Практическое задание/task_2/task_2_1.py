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

# гномья сортировка

from random import randint
from timeit import timeit


def lst_sort(lst):
    i, j, size = 1, 2, len(lists_task)
    i = 1
    while i < size:
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lst


m = 5
lists_task = [randint(0, 100) for _ in range(2 * m + 1)]
print(lst_sort(lists_task))
lst = lst_sort(lists_task)
print(lst[m])
print(timeit("lst_sort(lists_task[:])", globals=globals(), number=100))  # 0.000298037000000001


m = 50
lists_task = [randint(0, 200) for _ in range(2 * m + 1)]
print(lst_sort(lists_task))
lst = lst_sort(lists_task)
print(lst[m])
print(timeit("lst_sort(lists_task[:])", globals=globals(), number=100))  # 0.002546452999999997


m = 500
lists_task = [randint(0, 2000) for _ in range(2 * m + 1)]
print(lst_sort(lists_task))
lst = lst_sort(lists_task)
print(lst[m])
print(timeit("lst_sort(lists_task[:])", globals=globals(), number=100))  # 0.030413348000000007

# медиана - число с индексом m, то есть вводимое число будет индексом медианы.
