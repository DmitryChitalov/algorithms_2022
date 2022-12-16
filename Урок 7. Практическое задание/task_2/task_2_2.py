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

"""
2*5+1 элементов: 0.003018499999999591
2*50+1 элементов: 0.1104453000000003
2*500+1 элементов: 9.6089418
"""
from random import randint
from timeit import timeit


def median(lst):
    i = m
    while i > 0:
        lst_max = max(lst)
        lst.remove(lst_max)
        i -= 1
    return max(lst)


m = int(input("Введите натуральное число m: "))
list_len = 2*m+1
orig_list = [randint(0, 100) for _ in range(list_len)]


print(timeit("median(orig_list[:])", globals=globals(), number=1000))
print(orig_list)
print(median(orig_list))


