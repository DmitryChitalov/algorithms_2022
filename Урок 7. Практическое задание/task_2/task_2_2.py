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
from random import randint
from timeit import timeit


def no_sort(lst):
    left_list = []
    right_list = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] > lst[j]:
                left_list.append(lst[j])
            if lst[i] < lst[j]:
                right_list.append(lst[j])
            if lst[i] == lst[j] and i > j:
                left_list.append(lst[j])
            if lst[i] == lst[j] and i < j:
                right_list.append(lst[j])
        if len(left_list) == len(right_list):
            return lst[i]
        left_list.clear()
        right_list.clear()


m = 10
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("no_sort(user_lst)", globals=globals(), number=100))

m = 100
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("no_sort(user_lst)", globals=globals(), number=100))

m = 1000
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("no_sort(user_lst)", globals=globals(), number=100))

"""
Результаты:
0.006352500000502914
0.5455571999991662
13.857555800001137
"""
