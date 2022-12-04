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


def heap_sort(lst):
    length = len(lst)
    for i in range(length // 2 - 1, -1, -1):
        heapify(lst, length, i)
    for i in range(length - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst


def heapify(las, length, i):
    flag = True
    while flag:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and las[largest] < las[left]:
            largest = left
        if right < length and las[largest] < las[right]:
            largest = right
        if largest != i:
            las[i], las[largest] = las[largest], las[i]
            i = largest
        else:
            flag = False


def med_num(lst):
    return lst[len(lst) // 2]


m = 10
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("med_num(heap_sort(user_lst))", globals=globals(), number=100))

m = 100
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("med_num(heap_sort(user_lst))", globals=globals(), number=100))

m = 1000
user_lst = [randint(0, 100) for _ in range(2*m+1)]
print(timeit("med_num(heap_sort(user_lst))", globals=globals(), number=100))

"""
Результаты:
0.0022313000008580275
0.03547709999838844
0.50131190000684
"""
