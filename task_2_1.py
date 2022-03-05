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

##############################################################################
"""
Способ 1: оптимизированная гномья сортировка

Средняя сложность алгоритма: O(n^2)
    - (n-1) шаг для прохождения массива слева направо и попарного сравнения
    элементов;
    - при этом на k-ом шаге возможен проход в обратную сторону, число шагов в 
    котором лежит в диапазоне от 1 до (k-1).
    
Массив из 11 элементов: 0.00466
Массив из 101 элементов: 0.34569
Массив из 1001 элементов: 46.55039
"""

def gnome_sort(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            while lst[i-1] > lst[i] and i > 0:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                i-=1
    return lst

def median(lst):
    lst = gnome_sort(lst)
    return lst[len(lst)//2]


# Тестирование
for i in range(1,4):
    n = 10**i + 1
    test_lst = [randint(-100, 100) for _ in range(n)]
    print(f'Массив из {n} элементов: {timeit("median(test_lst[:])", globals=globals(), number=1000):.5f}')
