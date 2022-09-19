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
from random import randint
from timeit import timeit
from statistics import median


def no_sort_med(lst):
    for _ in range(len(lst)//2):
        lst.remove(max(lst))
    return max(lst)


m = 10
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {median(lst[:])}')
print(timeit("median(lst[:])", globals=globals(), number=100)) # время выполнения 0.00010648400348145515

m = 100
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {median(lst[:])}')
print(timeit("median(lst[:])", globals=globals(), number=100)) # время выполнения 0.0010302560003765393

m = 1000
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst = {median(lst[:])}')
print(timeit("median(lst[:])", globals=globals(), number=100)) # время выполнения 0.02478226099992753

# Быстрее всего поиск медианы осуществляется функцией из библиотеки statistics

