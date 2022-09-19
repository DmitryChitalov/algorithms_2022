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
    i = 1

    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


m = 10
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst[m] = {gnome_sort(lst[:])[m]}')
print(timeit("gnome_sort(lst[:])", globals=globals(), number=100)) # время выполнения 0.008149416997184744

m = 100
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst[m] = {gnome_sort(lst[:])[m]}')
print(timeit("gnome_sort(lst[:])", globals=globals(), number=100)) # время выполнения 0.5693433289998211

m = 1000
lst = [randint(-100, 100) for i in range(m*2+1)]
print(lst)
print(f' медианный элементе массива lst[m] = {gnome_sort(lst[:])[m]}')
print(timeit("gnome_sort(lst[:])", globals=globals(), number=100)) # время выполнения 69.20749484800035

