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

list_1 = [randint(-100, 100) for _ in range(2 * randint(10, 15) + 1)]
list_2 = [randint(-100, 100) for _ in range(2 * randint(100, 105) + 1)]
list_3 = [randint(-100, 100) for _ in range(2 * randint(1000, 1005) + 1)]


def m1(list):
    index = 1
    i = 0
    n = len(list)
    while i < n - 1:
        if list[i] <= list[i + 1]:
            i, index = index, index + 1
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i -= 1
            if i < 0:
                i, index = index, index + 1
    return f'Медиана : {list[int(len(list) / 2)]}\n{list}'


print('Массив 10-15 элементов: ', timeit('m1(list_1[:])', globals=globals(), number=100), f'\n{m1(list_1[:])}')
print('Массив 100-105 элементов: ', timeit('m1(list_2[:])', globals=globals(), number=100), f'\n{m1(list_2[:])}')
print('Массив 1000-1005 элементов: ', timeit('m1(list_3[:])', globals=globals(), number=100), f'\n{m1(list_3[:])}')

"""
Массив 10-15 элементов:  0.001978599997528363 
Массив 100-105 элементов:  0.1619605000014417 
Массив 1000-1005 элементов:  19.282288499998685 

"""